"""Read-only service health, independent of optional historical Temporal evidence."""
import argparse
import asyncio
import base64
from dataclasses import dataclass
from datetime import timedelta
import hashlib
import ipaddress
import json
import logging
import math
from pathlib import Path
import re
import stat
import sys
import time
from urllib.parse import urlsplit
import uuid

from scripts._process import run_cli, run_process

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / "local-data"
RPC_TIMEOUT = timedelta(seconds=5)
# Includes bounded termination and a separately bounded final receipt audit.
CLEANUP_ALLOWANCE = 5
MAX_FILE_BYTES = 1048576


class CheckFailure(Exception):
    """Only fixed, non-secret reasons may cross the worker boundary."""


@dataclass(frozen=True, repr=False)
class ServiceConfig:
    postgres: dict
    azurite: dict
    temporal: dict


def read_file(path, field):
    try:
        if not stat.S_ISREG(path.stat().st_mode):
            raise CheckFailure(f"{field}: expected a regular file")
        with path.open("rb") as stream:
            content = stream.read(MAX_FILE_BYTES + 1)
        if len(content) > MAX_FILE_BYTES:
            raise CheckFailure(f"{field}: file too large")
        return content
    except OSError:
        raise CheckFailure(f"{field}: file unavailable") from None


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("Duplicate JSON field")
        result[key] = value
    return result


def read_json(path, field):
    try:
        return json.loads(read_file(path, field), object_pairs_hook=unique_object)
    except (ValueError, UnicodeError):
        raise CheckFailure(f"{field}: malformed JSON") from None


def require_fields(value, fields, field):
    if not isinstance(value, dict) or set(value) != set(fields):
        raise CheckFailure(f"{field}: missing or unknown fields")


def string(value, field):
    if (not isinstance(value, str) or not value or value != value.strip()
            or any(ord(char) < 32 or ord(char) == 127 for char in value)):
        raise CheckFailure(f"{field}: expected nonempty text without surrounding whitespace")
    return value


def identifier(value, field):
    value = string(value, field)
    if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]{0,254}", value):
        raise CheckFailure(f"{field}: invalid identifier")
    return value


def host(value, field):
    value = string(value, field)
    try:
        ipaddress.ip_address(value)
        return value
    except ValueError:
        pass
    if len(value) > 253 or any(not re.fullmatch(r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?", part)
                               for part in value.rstrip(".").split(".")):
        raise CheckFailure(f"{field}: invalid host")
    return value


def port(value, field):
    if type(value) is not int or not 1 <= value <= 65535:
        raise CheckFailure(f"{field}: invalid port")
    return value


def secret_file(value, base, field):
    value = string(value, field)
    try:
        path = Path(value)
        raw = read_file(path if path.is_absolute() else base / path, field)
        secret = raw.decode("utf-8").strip()
    except (ValueError, UnicodeError):
        raise CheckFailure(f"{field}: invalid secret file") from None
    if not secret:
        raise CheckFailure(f"{field}: empty secret file")
    return secret


def load_config(path=None, local=LOCAL):
    if path is None:
        base = local
        raw = {
            "postgres": {"host": "gre-postgres", "port": 5432, "database": "gre_dev",
                         "user": "gre_dev", "password_file": "postgres/password"},
            "azurite": {"endpoint": "http://gre-azurite:10000/gredev", "account_name": "gredev",
                        "account_key_file": "azurite/.env"},
            "temporal": {"address": "gre-temporal:7233", "namespace": "default"},
        }
    else:
        path = Path(path)
        base = path.absolute().parent
        raw = read_json(path, "config")
    require_fields(raw, ("postgres", "azurite", "temporal"), "config")
    pg, blob, temporal = (raw[key] for key in ("postgres", "azurite", "temporal"))
    require_fields(pg, ("host", "port", "database", "user", "password_file"), "postgres")
    require_fields(blob, ("endpoint", "account_name", "account_key_file"), "azurite")
    require_fields(temporal, ("address", "namespace"), "temporal")
    pg = dict(pg)
    blob = dict(blob)
    temporal = dict(temporal)
    pg["host"] = host(pg["host"], "postgres.host")
    pg["port"] = port(pg["port"], "postgres.port")
    for key in ("database", "user"):
        pg[key] = identifier(pg[key], "postgres." + key)
    account = string(blob["account_name"], "azurite.account_name")
    if not re.fullmatch(r"[a-z0-9]{3,24}", account):
        raise CheckFailure("azurite.account_name: invalid account")
    try:
        endpoint = urlsplit(string(blob["endpoint"], "azurite.endpoint"))
        if (endpoint.scheme not in ("http", "https") or endpoint.username is not None
                or endpoint.password is not None or endpoint.query or endpoint.fragment or endpoint.netloc.endswith(":")
                or endpoint.path.rstrip("/") != "/" + account):
            raise ValueError()
        host(endpoint.hostname, "azurite.endpoint")
        if endpoint.port is not None:
            port(endpoint.port, "azurite.endpoint")
    except ValueError:
        raise CheckFailure("azurite.endpoint: invalid Blob account URL") from None
    try:
        address = urlsplit("//" + string(temporal["address"], "temporal.address"))
        if address.username is not None or address.password is not None or address.path or address.query or address.fragment:
            raise ValueError()
        host(address.hostname, "temporal.address")
        port(address.port, "temporal.address")
    except ValueError:
        raise CheckFailure("temporal.address: expected host and port without credentials") from None
    temporal["namespace"] = identifier(temporal["namespace"], "temporal.namespace")
    pg["password"] = secret_file(pg.pop("password_file"), base, "postgres.password_file")
    key = secret_file(blob.pop("account_key_file"), base, "azurite.account_key_file")
    if path is None:
        prefix = "AZURITE_ACCOUNTS=gredev:"
        if not key.startswith(prefix):
            raise CheckFailure("azurite.account_key_file: invalid local account configuration")
        key = key[len(prefix):]
    try:
        if not base64.b64decode(key, validate=True):
            raise ValueError()
    except ValueError:
        raise CheckFailure("azurite.account_key_file: invalid account key") from None
    blob["account_key"] = key
    return ServiceConfig(pg, blob, temporal)


def check_postgres(config):
    from alembic.migration import MigrationContext
    from sqlalchemy import URL, create_engine, text
    pg = config.postgres
    url = URL.create("postgresql+psycopg", username=pg["user"], password=pg["password"],
                     host=pg["host"], port=pg["port"], database=pg["database"])
    engine = create_engine(url, connect_args={"connect_timeout": 5, "options": "-c statement_timeout=10000"})
    try:
        with engine.connect() as connection:
            connection.execute(text("SET TRANSACTION READ ONLY"))
            database, version = connection.execute(text("SELECT current_database(), current_setting('server_version')")).one()
            if database != pg["database"] or not re.match(r"^18\.6(?:\s|$)", version):
                raise CheckFailure("postgres: unexpected database or server version")
            MigrationContext.configure(connection).get_current_heads()
    finally:
        engine.dispose()
    return "PASS PostgreSQL 18.6 authenticated read-only access and Alembic revision read"


def check_azurite(config):
    from azure.storage.blob import BlobServiceClient
    blob = config.azurite
    with BlobServiceClient(blob["endpoint"], credential={"account_name": blob["account_name"], "account_key": blob["account_key"]},
                           api_version="2025-11-05", retry_total=0, connection_timeout=5, read_timeout=10) as client:
        client.get_service_properties()
        # Read every page without logging customer-controlled names or metadata.
        for _ in client.list_containers():
            pass
    return "PASS Azurite API 2025-11-05 authenticated read-only properties and listing"


def historical_receipt(path):
    if not path.exists():
        return None
    state = read_json(path, "historical Temporal receipt")
    if not isinstance(state, dict) or not isinstance(state.get("verification"), dict) or not state["verification"]:
        raise CheckFailure("historical Temporal receipt: missing verification record")
    string(state.get("workflow_id"), "historical Temporal receipt.workflow_id")
    try:
        uuid.UUID(state["run_id"])
    except (KeyError, ValueError, TypeError, AttributeError):
        raise CheckFailure("historical Temporal receipt: invalid run identifier") from None
    return state


async def check_temporal(config, inspect_historical=False, local=LOCAL):
    from temporalio.api.enums.v1 import NamespaceState
    from temporalio.api.workflowservice.v1 import DescribeNamespaceRequest
    from temporalio.client import Client, WorkflowExecutionStatus
    from temporalio.service import RPCError, RPCStatusCode
    client = await Client.connect(config.temporal["address"], namespace=config.temporal["namespace"])
    if not await client.service_client.check_health(timeout=RPC_TIMEOUT):
        raise CheckFailure("temporal: current service unhealthy")
    namespace = await client.workflow_service.describe_namespace(
        DescribeNamespaceRequest(namespace=config.temporal["namespace"]), timeout=RPC_TIMEOUT)
    if (namespace.namespace_info.name != config.temporal["namespace"]
            or namespace.namespace_info.state != NamespaceState.NAMESPACE_STATE_REGISTERED):
        raise CheckFailure("temporal: configured namespace is not registered")
    messages = ["PASS current Temporal service health and configured namespace access"]
    if not inspect_historical:
        return messages
    state = historical_receipt(local / "temporal/workflow-probe.json")
    if state is None:
        return messages + ["INFO no historical Temporal receipt; no historical comparison performed"]
    try:
        info = await client.get_workflow_handle(state["workflow_id"], run_id=state["run_id"]).describe(rpc_timeout=RPC_TIMEOUT)
    except RPCError as error:
        if error.status == RPCStatusCode.NOT_FOUND:
            return messages + ["INFO historical Temporal evidence unavailable (NOT_FOUND); retention/deletion possible, cause unverified"]
        raise CheckFailure("historical Temporal inspection RPC failed: " + error.status.name) from None
    except Exception:
        raise CheckFailure("historical Temporal inspection failed (details withheld)") from None
    if info.status != WorkflowExecutionStatus.COMPLETED or info.run_id != state["run_id"]:
        raise CheckFailure("historical Temporal receipt: status or run mismatch")
    return messages + ["PASS historical Temporal completed workflow/run match (separate from current health)"]


def redacted_error(error):
    if isinstance(error, CheckFailure):
        return str(error)
    from temporalio.service import RPCError
    if isinstance(error, RPCError):
        return "service RPC failed: " + error.status.name
    return "service check failed (details withheld)"


async def service_payload(config, inspect_historical, local):
    results = await asyncio.gather(asyncio.to_thread(check_postgres, config),
                                   asyncio.to_thread(check_azurite, config),
                                   check_temporal(config, inspect_historical, local), return_exceptions=True)
    messages = []
    ok = True
    for name, result in zip(("PostgreSQL", "Azurite", "Temporal"), results):
        if isinstance(result, BaseException):
            ok = False
            messages.append("FAIL " + name + ": " + redacted_error(result))
        else:
            messages.extend(result if isinstance(result, list) else [result])
    return {"ok": ok, "messages": messages}


def snapshot_receipts(local):
    paths = set(local.glob("*/server.json")) | {local / "temporal/workflow-probe.json"}
    return {str(path.relative_to(local)): hashlib.sha256(read_file(path, "verification receipt")).hexdigest()
            for path in sorted(paths) if path.exists()}


def worker_command(mode, local, config=None, inspect_historical=False):
    command = [sys.executable, "-B", "-m", "scripts.check_services", "--_mode", mode, "--_local", str(local)]
    if config is not None:
        command.extend(("--config", str(Path(config).absolute())))
    if inspect_historical:
        command.append("--inspect-historical-temporal")
    return command


def _payload(command, timeout):
    result = run_process(command, timeout=max(0, timeout))
    if result.timed_out:
        raise CheckFailure("service phase exceeded its wall-clock deadline")
    if result.returncode:
        raise CheckFailure("check subprocess failed (details withheld)")
    try:
        payload = json.loads(result.output)
        if not payload["ok"]:
            raise CheckFailure("receipt snapshot unavailable")
        return payload
    except (ValueError, KeyError, TypeError):
        raise CheckFailure("check subprocess returned an invalid result") from None


def run_checks(config=None, inspect_historical=False, timeout=30, *, local=LOCAL, _command=None):
    """One shared service boundary for standalone and combined commands."""
    deadline = time.monotonic() + timeout
    before = None
    code = 1
    try:
        before = _payload(worker_command("snapshot", local), deadline - time.monotonic())["receipts"]
        command = _command if _command is not None else worker_command("checks", local, config, inspect_historical)
        result = run_process(command, timeout=max(0, deadline - time.monotonic()))
        if result.timed_out:
            raise CheckFailure("service phase exceeded its wall-clock deadline")
        if result.returncode:
            raise CheckFailure("check subprocess failed (details withheld)")
        try:
            payload = json.loads(result.output)
            if type(payload["ok"]) is not bool or not isinstance(payload["messages"], list):
                raise ValueError()
        except (ValueError, KeyError, TypeError):
            raise CheckFailure("check subprocess returned an invalid result") from None
        for message in payload["messages"]:
            print(message, flush=True)
        code = 0 if payload["ok"] else 1
    except (CheckFailure, OSError, RuntimeError):
        # All dynamic child errors and command arguments stay out of the log.
        print("FAIL service phase: failed or exceeded wall-clock deadline", flush=True)
    finally:
        try:
            after = _payload(worker_command("snapshot", local), 2)["receipts"]
            if before is None or before != after:
                raise CheckFailure("verification receipts changed or could not be compared")
            print("PASS verification receipts unchanged", flush=True)
        except (CheckFailure, OSError, RuntimeError):
            code = 1
            print("FAIL verification receipts changed or preservation could not be verified", flush=True)
    if code == 0:
        print("PASS all three current services accessible; historical evidence reported separately", flush=True)
    return code


class SafeParser(argparse.ArgumentParser):
    def error(self, message):
        self.exit(2, "FAIL invalid check arguments (values withheld)\n")


def positive_timeout(value):
    number = float(value)
    if not math.isfinite(number) or number <= 0:
        raise ValueError()
    return number


def add_service_arguments(parser):
    parser.add_argument("--config", type=Path, help="Strict JSON service configuration; defaults to local services")
    parser.add_argument("--timeout", type=positive_timeout, default=30,
                        help="Service wall-clock deadline in seconds (default 30), plus at most 5s cleanup")
    parser.add_argument("--inspect-historical-temporal", action="store_true",
                        help="Inspect the retained receipt separately from current health")


def main(argv=None):
    parser = SafeParser(description=__doc__)
    add_service_arguments(parser)
    parser.add_argument("--_mode", choices=("snapshot", "checks"), help=argparse.SUPPRESS)
    parser.add_argument("--_local", type=Path, default=LOCAL, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if args._mode:
        # Only fixed diagnostic strings/receipt hashes cross this private boundary.
        logging.disable(logging.CRITICAL)
        try:
            if args._mode == "snapshot":
                payload = {"ok": True, "receipts": snapshot_receipts(args._local)}
            else:
                config = load_config(args.config, args._local)
                payload = asyncio.run(service_payload(config, args.inspect_historical_temporal, args._local))
        except Exception as error:
            payload = {"ok": False, "messages": ["FAIL " + redacted_error(error)]}
        print(json.dumps(payload), flush=True)
        return 0
    return run_checks(args.config, args.inspect_historical_temporal, args.timeout)


if __name__ == "__main__":
    run_cli(main)

"""P-001.01 behavior checks; synthetic files/processes only, no live services."""
import asyncio
import base64
import contextlib
import copy
import hashlib
import io
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import time
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, Mock, patch
import uuid

from scripts import check_environment as environment
from scripts import check_services as services
from scripts._process import run_process
from temporalio.client import WorkflowExecutionStatus
from temporalio.service import RPCError, RPCStatusCode

SECRET = "synthetic-secret-DO-NOT-LOG"
RUN_ID = "01a07906-7524-703d-9f22-507260b910c5"


class Scratch(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory(prefix="gre-service-unit-")
        self.addCleanup(self.scratch.cleanup)
        self.root = Path(self.scratch.name)
        self.local = self.root / "local"
        (self.local / "temporal").mkdir(parents=True)
        self.receipt = self.local / "temporal/workflow-probe.json"
        self.password = self.root / "password"
        self.password.write_text(SECRET)
        self.key = self.root / "key"
        self.key.write_text(base64.b64encode(b"synthetic-emulator-key").decode())
        self.raw = {
            "postgres": {"host": "database.example", "port": 5433, "database": "job_db", "user": "job_user", "password_file": "password"},
            "azurite": {"endpoint": "http://blob.example:10001/jobaccount", "account_name": "jobaccount", "account_key_file": "key"},
            "temporal": {"address": "workflow.example:7234", "namespace": "job-namespace"},
        }
        self.path = self.root / "services.json"
        self.path.write_text(json.dumps(self.raw))

    def config(self):
        return services.load_config(self.path)

    def record(self):
        self.receipt.write_text(json.dumps({"workflow_id": "synthetic-workflow", "run_id": RUN_ID,
                                            "verification": {"result": "synthetic"}}))

    def run_checks(self, command, timeout=2):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = services.run_checks(timeout=timeout, local=self.local, _command=command)
        return code, output.getvalue()


class ConfigurationTests(Scratch):
    def test_explicit_config_uses_relative_secret_files_and_no_local_fallback(self):
        with patch.object(services, "LOCAL", self.root / "unavailable"):
            config = self.config()
        self.assertEqual(config.postgres["database"], "job_db")
        self.assertEqual(config.postgres["port"], 5433)
        self.assertEqual(config.postgres["password"], SECRET)
        self.assertEqual(config.azurite["account_key"], self.key.read_text())
        self.assertEqual(config.temporal["namespace"], "job-namespace")
        self.assertNotIn(SECRET, repr(config))
        self.assertNotIn(config.azurite["account_key"], repr(config))

    def test_existing_local_defaults_and_env_key_format(self):
        (self.local / "postgres").mkdir()
        (self.local / "azurite").mkdir()
        (self.local / "postgres/password").write_text(SECRET)
        (self.local / "azurite/.env").write_text("AZURITE_ACCOUNTS=gredev:" + self.key.read_text())
        config = services.load_config(local=self.local)
        self.assertEqual(config.postgres["host"], "gre-postgres")
        self.assertEqual(config.postgres["database"], "gre_dev")
        self.assertEqual(config.azurite["endpoint"], "http://gre-azurite:10000/gredev")
        self.assertEqual(config.temporal, {"address": "gre-temporal:7233", "namespace": "default"})

    def test_missing_unknown_and_malformed_fields_are_rejected(self):
        variants = [[], {}, {**self.raw, "unknown": SECRET}]
        for section in self.raw:
            missing_section = copy.deepcopy(self.raw)
            del missing_section[section]
            variants.append(missing_section)
            extra = copy.deepcopy(self.raw)
            extra[section][SECRET] = SECRET
            variants.append(extra)
            for key in self.raw[section]:
                missing_field = copy.deepcopy(self.raw)
                del missing_field[section][key]
                variants.append(missing_field)
                for value in (None, "", [], {}):
                    invalid = copy.deepcopy(self.raw)
                    invalid[section][key] = value
                    variants.append(invalid)
        for raw in variants:
            with self.subTest(raw_type=type(raw).__name__):
                self.path.write_text(json.dumps(raw))
                with self.assertRaises(services.CheckFailure) as error:
                    self.config()
                self.assertNotIn(SECRET, str(error.exception))

    def test_credentials_urls_ports_and_namespace_validation(self):
        values = {
            ("postgres", "host"): ["host/path", "user@host", " ", SECRET + "\n"],
            ("postgres", "port"): [True, 0, 65536, 5432.0, "5432"],
            ("azurite", "endpoint"): ["ftp://blob/jobaccount", "http://user:" + SECRET + "@blob/jobaccount", "http://blob/jobaccount?sig=" + SECRET, "http://blob/other", "http://blob:99999/jobaccount", "http://blob:/jobaccount", "http://bl\nob/jobaccount"],
            ("azurite", "account_name"): ["BadAccount", "a", "a" * 25],
            ("temporal", "address"): ["https://workflow:7233", "workflow", "workflow:0", "workflow:65536", "workflow:7233/path", "user:" + SECRET + "@workflow:7233"],
            ("temporal", "namespace"): [" ", "nested/name", SECRET + "\n"],
        }
        for (section, key), cases in values.items():
            for value in cases:
                with self.subTest(section=section, key=key):
                    raw = copy.deepcopy(self.raw)
                    raw[section][key] = value
                    self.path.write_text(json.dumps(raw))
                    with self.assertRaises(services.CheckFailure) as error:
                        self.config()
                    self.assertNotIn(SECRET, str(error.exception))

    def test_config_and_secret_file_failures(self):
        for content in ("{", '{"postgres": {}, "postgres": {}}', '"' + SECRET + '"'):
            self.path.write_text(content)
            with self.assertRaises(services.CheckFailure):
                self.config()
        self.path.write_text(json.dumps(self.raw))
        for content in ("", "not-base64-" + SECRET):
            self.key.write_text(content)
            with self.assertRaises(services.CheckFailure) as error:
                self.config()
            self.assertNotIn(SECRET, str(error.exception))
        self.key.unlink()
        with self.assertRaises(services.CheckFailure):
            self.config()
        self.key.mkdir()
        with self.assertRaises(services.CheckFailure):
            self.config()
        self.path.write_bytes(b'\xff')
        with self.assertRaises(services.CheckFailure):
            self.config()

    def test_unreadable_secret_file_is_redacted(self):
        if os.geteuid() == 0:
            self.skipTest("Root can bypass Unix permission checks")
        self.password.chmod(0)
        try:
            with self.assertRaises(services.CheckFailure) as error:
                self.config()
            self.assertIn("postgres.password_file", str(error.exception))
            self.assertNotIn(SECRET, str(error.exception))
        finally:
            self.password.chmod(0o600)

    def test_ipv6_and_absolute_secret_paths(self):
        self.raw["postgres"]["host"] = "::1"
        self.raw["postgres"]["password_file"] = str(self.password)
        self.raw["temporal"]["address"] = "[::1]:7233"
        self.raw["azurite"]["endpoint"] = "http://[::1]:10000/jobaccount"
        self.path.write_text(json.dumps(self.raw))
        self.assertEqual(self.config().postgres["password"], SECRET)

    def test_cli_config_failure_is_redacted_and_audits_receipts(self):
        self.record()
        original = self.receipt.read_bytes()
        self.path.write_text(json.dumps({"secret": SECRET}))
        result = run_process(services.worker_command("checks", self.local, self.path), timeout=5)
        self.assertNotIn(SECRET, result.output)
        self.assertIn("missing or unknown fields", result.output)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = services.run_checks(self.path, timeout=5, local=self.local)
        self.assertEqual(code, 1)
        self.assertNotIn(SECRET, output.getvalue())
        self.assertIn("verification receipts unchanged", output.getvalue())
        self.assertEqual(self.receipt.read_bytes(), original)

    def test_cli_invalid_timeout_or_argument_never_echoes_value(self):
        for module in ("scripts.check_services", "scripts.check_environment"):
            for args in (["--timeout", SECRET], ["--timeout", "nan"], ["--timeout", "0"], ["--unknown=" + SECRET]):
                result = run_process([sys.executable, "-B", "-m", module, *args], timeout=5)
                self.assertEqual(result.returncode, 2)
                self.assertNotIn(SECRET, result.output)


class TemporalTests(Scratch):
    def fake_client(self):
        handle = SimpleNamespace(describe=AsyncMock(return_value=SimpleNamespace(status=WorkflowExecutionStatus.COMPLETED, run_id=RUN_ID)))
        return SimpleNamespace(
            service_client=SimpleNamespace(check_health=AsyncMock(return_value=True)),
            workflow_service=SimpleNamespace(describe_namespace=AsyncMock(return_value=SimpleNamespace(namespace_info=SimpleNamespace(name="job-namespace", state=1)))),
            get_workflow_handle=Mock(return_value=handle),
        )

    def check(self, client, inspect_history=True):
        with patch("temporalio.client.Client.connect", AsyncMock(return_value=client)) as connect:
            result = asyncio.run(services.check_temporal(self.config(), inspect_history, self.local))
        connect.assert_awaited_once_with("workflow.example:7234", namespace="job-namespace")
        return result

    def test_normal_health_never_consults_history_even_if_malformed(self):
        self.receipt.write_text("malformed " + SECRET)
        client = self.fake_client()
        with patch.object(services, "historical_receipt", side_effect=AssertionError("History must not be read")):
            result = self.check(client, False)
        self.assertIn("current Temporal", result[0])
        client.get_workflow_handle.assert_not_called()
        namespace_call = client.workflow_service.describe_namespace.call_args
        self.assertEqual(namespace_call.args[0].namespace, "job-namespace")
        self.assertEqual(namespace_call.kwargs["timeout"], services.RPC_TIMEOUT)

    def test_absent_receipt_is_reported_without_historical_pass(self):
        client = self.fake_client()
        result = self.check(client)
        self.assertIn("no historical comparison", result[-1])
        client.get_workflow_handle.assert_not_called()

    def test_valid_completed_match_preserves_exact_receipt(self):
        self.record()
        before = self.receipt.read_bytes()
        client = self.fake_client()
        result = self.check(client)
        self.assertIn("PASS historical", result[-1])
        client.get_workflow_handle.assert_called_once_with("synthetic-workflow", run_id=RUN_ID)
        client.get_workflow_handle.return_value.describe.assert_awaited_once_with(rpc_timeout=services.RPC_TIMEOUT)
        self.assertEqual(self.receipt.read_bytes(), before)

    def test_only_typed_historical_not_found_is_nonfatal(self):
        self.record()
        client = self.fake_client()
        client.get_workflow_handle.return_value.describe.side_effect = RPCError(SECRET, RPCStatusCode.NOT_FOUND, SECRET.encode())
        result = self.check(client)
        self.assertIn("NOT_FOUND", result[-1])
        self.assertIn("cause unverified", result[-1])
        self.assertNotIn(SECRET, " ".join(result))
        for error in (RuntimeError("NOT_FOUND " + SECRET), TimeoutError(SECRET),
                      RPCError(SECRET, RPCStatusCode.PERMISSION_DENIED, b""),
                      RPCError(SECRET, RPCStatusCode.DEADLINE_EXCEEDED, b""),
                      RPCError(SECRET, RPCStatusCode.UNAVAILABLE, b"")):
            client.get_workflow_handle.return_value.describe.side_effect = error
            with self.assertRaises(services.CheckFailure) as caught:
                self.check(client)
            self.assertNotIn(SECRET, str(caught.exception))

    def test_malformed_receipts_fail_without_overwriting(self):
        for value in ("{", "[]", "null", '{}', json.dumps({"workflow_id": "id", "run_id": RUN_ID}),
                      json.dumps({"workflow_id": "", "run_id": RUN_ID, "verification": {"ok": True}}),
                      json.dumps({"workflow_id": "id", "run_id": SECRET, "verification": {"ok": True}})):
            self.receipt.write_text(value)
            with self.assertRaises(services.CheckFailure) as error:
                self.check(self.fake_client())
            self.assertNotIn(SECRET, str(error.exception))
            self.assertEqual(self.receipt.read_text(), value)

    def test_mismatched_status_or_run_fails(self):
        self.record()
        for status, run_id in ((WorkflowExecutionStatus.RUNNING, RUN_ID),
                               (WorkflowExecutionStatus.COMPLETED, str(uuid.uuid4()))):
            client = self.fake_client()
            client.get_workflow_handle.return_value.describe.return_value = SimpleNamespace(status=status, run_id=run_id)
            with self.assertRaises(services.CheckFailure):
                self.check(client)

    def test_current_failures_fail_even_with_a_matching_receipt(self):
        self.record()
        for fail_at in ("connect", "health", "namespace-denied", "namespace-not-found", "namespace-wrong", "namespace-inactive"):
            client = self.fake_client()
            if fail_at == "connect":
                with patch("temporalio.client.Client.connect", AsyncMock(side_effect=RuntimeError(SECRET))):
                    with self.assertRaises(RuntimeError):
                        asyncio.run(services.check_temporal(self.config(), True, self.local))
                continue
            if fail_at == "health":
                client.service_client.check_health.return_value = False
            elif fail_at in ("namespace-denied", "namespace-not-found"):
                status = RPCStatusCode.PERMISSION_DENIED if fail_at.endswith("denied") else RPCStatusCode.NOT_FOUND
                client.workflow_service.describe_namespace.side_effect = RPCError(SECRET, status, b"")
            elif fail_at == "namespace-wrong":
                client.workflow_service.describe_namespace.return_value.namespace_info.name = "different"
            else:
                client.workflow_service.describe_namespace.return_value.namespace_info.state = 2
            with self.assertRaises((services.CheckFailure, RPCError)):
                self.check(client)
            client.get_workflow_handle.assert_not_called()

    def test_all_service_exceptions_are_redacted_in_worker_result(self):
        with patch.object(services, "check_postgres", side_effect=RuntimeError(SECRET)), \
             patch.object(services, "check_azurite", side_effect=ValueError(SECRET)), \
             patch.object(services, "check_temporal", AsyncMock(side_effect=RPCError(SECRET, RPCStatusCode.PERMISSION_DENIED, SECRET.encode()))):
            payload = asyncio.run(services.service_payload(self.config(), True, self.local))
        self.assertFalse(payload["ok"])
        self.assertEqual(len(payload["messages"]), 3)
        self.assertNotIn(SECRET, json.dumps(payload))
        self.assertIn("PERMISSION_DENIED", json.dumps(payload))


class DeadlineAndAggregateTests(Scratch):
    def command(self, text, *args):
        return [sys.executable, "-B", "-c", text, *map(str, args)]

    def test_failed_child_still_checks_receipts(self):
        self.record()
        before = self.receipt.read_bytes()
        for command in (self.command("raise SystemExit(7)"), self.command("print('not JSON')"),
                        self.command('print(\'{"ok": false, "messages": ["FAIL synthetic"]}\')')):
            code, output = self.run_checks(command)
            self.assertEqual(code, 1)
            self.assertIn("verification receipts unchanged", output)
            self.assertEqual(self.receipt.read_bytes(), before)

    def test_receipt_change_is_detected_on_failure_and_timeout(self):
        for stuck in (False, True):
            self.record()
            text = "import pathlib,sys,time; pathlib.Path(sys.argv[1]).write_text('changed'); "
            text += "time.sleep(60)" if stuck else "raise SystemExit(7)"
            code, output = self.run_checks(self.command(text, self.receipt), timeout=0.8)
            self.assertEqual(code, 1)
            self.assertIn("FAIL verification receipts", output)

    def test_stuck_child_is_killed_reaped_and_unrelated_process_survives(self):
        self.record()
        original = self.receipt.read_bytes()
        pid_file = self.root / "pid"
        unrelated = subprocess.Popen(self.command("import time; time.sleep(60)"), start_new_session=True)
        try:
            text = "import os,pathlib,signal,sys,time; pathlib.Path(sys.argv[1]).write_text(str(os.getpid())); signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
            started = time.monotonic()
            code, output = self.run_checks(self.command(text, pid_file), timeout=0.8)
            self.assertLess(time.monotonic() - started, 0.8 + services.CLEANUP_ALLOWANCE)
            self.assertEqual(code, 1)
            self.assertIn("wall-clock deadline", output)
            self.assertIn("verification receipts unchanged", output)
            self.assertEqual(self.receipt.read_bytes(), original)
            self.assertIsNone(unrelated.poll())
            with self.assertRaises(ProcessLookupError):
                os.kill(int(pid_file.read_text()), 0)
        finally:
            unrelated.terminate()
            unrelated.wait(timeout=5)

    def test_snapshot_failure_is_bounded_and_preservation_not_claimed(self):
        self.receipt.mkdir()
        code, output = self.run_checks(self.command('print(\'{"ok": true, "messages": []}\')'))
        self.assertEqual(code, 1)
        self.assertIn("preservation could not be verified", output)
        self.assertNotIn("PASS verification", output)

    def test_aggregate_forwards_options_and_does_not_continue_after_service_failure(self):
        with patch.object(environment, "run_checks", return_value=1) as check, \
             patch.object(environment, "run") as run:
            self.assertEqual(environment.main(["--config", str(self.path), "--timeout", "2", "--inspect-historical-temporal"]), 1)
        check.assert_called_once_with(self.path, True, 2.0)
        run.assert_not_called()

    def test_aggregate_uses_actual_hard_boundary_for_a_stuck_service(self):
        self.record()
        text = "import signal,time; signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
        def bounded(config, history, timeout):
            return services.run_checks(config, history, timeout, local=self.local, _command=self.command(text))
        output = io.StringIO()
        started = time.monotonic()
        with patch.object(environment, "run_checks", side_effect=bounded), \
             patch.object(environment, "run") as run, contextlib.redirect_stdout(output):
            code = environment.main(["--timeout", "0.8"])
        self.assertEqual(code, 1)
        self.assertLess(time.monotonic() - started, 0.8 + services.CLEANUP_ALLOWANCE)
        self.assertIn("verification receipts unchanged", output.getvalue())
        run.assert_not_called()

    def test_aggregate_setup_subprocess_failure_propagates(self):
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(RuntimeError):
                environment.run(*self.command("raise SystemExit(9)"), timeout=2)

    def test_handled_termination_reaps_worker_and_audits_receipts(self):
        self.record()
        original = self.receipt.read_bytes()
        pid_file = self.root / "worker-pid"
        worker = "import os,pathlib,signal,sys,time; pathlib.Path(sys.argv[1]).write_text(str(os.getpid())); signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
        driver = "from pathlib import Path; import sys; from scripts._process import run_cli; from scripts.check_services import run_checks; run_cli(lambda: run_checks(local=Path(sys.argv[1]), _command=[sys.executable,'-c',sys.argv[2],sys.argv[3]]))"
        process = subprocess.Popen(self.command(driver, self.local, worker, pid_file), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        try:
            deadline = time.monotonic() + 5
            while not pid_file.exists() and time.monotonic() < deadline:
                time.sleep(0.01)
            self.assertTrue(pid_file.exists())
            process.terminate()
            output, _ = process.communicate(timeout=services.CLEANUP_ALLOWANCE)
            self.assertEqual(process.returncode, 143)
            self.assertIn(b"verification receipts unchanged", output)
            self.assertEqual(self.receipt.read_bytes(), original)
            with self.assertRaises(ProcessLookupError):
                os.kill(int(pid_file.read_text()), 0)
        finally:
            if process.poll() is None:
                process.kill()
                process.wait(timeout=2)

    def test_process_group_cleanup_stops_owned_descendants(self):
        pid_file = self.root / "descendant"
        child = "import os,pathlib,signal,sys,time; pathlib.Path(sys.argv[1]).write_text(str(os.getpid())); signal.signal(signal.SIGTERM, signal.SIG_IGN); time.sleep(60)"
        parent = "import subprocess,sys,time; subprocess.Popen([sys.executable,'-c',sys.argv[1],sys.argv[2]]); time.sleep(60)"
        result = run_process(self.command(parent, child, pid_file), timeout=0.8)
        self.assertTrue(result.timed_out)
        pid = int(pid_file.read_text())
        proc = Path(f"/proc/{pid}/stat")
        deadline = time.monotonic() + 2
        while proc.exists() and proc.read_text().split()[2] != "Z" and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue(not proc.exists() or proc.read_text().split()[2] == "Z")


if __name__ == "__main__":
    unittest.main()

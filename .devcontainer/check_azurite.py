# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["azure-storage-blob==12.30.1"]
# ///
"""Synthetic Blob SDK probe: seed, normal Mac service restart, verify, cleanup."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
from urllib.error import HTTPError
from urllib.request import Request, ProxyHandler, build_opener
import uuid

from azure.core.exceptions import AzureError, ResourceNotFoundError
from azure.storage.blob import BlobServiceClient

LOCAL = Path(__file__).resolve().parent.parent / "local-data/azurite"
STATE = LOCAL / "blob-probe.json"
API_VERSION = "2025-11-05"
ENDPOINT = "http://gre-azurite:10000/gredev"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def content(token):
    return b"GRE synthetic Blob Storage probe\n" + token.encode() + bytes(range(256)) * 32


def verify_blob(service, state):
    container = service.get_container_client(state["container"])
    require(container.get_container_properties().metadata == {"gre_probe": state["token"]},
            "Container ownership metadata mismatch")
    require(container.get_container_access_policy()["public_access"] is None,
            "Probe container must remain private")
    blob = container.get_blob_client("payload.bin")
    downloaded = blob.download_blob().readall()
    properties = blob.get_blob_properties()
    require(downloaded == content(state["token"]) == (LOCAL / "payload.bin").read_bytes(),
            "Downloaded bytes differ from synthetic file")
    require(properties.metadata == state["metadata"], "Blob metadata mismatch")
    require(properties.etag == state["etag"], "Blob ETag changed")
    require(properties.last_modified.isoformat() == state["last_modified"], "Blob modified time changed")
    print(f"PASS authenticated bytes, metadata, ETag: {state['container']}/payload.bin", flush=True)
    # No SDK credentials, SAS, Authorization header, cookies, or proxy are used.
    request = Request(blob.url, headers={"x-ms-version": API_VERSION})
    try:
        with build_opener(ProxyHandler({})).open(request, timeout=10) as response:
            raise RuntimeError(f"Anonymous read unexpectedly returned HTTP {response.status}")
    except HTTPError as error:
        require(error.code == 403 and error.headers.get("x-ms-error-code") == "AuthorizationFailure",
                f"Unexpected anonymous response: HTTP {error.code}, {error.headers.get('x-ms-error-code')}")
        print("PASS unauthenticated read rejected: HTTP 403 AuthorizationFailure", flush=True)


def main(action):
    require(platform.system() == "Linux" and platform.machine() == "aarch64",
            "Run this probe inside the ARM64 development container")
    credential_line = (LOCAL / ".env").read_text().strip()
    prefix = "AZURITE_ACCOUNTS=gredev:"
    require(credential_line.startswith(prefix), "Unexpected emulator account configuration")
    with BlobServiceClient(ENDPOINT, credential={"account_name": "gredev", "account_key": credential_line[len(prefix):]},
                           api_version=API_VERSION, retry_total=0, connection_timeout=5, read_timeout=10) as service:
        require(service.api_version == API_VERSION, "SDK API version mismatch")
        service.get_service_properties()
        print(f"PASS authenticated SDK connectivity: Python {platform.python_version()}, API {API_VERSION}", flush=True)
        if action == "connect":
            return
        if action == "seed":
            require(not STATE.exists(), "Probe receipt exists; verify/cleanup it first")
            token = str(uuid.uuid4())
            payload = content(token)
            state = {"token": token, "container": f"gre-probe-{token}",
                     "server": json.loads((LOCAL / "server.json").read_text()),
                     "metadata": {"gre_probe": token, "purpose": "synthetic-environment-check",
                                  "sha256": hashlib.sha256(payload).hexdigest()}}
            (LOCAL / "payload.bin").write_bytes(payload)
            STATE.write_text(json.dumps(state, indent=2) + "\n")
            container = service.create_container(state["container"], metadata={"gre_probe": token}, public_access=None)
            blob = container.get_blob_client("payload.bin")
            with (LOCAL / "payload.bin").open("rb") as source:
                blob.upload_blob(source, metadata=state["metadata"], overwrite=False)
            properties = blob.get_blob_properties()
            state.update(etag=properties.etag, last_modified=properties.last_modified.isoformat())
            STATE.write_text(json.dumps(state, indent=2) + "\n")
            verify_blob(service, state)
            print(f"PASS seeded {len(payload)} bytes; SHA256 {state['metadata']['sha256']}", flush=True)
        else:
            state = json.loads(STATE.read_text())
            require(state["container"] == f"gre-probe-{uuid.UUID(state['token'])}", "Invalid probe resource identity")
            if action == "verify":
                server = json.loads((LOCAL / "server.json").read_text())
                require(server["container_id"] == state["server"]["container_id"] and
                        server["started_at"] != state["server"]["started_at"],
                        "Expected a normal restart of the same Azurite container")
                verify_blob(service, state)
                state["verified_server"] = server
                STATE.write_text(json.dumps(state, indent=2) + "\n")
                print(f"PASS same blob survived restart: {state['server']['started_at']} -> {server['started_at']}", flush=True)
            else:
                container = service.get_container_client(state["container"])
                require(container.get_container_properties().metadata == {"gre_probe": state["token"]},
                        "Refusing cleanup: container ownership mismatch")
                blobs = list(container.list_blobs(include=["metadata"]))
                require(all(b.name == "payload.bin" and b.metadata == state["metadata"] for b in blobs),
                        "Refusing cleanup: unexpected blobs or metadata in probe container")
                before = {c.name: dict(c.metadata or {}) for c in service.list_containers(include_metadata=True)}
                # Exact UUID/ownership-checked container only; never bulk-delete by prefix.
                container.delete_container()
                try:
                    container.get_container_properties()
                    raise RuntimeError("Probe container still exists after cleanup")
                except ResourceNotFoundError:
                    pass
                after = {c.name: dict(c.metadata or {}) for c in service.list_containers(include_metadata=True)}
                require(after == {k: v for k, v in before.items() if k != state["container"]},
                        "Unexpected change to other containers during cleanup")
                STATE.unlink()
                (LOCAL / "payload.bin").unlink(missing_ok=True)
                print(f"PASS cleanup removed only {state['container']}; other container names/metadata unchanged", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("connect", "seed", "verify", "cleanup"))
    try:
        main(parser.parse_args().action)
    except (AzureError, OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"GRE Azurite check: FAIL — {error}", file=sys.stderr)
        sys.exit(1)

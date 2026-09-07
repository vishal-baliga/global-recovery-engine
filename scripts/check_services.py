"""Concurrent read-only checks through the shared Python dependency environment."""
import asyncio
import hashlib
import json
from pathlib import Path

from alembic.migration import MigrationContext
from azure.storage.blob import BlobServiceClient
from sqlalchemy import URL, create_engine, text
from temporalio.client import Client, WorkflowExecutionStatus

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / "local-data"


def check_postgres():
    url = URL.create("postgresql+psycopg", username="gre_dev",
                     password=(LOCAL / "postgres/password").read_text().strip(),
                     host="gre-postgres", port=5432, database="gre_dev")
    engine = create_engine(url, connect_args={"connect_timeout": 5, "options": "-c statement_timeout=10000"})
    try:
        with engine.connect() as connection:
            connection.execute(text("SET TRANSACTION READ ONLY"))
            database, version = connection.execute(text("SELECT current_database(), current_setting('server_version')")).one()
            if database != "gre_dev" or not version.startswith("18.6"):
                raise RuntimeError("Unexpected PostgreSQL database/version")
            heads = MigrationContext.configure(connection).get_current_heads()
            print(f"PASS SQLAlchemy/Psycopg read-only PostgreSQL {version}; Alembic revision read: {heads}", flush=True)
    finally:
        engine.dispose()


def check_azurite():
    account = (LOCAL / "azurite/.env").read_text().strip()
    prefix = "AZURITE_ACCOUNTS=gredev:"
    if not account.startswith(prefix):
        raise RuntimeError("Unexpected local emulator account configuration")
    with BlobServiceClient("http://gre-azurite:10000/gredev",
                           credential={"account_name": "gredev", "account_key": account[len(prefix):]},
                           api_version="2025-11-05", retry_total=0,
                           connection_timeout=5, read_timeout=10) as client:
        client.get_service_properties()
        containers = list(client.list_containers())
        print(f"PASS authenticated Azurite API {client.api_version}; read-only listing: {len(containers)} containers", flush=True)


async def check_temporal():
    client = await Client.connect("gre-temporal:7233", namespace="default")
    if not await client.service_client.check_health():
        raise RuntimeError("Temporal service unhealthy")
    receipt = LOCAL / "temporal/workflow-probe.json"
    if receipt.exists():
        state = json.loads(receipt.read_text())
        if "verification" in state:
            handle = client.get_workflow_handle(state["workflow_id"], run_id=state["run_id"])
            info = await handle.describe()
            if info.status != WorkflowExecutionStatus.COMPLETED or info.run_id != state["run_id"]:
                raise RuntimeError("Recorded Temporal probe is no longer the expected completed run")
            print("PASS Temporal connectivity; recorded completed workflow/run preserved", flush=True)
            return
    print("PASS Temporal connectivity (no retained completed probe receipt to check)", flush=True)


async def main():
    receipts = [*LOCAL.glob("*/server.json"), LOCAL / "temporal/workflow-probe.json"]
    before = {path: hashlib.sha256(path.read_bytes()).digest() for path in receipts if path.exists()}
    await asyncio.wait_for(asyncio.gather(asyncio.to_thread(check_postgres), check_temporal(),
                                         asyncio.to_thread(check_azurite)), timeout=30)
    if any(not path.exists() or hashlib.sha256(path.read_bytes()).digest() != digest for path, digest in before.items()):
        raise RuntimeError("An existing service verification receipt changed during checks")
    print("PASS all three services accessible in the shared environment; verification receipts unchanged", flush=True)


if __name__ == "__main__":
    asyncio.run(main())

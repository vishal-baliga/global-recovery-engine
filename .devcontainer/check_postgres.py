# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["psycopg[binary]==3.3.5"]
# ///
"""Synthetic environment probe; Docker restart is performed separately on the Mac."""
import argparse
import json
from pathlib import Path
import sys
import uuid

import psycopg

ROOT = Path(__file__).resolve().parent.parent
LOCAL = ROOT / "local-data/postgres"
STATE = LOCAL / "restart-probe.json"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("connect", "seed", "verify", "cleanup"))
    args = parser.parse_args()
    password = (LOCAL / "password").read_text().strip()
    with psycopg.connect(host="gre-postgres", port=5432, dbname="gre_dev",
                         user="gre_dev", password=password, connect_timeout=5) as conn:
        version, started, data_dir = conn.execute(
            "SELECT version(), pg_postmaster_start_time()::text, current_setting('data_directory')"
        ).fetchone()
        if conn.info.server_version != 180006:
            raise RuntimeError(f"Expected PostgreSQL 18.6, found {conn.info.server_version}")
        if 'aarch64' not in version or data_dir != '/var/lib/postgresql/18/docker':
            raise RuntimeError(f"Unexpected architecture or data directory: {version}; {data_dir}")
        print(f"PASS connection from development container: {version}")
        print(f"PASS PostgreSQL data directory: {data_dir}")
        if args.action == "seed":
            if STATE.exists():
                raise RuntimeError("A restart probe already exists; verify/cleanup it before reseeding.")
            token = str(uuid.uuid4())
            conn.execute("CREATE SCHEMA IF NOT EXISTS gre_environment_check")
            conn.execute("""CREATE TABLE IF NOT EXISTS gre_environment_check.restart_probe (
                id uuid PRIMARY KEY, payload text NOT NULL)""")
            conn.execute("INSERT INTO gre_environment_check.restart_probe VALUES (%s, %s)",
                         (token, "GRE synthetic persistence probe"))
            conn.commit()
            STATE.write_text(json.dumps({"id": token, "started": started}) + "\n")
            print(f"PASS committed synthetic record {token}; restart PostgreSQL on the Mac next.")
        elif args.action in ("verify", "cleanup"):
            state = json.loads(STATE.read_text())
            if args.action == "verify":
                row = conn.execute("SELECT payload FROM gre_environment_check.restart_probe WHERE id = %s",
                                   (state["id"],)).fetchone()
                if row != ("GRE synthetic persistence probe",):
                    raise RuntimeError("Synthetic record missing or changed after restart.")
                if started == state["started"]:
                    raise RuntimeError("PostgreSQL has not restarted since the record was seeded.")
                print(f"PASS synthetic record {state['id']} survived PostgreSQL restart")
                print(f"Server start changed: {state['started']} -> {started}")
            else:
                conn.execute("DELETE FROM gre_environment_check.restart_probe WHERE id = %s", (state["id"],))
                conn.commit()
                STATE.unlink()
                print("PASS removed this probe record and local receipt")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, RuntimeError, psycopg.Error) as exc:
        print(f"GRE PostgreSQL check: FAIL — {exc}", file=sys.stderr)
        sys.exit(1)

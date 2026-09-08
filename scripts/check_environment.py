"""Combined setup check. Run from the repository: uv run --locked python -m scripts.check_environment."""
import argparse
import asyncio
import os
from pathlib import Path
import socket
import subprocess
import sys
import time

import httpx

from fixtures.api.app import app
from scripts._process import run_cli, run_process
from scripts.check_services import SafeParser, add_service_arguments, run_checks
from scripts.export_openapi import main as export_openapi

ROOT = Path(__file__).resolve().parent.parent


def run(*args, timeout=180):
    result = run_process(list(args), timeout=timeout, cwd=ROOT,
                         env={**os.environ, "NEXT_TELEMETRY_DISABLED": "1"})
    print(result.output, end="", flush=True)
    if result.returncode:
        raise RuntimeError("Setup subprocess failed or exceeded its wall-clock deadline")


async def check_api():
    async with httpx.AsyncClient(transport=httpx.ASGITransport(app=app), base_url="http://fixture") as client:
        response = await client.post("/setup/echo", json={"message": "synthetic-check"})
        if response.status_code != 200 or response.json() != {"message": "synthetic-check", "length": 15}:
            raise RuntimeError("FastAPI request/response mismatch")
        if (await client.post("/setup/echo", json={"message": ""})).status_code != 422:
            raise RuntimeError("Pydantic accepted an invalid request")
    print("PASS FastAPI request/response and Pydantic invalid-input rejection", flush=True)


def check_generated_client():
    # Bind an ephemeral loopback port before launching Uvicorn; no port race or host exposure.
    with socket.socket() as listener:
        listener.bind(("127.0.0.1", 0))
        listener.listen()
        base_url = f"http://127.0.0.1:{listener.getsockname()[1]}"
        server = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "fixtures.api.app:app", "--fd", str(listener.fileno()),
             "--no-access-log", "--log-level", "warning"],
            cwd=ROOT, pass_fds=(listener.fileno(),))
        try:
            with httpx.Client(trust_env=False, timeout=1) as client:
                for _ in range(100):
                    if server.poll() is not None:
                        raise RuntimeError("Fixture API server exited before readiness")
                    try:
                        if client.get(base_url + "/openapi.json").status_code == 200:
                            break
                    except httpx.TransportError:
                        pass
                    time.sleep(0.1)
                else:
                    raise RuntimeError("Fixture API readiness timed out")
            run("pnpm", "check:client", base_url)
        finally:
            server.terminate()
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait(timeout=1)


def main(argv=None):
    parser = SafeParser(description=__doc__)
    add_service_arguments(parser)
    parser.add_argument("--_phase", choices=("api", "export", "client"), help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    try:
        if args._phase:
            if args._phase == "api":
                asyncio.run(check_api())
            elif args._phase == "export":
                export_openapi()
            else:
                check_generated_client()
            return 0
        # The same supervisor and receipt-finalization path as the standalone CLI.
        if run_checks(args.config, args.inspect_historical_temporal, args.timeout):
            return 1
        for phase in ("api", "export"):
            run(sys.executable, "-B", "-m", "scripts.check_environment", "--_phase", phase)
        run("pnpm", "generate:client")
        run("pnpm", "typecheck")
        run(sys.executable, "-B", "-m", "scripts.check_environment", "--_phase", "client")
        run("pnpm", "build", timeout=300)
        print("GRE combined dependency/environment check: PASS", flush=True)
        return 0
    except Exception:
        print("FAIL combined setup check (details withheld)", flush=True)
        return 1


if __name__ == "__main__":
    run_cli(main)

"""Combined setup check. Run from the repository: uv run --locked python -m scripts.check_environment."""
import asyncio
import os
from pathlib import Path
import socket
import subprocess
import sys
import time

import httpx

from fixtures.api.app import app
from scripts.check_services import main as check_services
from scripts.export_openapi import main as export_openapi

ROOT = Path(__file__).resolve().parent.parent


def run(*args, timeout=180):
    subprocess.run(args, cwd=ROOT, check=True, timeout=timeout,
                   env={**os.environ, "NEXT_TELEMETRY_DISABLED": "1"})


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
                server.wait()


def main():
    asyncio.run(check_services())
    asyncio.run(check_api())
    export_openapi()
    run("pnpm", "generate:client")
    run("pnpm", "typecheck")
    check_generated_client()
    run("pnpm", "build", timeout=300)
    print("GRE combined dependency/environment check: PASS", flush=True)


if __name__ == "__main__":
    main()

"""Verify final lockfiles in empty temporary environments without touching the working install."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent.parent
MANIFESTS = (
    ".python-version", "pyproject.toml", "uv.lock", "package.json", "pnpm-lock.yaml",
    "pnpm-workspace.yaml", "fixtures/web/package.json", "packages/api-client/package.json",
)


def main():
    with tempfile.TemporaryDirectory(prefix=".gre-env-check-", dir=ROOT) as directory:
        scratch = Path(directory)
        for name in MANIFESTS:
            destination = scratch / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, destination)
        env = {**os.environ, "CI": "true", "UV_PROJECT_ENVIRONMENT": str(scratch / ".venv")}
        env.pop("VIRTUAL_ENV", None)
        subprocess.run(["uv", "sync", "--locked"], cwd=scratch, env=env, check=True, timeout=180)
        subprocess.run(["pnpm", "install", "--frozen-lockfile"], cwd=scratch, env=env, check=True, timeout=180)
        for name in MANIFESTS:
            if (scratch / name).read_bytes() != (ROOT / name).read_bytes():
                raise RuntimeError(f"Fresh installation changed {name}")
    print("PASS fresh uv sync --locked and pnpm install --frozen-lockfile; manifests/locks unchanged")


if __name__ == "__main__":
    main()

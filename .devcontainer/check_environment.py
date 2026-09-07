"""Check the installed GRE container toolchain without external service calls."""

import argparse
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
import tempfile


def run(*command):
    result = subprocess.run(
        command, capture_output=True, text=True, timeout=60, check=False
    )
    if result.returncode:
        detail = (result.stderr or result.stdout).strip()
        raise RuntimeError(f"{command[0]} failed ({result.returncode}): {detail}")
    return result.stdout.strip()


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--expect-arch", choices=("arm64", "amd64"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    config = json.loads((root / ".devcontainer/devcontainer.json").read_text())
    pins = config["build"]["args"]
    machine = platform.machine().lower()
    arch = {"aarch64": "arm64", "arm64": "arm64", "x86_64": "amd64"}.get(machine)

    require(platform.system() == "Linux", "Run this check inside the GRE container.")
    require(arch is not None, f"Unsupported container architecture: {machine}")
    require(os.geteuid() != 0, "The development session must run as a non-root user.")
    if args.expect_arch:
        require(arch == args.expect_arch, f"Expected {args.expect_arch}; found {arch}.")

    observed = {
        "PYTHON_VERSION": platform.python_version(),
        "NODE_VERSION": run("node", "--version").removeprefix("v"),
        "PNPM_VERSION": run("pnpm", "--version"),
    }
    uv_output = run("uv", "--version")
    match = re.match(r"uv (\d+\.\d+\.\d+)\b", uv_output)
    require(match is not None, f"Unexpected uv version output: {uv_output}")
    observed["UV_VERSION"] = match.group(1)
    for name, actual in observed.items():
        require(actual == pins[name], f"{name}: expected {pins[name]}, found {actual}.")
        print(f"PASS {name}: {actual}", flush=True)

    node_arch = run("node", "-p", "process.platform + '/' + process.arch")
    expected_node_arch = "x64" if arch == "amd64" else "arm64"
    require(node_arch == f"linux/{expected_node_arch}", "Node/Python architecture mismatch.")
    print(run("git", "--version"), flush=True)
    print(f"npm {run('npm', '--version')}", flush=True)

    # Exercise project-volume write access, a real Python venv, and pnpm execution.
    # The context manager removes only this uniquely created scratch directory.
    with tempfile.TemporaryDirectory(prefix=".gre-env-check-", dir=root) as scratch:
        temporary = Path(scratch)
        venv = temporary / "venv"
        run("uv", "venv", "--python", sys.executable, str(venv))
        result = run(
            str(venv / "bin/python"), "-c",
            "import ssl, sqlite3, sys; "
            "assert sys.prefix != sys.base_prefix; print('venv ready')",
        )
        require(result == "venv ready", "Virtual-environment execution failed.")
        print("PASS Python virtual environment, SSL, and SQLite", flush=True)

        node_project = temporary / "node-project"
        node_project.mkdir()
        (node_project / "package.json").write_text(json.dumps({
            "name": "gre-environment-check", "private": True,
            "packageManager": f"pnpm@{pins['PNPM_VERSION']}",
        }))
        # pnpm 11 defaults to installing before exec. Keep this dependency-free
        # smoke check local to the installed runtime and its temporary project.
        (node_project / "pnpm-workspace.yaml").write_text(
            "verifyDepsBeforeRun: false\nupdateNotifier: false\n"
        )
        result = run(
            "pnpm", "--dir", str(node_project), "exec", "node", "--eval",
            "process.stdout.write('pnpm ready')",
        )
        require(result == "pnpm ready", "pnpm could not execute the Node runtime.")
        print("PASS pnpm execution and workspace write access", flush=True)

    print(f"GRE development toolchain: PASS (linux/{arch})")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, subprocess.TimeoutExpired, KeyError, ValueError) as error:
        print(f"GRE development toolchain: FAIL — {error}", file=sys.stderr)
        sys.exit(1)

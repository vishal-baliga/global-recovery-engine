"""Bound commands and clean up only the process group created for each command."""
from dataclasses import dataclass
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import time

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class ProcessResult:
    returncode: int
    output: str
    timed_out: bool = False


def _cleanup(process):
    # Each child starts a new session: never signal the caller's process group.
    for sig, wait in ((signal.SIGTERM, 0.25), (signal.SIGKILL, 0.75)):
        try:
            os.killpg(process.pid, sig)
        except ProcessLookupError:
            pass
        try:
            process.wait(timeout=wait)
        except subprocess.TimeoutExpired:
            continue
    if process.poll() is None:
        raise RuntimeError("Owned subprocess could not be reaped")


def run_process(command, *, timeout, cwd=ROOT, env=None):
    """Return a bounded output tail; timeout includes startup, plus <=1s cleanup."""
    started = time.monotonic()
    # A file avoids pipe deadlocks and unbounded in-memory subprocess output.
    with tempfile.TemporaryFile() as output:
        process = subprocess.Popen(command, cwd=cwd, env=env, start_new_session=True,
                                   stdout=output, stderr=subprocess.STDOUT)
        timed_out = False
        try:
            process.wait(timeout=max(0, timeout - (time.monotonic() - started)))
        except subprocess.TimeoutExpired:
            timed_out = True
        finally:
            _cleanup(process)
        output.seek(0, os.SEEK_END)
        output.seek(max(0, output.tell() - 262144))
        text = output.read().decode("utf-8", errors="replace")
    return ProcessResult(124 if timed_out else process.returncode, text, timed_out)


def run_cli(main):
    """Let an owned CLI unwind cleanup on TERM/interrupt instead of orphaning work."""
    def terminate(signum, frame):
        raise SystemExit(128 + signum)
    previous = signal.signal(signal.SIGTERM, terminate)
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("FAIL check interrupted", flush=True)
        raise SystemExit(130) from None
    finally:
        signal.signal(signal.SIGTERM, previous)

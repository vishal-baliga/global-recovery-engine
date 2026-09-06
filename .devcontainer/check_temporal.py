# /// script
# requires-python = ">=3.14,<3.15"
# dependencies = ["temporalio==1.32.0"]
# ///
"""Run seed, restart Temporal on the Mac, then run resume in a new process."""
import argparse
import asyncio
from datetime import timedelta
import json
from pathlib import Path
import platform
import sys
import uuid

from temporalio.client import Client, WorkflowExecutionStatus
from temporalio.worker import Worker

from temporal_probe_workflow import EnvironmentSignalProbe

LOCAL = Path(__file__).resolve().parent.parent / "local-data/temporal"
STATE = LOCAL / "workflow-probe.json"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


async def main(action):
    require(platform.system() == "Linux" and platform.machine() == "aarch64",
            "Run this probe in the ARM64 development container.")
    identity = f"gre-environment-worker-{uuid.uuid4()}"
    client = await Client.connect("gre-temporal:7233", namespace="default", identity=identity)
    require(await client.service_client.check_health(), "Temporal health check failed")
    print(f"PASS SDK connectivity: Python {platform.python_version()}, linux/arm64", flush=True)
    if action == "connect":
        return
    server = json.loads((LOCAL / "server.json").read_text())
    if action == "seed":
        require(not STATE.exists(), "Probe receipt already exists; resume that execution first.")
        token = str(uuid.uuid4())
        state = {"workflow_id": f"gre-environment-{token}", "token": token,
                 "queue": f"gre-environment-{token}", "worker_identity": identity,
                 "server": server}
    else:
        state = json.loads(STATE.read_text())
        require(server["container_id"] == state["server"]["container_id"],
                "Expected a normal restart of the same Temporal container.")
        require(server["started_at"] != state["server"]["started_at"],
                "Server has not restarted; run the Mac restart helper first.")
        require(identity != state["worker_identity"], "Worker identity must change")
    async with Worker(client, task_queue=state["queue"], workflows=[EnvironmentSignalProbe]):
        if action == "seed":
            handle = await client.start_workflow(
                EnvironmentSignalProbe.run, state["token"], id=state["workflow_id"],
                task_queue=state["queue"], execution_timeout=timedelta(days=1))
            state["run_id"] = handle.first_execution_run_id
            STATE.write_text(json.dumps(state, indent=2) + "\n")
        else:
            handle = client.get_workflow_handle(state["workflow_id"], run_id=state["run_id"])
        description = await handle.describe()
        require(description.run_id == state["run_id"], "Workflow run ID changed")
        require(description.status == WorkflowExecutionStatus.RUNNING, "Workflow is not running")
        require(await handle.query(EnvironmentSignalProbe.is_waiting), "Workflow is not waiting for its signal")
        print(f"PASS waiting workflow: {state['workflow_id']} run={state['run_id']}", flush=True)
        if action == "resume":
            await handle.signal(EnvironmentSignalProbe.release, state["token"])
            result = await handle.result(follow_runs=False)
            require(result == f"GRE synthetic probe completed: {state['token']}", "Unexpected workflow result")
            description = await handle.describe()
            require(description.run_id == state["run_id"] and
                    description.status == WorkflowExecutionStatus.COMPLETED,
                    "Same workflow execution did not complete")
            history = await handle.fetch_history()
            for event_field in ("workflow_execution_started_event_attributes",
                                "workflow_execution_signaled_event_attributes",
                                "workflow_execution_completed_event_attributes"):
                require(sum(event.HasField(event_field) for event in history.events) == 1,
                        f"Expected exactly one {event_field}")
            state["verification"] = {"server": server, "worker_identity": identity, "result": result,
                                     "history_events": len(history.events)}
            STATE.write_text(json.dumps(state, indent=2) + "\n")
            print(f"PASS same execution completed after server and worker restart: {result}", flush=True)
            print(f"Server start: {state['server']['started_at']} -> {server['started_at']}", flush=True)
            print(f"Worker identity: {state['worker_identity']} -> {identity}", flush=True)
            print(f"PASS history: one start, one signal, one completion; {len(history.events)} events", flush=True)
    print("PASS worker shut down cleanly", flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("connect", "seed", "resume"))
    try:
        asyncio.run(asyncio.wait_for(main(parser.parse_args().action), timeout=60))
    except (OSError, ValueError, RuntimeError, TimeoutError) as error:
        print(f"GRE Temporal check: FAIL — {error}", file=sys.stderr)
        sys.exit(1)

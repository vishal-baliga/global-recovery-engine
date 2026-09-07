"""Synthetic workflow used only to verify the local development environment."""
from temporalio import workflow


@workflow.defn
class EnvironmentSignalProbe:
    def __init__(self):
        self.waiting = False
        self.received = None

    @workflow.run
    async def run(self, token: str) -> str:
        self.waiting = True
        await workflow.wait_condition(lambda: self.received is not None)
        if self.received != token:
            raise ValueError("Unexpected synthetic signal payload")
        return f"GRE synthetic probe completed: {token}"

    @workflow.signal
    def release(self, token: str):
        self.received = token

    @workflow.query
    def is_waiting(self) -> bool:
        return self.waiting and self.received is None

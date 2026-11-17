"""Proposed application boundary for Kinesis to Kafka Bridge Lab.

This is a design scaffold, not a functional SDK or service. Refine the return
models during milestone 1; dict/list types leave that decision open deliberately.
"""

class EventBridge:
    def forward(self, record: dict) -> dict:
        """Forward one source record while preserving stable event identity."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")

    def checkpoint(self, shard_id: str, sequence_number: str) -> None:
        """Advance only after the chosen destination durability condition."""
        raise NotImplementedError("Implement this boundary with behavior tests first.")


"""Initial application boundary for Kinesis Kafka Bridge.

The runtime is in development. Refine models and errors alongside the first
implementation; dict/list annotations mark contracts still to be formalized.
"""

class EventBridge:
    def forward(self, record: dict) -> dict:
        """Forward one source record while preserving stable event identity."""
        raise NotImplementedError("Runtime implementation is in development.")

    def checkpoint(self, shard_id: str, sequence_number: str) -> None:
        """Advance only after the chosen destination durability condition."""
        raise NotImplementedError("Runtime implementation is in development.")

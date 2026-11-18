# Functional and quality requirements

Status: proposed requirements, not delivered capabilities.

## Purpose
A streaming integration service for moving records from Amazon Kinesis into Kafka while preserving event identity and making retry and replay behavior observable. Checkpoint ownership and acknowledgement boundaries are central design concerns.

## Target capabilities
- Write a delivery-semantics ADR and identify the crash windows around Kafka acknowledgement and Kinesis checkpointing.
- Implement a local source adapter and destination simulator; preserve source identifiers and schema versions.
- Add real service adapters, durable per-shard checkpoints, bounded batches and bounded memory. Start with a small isolated AWS experiment.
- Handle retry exhaustion, quarantined records, shutdown, shard assignment and resharding. Confirm behavior against real Kinesis because a simulator cannot prove it.
- Add source-age, destination-lag and retry metrics. Run outage/recovery tests and document replay and teardown procedures.

## Acceptance criteria
- All accepted event IDs reach the destination eventually in the measured recovery test; duplicates are counted.
- Memory stays bounded during a destination outage.
- A checkpoint cannot silently skip an unacknowledged record.
- Recovery report separates simulator findings from actual cloud findings.

## Cross-cutting requirements
- Reproducible configuration and documented version requirements.
- Explicit invalid-input, authorization and dependency-failure behavior.
- Clearly defined durable state, retries and concurrency boundaries.
- Observable operations with bounded, non-sensitive diagnostic output.
- A documented resource lifecycle, recovery procedure and cleanup path.

## Scope control
This repository owns its implementation and contracts. Optional integrations with other personal projects use versioned interfaces. Sample data is synthetic. External accounts and paid services are not required for the current source checks.

# ADR 0001: System boundaries and implementation approach

Status: proposed.

## Context
A streaming integration service for moving records from Amazon Kinesis into Kafka while preserving event identity and making retry and replay behavior observable. Checkpoint ownership and acknowledgement boundaries are central design concerns.

## Questions
- At-least-once delivery and downstream deduplication
- Checkpoint ownership and shard coordination
- Quarantine versus blocking a shard

## Alternatives
- A local implementation with synthetic external adapters.
- An integrated deployment with real dependencies in an isolated environment.
- A smaller implementation that preserves the core invariant.

## Decision
Pending. Record the selected option, rejected alternatives and rationale before implementing external adapters.

## Consequences
Assess correctness, operational complexity, cost, security boundaries, recovery and maintenance. Define the concrete constraint that would justify revisiting the decision.

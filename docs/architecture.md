# Architecture

Status: proposed. Components shown below are implementation targets.

## Product context
A streaming integration service for moving records from Amazon Kinesis into Kafka while preserving event identity and making retry and replay behavior observable. Checkpoint ownership and acknowledgement boundaries are central design concerns.

## Component view
```text
Synthetic source -> Kinesis shards -> Bridge worker -> Kafka
                                         |
                                         +-> checkpoint / quarantine / metrics
```

## Design decisions
- At-least-once delivery and downstream deduplication
- Checkpoint ownership and shard coordination
- Quarantine versus blocking a shard

Record decisions and alternatives in [ADR 0001](adr/0001-system-boundaries.md). Define authoritative state, acknowledgement boundaries, identities, retry behavior and recovery ownership before implementing adapters.

## Interface boundary
`src/kinesis_kafka_bridge/interfaces.py` defines the initial application boundary. Return models and error contracts remain to be specified. These interfaces do not implement the component graph.

## Integration boundaries
Local adapters and synthetic fixtures precede external integrations. Every live adapter needs an explicit identity, permission scope, timeout strategy and observability contract. Separate user-supplied content from execution authority.

## Deployment design
Document topology, dependency versions, configuration and state persistence alongside the first executable delivery. Record what local environments cannot establish about availability, ordering or durability.

## Compatibility
Version interfaces and fixtures when their semantics change. Sibling projects are optional integrations, not implicit filesystem dependencies.

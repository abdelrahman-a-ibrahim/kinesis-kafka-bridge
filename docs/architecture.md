# Architecture brief

Status: proposed, not implemented.

## Scenario
Bridge synthetic attendance events from Kinesis into Kafka. Design for retries, duplicate delivery, shard changes and a destination outage. Do not claim an atomic transaction across the two services.

## System boundary
```text
Synthetic source -> Kinesis shards -> Bridge worker -> Kafka
                                         |
                                         +-> checkpoint / quarantine / metrics
```

The first implementation must run against synthetic inputs or a local adapter. Add live infrastructure only as a separately documented step. Describe the trust boundary between the interface, persistence and any external system.

## Decisions to resolve
1. At-least-once delivery and downstream deduplication
2. Checkpoint ownership and shard coordination
3. Quarantine versus blocking a shard

For each decision, record alternatives, rejected options, operational cost, failure behavior and the condition under which you would revisit it. Use [ADR 0001](adr/0001-system-boundaries.md) as a starting point; its status is proposed.

## Before writing adapters
- Identify the authoritative state and the acknowledgement/commit boundary.
- Define stable identifiers, versioning and invalid input handling.
- Describe concurrency, retry and recovery behavior; specify what is atomic and what is not.
- Map identities and permissions. Separate data supplied by a user/tool from execution authority.
- Define observable success, failure and missing telemetry.
- Explain resource cleanup and state retention.

## Diagram assignment
Create your own component diagram plus a sequence diagram for one happy path and one partial-failure path. Label ownership, persistence, identities and acknowledgement points. Diagrams should describe the implemented system when promoted into portfolio evidence.

## Design review prompts
1. Which invariant would be violated by two concurrent requests?
2. What becomes durable before the caller receives success?
3. What can be replayed and what cannot?
4. Which failure does a local simulator fail to reproduce?
5. What is the smallest useful implementation of this design?

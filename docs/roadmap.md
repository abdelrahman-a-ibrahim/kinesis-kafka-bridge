# Delivery roadmap

Status: planned. No delivery stage is complete.

### 1. Contracts and system boundaries

Write a delivery-semantics ADR and identify the crash windows around Kafka acknowledgement and Kinesis checkpointing.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 2. Core implementation

Implement a local source adapter and destination simulator; preserve source identifiers and schema versions.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 3. Integrations and access controls

Add real service adapters, durable per-shard checkpoints, bounded batches and bounded memory. Start with a small isolated AWS experiment.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 4. Recovery and operational behavior

Handle retry exhaustion, quarantined records, shutdown, shard assignment and resharding. Confirm behavior against real Kinesis because a simulator cannot prove it.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

### 5. Release validation

Add source-age, destination-lag and retry metrics. Run outage/recovery tests and document replay and teardown procedures.

- [ ] Implementation
- [ ] Behavior verification and failure coverage
- [ ] Documentation and reproducible results

## Future scope

- Benchmark batch-size and latency tradeoffs
- Trace context across bridge boundaries
- Schema evolution with mixed-version records
- Build an end-to-end reconciliation job

Select and pin implementation dependencies when introduced. Scope is refined through architecture decisions; completion requires working behavior and verification evidence.

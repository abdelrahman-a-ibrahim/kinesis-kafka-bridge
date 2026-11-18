# Verification plan

Runtime behavior tests will be added with the implementation. The current source integrity check does not provide runtime coverage.

## Required behavior coverage
- All accepted event IDs reach the destination eventually in the measured recovery test; duplicates are counted.
- Memory stays bounded during a destination outage.
- A checkpoint cannot silently skip an unacknowledged record.
- Recovery report separates simulator findings from actual cloud findings.

## Failure coverage
- Stop Kafka long enough to exhaust the normal retry budget.
- Crash the bridge after Kafka acknowledgement but before checkpointing.
- Inject a malformed record between valid records.
- Split a source shard during sustained traffic.

Add domain tests, adapter contract tests and integration tests as those components are implemented. Include relevant invalid input, unauthorized access, concurrency, retry and restart scenarios. Real dependency guarantees require real integration evidence; mocks alone cannot establish ordering, replication, consistency or durability.

See [reliability](../docs/reliability.md) for execution/reporting requirements.

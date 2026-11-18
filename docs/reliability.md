# Reliability and failure verification

Status: verification scenarios planned; no results recorded yet.

## Required scenarios
- Stop Kafka long enough to exhaust the normal retry budget.
- Crash the bridge after Kafka acknowledgement but before checkpointing.
- Inject a malformed record between valid records.
- Split a source shard during sustained traffic.

## Verification protocol
For each implemented scenario, document:
1. Commit, runtime versions, environment and topology.
2. Input workload and the expected invariant.
3. Baseline observations, fault injection and timestamps.
4. Observed errors, duplicate effects or state inconsistencies.
5. Recovery steps and measured time to restore behavior.
6. Resource cleanup and remaining limitations.

A simulator establishes application behavior within its assumptions. Real service ordering, consistency, failover and durability claims require verification against the selected dependencies. Distinguish those results in reports.

## Release evidence
- All accepted event IDs reach the destination eventually in the measured recovery test; duplicates are counted.
- Memory stays bounded during a destination outage.
- A checkpoint cannot silently skip an unacknowledged record.
- Recovery report separates simulator findings from actual cloud findings.

Store concise reports in [verification results](verification/README.md). Targets and illustrative fixture values must not be reported as measurements.

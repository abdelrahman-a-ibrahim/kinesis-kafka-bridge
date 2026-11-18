# Kinesis Kafka Bridge

A recoverable Kinesis-to-Kafka event bridge with checkpointing, backpressure and replay controls.

**Status: In development** · Personal project by Abdelrahman Ahmed

## Overview

A streaming integration service for moving records from Amazon Kinesis into Kafka while preserving event identity and making retry and replay behavior observable. Checkpoint ownership and acknowledgement boundaries are central design concerns.

## Current state

The repository currently contains the system design, delivery requirements, a synthetic input fixture and initial Python interfaces. Runtime behavior, service integrations and deployment are planned. Interface methods raise `NotImplementedError`; there is no running application or published runtime benchmark yet.

## Planned capabilities

- Kinesis-to-Kafka forwarding with stable event identities.
- Durable per-shard checkpoints tied to destination acknowledgements.
- Bounded batches, retries and memory use during destination outages.
- Malformed-record quarantine and controlled replay.
- Shard lifecycle handling, lag metrics and reconciliation reports.

Detailed scope is tracked in the [delivery roadmap](docs/roadmap.md) and [requirements](docs/requirements.md).

## Architecture

```text
Synthetic source -> Kinesis shards -> Bridge worker -> Kafka
                                         |
                                         +-> checkpoint / quarantine / metrics
```

This is the proposed component design. See [architecture](docs/architecture.md) for boundaries and [architecture decisions](docs/adr/0001-system-boundaries.md) for the choices still to resolve.

## Technology direction

Amazon Kinesis · Kafka · Python · Checkpoints · Backpressure.

These technologies describe the intended implementation. Dependencies and compatible versions will be pinned when introduced. Optional services are not required by the current source checks.

## Working with the source

```sh
git clone https://github.com/abdelrahman-a-ibrahim/kinesis-kafka-bridge.git
cd kinesis-kafka-bridge
python3 tools/check_project.py
```

Python 3.9+ is sufficient for the current standard-library source check. It parses Python and JSON and checks required project files. It does **not** run an application, validate deployment behavior or establish feature completion.

The initial application boundary is in [`src/kinesis_kafka_bridge/interfaces.py`](src/kinesis_kafka_bridge/interfaces.py). [`examples/scenario.json`](examples/scenario.json) provides a synthetic development input. Installation and runtime commands will be added with the first executable release.

## Quality and reliability

- All accepted event IDs reach the destination eventually in the measured recovery test; duplicates are counted.
- Memory stays bounded during a destination outage.
- A checkpoint cannot silently skip an unacknowledged record.
- Recovery report separates simulator findings from actual cloud findings.

These are acceptance targets. Failure scenarios are specified in [reliability verification](docs/reliability.md); [results](docs/verification/README.md) will be recorded as implementation progresses. Correctness and performance claims must reference an actual environment, workload and commit.

## Development roadmap

- [ ] Contracts and system boundaries
- [ ] Core implementation and behavior tests
- [ ] External adapters and scoped access
- [ ] Failure recovery and operational visibility
- [ ] Reproducible deployment and release validation

See [delivery stages and future scope](docs/roadmap.md). For deployment prerequisites and resource lifecycle, see [operations](docs/operations.md).

## Repository structure

```text
src/kinesis_kafka_bridge/       Initial application interfaces
examples/                  Synthetic development inputs
tests/                     Behavior verification plan
docs/architecture.md       Component design and boundaries
docs/requirements.md       Functional and quality requirements
docs/roadmap.md            Delivery stages and future scope
docs/reliability.md        Failure and recovery scenarios
docs/operations.md         Runtime and deployment plan
docs/verification/         Results as implementation progresses
tools/check_project.py     Source integrity check
```

## Development

Use focused feature branches, add behavior tests with implementation changes and update the relevant architecture decision when guarantees change. Read [CONTRIBUTING.md](CONTRIBUTING.md).

This is an independent personal project. Examples use synthetic data. See [NOTICE.md](NOTICE.md) for licensing status.

## References

- https://docs.aws.amazon.com/streams/latest/dev/introduction.html
- https://kafka.apache.org/documentation/

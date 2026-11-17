# Failure lab

These are planned experiments, not observed results. Begin with disposable local fixtures. For each experiment establish a baseline, inject one fault, record timestamps, verify invariants and perform cleanup.

## Project-specific experiments
1. Stop Kafka long enough to exhaust the normal retry budget.
2. Crash the bridge after Kafka acknowledgement but before checkpointing.
3. Inject a malformed record between valid records.
4. Split a source shard during sustained traffic.

## Experiment record
Copy this block for each run:

- Experiment / commit:
- Date, platform and tool versions:
- Input dataset and deterministic seed where applicable:
- Expected invariant:
- Hypothesis:
- Exact fault and injection command:
- Start/end timestamps:
- Observed behavior and raw output location:
- Lost/duplicate/rejected operations, if applicable:
- Recovery steps and elapsed time:
- Pass/fail against the stated invariant:
- Environment limits / what this does not prove:
- Residual resources and cleanup result:

## Stop conditions
Stop when the fault escapes the disposable boundary, the evidence cannot identify the affected resources, or the planned resource/cost allowance is exceeded. Do not conduct these experiments on shared production systems.

---
name: apple-observability
description: "Diagnose Apple app failures with unified logs, signposts, Instruments, crash symbols and memory graphs."
---

# Diagnose Apple app failures

## Inputs

Identify build, process, workload, symptom, incident window and permitted data.

## Rules

- **OBS-001 — Privacy.** Log phases, error categories and short-lived opaque IDs. Exclude secrets and protected content.
- **OBS-002 — Intervals.** Count a duration only when one operation has a matched start and end. Include failed, cancelled and timed-out attempts.
- **OBS-003 — Diagnosis.** Inspect main-thread samples or waits for hangs, update causes for invalidation, allocations and retainers for growth.
- **OBS-004 — Capture.** Keep originals private and summaries reproducible.
- **OBS-005 — Overhead.** Check whether instrumentation changes the symptom.

## Workflow

1. Reproduce. Check trace coverage or match dSYM and binary UUIDs.
2. Identify the operation or retaining owner. Test one correction.

## Verify

- OBS-001, OBS-004: Before sharing, check for tool version, capture conditions and redaction of sensitive data.
- OBS-002: Cancel mid-interval. Count one matching end.
- OBS-003: Repeat presentation and dismissal. Trace owners surviving teardown.
- OBS-005: Replay on the final build without debugger or temporary fixtures. Compare symptoms.

## Output

Give build, conditions, cause, correction, comparison and unresolved hypotheses.

## References

- [Logs and traces](references/logging-and-traces.md)
- [Memory and crash diagnosis](references/memory-and-crashes.md)

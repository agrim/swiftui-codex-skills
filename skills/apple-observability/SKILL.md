---
name: apple-observability
description: "Diagnose Apple app failures with unified logging, signposts, Instruments traces, crash symbols and memory graphs."
---

# Privacy-safe logs and performance diagnostics

## Inputs

Identify the symptom, build, process, workload, time window and permitted capture data.

## Rules

- **OBS-001 — Limit logged data.** Log phases and error categories. Correlate with short-lived opaque IDs. Exclude credentials and protected content.
- **OBS-002 — Pair interval boundaries.** End each started signpost once on success, failure, cancellation or timeout. Compare durations in consistent units.
- **OBS-003 — Choose a diagnostic.** Inspect samples and waits for hangs, update causes for invalidation, and allocations and retaining paths for memory growth.
- **OBS-004 — Preserve the original.** Keep raw captures private. Record tool version and capture conditions with each summary.
- **OBS-005 — Check instrumentation effects.** Repeat the workload on the final build after removing temporary fixtures and detaching the debugger.

## Workflow

1. Reproduce once. Verify the trace covers the incident or match the dSYM and binary UUIDs.
2. Identify the suspect operation or retaining owner. Test one correction.

## Verify

- OBS-001: Before sharing diagnostics, inspect the export for credentials and protected content.
- OBS-002: Cancel a signposted operation. Its interval has one matching end.
- OBS-003: For suspected retention, repeat presentation and dismissal. Inspect the retaining path of any owner still alive after expected teardown.

## Output

Report the build, capture conditions, observed cause, change, comparison and unresolved hypotheses.

## References

- [Logs, signposts and trace coverage](references/logging-and-traces.md)
- [Retaining paths and crash symbolication](references/memory-and-crashes.md)

---
name: apple-performance-cleanup
description: "Diagnose SwiftUI hitches, slow startup, memory growth and energy use. Verify performance gains and preserve behavior during cleanup."
---

# Apple performance and behavior-preserving cleanup

## Inputs

Identify the affected interaction, symptom, measurements and authorized changes.

## Rules

- **PERF-001 — Record a baseline.** Capture the device, toolchain, build configuration, input size, cache state and metric for the workload.
- **PERF-002 — Locate the cost.** Trace the costly interval to updates, layout, CPU, allocations, I/O or contention.
- **PERF-003 — Preserve behavior.** Keep ordering, identity, cancellation, errors, stale and empty states, persistence and accessibility intact where affected.
- **PERF-004 — Bound resource use.** Define when tasks stop and observers detach. Limit caches, buffers, logging and polling.
- **PERF-005 — Measure the outcome.** Check correctness with behavior tests. Compare matched runs before claiming a speed, memory or energy gain.

## Workflow

1. For a scrolling hitch, align the gesture, SwiftUI updates and main-thread samples on one timeline.
2. Identify the smallest correction. For a requested fix, retain the tests and diagnostics that expose the failure.

## Verify

- PERF-001, PERF-005: For a claimed gain, repeat typical and high-load interactions under matched release-like conditions. Compare the symptom metric and its variation.
- PERF-003: Rerun the affected interaction. Check that its visible result and side effects still match the behavior contract.
- PERF-004: For suspected retention, repeat entry and exit. Inspect memory and owners left alive after teardown.

## Output

Report the bottleneck, change, before/after measurements, behavior results and unmeasured effects.

## References

- [Diagnosis by symptom and behavior-preserving cleanup](references/performance-cleanup-patterns.md)
- [Trace a hitch, frequent updates or slow filtered list](references/trace-led-performance.md)

---
name: apple-performance-cleanup
description: "Profile SwiftUI hitches, startup, memory and energy. Measure gains and preserve behavior during cleanup."
---

# Diagnose performance regressions

## Inputs

Identify symptom, interaction, measurements and scope.

## Rules

- **PERF-001 — Baseline.** Record device, toolchain, build mode, input size, cache state and metric.
- **PERF-002 — Attribution.** Trace the interval to updates, layout, CPU, allocations, I/O or contention.
- **PERF-003 — Behavior.** Preserve ordering, identity, cancellation, errors, stale and empty states, persistence and accessibility.
- **PERF-004 — Lifetime.** Define task and observer lifetimes. Bound caches, buffers, logs and polling.
- **PERF-005 — Gains.** Test behavior. Measure gains against baseline.

## Workflow

1. For a hitch, align the gesture, updates and main-thread samples.
2. Choose the smallest correction. Retain reproducing tests and diagnostics when fixing.

## Verify

- PERF-001, PERF-005: Compare repeated typical and heavy workloads under matched release-like conditions. Report metric variation.
- PERF-002: Within the slow interval, identify the responsible update, sampled function or wait.
- PERF-003: Replay and compare visible results and side effects.
- PERF-004: Repeat entry and exit. Inspect memory and surviving owners.

## Output

Give bottleneck, correction, before/after measurements, behavior results and unmeasured effects.

## References

- [Diagnose by symptom](references/performance-cleanup-patterns.md)
- [Hitches, updates and filtered lists](references/trace-led-performance.md)

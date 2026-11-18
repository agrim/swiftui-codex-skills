---
name: apple-performance-cleanup
description: "Profile SwiftUI hitches, startup, memory and energy. Measure gains and preserve behavior during cleanup."
---

# Find and fix the work that slows an Apple app

Use this to investigate a slow launch, scrolling hitch, or excessive memory or energy use. Choose a change based on the work that causes the symptom.

## Start here

Choose a repeatable action and a measure that reflects the complaint. For photo scrolling, measure hitch duration. For energy drain, reproduce the sustained workload.

## How to proceed

1. **Record a baseline.** Repeat the action with a release-like build. Record device, toolchain, data size and whether the cache is warm. <!-- PERF-001 -->
2. **Find the cost inside the affected interval.** Align the gesture, view updates and main-thread samples or waits. Change the operation that accounts for the delay. <!-- PERF-002 -->
3. **Define what the fix must preserve.** When caching or prefiltering a list, track an edit through reordering. Preserve cancellation, error, empty and stale states, persistence and accessibility. <!-- PERF-003 -->
4. **Specify when work and storage end.** Identify who stops a task, observer or poll and what limits a cache, buffer or log. <!-- PERF-004 -->
5. **Measure again with the same workload.** Retain the reproducing checks and diagnostics. Compare user-visible timing alongside internal counts. <!-- PERF-005 -->

## Check the result

- Repeat typical and heavy workloads under matched conditions. Report the variation and show which sampled operation or wait changed during the slow interval. <!-- PERF-001 PERF-002 PERF-005 -->
- Compare visible results and saved edits. Repeatedly reopen and dismiss the screen. Check that its owner is released and the cache stays bounded. <!-- PERF-003 PERF-004 -->

## What to report

Give the measured bottleneck, the change, before-and-after results, preserved behavior and anything unmeasured.

- [Choose a measurement for the reported symptom](references/performance-cleanup-patterns.md)
- [Investigate hitches, repeated updates and filtered lists](references/trace-led-performance.md)

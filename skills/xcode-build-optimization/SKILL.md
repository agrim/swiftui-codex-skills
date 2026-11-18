---
name: xcode-build-optimization
description: "Reduce Xcode clean, no-change, or edit-build latency. Diagnose compiler hotspots, script phases, target dependencies, and SwiftPM plugins."
---

# Xcode build optimization

## Inputs

Record workload, source revision, target graph, toolchain, destination, configuration, cache policy, and permitted changes.

## Rules

- **XBUILD-001 — Measure elapsed time.** Time clean, no-change, and representative edit builds separately. Parallel task durations can overlap.
- **XBUILD-002 — Match the comparison.** Keep command, dependencies, cache policy, and environment consistent. Retain samples and failures.
- **XBUILD-003 — Trace the critical path.** Use the timeline to identify which dependency delays completion.
- **XBUILD-004 — Fix the owner.** Edit the responsible source, setting, script, or package. Preserve correctness checks and release requirements.
- **XBUILD-005 — Define rollback.** Revert correctness or compatibility regressions. Explain any timing tradeoff before keeping the change.

## Workflow

1. Capture a baseline and identify the limiting task chain.
2. Apply a reversible, authorized change and inspect its effect on the build graph.
3. Repeat the baseline workload. Mark missing timings unavailable.

## Verify

- XBUILD-004: Build and test the candidate. Confirm required resources and generated outputs are current.
- XBUILD-001, XBUILD-002: Compare elapsed samples and spread per workload. Report inconclusive results when variation obscures the change.

## Output

Report samples, elapsed deltas, spread, failures, changed files, and the keep or revert decision.

## References

- [Optimization planning](references/orchestration.md)
- [Build benchmarks](references/benchmarking.md)
- [Diagnose compiler hotspots](references/compiler.md)
- [Settings, scripts, and targets](references/project.md)
- [SwiftPM and generated code](references/packages.md)
- [Verification and rollback](references/verification.md)

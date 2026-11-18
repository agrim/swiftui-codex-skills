---
name: xcode-build-optimization
description: "Diagnose slow Xcode clean, no-change and edit builds, including compiler hotspots, scripts, target dependencies and SwiftPM plugins."
---

# Xcode build optimization

## Inputs

Record workload, revision, toolchain, destination, configuration, cache state and scope.

## Rules

- **XBUILD-001 — Time each workload.** Measure elapsed time separately for clean, unchanged and representative edit builds.
- **XBUILD-002 — Match conditions.** Keep commands, dependencies, caches and environment comparable. Retain failures.
- **XBUILD-003 — Trace delays.** Follow the dependency chain that determines completion. Parallel durations overlap.
- **XBUILD-004 — Fix the owner.** Preserve tests, generated products and release requirements.
- **XBUILD-005 — Set rollback criteria.** Revert correctness or compatibility regressions.

## Workflow

1. Capture repeated baseline samples and locate the limiting task.
2. Make one scoped, reversible change and repeat the workload.

## Verify

- XBUILD-004: Build and test. Change a generator input and inspect the affected output when relevant.
- XBUILD-001, XBUILD-002: Compare elapsed samples and spread. Mark noise-obscured deltas inconclusive.
- XBUILD-003, XBUILD-005: Locate the limiting dependency in both timelines. Reject a speedup that breaks a supported target.

## Output

Report samples, failures, timing tradeoffs and the keep or revert decision.

## References

- [Planning](references/orchestration.md)
- [Benchmarks](references/benchmarking.md)
- [Compiler](references/compiler.md)
- [Scripts and targets](references/project.md)
- [Packages](references/packages.md)
- [Rollback](references/verification.md)

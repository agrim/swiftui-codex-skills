---
name: xcode-build-optimization
description: "Diagnose slow Xcode clean, no-change and edit builds, including compiler hotspots, scripts, target dependencies and SwiftPM plugins."
---

# Find what makes an Xcode build slow

Use this when a team needs to shorten a specific wait, such as rebuilding after a one-line edit. Identify the task responsible before changing the project.

## Start here

Record the command, revision, configuration, toolchain, destination and cache state so you can reproduce the delay.

## How to proceed

1. **Measure the right workload.** Time clean builds, unchanged rebuilds and builds after a representative edit separately. Collect repeated elapsed times for the affected workload. <!-- XBUILD-001 -->
2. **Keep comparisons fair.** Use the same command, dependencies, cache conditions and environment before and after the change. Retain failed runs with their errors. <!-- XBUILD-002 -->
3. **Find what delays completion.** Trace the slowest dependency chain in the timeline. Tasks running alongside it may consume time without delaying the product. <!-- XBUILD-003 -->
4. **Change the input responsible for the delay.** Make one reversible change to the target, script, compiler input or package. Preserve required tests, generated products and Release behavior. <!-- XBUILD-004 -->
5. **Decide whether to keep the change.** Repeat the workload. Revert correctness or compatibility regressions. <!-- XBUILD-005 -->

## Check the result

- Compare elapsed times and their spread. If the difference fits ordinary variation, report it as inconclusive. Compare the limiting task in both timelines. <!-- XBUILD-001 XBUILD-002 XBUILD-003 -->
- Build and test supported targets. After a generator change, edit its input and verify the consumer receives updated output. <!-- XBUILD-004 XBUILD-005 -->

## What to report

Give the workload, timing samples, failures, limiting task and your reason to keep or revert the change.

- [Choosing where to investigate](references/orchestration.md)
- [Comparing clean and incremental builds](references/benchmarking.md)
- [Compiler delays](references/compiler.md)
- [Scripts and target dependencies](references/project.md)
- [Package and plugin delays](references/packages.md)
- [Verifying a fix or reverting it](references/verification.md)

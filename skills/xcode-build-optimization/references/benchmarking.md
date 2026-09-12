# Clean, no-op, and edit-build benchmarks

Keep separate categories: cold dependency setup, clean build with declared cache state, warm no-change build, and a representative source edit followed by a build. Touching a file measures timestamp invalidation, not necessarily the same path as changing API or implementation. Report which stimulus was used and restore it without overwriting concurrent edits.

Record repeated successful samples, median, min/max, failures, sample count, and environment. Do not report only the fastest run, compare different build modes, or silently exclude failed measurements. Warm-up policy belongs in the artifact. A cache-warmed clean build must not be labeled fully cold. A new DerivedData directory does not prove all compiler or package caches are cold.

Use `xcodebuild -showBuildTimingSummary` for task categories and a monotonic timer for elapsed process duration. Keep raw logs. Mark an absent or unrecognized summary as missing evidence rather than zero cost. Never delete a user's shared caches as part of ordinary benchmarking; use an agreed disposable workspace and scoped output directories.

For before/after comparisons, hold toolchain, destination, configuration, signing policy, dependency revisions, workload, and competing load constant. Show spread alongside deltas. Range overlap is a useful caution, not a statistical proof either way. Small samples cannot establish a universal speedup. Increased target count or cache population may trade clean cost for incremental benefit; evaluate the user's actual workload.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

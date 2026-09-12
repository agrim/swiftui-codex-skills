# Build optimization orchestration

Define the objective as developer wait time, CI cost, clean setup, or edit-build latency. Record the source revision, hardware, toolchain, target graph, configuration, destination, and package/cache policy. Choose a representative workload before changing anything.

Separate analysis from source changes. Existing authorization to optimize can cover a scoped fix; do not ask repeatedly for permission already granted. A benchmark-only request permits measurements and agreed artifacts, not package replacement or configuration edits. Running a build can itself execute repository scripts, so establish trust first.

Classify each finding as project-local, toolchain behavior, environment, or unproven. Rank by plausible effect on the measured objective, confidence, risk, and verification cost. Cumulative parallel compiler seconds are not elapsed build time. A large cumulative-to-wall-time ratio does not identify the critical path by itself; inspect the task timeline and dependencies.

A recommendation records: evidence, hypothesis, affected source owner, compatibility, expected direction rather than invented seconds, acceptance criterion, and rollback plan. Report unchanged or inconclusive outcomes honestly. Keep a measured regression eligible for rollback even when a setting is popularly recommended. No setting is universally beneficial across Debug, archive, test, distribution, and supported Xcode versions.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

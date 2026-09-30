# Fix, compare, and report

Apply one coherent hypothesis at a time. Keep source-owned settings and generated project changes together; preserve unrelated work. A successful compile is necessary but does not prove behavior preservation or a build-time gain.

Re-run the original workload and record every retained, reverted, blocked, and inconclusive change. Report elapsed duration separately from total task cost. State sample count, spread, warm-up/cache policy, command differences, and whether each build category improved or regressed.

Acceptance can include lower edit-build latency, deterministic code generation, or preserved distribution symbols. A change valuable for correctness may remain even without speed improvement, but label that rationale. Do not advertise hypothetical future compiler improvements as measured benefit.

Rollback only the scoped experiment, respecting concurrent edits. A broad reset, global cache deletion, forced lockfile update, or loss of debug symbols is not an acceptable shortcut. Finish with a fresh final-candidate check so the last reported green run cannot belong to an earlier worktree.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

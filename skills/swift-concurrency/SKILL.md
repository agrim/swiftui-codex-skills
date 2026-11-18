---
name: swift-concurrency
description: "Diagnose Swift actor isolation, task lifetimes, stale async results, cancellation, continuations, stream buffering, and Swift 6 migration."
---

# Swift concurrency and task lifetimes

## Inputs

Record the compiler, language mode, isolation defaults, feature flags, task owners, and cross-actor data.

## Rules

- **CONC-001 — Isolate mutable state.** Keep UI state on its actor. Transfer immutable `Sendable` snapshots. Justify any unsafe annotation independently of compiler acceptance.
- **CONC-002 — Give tasks a lifetime.** Prefer structured children or `.task(id:)` for view work. Assign longer-lived tasks to a service that completes or cancels them.
- **CONC-003 — Stop obsolete work.** Check cancellation around costly work and before publishing. Invalidate obsolete requests even when the service ignores cancellation.
- **CONC-004 — Recheck after suspension.** Apply success, failure, and cleanup only while the account and request generation still match.
- **CONC-005 — Check the executor.** Locate CPU-heavy work before moving it. A `Task` created on the main actor can still block it.

## Workflow

1. Trace each suspension and handoff. Bound concurrent work, retries, and stream buffers.
2. Serialize callback completion and cancellation so each continuation resumes once.
3. For streams, specify which events may drop and who removes observers on early exit.

## Verify

- CONC-001: Build affected targets with strict concurrency checking in their supported language mode. The changed handoffs compile without isolation diagnostics.
- CONC-003, CONC-004: Replace a request or log out before completing it. Late success and failure leave current data and loading state intact.
- CONC-002: For a latest-only progress stream, deliver two samples before the first read. Only the newer sample is pending. Dismiss the consumer and verify its observer is removed once.

## Output

Report isolation, task owners, failing event order, and regression results.

## References

- [Task lifetime, actor reentrancy, and stale results](references/concurrency-patterns.md)
- [Stream teardown, callback races, and compiler settings](references/streams-and-migration.md)

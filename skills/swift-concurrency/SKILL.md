---
name: swift-concurrency
description: "Diagnose Swift isolation, task lifetimes, stale results, cancellation, continuations, stream buffering, and Swift 6 migration."
---

# Swift concurrency

## Inputs

Record compiler, language mode, isolation defaults, flags, and task owners.

## Rules

- **CONC-001 — Isolate UI state.** Name its writer and the synchronization behind any unsafe handoff.
- **CONC-002 — Own tasks.** Name what stops on dismissal and who owns surviving work.
- **CONC-003 — Revoke obsolete work.** Check cancellation around costly work and before publication. Invalidate replaced requests even if cancellation is ignored.
- **CONC-004 — Recheck after suspension.** Match account and request before applying success, failure, or cleanup.
- **CONC-005 — Check the executor.** Locate expensive work that blocks rendering on the main actor.

## Workflow

1. Trace actor crossings. Bound concurrency, retries, and buffers.
2. For callbacks, choose who completes the wait, which events may drop, and who removes observers.

## Verify

- CONC-001: Build supported modes with strict checking. Changed handoffs compile without isolation diagnostics.
- CONC-003, CONC-004: Replace a request or log out. Late results and errors preserve data and loading state.
- CONC-002: Buffer two latest-only samples. Read only the newer. Dismiss and verify one observer removal.
- CONC-005: Profile slow work on its executor. Compare main-thread time for the same interaction after the fix.

## Output

Report isolation, owners, event order, and results.

## References

- [Task lifetime and stale results](references/concurrency-patterns.md)
- [Streams, callbacks, and migration](references/streams-and-migration.md)

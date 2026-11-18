---
name: swift-concurrency
description: "Diagnose Swift isolation, task lifetimes, stale results, cancellation, continuations, stream buffering, and Swift 6 migration."
---

# Keep asynchronous Swift work tied to the request that started it

Use this when an older search overwrites a newer result, a dismissed screen keeps working, or the UI stalls during an async operation.

## Start here

For a search, record its text, scope, account, and owning task. Check the affected target’s compiler, language mode, isolation defaults and feature flags.

## How to proceed

1. **Identify who writes the state.** Follow values across actors to the UI. Pass immutable snapshots where possible. If the handoff uses unchecked shared state, identify how reads and writes are synchronized. <!-- CONC-001 -->
2. **Choose when work stops.** Give tasks that survive dismissal an owner. Bound concurrent work and retries. For callback streams, decide which events can be dropped, who finishes a wait, and who removes the observer. <!-- CONC-002 -->
3. **Retire a replaced request immediately.** When text, scope or account changes, invalidate the old request and cancel it. Check cancellation before expensive work and before publishing. <!-- CONC-003 -->
4. **Recheck identity after waiting.** Only the current account and request may publish results, report an error, or clear the loading indicator. A service may ignore cancellation. <!-- CONC-004 -->
5. **Locate work that delays input.** Profile the slow interaction and find what actually runs on the main actor before moving computation elsewhere. <!-- CONC-005 -->

## Check the result

- Replace a request or log out, then deliver its old result or error while the new request loads. The new request keeps its data, error and loading state. <!-- CONC-003 CONC-004 -->
- Buffer two samples before reading a latest-value stream. Read the newer sample, dismiss the screen and observe one removal of its subscription. <!-- CONC-002 -->
- Compile the changed handoff under strict concurrency in supported modes. For a stall, compare main-thread time during the same interaction before and after the fix. <!-- CONC-001 CONC-005 -->

## What to report

Show who owned the work, which completion exposed the bug, and what changed after the fix.

- [Scope changes, late replies, and overlapping writes](references/concurrency-patterns.md)
- [Stream buffering, observer teardown, and compiler modes](references/streams-and-migration.md)

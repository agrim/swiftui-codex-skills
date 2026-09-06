# Concurrency and lifecycle: playbook

## Choose execution and lifetime independently

| Work | Preferred owner | Failure to avoid |
| --- | --- | --- |
| Search for visible query | `.task(id: query)` plus model/service | Old query overwrites new result |
| Related concurrent requests | `async let` or task group | Unbounded task creation |
| App-wide sync | Explicit service task with stop/restart | Recreated by every view appearance |
| Shared mutable cache | Actor or another justified isolation boundary | Unsynchronized dictionaries |
| CPU-intensive transformation | Explicit executor strategy verified for the toolchain | Assuming `async` leaves the main actor |
| Callback or sensor stream | Owned adapter with termination and buffering | Leaked subscriptions or unbounded queues |

`Task {}` is unstructured and can inherit actor context. `Task.detached` changes inheritance and lifetime expectations; it is not a universal performance fix. Prefer the smallest explicit concurrency boundary that preserves cancellation, priority intent, and safe value transfer. Swift 6.2 adds opt-in default isolation and caller-context behavior for nonisolated async functions; inspect flags before applying older executor advice. Use `@concurrent` only when the compiler supports it and the boundary is appropriate.

## Latest-result-wins protocol

On start, create a request identity and mark it current. Capture the query/account that the request belongs to. After awaiting the service, check cancellation and compare the identity before publishing success or failure. Cleanup may clear a busy state only if its identity is still current. Invalidate the current identity on logout or explicit cancellation even when a service ignores cancellation.

A request token solves UI ordering, not remote exactly-once execution. Writes need their own operation identity, server contract, or reconciliation policy. A cancelled save may already have committed remotely; represent an uncertain result instead of retrying blindly or claiming rollback.

Cancellation and invalidation are separate operations: invalidate publication authority immediately when an account or scope changes, and cancel the owned task to request resource cleanup. Cancellation alone does not stop an arbitrary service that ignores it. Do not hold a lock while calling `cancel()` on work whose cancellation handlers might acquire that lock.

## Actor reentrancy

An actor can process another operation while one method is suspended. Read-check-await-write is not an atomic transaction. After `await`, revalidate the prerequisite or reserve the operation before suspension, with rollback rules. Do not hold a lock across suspension. Passing a non-Sendable persistence object between actors is not made safe by giving its surrounding method an `async` label.

## Callback bridges and streams

A checked continuation must resume exactly once along every terminal path. Handle success, failure, cancellation, and synchronous callback-before-registration without double resume or leakage. Centralize terminal state in a race-safe owner. Cancellation handlers can execute concurrently with the operation; inspect the protected state rather than relying on callback order.

For `AsyncStream`, select an explicit buffering policy where producers can outpace consumers. Finish the stream, release observers, and stop underlying resources on termination. Distinguish a stopped consumer from an actual stopped camera, microphone, location manager, or external subscription. Make stop idempotent and test interruption recovery separately from user cancellation.

## Deterministic tests

Use a fake service whose continuations can be completed by request ID. Start A, observe A registered, start B, observe B registered, finish B, then finish A; assert B remains visible. Repeat with A failing, cancellation during publication, and account replacement. Test that A's cleanup cannot clear B's loading state. Avoid tests that pass only because a sleep happens to schedule tasks in the desired order.

The repository's `SearchIntegrationTests` exercise the same `SearchModel` used by its SwiftUI example. They await actual controlled service registrations and complete those requests in adversarial orders, including success, failure, cancellation, and invalidation. Every accepted continuation is resumed. A test time limit is a deadlock watchdog, never a substitute for the registration handshake. This is model/service integration evidence, not SwiftUI scheduler, actual-network, or rendered-screen proof.

Thread Sanitizer and strict-concurrency diagnostics can identify classes of unsafe access. Neither establishes authorization, transaction ordering, or idempotency. Report those proofs separately.

## Sources

- [concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) — The Swift Programming Language: Concurrency.
- [swift62](https://www.swift.org/blog/swift-6.2-released/) — Swift 6.2 language and concurrency changes.
- [observation](https://developer.apple.com/documentation/SwiftUI/Migrating-from-the-observable-object-protocol-to-the-observable-macro) — Migrating to Observation.
- [task-cancellation](https://developer.apple.com/documentation/swift/task/cancel%28%29) — Cooperative cancellation and handler execution.

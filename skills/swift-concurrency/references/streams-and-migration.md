# Streams, continuations, and compiler migration

## Cross-target settings

Record compiler version separately from language mode, default actor isolation, strict checking, upcoming features, and deployment target. An app and package can compile identical syntax under different defaults. Do not treat a tools-version header as proof of every language setting.

Use `@concurrent`, isolated conformances, or newer isolation syntax only after checking the exact compiler and selected feature flags. `async` does not promise parallel or off-main execution. An awaited sleep does not block a main-actor thread; moving it elsewhere is not automatically an optimization. Prefer the simplest ownership-correct path, then measure CPU work.

## Bounded structured work

A task group scopes child lifetime, but normal scope exit waits for children; it does not universally cancel them. An early selected result may require `cancelAll()` and cooperative child termination. Bound active work when processing an unbounded collection instead of adding every item immediately. Cancellation cannot interrupt a blocking noncooperative call.

## Callback streams under load

Ask what a slow subscriber can reconstruct. A progress indicator can usually skip from 20% to 70%. An inventory total computed from individual deltas needs every change or a way to reload the total after a gap.

| Delivery contract | Adapter decision | Observable failure |
| --- | --- | --- |
| Each sample replaces the last | `.bufferingNewest(1)` can keep the most recent pending sample. | A slow display stays on the first sample of a burst. |
| The earliest pending samples have priority | `.bufferingOldest(n)` keeps the first pending samples up to capacity. | A new arrival displaces an item the subscriber expected to process. |
| Every event matters | Use demand from the consumer if the source can pause, or provide durable replay or reconciliation on overflow. | A dropped delta silently changes a stored total. |

`yield` returns immediately. Inspect `.dropped(let element)` where loss changes the recovery decision. With a newest-value buffer the displaced element can be an earlier sample. If processing requires acknowledgement, have the subscriber report completion separately. Define who receives each event when there are multiple subscribers.

## Leaving an observer-backed stream

Put ownership of the observation token and its idempotent removal in the adapter. Wire `onTermination` to teardown when cancellation ends active iteration. A caller can also take one value and `break` while the stream is retained elsewhere. If its underlying observation must end at that point, give the caller a scoped subscription or an explicit stop operation and invoke it on exit. For a shared source, remove only the departing subscriber until the last owner leaves.

If removal must run on another actor, expose a way to await shutdown completion on that actor. Route late callbacks through the closed subscription and ignore them after dismissal.

## An owner that never deallocates

An observation task can retain a controller for the entire wait for its next event. If the upstream stays open and only `deinit` cancels, neither teardown runs. Give the screen or service an explicit stop point. If using a weak capture, acquiring the owner once before an endless loop still extends its lifetime. Acquire it only while handling each value if that matches the ownership contract. A bounded task can safely retain its owner until completion.

Test with a stream that remains open and emits nothing. Wait for subscription, end the feature, await teardown, and drop the last external owner. Check observer removal and a nil weak reference without sending a final event.

## Continuation race table

Handle callback-before-registration, cancellation-before-registration, cancellation-after-registration, duplicate callback, and callback-after-cancellation. A checked continuation diagnoses misuse; it does not make the surrounding state machine race-free. Give completion one owner and never hold a synchronous lock across suspension. If a framework offers a native async API, inspect its cancellation behavior before writing a wrapper.

Tests must prove publication and cleanup authority, not merely call `cancel()`. Control completion registration with a handshake; arbitrary sleeps and repeated yields are not ordering guarantees. Test cancellation before the operation starts and after a replacement has become current. Preserve any necessary resource cancellation separately from revoking stale-result authority.

## Official sources

- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Swift 6.2 language and concurrency changes](https://www.swift.org/blog/swift-6.2-released/).
- [Swift Task cancellation semantics](https://developer.apple.com/documentation/swift/task/cancel%28%29).
- [AsyncStream buffering policies](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy).
- [Continuation yield results and delivery](https://developer.apple.com/documentation/swift/asyncstream/continuation/yield%28_%3A%29).
- [Cancellation of active stream iteration](https://developer.apple.com/documentation/swift/asyncstream/continuation/ontermination).
- [Swift Task closure lifetime](https://developer.apple.com/documentation/swift/task)

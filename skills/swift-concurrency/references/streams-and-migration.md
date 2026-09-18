# Streams, continuations, and compiler migration

## Cross-target settings

Record compiler version separately from language mode, default actor isolation, strict checking, upcoming features, and deployment target. An app and package can compile identical syntax under different defaults. Do not treat a tools-version header as proof of every language setting.

Use `@concurrent`, isolated conformances, or newer isolation syntax only after checking the exact compiler and selected feature flags. `async` does not promise parallel or off-main execution. An awaited sleep does not block a main-actor thread; moving it elsewhere is not automatically an optimization. Prefer the simplest ownership-correct path, then measure CPU work.

## Bounded structured work

A task group scopes child lifetime, but normal scope exit waits for children; it does not universally cancel them. An early selected result may require `cancelAll()` and cooperative child termination. Bound active work when processing an unbounded collection instead of adding every item immediately. Cancellation cannot interrupt a blocking noncooperative call.

For an async stream, choose a buffering policy appropriate to semantics. Dropping old progress can be acceptable; dropping business events may not be. `yield` into a buffer is not backpressure from a slow consumer. Define producer shutdown, subscriber cancellation, terminal failure, and whether each consumer needs its own sequence.

## Continuation race table

Handle callback-before-registration, cancellation-before-registration, cancellation-after-registration, duplicate callback, and callback-after-cancellation. A checked continuation diagnoses misuse; it does not make the surrounding state machine race-free. Give completion one owner and never hold a synchronous lock across suspension. If a framework offers a native async API, inspect its cancellation behavior before writing a wrapper.

Tests must prove publication and cleanup authority, not merely call `cancel()`. Control completion registration with a handshake; arbitrary sleeps and repeated yields are not ordering guarantees. Test cancellation before the operation starts and after a replacement has become current. Preserve any necessary resource cancellation separately from revoking stale-result authority.

## Official sources

- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Swift 6.2 language and concurrency changes](https://www.swift.org/blog/swift-6.2-released/).
- [Swift Task cancellation semantics](https://developer.apple.com/documentation/swift/task/cancel%28%29).

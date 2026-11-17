# Async tests, parameterization, and framework coexistence

Use `#expect` for observations that can accumulate and `#require` for a prerequisite whose failure makes the next operation invalid. Avoid forcing an unwrap after a nonfatal assertion. A passing test should establish its behavior, not merely execute code without a crash.

Keep Swift Testing and XCTest where each fits. Migrate unit/integration tests deliberately; retain XCTest for UI automation, supported metrics, and Objective-C surfaces when needed. Converting syntax is not proof that setup, cleanup, isolation, or assertion semantics stayed equivalent.

## Async tests

A confirmation counts events during its operation's lifetime; it is not an automatic wait for arbitrarily late callbacks. Await an operation or explicit completion handshake that keeps the scope alive. Continuation wrappers require exactly-once completion and cancellation handling. Do not use sleeps or `Task.yield()` as proof another task registered its callback.

Parallel tests need separate files, stores, clocks, clients, and mutable state. A serialized suite is a scoped compromise, not global isolation from unrelated suites or processes. Avoid a global mutable URL-protocol handler shared by concurrently running networking tests.

Parameterized argument collections can form a Cartesian product. Use paired tuples or `zip` when inputs are correlated, and test the number of generated cases. Keep failure output diagnostic and datasets bounded. New traits, attachments, exit tests, or isolation features need toolchain availability checks.

## Test a callback stream through its adapter

Use a fake source that acknowledges observer registration, can emit on demand, and records removal by token. Keep the production adapter between this source and the test. Two independent probes expose different defects.

- **Overflow.** For an adapter promising only the latest pending value, subscribe, await registration and hold off on the first iterator read. Deliver two distinguishable samples in order and let the adapter handle both before signaling normal completion. The iterator should return the second sample followed by `nil`. Reversing the capacity-one buffer policy should fail this test. For a lossless contract, drive the same burst and assert every required event or the documented recovery outcome.
- **Early exit.** Receive one sample, leave the consumer loop while retaining the stream, and exercise the caller's real dismissal or scoped cleanup path. Await the teardown acknowledgement and check that the matching observer was removed once. Invoke a saved callback to simulate a delivery already in flight and drain the adapter's outstanding work before checking for a late publication. Bypassing removal should fail the observer check even if the screen ignores all later updates.

If using a zero-count confirmation for late publication, drive the late delivery and join its effects inside the confirmation closure. A closure that returns before the fake source emits can pass without exercising the race.

## Reliability probes

Run a deliberate negative control to show the test fails when its invariant is broken. Verify test discovery and nonzero execution for selected filters. Track skipped tests, known issues, and snapshot baseline changes as explicit evidence gaps rather than counting them as coverage.

For persistence, distinguish in-memory behavior, disk reopen, migration, and live sync. For UI, distinguish snapshots, semantic audits, and assistive journeys. Preserve unique tests during refactoring; a shorter suite is not better when it drops a separate proof claim.

## Official sources

- [Swift Testing](https://developer.apple.com/xcode/swift-testing/).
- [Swift Testing parallelization](https://developer.apple.com/documentation/Testing/Parallelization).
- [Swift Task cancellation semantics](https://developer.apple.com/documentation/swift/task/cancel%28%29).
- [XCUI accessibility audits](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue).
- [Testing asynchronous code](https://developer.apple.com/documentation/testing/testing-asynchronous-code).
- [AsyncStream buffering policies](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy).

# Async tests, parameterization, and framework coexistence

## Preserve the proof during a framework migration

Compare the fixtures, failure behavior and teardown of one representative case before converting its siblings. A missing prerequisite should fail the case at the missing value. If the rewritten assertion continues into a forced unwrap, the resulting crash obscures the defect. Retain the XCTest path for UI automation, metrics or Objective-C callers that still need it.

For intermittent failures in a parallel run, look for a shared temporary path, store, clock or mutable request handler. Give each case its own fixture. If a suite must serialize access to a real resource, also check which other suites or processes can reach it.

## Consolidate tests that differ only by input

If a validator runs the same action and assertion for empty, whitespace-only and valid titles, use one parameterized test with a named case containing the input and expected result. Keep a cancel-and-reopen journey separate because it exercises persistence and teardown. Check that a deliberately broken whitespace rule fails its own case.

Cross independent inputs only when each pairing matters. Store correlated inputs and expectations in one case. If fixtures must stay separate, verify their lengths and correspondence before passing `zip` to the test. Adding an invalid title to only one array would otherwise omit the very case meant to catch the defect.

## Test a callback stream through its adapter

Use a fake source that acknowledges observer registration, can emit on demand, and records removal by token. Drive the production adapter with that source.

- **Overflow.** For an adapter promising only the latest pending value, subscribe, await registration and hold off on the first iterator read. Deliver two distinguishable samples in order and let the adapter handle both before signaling normal completion. The iterator should return the second sample followed by `nil`. Reversing the capacity-one buffer policy should fail this test. For a lossless contract, drive the same burst and assert every required event or the documented recovery outcome.
- **Early exit.** Receive one sample, leave the consumer loop while retaining the stream, and exercise the caller's real dismissal or scoped cleanup path. Await the teardown acknowledgement and check that the matching observer was removed once. Invoke a saved callback to simulate a delivery already in flight and drain the adapter's outstanding work before checking for a late publication. Bypassing removal should fail the observer check even if the screen ignores all later updates.

If using a zero-count confirmation for late publication, drive the late delivery and join its effects inside the confirmation closure. A closure that returns before the fake source emits can pass without exercising the race.

## Reliability probes

Check that the filter executed the intended case. Record skipped checks and known issues. A deliberate reversal of a buffer policy or removal of teardown should turn its corresponding probe red.

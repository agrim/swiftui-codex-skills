# Stream delivery, teardown, and migration

## Different compiler defaults

If the app and package disagree about isolation, compare their effective language modes, default isolation, and feature flags. Change the boundary that owns the state. Require a concrete synchronization argument before accepting an unsafe conformance. For unbounded input, limit active children. When returning the first result from a task group, exercise a losing child that ignores cancellation before promising a deadline.

## What can a slow subscriber lose?

A progress display may skip from 20% to 70%. Deliver both before reading and check that only 70% remains in its latest-value buffer. A running total based on individual deltas needs every delta or a way to reconstruct the total. Force overflow and verify recovery against a known total. If the producer requires acknowledgement, wait for the consumer's confirmation of processing.

## Leaving an observer-backed stream

Cancelling active iteration and breaking after one value have different teardown paths. Retain the stream elsewhere, read one value, then break. If observation must stop there, give the caller a scoped subscription or explicit stop operation. For a shared source, detach only this subscriber. Await removal on its owning actor, drive a late callback, and verify no further publication.

Test a second case with an open stream that sends *nothing*. A controller captured before an endless loop can stay alive while the task waits. Put stop on the screen or service lifecycle. After registration, end the feature, await teardown, and drop the external owner. Check one observer removal and a nil weak reference without sending a final event.

## Competing terminal events

Choose one owner for the transition from waiting to finished. Drive synchronous completion during registration, cancellation on either side of registration, duplicate callbacks, and a callback after cancellation. Use a registration handshake to order the probe. Each waiter must finish once, and late callbacks must leave a replacement operation intact.

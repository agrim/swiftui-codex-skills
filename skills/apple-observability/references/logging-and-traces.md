# Logging, signposts, and trace interpretation

## Can the capture answer the question?

- **Error report.** Use a component category, operation phase and sanitized error class. Inspect an exported failure for payloads or identifiers embedded in error descriptions. Correlate retries with short-lived opaque IDs.
- **Overlapping operations.** Cancel one operation while the other completes. Pair boundaries by operation ID and compare durations in the same units. Pairing the nearest timestamps can attribute the first cancellation to the second operation.
- **Empty trace lane.** Check process, time window, template support, filters and symbols before interpreting the gap. Record device, build, tool version and warm-up so a second run can reproduce it.

## A freeze with high process CPU

Select the interval when input stopped responding. A sleeping main thread between interactions is expected. High process CPU during the freeze can come from a worker while the main thread waits.

- **Main thread running.** Inspect Time Profiler samples from that thread within the freeze. Follow the stack to the app operation doing the work.
- **Main thread waiting.** Record Thread State Trace and inspect the backtrace where the wait began. For a lock, identify its holder if the trace exposes it. For a synchronous dependency, find the operation that must finish to release the wait. An empty CPU sample range alone leaves the cause open.

Replay the same input. Check that the identified interval shortened and input became responsive, including on the final build without the debugger.

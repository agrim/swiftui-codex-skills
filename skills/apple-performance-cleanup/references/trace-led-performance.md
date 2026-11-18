# Trace-led runtime performance work

Select a runtime symptom and reproduce it. If the complaint ends before the app launches, collect compiler or build diagnostics. A runtime trace cannot locate a slow type check.

## Find the work behind one hitch

1. Mark the gesture and select its hitch. A full-recording call tree may rank unrelated startup work first.
2. For one long body or representable update, inspect samples from that interval and follow the cost into the app function or platform view. For many short updates, trace one repeated dependency and change one input boundary.
3. If the SwiftUI track is quiet, inspect rendering and main-thread waits. On older tooling, use samples or signposts and record unresolved attribution. Replay the gesture against the same data. Compare hitch count or duration alongside update counts.

## A filtered list opens slowly

If a row-producing `ForEach` conditionally emits zero or one row, compare opening the list with an already-filtered input that emits one row per record. Measure the filter itself on each update. Recalculate a stored result when either the filter or the records change. A conditional badge inside an existing row leaves its row count intact. Preserve it unless its own work is costly.

Compare opening and scrolling at the same data size, then select, delete and reorder filtered rows. Check the affected record IDs.

## A computed property updates an expensive parent

An upload screen shows how many files are pending. Complete one upload and select the resulting update in the trace. If the expensive work is reevaluating the enclosing screen, move the count read into the badge. If scanning the queue dominates, that move still performs the scan. Maintain a count only if enqueue, completion, retry and removal all keep it correct.

Rename a file, complete an upload, then retry a failed upload. Check the count, the views updated and the duration of the original interaction.

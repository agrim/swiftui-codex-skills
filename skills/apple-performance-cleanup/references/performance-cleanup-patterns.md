# Apple performance and behavior-preserving cleanup: playbook

## Diagnose by symptom

| Symptom | Inspect first | Possible correction after evidence |
| --- | --- | --- |
| Repeated slow body updates | Dependency reads and repeated work | Narrow dependencies; move or cache expensive derivation |
| Scrolling hitch | Main-thread work, layout, image decode, identity | Bound decode work; stabilize IDs; simplify measured layout |
| Startup delay | Synchronous I/O, initialization, eager services | Defer nonessential work with explicit readiness states |
| Memory growth after navigation | Tasks, observers, delegates, caches | Break retained lifetimes and bound retained data |
| High energy use | Sampling, timers, background work, updates | Reduce unnecessary work and honor lifecycle limits |
| Slow persistence | Query scope, write frequency, serialization | Batch only where transaction and failure semantics permit |

## Change the measured cost

- **Repeated decode or filtering.** Compare the cost of deriving the result with the cost of rereading it. Before caching, identify the invalidating inputs, account scope and a size bound. Change an input and switch accounts to expose stale or cross-account results.
- **Busy main thread after moving work into a task.** Inspect where the expensive function ran with the target’s isolation settings. Keep cancellation and result ownership attached to the feature. Switch features mid-operation and confirm a late result cannot replace current content.
- **Growth after dismissal.** Compare live owners across repeated entry and exit after expected teardown. Compare against the cache’s intended bound before weakening a reference.
- **Noisy hot-path logs.** Reproduce with and without temporary instrumentation. Retain the minimal event that distinguishes the failing path without recording payloads.

## Review a cleanup

Before merging helpers, follow the callers that handle missing, zero, stale, denied or failed values differently. Verify fallback order and commit timing in each affected caller. In a large cleanup, group changes by behavior so a regression can be traced to one batch.

Compare typical and heavy inputs on matched hardware, build mode and cache state. Report variation across repeated runs. If only source inspection is available, report the work eliminated, such as one decode per input instead of per update. Leave the time saved unmeasured.

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

A profiler establishes where time or memory goes; a screenshot does not. Use the installed Instruments templates and SwiftUI profiling facilities appropriate to the available Xcode version. Record the chosen tool rather than requiring one third-party integration.

## SwiftUI dependency and identity work

Inspect what a view reads, which changes invalidate it, and whether its identity survives updates. Extracting a subview is useful when it creates a meaningful dependency or ownership boundary, not simply because a file is long. Computed properties do not magically cache results.

Keep expensive parsing, sorting, decoding, synchronous I/O, and repeated formatting out of frequent updates when measurement shows cost. Cache with an explicit key, invalidation rule, size limit, and account scope; an unbounded cache trades one bug for another.

`AnyView`, `GeometryReader`, custom layout, and broad observation are not universally wrong. Assess their actual use and measured impact. Prefer concrete types and targeted observations when they fit, but do not rewrite working architecture on folklore alone.

## Main actor and tasks

An `async` function is not proof of background execution. Inspect actor isolation, the selected Swift language mode and concurrency features, and where CPU-heavy work actually runs. Do not use detached tasks as a blanket escape from isolation.

Cancel view-bound work when its owner changes or ends. Cancellation is cooperative; stale completion still needs a correctness guard where results can race. Bound streams, retries, and buffering. Keep task handles and delegate lifetimes explicit.

## Memory and diagnostics

Exercise repeated present/dismiss, login/logout, start/stop, and load/cancel cycles. Compare retained graphs and allocations after the system has had a reasonable opportunity to settle. One rising sample is not proof of a leak; one low sample is not proof of absence.

Avoid verbose hot-path logging of sensitive or high-frequency data. Use scoped diagnostic events and measurements that can establish causality. Keep enough evidence to reproduce regressions; do not remove useful telemetry merely because the optimized code looks cleaner.

## Behavior-preserving cleanup

Before helper extraction, trace callers and edge cases. Preserve distinctions among missing, nil, zero, stale, denied, failed, and unavailable. Preserve fallback order and externally observable timing or persistence boundaries that matter to the product.

For whole-codebase compaction, inventory candidates first and execute reviewable batches. Keep production code, test scenarios, generated artifacts, compatibility paths, and measurements separate. Do not target an arbitrary deletion percentage or replace readable domain types with dense abstractions.

## Measurement contract

Use the same source baseline, build mode, hardware/runtime, input data, and operation sequence. Record warm/cold state and relevant background conditions. Run enough repetitions to expose variation and report the method alongside summary values; do not treat a single noisy run as a benchmark.

A change can be correct but slower, or faster but wrong. Keep behavior tests and performance evidence separate. If profiling is unavailable, state the structural inference precisely—for example, one decode per input instead of per update—and leave runtime improvement unverified.

## Sources

- [performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance) — Understanding and improving SwiftUI performance.
- [rendering](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency) — Improving rendering efficiency.
- [concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html) — The Swift Programming Language: Concurrency.
- [model-context](https://developer.apple.com/documentation/swiftdata/modelcontext) — SwiftData ModelContext.

# Trace-led runtime performance work

Separate runtime responsiveness from build latency. A slow type checker needs compiler/project evidence; a hitch needs rendering/main-thread evidence; memory growth needs allocation and retention evidence. Do not use one metric to justify changes in another domain.

Capture a reproducible workload, source/build, device/OS, configuration, warm-up, dataset, and power/resource conditions. Keep raw evidence and compare like-for-like. Simulator results can help localize a path but cannot establish device energy or memory-pressure behavior.

For SwiftUI, inspect the dependency that triggered an update, the work done by `body`, collection identity, measurement loops, formatting, image decoding, and broad observation. Optimize measured repetition by narrowing inputs or moving work to the right owner. Do not blanket-ban computed properties, all type erasure, or every custom binding.

For hangs, distinguish CPU-bound work from waiting or blocking. For memory, distinguish temporary peaks from persistent retention and intentional caches. A weak capture is not a universal repair for task ownership. For startup, separate static initialization, store readiness, migrations, networking, and first meaningful interaction.

## Find the work behind one hitch

1. Mark the gesture in a release-like recording, then select the hitch within it. Note the time range and the view on screen. A call tree for the entire recording can rank startup work above everything that happened during the gesture.
2. In a supported Instruments 26 SwiftUI recording, inspect the update groups in that range. For a long body update, select its interval and inspect the main thread in Time Profiler. Follow samples down to the application function. A long representable update points to the bridge and its underlying platform view.
3. If individual bodies are short but numerous, inspect which views updated and follow a dependency back through the cause-and-effect graph where available. Change one input or observation boundary, then compare the update count **and** the hitch. If the SwiftUI track is quiet during a hitch, inspect main-thread waits, rendering, or other recorded work. With an older toolchain, use the hitch interval and available samples or signposts and record any gap in attribution.
4. Repeat the same gesture against the same data. Record hitch count or duration alongside the diagnostic measure. Fewer body updates alone do not show whether scrolling improved.

## A filtered list opens slowly

Inspect how many rows each element in a `List` or `Table` produces. A conditional directly inside a row-producing `ForEach` may emit zero or one row. To discover the identities up front, the list can have to construct content for every element. Compare with supplying the visible records to the `ForEach` and emitting one row per record. Measure filtering separately if it scans a large collection on each update. If a derived collection is stored, refresh it when either the records or the filter changes.

A conditional badge *inside* a row that always exists has a different cost. Keep the badge and its semantics unless its own measured update is expensive. Compare opening the list as well as scrolling it, and verify that selecting, deleting, or reordering filtered records still targets the correct IDs.

## Change contract

A proposed optimization records the observed cost, semantic invariant, affected path, hypothesis, comparison workload, and stop condition. Keep a behavior regression test alongside the measurement. Preserve nil/zero/stale/failed distinctions and cancellation semantics while reducing work.

Do not delete diagnostics, compatibility paths, or unique tests to improve a line-count metric. Re-measure after the final combined change and identify whether the result is improvement, tradeoff, regression, or inconclusive. Structural reduction in work can be stated as such, but it is not an invented wall-time percentage.

## Official sources

- [Optimize SwiftUI performance with Instruments](https://developer.apple.com/videos/play/wwdc2025/306/) demonstrates interval selection, sampled stacks, and the update cause-and-effect graph.
- [Demystify SwiftUI performance](https://developer.apple.com/videos/play/wwdc2023/10160/) explains how row counts affect identity gathering in lists and tables.

- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance).
- [Improving rendering efficiency](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Unified logging Logger](https://developer.apple.com/documentation/os/logger).

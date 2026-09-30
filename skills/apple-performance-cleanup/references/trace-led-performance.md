# Trace-led runtime performance work

Separate runtime responsiveness from build latency. A slow type checker needs compiler/project evidence; a hitch needs rendering/main-thread evidence; memory growth needs allocation and retention evidence. Do not use one metric to justify changes in another domain.

Capture a reproducible workload, source/build, device/OS, configuration, warm-up, dataset, and power/resource conditions. Keep raw evidence and compare like-for-like. Simulator results can help localize a path but cannot establish device energy or memory-pressure behavior.

For SwiftUI, inspect the dependency that triggered an update, the work done by `body`, collection identity, measurement loops, formatting, image decoding, and broad observation. Optimize measured repetition by narrowing inputs or moving work to the right owner. Do not blanket-ban computed properties, all type erasure, or every custom binding.

For hangs, distinguish CPU-bound work from waiting or blocking. For memory, distinguish temporary peaks from persistent retention and intentional caches. A weak capture is not a universal repair for task ownership. For startup, separate static initialization, store readiness, migrations, networking, and first meaningful interaction.

## Change contract

A proposed optimization records the observed cost, semantic invariant, affected path, hypothesis, comparison workload, and stop condition. Keep a behavior regression test alongside the measurement. Preserve nil/zero/stale/failed distinctions and cancellation semantics while reducing work.

Do not delete diagnostics, compatibility paths, or unique tests to improve a line-count metric. Re-measure after the final combined change and identify whether the result is improvement, tradeoff, regression, or inconclusive. Structural reduction in work can be stated as such, but it is not an invented wall-time percentage.

## Official sources

- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance).
- [Improving rendering efficiency](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).
- [Unified logging Logger](https://developer.apple.com/documentation/os/logger).

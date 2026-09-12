# Memory graphs and crash investigation

A rising memory graph may indicate caches, temporary allocation, autorelease behavior, leaked objects, or intended retention. Reproduce repeated navigation/presentation cycles and compare after expected teardown. Identify the retaining path before adding weak references indiscriminately.

Inspect tasks capturing owners, subscriptions, notification tokens, timers, delegates, coordinators, image caches, and closures. A task can keep an owner alive across suspension even after a weak capture was promoted to strong. Pair start with cancellation and registration with removal. Weakening a necessary owner can turn a leak into lost callbacks.

Memory graph capture, Instruments, and command-line leak tools have destination and permission constraints. A simulator result is not equivalent to device memory pressure. Redact captured object contents and filenames before sharing diagnostics.

For a crash, keep the original incident, binary/build identity, platform, reproduction, and matching symbols. Verify symbol UUID matching; a stack with addresses is not yet a reliable source-level diagnosis. Classify app assertions, access violations, watchdogs, memory termination, and system/infrastructure failures separately.

Fix the evidenced ownership defect, then test deallocation or lifecycle completion deterministically. A source search for retain cycles is only a hypothesis generator; no generic scanner proves leak freedom.

## Official sources

- [Unified logging Logger](https://developer.apple.com/documentation/os/logger).
- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance).
- [Improving rendering efficiency](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

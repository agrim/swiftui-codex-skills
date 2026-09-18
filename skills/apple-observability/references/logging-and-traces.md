# Logging, signposts, and trace interpretation

Use stable subsystem/category names that describe components, not user identities. Choose severity intentionally: routine lifecycle noise should not masquerade as faults, and operational failures should not vanish behind debug-only logging. Log typed phases and sanitized error classes instead of interpolating full `Error` descriptions or network payloads.

Treat privacy explicitly even where a logging API offers redaction defaults. A hashing option does not make arbitrary user data harmless. An operation ID should be opaque, bounded in retention, and unsuitable as a credential. Keep metrics useful when diagnostics are disabled.

Pair interval start/end through success, failure, and cancellation. Do not measure across incompatible clocks or infer elapsed wall time from a count of samples. Group by operation and target workload, not by broad timestamps alone.

For traces, record process, device/OS, build configuration, symbols, template, warm-up, and time window. Discover available templates and schemas in the installed tool rather than hard-coding a third-party parser's expectations. An empty lane can mean absent capture support, filtering, missing symbols, or no events; it is not proof of no defect.

Inspect the main thread's samples and wait states around a hang. CPU samples, blocked duration, SwiftUI invalidation causes, and animation hitches answer different questions. Do not infer a universal blocked/CPU diagnosis from an arbitrary sample-coverage percentage. Compare the same scenario before and after, including instrumentation overhead.

## Official sources

- [Unified logging Logger](https://developer.apple.com/documentation/os/logger).
- [Understanding and improving SwiftUI performance](https://developer.apple.com/documentation/xcode/understanding-and-improving-swiftui-performance).
- [Improving rendering efficiency](https://developer.apple.com/documentation/xcode/improving-your-app-s-rendering-efficiency).
- [The Swift Programming Language: Concurrency](https://docs.swift.org/swift-book/LanguageGuide/Concurrency.html).

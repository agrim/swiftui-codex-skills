# Compiler hotspots and source complexity

Start from the build timeline. Separate type checking, source compilation, module emission, linking, and dependency planning. A warning about one slow expression identifies compiler work, not automatically the longest user wait.

Use temporary diagnostic flags supported by the selected compiler, record them, and compare normal builds separately. Do not persist unsupported frontend flags across every target. Narrow an expensive result builder with real view types or intermediate typed expressions; preserve identity, environment, generic behavior, and accessibility.

Inspect bridging headers, exported API, generic constraints, overload sets, macro expansion, and unnecessary imports. Tighten access only after checking subclasses, extensions, dynamic dispatch, external clients, and Objective-C requirements. `final` is a semantic restriction, not a harmless performance annotation.

A source change must compile and pass behavior tests in its intended configurations. Check whether it reduces elapsed time or merely total compiler work. Do not move all code into one file to reduce task count, or split every expression to meet an arbitrary line-count threshold. Use a repeatable example that actually triggers the slow compiler path.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

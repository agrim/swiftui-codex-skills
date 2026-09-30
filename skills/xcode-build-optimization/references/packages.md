# SwiftPM graph, plugins, and generated code

Trace package references to linked products and consuming targets. A directory named Vendor is not proof that its code affects the build. Record dependency revisions and package resolution separately from compilation.

Inspect plugin and macro targets, host-tool compilation, repeated module variants, network resolution, and unnecessarily broad product dependencies. Pin tool and generator versions according to the project's dependency policy. Do not update every dependency or replace a package manager as a side effect of a performance audit.

Splitting a package can reduce invalidation but introduces module and linking overhead. Compare actual import consumers, public API changes, resources, tests, startup, and total build time. Do not invent a universal maximum files-per-module rule.

Generated source should have one template owner, reproducible ordering, declared inputs, and a check for stale output. Review generated diffs and target membership. Hot reload and injected debug helpers may shorten a feedback loop but do not validate a clean launch or shipping build. Exclude development injection from Release and retest without it.

A clean clone should resolve and build with the documented commands. Missing optional directories or stale package exclusions need diagnosis; do not silently create arbitrary paths to appease a remembered upstream issue.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

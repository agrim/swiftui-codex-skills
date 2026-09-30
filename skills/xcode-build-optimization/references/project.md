# Build settings, scripts, and dependency graphs

Inspect effective per-target settings, shared schemes, generated manifests, file membership, and the actual build task graph. Missing dependencies can produce stale outputs even if the build is fast. Redundant dependencies can serialize work. Prove either condition before editing.

For custom script phases, declare accurate inputs and outputs, including templates, configuration, tool versions, and generated files. Use file lists for large sets. Write outputs only when bytes change. A fake stamp that ignores real inputs can make a benchmark faster by making the product wrong. Do not turn off sandboxing, signing, validation, tests, or metadata extraction to manufacture a speedup.

Audit Debug and Release independently. Active-architecture policy, debug symbols, optimization, compilation caching, explicit modules, and linking settings must match toolchain support and distribution requirements. Align options only where the targets are semantically equivalent; simulator/device, platform, language-mode, and conditional-definition differences can legitimately need separate modules.

After a change, inspect resolved settings and built resources, then build both an incremental path and an appropriate clean path. Verify downstream targets receive changed generated files. Archive/signing checks remain separate when a change could affect distribution.

## Official sources

- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Improving build efficiency with good coding practices](https://developer.apple.com/documentation/xcode/improving-build-efficiency-with-good-coding-practices).
- [Xcode documentation](https://developer.apple.com/documentation/xcode).

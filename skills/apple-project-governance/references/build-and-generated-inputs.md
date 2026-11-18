# Generated inputs, toolchains, and target membership

Locate the source owner for project structure, package configuration, entitlements, Info.plist values, resources, and generated code. Prefer changing that owner and regenerating. Do not hand-edit generated project output simply because it is the file named by a compiler error.

Inspect target membership after adopting buildable folders or automatic discovery. Preview fixtures, test resources, generated sources, privacy manifests, and extension assets must enter exactly the intended products. Check duplicate file basenames and asset/resource lookup assumptions in packages.

Keep compiler version, language mode, platform SDK, deployment minimum, and upcoming feature settings separate. Verify effective settings for each target/configuration rather than assuming the app and all dependencies inherit the same defaults. Changes to actor isolation or warning policies require code and dependency compatibility checks.

Build scripts and generators need declared inputs, outputs, pinned tool versions, deterministic order, and no-op stability. Formatting or regeneration that rewrites unchanged bytes can cause needless invalidation. A cached generated file is valid only when all semantic inputs are represented in its key.

## Fresh-clone proof

Resolve dependencies from tracked inputs, regenerate where required, list schemes/destinations, build the affected product graph, and inspect bundled files and effective entitlements. Confirm CI uses the same owner and commands. Do not repair a missing dependency by silently using an untracked local installation.

For build speed, preserve correctness first: no skipped metadata, broad sandbox exceptions, disabled tests, or removed signing requirements simply to obtain a faster timing. For identity changes, preserve stable storage keys and migration paths unless an intentional migration includes them.

## A configuration override hides a dependency

Suppose a framework builds in Debug and the same import fails in Release. Compare `xcodebuild -showBuildSettings` for the same scheme and destination in both configurations. If a needed search path disappears, trace the resolved value through the project, configuration file and target override. When the override must *extend* the inherited paths, use `$(inherited)` in the owning setting, regenerate if needed, then rebuild Release from tracked inputs.

If an extension deliberately excludes a private app-only search path, keep that boundary. An import of the app-only module in extension code calls for checking source membership or moving the shared interface into an appropriate module. Forcing both targets to inherit every path can hide that ownership error.

## Official sources

- [Xcode documentation](https://developer.apple.com/documentation/xcode).
- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Distributing your app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).
- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests).
- [Adding a build configuration file to your project](https://developer.apple.com/documentation/xcode/adding-a-build-configuration-file-to-your-project).

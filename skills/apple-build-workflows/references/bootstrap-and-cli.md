# Bootstrap, CLI, and debugger contract

## Existing projects first

Choose the project or workspace that actually owns the dependency graph; neither suffix wins automatically. Inspect generated-project inputs before editing `.pbxproj`. For a package-first repo, `swift build` and `swift test` are sufficient until an app-bundle or platform destination is part of the claim. Do not create a nested Git repository.

A useful local entry point exposes discover, build, test, and explicitly separate run/install actions. Keep scheme, configuration, destination, and output paths configurable. A Makefile is an optional convenience, not another source of build settings. Do not infer the user's team identifier, signing identity, or device. Respect tracked lockfiles and generator versions.

Buildable folders need membership review: an automatically included source, preview, fixture, or resource can accidentally enter a shipping target. Check exclusions, target exceptions, resource collisions, and actual compiled membership. New warning policies need a baseline: tighten warnings for owned code without globally suppressing diagnostics or making unrelated third-party warnings a surprise release blocker.

## Evidence-preserving shell fallback

Use explicit argument arrays in automation, not a concatenated shell command assembled from names or paths. In an interactive shell pipeline, enable `pipefail` and retain the build process's exit status. Formatting output is optional; store raw output first. Logs can contain paths and user data, so do not upload them without review.

A failed build should stop install/launch. A passed test process still needs a nonzero executed test count for the intended suite; a wrong filter can otherwise appear green. Record the selected test plan and skipped tests. Derive the built product from actual build settings instead of guessing its path.

## Debugging loop

State the reproduction and expected state; build a matching debug candidate, attach to the intended process, and use the smallest breakpoint/log probe. Inspect thread and actor context without assuming they are interchangeable. Debugger expressions can mutate state or call services: inspect before evaluating. Remove temporary logging and launch fixtures, then reproduce again without the debugger when timing matters.

Resetting a simulator, clearing DerivedData, or reinstalling is not the default fix. Classify missing runtime, project configuration, compilation, provisioning, install, crash, and store-readiness failures separately. Preserve data and unexplained crash evidence before any cleanup.

## Capability contract

A tool adapter should declare available actions, current defaults, chosen destination, evidence paths, and side effects. Missing plugins must not block a shell-capable environment; missing Xcode must not lead to fabricated Apple execution. Project processes may invoke arbitrary scripts even when the wrapper itself accepts only build/test actions.

## Official sources

- [Xcode documentation](https://developer.apple.com/documentation/xcode).
- [Improving incremental build speed](https://developer.apple.com/documentation/xcode/improving-the-speed-of-incremental-builds).
- [Distributing your app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).

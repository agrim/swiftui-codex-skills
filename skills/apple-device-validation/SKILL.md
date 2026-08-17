---
name: apple-device-validation
description: Apple app runtime proof across simulators, Macs, physical Apple devices, Apple Watch, and paired-device workflows. Use when the request requires building for a destination as part of a launch or runtime check, running, installing or sending an app to a phone, capturing screenshots, validating rendering or interaction, proving watch and phone behavior, exercising hardware-dependent behavior, or diagnosing and classifying simulator, device, and tooling infrastructure failures, including signing or provisioning that blocks installation. Do not use for an ordinary compile-only build, routine source-level tests, UI design review, or standalone signing configuration; pair with apple-swiftui-native-apps for UI semantics, apple-app-store-readiness for TestFlight and App Review orchestration, and the relevant governance or productization skill for configuration and distribution fixes.
---

# Apple Device Validation

## Scope And First Pass

- Own runtime evidence: destination selection, build-for-run, install, launch, screenshot, interaction, lifecycle, watch or phone projection, hardware proof, and infrastructure classification.
- Preserve the user's requested boundary. `Send` or `install` means install only; do not infer launch, uninstall, state reset, or source changes.
- Define the exact claim before running tools: compile, test, install, launch, render, tap, drag, persist, sync, use hardware, or reproduce a failure.
- Resolve the repository, project or workspace, scheme, configuration, target platform, bundle identity, destination, and expected state. Inspect current destinations rather than relying on remembered identifiers.
- Prefer XcodeBuildMCP when available for simulator build-and-run, runtime tests, screenshots, UI inspection, and paired watch or iOS workflows. Call `session_show_defaults` before the first build, run, or test in a session.
- When using shell tools, retain the exact `xcodebuild`, `simctl`, or `devicectl` command, destination, exit status, and relevant output.
- Read `references/device-validation-patterns.md` for the proof matrix and operational procedures whenever the task involves screenshots, phone delivery, watch parity, physical hardware, simulator failure, or a claim stronger than compile success.

## Route And Pair

- Pair with `apple-swiftui-native-apps` when deciding whether the rendered control, hierarchy, navigation, accessibility, or interaction-state model is correct. This skill proves the runtime claim; it does not invent the UI contract.
- Pair with `apple-project-governance` for target, scheme, bundle identity, entitlement, signing setting, or generated-project ownership failures.
- Pair with `apple-privacy-system-integrations` for permission prompts, protected data, Apple framework semantics, or privacy artifacts, and with `macos-productization` for macOS distribution signing or packaging.
- Pair with `apple-app-store-readiness` when this runtime evidence is a gate for TestFlight, storefront screenshots, App Review instructions, submission, or release. This skill proves the candidate behavior; it does not own App Store Connect state.

## Proof Procedure

1. **Set the proof contract.** State the claim, minimum sufficient destination, required app state, and evidence that would establish or refute it.
2. **Check the environment.** Confirm destination availability, boot or pairing state, platform runtime, and tool or service health before attributing a failure to source.
3. **Run the narrow prerequisite.** Build or test only the scheme and destination needed for the requested runtime proof.
4. **Advance only as authorized.** Install, launch, interact, reset, or uninstall only when the claim or user request requires that step.
5. **Capture comparable evidence.** Preserve relevant logs and use deterministic screenshot state, device, orientation, appearance, and output location.
6. **Clean the harness.** Remove temporary launch arguments, fixtures, accessibility shortcuts, injected state, and validation-only source unless the user asked to keep them.
7. **Report the evidence level.** Separate source inspection, compile, test, install, launch, render, interaction, hardware, and cross-device proof; name anything still unverified.

## Runtime Rules

- Never present build success as launch, rendering, interaction, or visual proof.
- Never present a simulator result as physical-device proof when touch, drag, camera, microphone, sensors, protected data, watch delivery, signing, provisioning, or installation behavior is material.
- Do not treat a documented API, successful compile, or matching first-party screenshot as proof that a public affordance renders on the target platform. Distinguish API availability, simulator limitations, hardware requirements, and app defects before changing source.
- Use physical-device confirmation when the behavior depends on hardware or when the user explicitly asks for device confidence.
- If simulator and device intentionally use different persistence, account, cloud, or integration backends, report them as separate proof lanes. A local simulator fallback does not prove the signed device or service path, and a host-shell read does not prove sandboxed-container state.
- For phone delivery, install without launching unless launch is explicit. Uninstall or reset first only when explicit; after installation, verify the requested bundle is present instead of inferring success from a build log.
- Do not claim that uninstalling an app cleared protected or system-managed data unless that data store was independently inspected and proven clear.
- For watch work, validate the watch surface and the paired-phone projection when state or delivery crosses devices. Treat phone and watch as distinct interaction surfaces even when they share state.
- For widgets and other extensions, prove the whole projection chain that matters to the claim: target embedding, installation or registration, shared-data handoff, snapshot or timeline generation, rendering, refresh, stale or unavailable transitions, and host-surface behavior. A single app launch or widget screenshot does not prove freshness over time.
- When launch, migration, or persistence readiness is material, extend launch proof through store readiness and the first meaningful mutation. Observe the resulting state and exercise relaunch or restoration when persistence is part of the claim.
- Treat CoreSimulator service failures, unavailable runtimes, device visibility, pairing state, install-service errors, signing or provisioning errors, and screenshot timeouts as separate classes. Do not change app source without evidence that source caused the failure.
- Keep raw logs and command output until classification is complete.
- Save screenshots outside tracked source unless the repository intentionally owns them. Remove temporary screenshot harnesses and launch state before the final build.
- If relevant source or generated project state changes during validation, repeat the affected checks against the current combined state. Do not hand off a green result from an older worktree snapshot.

## Completion Contract

- Run narrow builds or tests before expensive visual and hardware checks.
- Capture the smallest relevant destination and a representative larger destination when truncation or layout is at risk.
- Record the exact destination, platform and OS context, app state, command or tool action, and resulting artifact.
- Report what passed, what failed, whether a failure belongs to app, configuration, infrastructure, or unknown state, and the strongest claim the evidence supports.
- Do not describe requested runtime proof as complete when only a weaker evidence level succeeded.

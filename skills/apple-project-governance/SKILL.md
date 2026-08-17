---
name: apple-project-governance
description: "Govern source-controlled Apple project structure and effective build configuration for Swift, SwiftUI, Xcode, XcodeGen, and SwiftPM repositories. Use when creating, modifying, auditing, or debugging manifests, generated projects, targets, target membership, schemes, bundle identifiers, app groups, entitlement wiring, Info.plist inputs, build settings, package exposure, CI project settings, app-icon sources, or app identity, including missing resources, unknown schemes, inconsistent products, and local-versus-CI configuration drift. This skill owns where configuration is declared and whether the built product receives it. Pair with apple-privacy-system-integrations for protected-data and permission semantics, apple-device-validation for runtime proof, apple-app-store-readiness for App Store record and submission coherence, and macos-productization for macOS distribution artifacts."
---

# Apple Project Governance

## Workflow

1. Define the affected products, targets, schemes, configurations, platforms, and CI paths before editing.
2. Find the owner of each value. Inspect `project.yml` or another generator manifest, `.xcodeproj`, `.xcworkspace`, `Package.swift`, shared schemes, target membership, entitlement files, `Info.plist` inputs, build settings, app constants, and CI configuration.
3. Map cross-product consequences. Trace identity and capability values through the app, extensions, widgets, watch products, tests, associated domains, provisioning expectations, and services.
4. Edit the source of truth. If a manifest generates the project, change the manifest and regenerate; do not hand-edit generated structure unless no upstream owner exists or the user explicitly requests a temporary emergency patch.
5. Inspect the regenerated diff before debugging code. Treat a missing target, scheme, resource, entitlement, or generated setting as a project defect even when it presents as a runtime bug.
6. Prove both declaration and effect with the validation ladder below.

Read [the project governance playbook](references/project-governance-patterns.md) for the ownership matrix, cross-target checks, command semantics, and failure routing whenever work touches multiple products, generated files, schemes, dependencies, signing inputs, or app identity.

## Invariants

- Keep source-owned and generated files distinct. Never place a lasting decision only in output owned by an upstream manifest.
- Keep target membership explicit. Verify that code, resources, model files, privacy manifests, intents, widgets, watch assets, and tests belong to every intended target and no unintended target.
- Keep schemes reviewable. When build or test actions change, inspect shared schemes and CI selection rather than assuming Xcode inferred the contract.
- Keep app identity coherent. Reconcile bundle IDs, app groups, keychain groups, suite names, CloudKit containers, HealthKit identifiers, associated domains, deep-link constants, and provisioning expectations across every product.
- Keep public identity coherent across product display names, companion products, system metadata, icon sources, and built resources. Pair with `apple-app-store-readiness` for App Store record, storefront, and review coherence; do not rename stable internal identifiers or storage keys merely to make source spelling match the public brand.
- Keep one canonical editable shipping app-icon source per intended pipeline. Verify generator or project ownership, target membership, asset-name settings, and compiled variants before removing a legacy catalog or checkpoint copy.
- Prefer typed constants to repeated identifier strings shared by apps, extensions, widgets, watch products, services, and tests.
- Treat build settings as code. Minimize unrelated churn and justify whether each setting belongs at project, target, or configuration scope.
- Check package and dependency changes for platform availability and target exposure; resolving a package is not proof that the intended target links or embeds it.
- Keep project-configuration changes separate from unrelated UI or business-logic refactors when practical.

## Skill Boundaries

- Use this skill to wire capabilities and prove effective `Info.plist`, resources, build settings, and entitlements in a built product.
- Pair with `apple-privacy-system-integrations` to decide whether protected data access, permission behavior, purpose text, retention, projections, and disclosures are correct.
- Pair with `apple-device-validation` to prove launch, installation, prompts, extensions, and device behavior at runtime.
- Pair with `apple-app-store-readiness` for App Store Connect identity, metadata-to-binary coherence, release-candidate selection, reviewability, and submission gates.
- Pair with `macos-productization` for Developer ID or App Store signing, hardened runtime, notarization, packaging, update channels, and release verification.

## Validation Ladder

Run only the applicable steps, but do not substitute one step for a different claim:

1. Run the repository's manifest generator, then inspect the generated project diff. Confirm intended changes and reject unrelated generated churn.
2. Run `xcodebuild -list` against the selected project or workspace to prove which targets, configurations, and schemes Xcode discovers.
3. Run `xcodebuild -showdestinations` for the selected scheme to prove destination availability. Do not treat destination discovery as proof of target membership or effective settings.
4. Run `xcodebuild -showBuildSettings` for the exact project or workspace, scheme, configuration, and destination needed to inspect inherited and resolved settings.
5. Run the narrowest build or test that exercises the affected product and target graph.
6. Inspect the built `Info.plist` and bundled resources when the claim concerns generated properties or resource membership; inspecting source files alone is insufficient.
7. Inspect the built product's signed entitlements when capabilities or signing are involved and the build type supports meaningful signing evidence; an entitlement source file alone is insufficient.
8. Run `git diff --check` and review source-owned plus generated diffs before handoff or any authorized commit.

If Xcode, simulator, or device services fail, first classify the failure as project configuration, compilation, signing, destination availability, or infrastructure. Do not change source to compensate for an unproven infrastructure failure.

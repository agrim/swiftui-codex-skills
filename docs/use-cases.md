# Use Cases

This repository is useful when an AI coding agent can already write Swift or SwiftUI, but needs sharper Apple-app judgment.

## Native SwiftUI UI

Use `apple-swiftui-native-apps` when a UI looks plausible but not native enough.

It pushes the agent to inspect actual SwiftUI control structure: `Button`, `Menu`, toolbar placement, role, button style, tint, foreground resolution, Dynamic Type, VoiceOver, layout stability, and device screenshots.

## Xcode Project Integrity

Use `apple-project-governance` when the work touches targets, schemes, manifests, generated Xcode projects, bundle identifiers, app groups, entitlements, or build settings.

It prevents "the code is right but the project is wrong" failures.

## Privacy And Apple Frameworks

Use `apple-privacy-system-integrations` when adding or auditing permissions, HealthKit, CloudKit, App Intents, widgets, Live Activities, Spotlight, companion sync, or privacy manifests.

It pushes the agent to handle user purpose, denied states, fallbacks, retention, system projection, and tests in one coherent change.

## Device And Screenshot Proof

Use `apple-device-validation` when a change needs proof on a simulator, phone, watch, screenshot, or real installation.

It helps separate build success from visual proof, device proof, and infrastructure failure.

## Performance-Sensitive Cleanup

Use `apple-performance-cleanup` when simplifying code that affects startup, parsing, telemetry, rendering, persistence, memory, or concurrency.

It keeps the agent from turning cleanup into a rewrite and losing edge-case behavior.

## macOS Productization

Use `macos-productization` when preparing a macOS app for distribution.

It focuses the agent on signing, entitlements, hardened runtime, notarization, packaging, app icons, release artifacts, install behavior, and Gatekeeper expectations.

## Public Skill Hygiene

Use the repository validators before publishing:

```bash
python3 scripts/validate_skills.py .
python3 scripts/scan_apple_repo.py /path/to/apple-app-repo
```

They help keep skill packages structurally valid and reduce the chance of publishing local paths, secrets, or private artifacts.

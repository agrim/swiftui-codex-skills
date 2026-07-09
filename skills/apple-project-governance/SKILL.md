---
name: apple-project-governance
description: Apple project governance for Swift, SwiftUI, Xcode, and XcodeGen app repositories. Use when modifying or reviewing project manifests, generated Xcode projects, targets, schemes, bundle identifiers, entitlements, build settings, package dependencies, app groups, CI project settings, or app identity.
---

# Apple Project Governance

## First Pass

- Find the source of truth before editing: `project.yml`, `.xcodeproj`, `.xcworkspace`, `Package.swift`, schemes, target membership, entitlements, `Info.plist`, build settings, app constants, and CI configuration.
- If a generated project has a manifest, edit the manifest first and regenerate. Do not hand-edit generated project structure unless no manifest exists or the user explicitly asks for an emergency patch.
- Map every app identity change across bundle identifiers, entitlements, app groups, associated domains, provisioning expectations, constants, widgets, extensions, watch targets, and tests.
- Treat project configuration as product surface. A target, entitlement, scheme, or generated resource mistake can look like a runtime bug.
- Read `references/project-governance-patterns.md` when the task touches multiple targets, generated files, signing, schemes, or app identity.

## Rules

- Keep generated and source-owned files distinct. Do not make lasting design decisions in generated output when an upstream manifest owns the value.
- Keep target membership explicit. When adding code, resources, privacy files, intents, widgets, watch assets, or tests, verify the intended targets include them and unintended targets do not.
- Keep schemes reviewable. If tests or build actions change, inspect shared schemes and CI behavior rather than assuming Xcode inferred the right thing.
- Keep app identity coherent. Bundle IDs, app groups, keychain groups, suite names, CloudKit containers, HealthKit identifiers, and deep-link constants must agree.
- Prefer typed constants over string drift for identifiers used across app, extension, watch, widget, and tests.
- Treat build settings as code. Avoid broad settings churn and document why the setting belongs at project, target, or configuration level.

## Validation

- Run the manifest generator if one exists.
- Run `xcodebuild -showdestinations` or the equivalent project discovery step after scheme/project changes.
- Run the narrowest build or test that proves target membership, resources, entitlements, and generated project state.
- Inspect `git diff --check` and the generated project diff before committing.
- If validation fails because simulator or Xcode services are broken, separate infrastructure failure from project failure before changing source.

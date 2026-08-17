# How These Skills Layer On Codex

These skills are a sharpening layer for Apple-platform app work. They sit on top of Codex's existing coding ability, tool use, built-in skills, and any instructions already present in the app repository.

## The Stack

1. **Codex core behavior**
   - Reads and edits the current repo.
   - Runs commands, tests, builds, and source searches.
   - Preserves user instructions and avoids unrelated changes.

2. **Existing Codex skills and tools**
   - Provide broad workflows for SwiftUI implementation, Liquid Glass, simulator/device debugging, GitHub publishing, skill authoring, and other reusable tasks.
   - Supply tool-specific procedures such as XcodeBuildMCP session defaults or GitHub branch/push flow.

3. **App-local instructions**
   - Capture the actual app's current architecture, schemes, targets, product direction, naming, tests, and constraints.
   - Override generic advice when the local repo has a deliberate pattern.

4. **This repository's Apple skills**
   - Add narrow Apple-app judgment rules that repeatedly matter in production-feeling app work.
   - Force sharper questions before implementation: Is this a native control? Is the foreground system-resolved? Is the entitlement wired? Is the permission explained? Is the screenshot proof real? Is this cleanup behavior-preserving?

## How The Skills Improve App Creation

- `apple-swiftui-native-apps` tightens UI and interaction work.
  - Example: instead of making a tappable `HStack` look like a button, start from `Button`, role, style, shape, toolbar placement, and system foreground behavior.
  - Example: if a colored button has unreadable text, debug the button structure and environment rather than hard-coding label color.

- `apple-project-governance` tightens project changes.
  - Example: before adding an extension or capability, inspect the manifest, generated project, target membership, schemes, bundle identifiers, entitlements, and constants together.
  - Example: if a manifest owns the Xcode project, edit the manifest and regenerate instead of hand-editing generated files.

- `apple-privacy-system-integrations` tightens framework adoption.
  - Example: adding a sensitive framework is not just an import. Audit permission purpose, entitlements, manifests, disclosures, retention, denied/unavailable states, user explanation, and focused tests, then change only the layers that apply.
  - Example: exporting to a system service should preserve truthful app data and degrade gracefully when the service is unavailable.

- `apple-device-validation` tightens proof.
  - Example: a build proves compilation, not layout. Use screenshots when typography, truncation, glass, color, or watch sizing matters.
  - Example: a simulator failure may be infrastructure. Separate simulator service, signing, install, destination, and app-code failures before rewriting source.

- `apple-performance-cleanup` tightens simplification.
  - Example: remove duplication through tiny helpers and source-contract tests instead of broad rewrites.
  - Example: preserve the distinction between nil, zero, stale, failed, denied, and unavailable states when cleaning parsing or state code.

- `apple-app-store-readiness` tightens submission orchestration.
  - Example: freeze the smallest complete release promise before adding infrastructure, then align the exact binary, public support and privacy pages, screenshots, metadata, review access, and App Store Connect state.
  - Example: treat an App Store name, domain, trademark clearance, TestFlight upload, App Review approval, and public release as separate evidence gates.

- `macos-productization` tightens release work.
  - Example: local signing is not notarization. Verify signing, entitlements, hardened runtime, packaging, launch, and Gatekeeper behavior for the intended distribution channel.
  - Example: app icon and packaging quality must be verified in the built product, not only in source assets.

## How To Choose A Skill

- Use `apple-swiftui-native-apps` for UI, SwiftUI surface structure, Liquid Glass, controls, navigation, visual hierarchy, and accessibility-sensitive interaction.
- Use `apple-project-governance` for project files, schemes, target membership, bundle IDs, entitlements, generated project files, build settings, and dependency exposure.
- Use `apple-privacy-system-integrations` for permissions, sensitive data, privacy artifacts, and HealthKit, CloudKit, App Intents, widgets, Live Activities, Spotlight, or companion work that requires reasoning about data, account, service, process, or device boundaries.
- Use `apple-device-validation` for simulator runs, physical-device installs, watch validation, screenshots, UI proof, and infrastructure triage.
- Use `apple-performance-cleanup` for startup, hot paths, telemetry, parsing, rendering, concurrency, memory, and behavior-preserving simplification.
- Use `apple-app-store-readiness` for first submissions and updates, App Store Connect, rejection-readiness audits, public support and privacy surfaces, exact release candidates, review access, metadata, screenshots, submission, and release state.
- Use `macos-productization` for signing, notarization, packaging, DMGs, icons, release notes, installation, and direct distribution.

For a Mac App Store release, use both: `apple-app-store-readiness` owns storefront and App Review orchestration, while `macos-productization` owns the macOS archive, signing, sandbox, export, packaging, and installed-artifact proof.

## What This Layer Is Not

- It is not a replacement for official Apple documentation.
- It is not a replacement for app-local instructions.
- It is not a replacement for real builds, tests, screenshots, or device proof.
- It is not a reason to overrule a deliberate repo-specific pattern without evidence.

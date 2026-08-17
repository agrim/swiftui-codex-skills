---
name: macos-productization
description: "Release and distribution productization for macOS Swift and SwiftUI apps. Use when preparing, reviewing, or validating an installable or shippable macOS artifact or release flow: distribution signing and embedded entitlements, hardened runtime, notarization and Gatekeeper, App Store export, DMG or package creation, built-product icons, installation checks, Sparkle or update feeds, and local, internal, direct, or Mac App Store channels. Do not use for ordinary development-time project configuration, target wiring, or App Store storefront and review orchestration alone; pair with apple-project-governance for source-of-truth changes and apple-app-store-readiness for App Store Connect, metadata, reviewability, submission, and release gates."
---

# macOS Productization

## Establish the Release Contract

- Identify both the requested mode—review or diagnose, implement or prepare, validate or release—and the distribution channel: local development, internal or enterprise, direct download, or App Store. Treat DMG or package delivery and Sparkle or another updater as channel overlays.
- Do not infer permission to install, launch, sign with private credentials, notarize, upload, publish, delete, or make a system-wide change from a review or preparation request.
- Inspect bundle identity, signing identity, embedded entitlements, hardened runtime, sandboxing, app icon source, packaging scripts, release metadata, artifacts, and install-path expectations.
- Treat project settings as intent and the archive, built app, package, installed copy, and service receipts as progressively stronger evidence.
- Read `references/macos-productization-patterns.md` for the authority model, channel gates, operational sequences, and evidence checklist.
- Pair with `$apple-project-governance` for source-owned project, target, scheme, identity, build-setting, and entitlement changes. Use this skill to verify what the release artifact actually contains.
- Pair with `$apple-app-store-readiness` for Mac App Store product promise, public URLs, storefront metadata, review access, submission state, and release method. This skill retains ownership of the macOS archive, signing, sandbox, embedded code, export, package, and installed-artifact gates.

## Release Rules

- Do not claim an app is notarized, signed for distribution, or Gatekeeper-clean unless verified.
- Keep local ad hoc signing distinct from Developer ID signing, App Store signing, and notarized distribution.
- Prefer reproducible packaging scripts over hand-built archives.
- Verify app icons through the current Apple asset pipeline. Do not flatten or simplify assets in a way that breaks platform presentation.
- Keep privileged installs, deletion, and system-wide changes explicit and user-approved.
- Preserve release notes, version numbers, build numbers, and attached artifacts as a coherent release.
- Treat packaging and signing as user-facing product behavior, not an afterthought.

## Validate the Requested Gate

- Run signing inspection, entitlement inspection, and Gatekeeper/notarization checks appropriate to the distribution channel.
- When packaging changes and the requested mode authorizes runtime validation, mount or install the packaged artifact and launch the installed copy. Otherwise, report that gate as unverified rather than changing external state.
- Verify app icon appearance in the built product, not only source assets.
- Confirm release artifacts match the commit and version being published.
- Pair with `$apple-device-validation` when release proof includes a simulator, physical device, watch, screenshot, or companion target; keep macOS installed-artifact checks in this workflow.
- Report the exact artifact inspected, the checks performed, any external action taken, and every release gate that remains unverified.

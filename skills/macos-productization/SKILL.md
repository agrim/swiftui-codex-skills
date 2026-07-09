---
name: macos-productization
description: macOS app productization for Swift and SwiftUI apps. Use when preparing or reviewing signing, entitlements, hardened runtime, notarization, packaging, DMG creation, app icons, release notes, installation, Gatekeeper behavior, Sparkle/update distribution, or App Store versus direct distribution.
---

# macOS Productization

## First Pass

- Identify the distribution channel: local development, direct download, enterprise/internal, or App Store.
- Inspect bundle identifiers, signing identity, entitlements, hardened runtime, sandboxing, app icon source, packaging scripts, release artifacts, and install path expectations.
- Read `references/macos-productization-patterns.md` for signing, notarization, packaging, icon, or release-flow work.
- Treat packaging and signing as user-facing product behavior, not an afterthought.

## Rules

- Do not claim an app is notarized, signed for distribution, or Gatekeeper-clean unless verified.
- Keep local ad hoc signing distinct from Developer ID signing, App Store signing, and notarized distribution.
- Prefer reproducible packaging scripts over hand-built archives.
- Verify app icons through the current Apple asset pipeline. Do not flatten or simplify assets in a way that breaks platform presentation.
- Keep privileged installs, deletion, and system-wide changes explicit and user-approved.
- Preserve release notes, version numbers, build numbers, and attached artifacts as a coherent release.

## Validation

- Run signing inspection, entitlement inspection, and Gatekeeper/notarization checks appropriate to the distribution channel.
- Mount or install packaged artifacts and launch the installed app when packaging changes.
- Verify app icon appearance in the built product, not only source assets.
- Confirm release artifacts match the commit and version being published.

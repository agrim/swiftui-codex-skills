---
name: apple-privacy-system-integrations
description: Privacy-safe Apple system integration for Swift and SwiftUI apps. Use when adding, changing, auditing, or debugging HealthKit, CloudKit, App Intents, WidgetKit, ActivityKit, Live Activities, Core Spotlight, WatchConnectivity, permissions, privacy manifests, Info.plist purpose strings, sensitive data flows, or App Store privacy behavior.
---

# Apple Privacy System Integrations

## First Pass

- Identify the user value, data touched, permission boundary, fallback behavior, retention model, and export/sync path before writing integration code.
- Inspect entitlements, `Info.plist` purpose strings, privacy manifests, app constants, system-service wrappers, settings/onboarding copy, tests, and existing denial/unavailable handling.
- Read `references/privacy-system-patterns.md` when a change touches sensitive data, Apple system frameworks, companion devices, app extensions, or App Store privacy claims.
- Prefer local-first behavior and best-effort integrations. The app should remain useful when a permission, account, device, service, or framework is unavailable.

## Rules

- Bundle privacy work. A sensitive framework change should include code, entitlements, purpose strings, privacy manifest updates, user-facing explanation, storage/retention mapping, and tests in the same change.
- Never add hidden permission paths. Every camera, microphone, health, location, contacts, Bluetooth, speech, notification, or similar access path needs a clear user-facing purpose.
- Do not invent system data. Export truthful system-compatible projections only; keep app-only details in the app's own store unless the platform provides a truthful representation.
- Keep sync and export distinct. Local persistence, cloud sync, health export, widget projection, live activity projection, and companion-device transfer have different guarantees.
- Use typed permission scopes and typed integration state. Avoid scattered booleans and string commands.
- Treat denial, absence, account mismatch, and device unavailability as normal states, not exceptional surprises.

## Validation

- Test first-run, granted, denied, unavailable, revoked, and retry states where relevant.
- Verify entitlement and purpose-string changes compile into the intended targets.
- Verify widgets, intents, live activities, spotlight, watch, or cloud projections do not expose private data beyond their stated purpose.
- Run focused tests around data mapping and fallback behavior before broad UI tests.

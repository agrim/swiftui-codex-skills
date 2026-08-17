---
name: apple-privacy-system-integrations
description: "Design and audit privacy-safe Apple system integrations for Swift and SwiftUI apps. Use when adding, changing, reviewing, or debugging protected-data access; permission prompts or states; Info.plist purpose strings; PrivacyInfo.xcprivacy; retention or deletion; truthful export and projection; App Store privacy details; or HealthKit, CloudKit, App Intents, WidgetKit, ActivityKit, Live Activities, Core Spotlight, WatchConnectivity, companion-device, extension, or similar work that requires reasoning about data, permission, account, service, process, or device boundaries. This skill owns data and permission semantics, user purpose, boundary crossing, fallback state, retention, disclosure, and system projections. Pair with apple-project-governance for target wiring and effective entitlements, apple-device-validation for runtime proof, apple-app-store-readiness for store submission orchestration, and macos-productization for distribution artifacts."
---

# Apple Privacy System Integrations

## Workflow

1. Write the integration contract before code: user value, exact data and scope, source, destination, permission boundary, supplementary-or-essential role, fallback, retention and deletion, and every sync, export, index, or projection path.
2. Inspect the complete path: framework wrapper, typed app constants, local store, cloud or companion transport, entitlement wiring, `Info.plist` purpose strings, `PrivacyInfo.xcprivacy`, settings and onboarding copy, system surfaces, tests, and App Store privacy details.
3. Classify the dependency. Prefer local-first and best-effort behavior for supplementary integrations, or whenever core user value can remain local. For an essential integration, explain the dependency before access, gate only the dependent experience, and represent denial or unavailability honestly.
4. Model permission scopes and integration state with types. Include first-run or not-determined, granted, denied, unavailable or restricted, revoked, and retry or transient-failure behavior where the framework supports or requires them.
5. Audit every layer in [the privacy and integration playbook](references/privacy-system-patterns.md). Update only the artifacts that apply, but keep code, applicable declarations, user explanation, storage and retention mapping, disclosures, and focused tests coherent in the same change.
6. Validate the truthful data mapping and every relevant failure path before broad UI testing.

## Invariants

- Never introduce a hidden permission path. Camera, microphone, health, location, contacts, Bluetooth, speech, notifications, and similar access require a clear user-facing purpose and context before the system prompt.
- Never infer “we do not store data” from the absence of developer-operated servers. Inventory local persistence, app-controlled CloudKit containers, public records, managed relays, provider storage, credentials, derived data, retention, and operator access; use a narrower category-and-boundary claim when any data persists.
- Make privacy copy name the protected data category, boundary, and relevant operator precisely. Distinguish “this app's operator does not receive or store existing calendar event details” from broader claims about all user data, on-device storage, Apple-managed cloud storage, or connection credentials.
- Never infer a user's identity from provider labels, system-source titles, event participants, or similar metadata unless the framework documents an explicit stable identity contract. Collect identity in the workflow that needs it and preserve an existing value when removing or deferring an earlier field.
- Do not equate an entitlement with user consent, a purpose string with a privacy manifest, or a privacy manifest with App Store privacy details. Audit each layer according to its own role.
- Treat a privacy policy as disclosure, not blanket consent. Do not make a general `Continue` action claim policy agreement unless the product genuinely requires, versions, records, and can honor withdrawal of that agreement; keep protected-resource permissions and collection-specific consent at the point of need.
- If a privacy policy is linked during first run, keep the same current policy permanently reachable after onboarding. A transient disclosure does not replace durable in-app access or the public policy URL required by the release channel.
- Do not invent system data. Keep app-only truth in the app's canonical store unless the platform provides a semantically truthful representation; export only the supported projection.
- Keep local persistence, cloud sync, system export, widget projection, live-activity projection, search indexing, intent exposure, and companion-device transfer distinct. They cross different boundaries and carry different guarantees.
- Minimize the data and fields exposed by widgets, intents, live activities, Spotlight, watch or companion products, cloud stores, and other boundary surfaces to their stated purpose.
- Use typed permission scopes, commands, operation status, and integration state. Avoid scattered booleans, magic strings, and ambiguous success flags.
- Keep App Intent, App Schema, Shortcut, Siri, and model-assisted adapters thin. Resolve and validate their parameters, then call the same typed, permission-aware command or repository path used by the app UI; do not create a parallel system-only mutation model.
- Let probabilistic language or model interpretation propose a typed operation, but keep authorization, confirmation, persistence, idempotency, retry, audit, and user-visible consequences deterministic. Prefer specific truthful intents, entities, and schema semantics over one unrestricted catch-all action.
- Treat denial, data absence, account mismatch, service or framework unavailability, and device absence as expected states. Never report success when an essential dependency did not complete.
- Make retries durable and idempotent where work can be repeated. Distinguish a user-controlled permission decision from a transient transport or service failure; do not create repeated prompts, duplicate exports, or invisible data loss.
- Keep notification authorization, remote-subscription coverage, background delivery, visible-alert preference, and successful fetch as separate states. Report alerts as active only when the exact requested subscription set is covered; expose reconciling and retryable failure honestly.
- Minimize notification payloads to the generic destination or operation needed for routing. Deliver UI-facing routing on the main actor, and do not manufacture a visible new-data alert when a background fetch reports no change.
- For externally persisted side effects such as Calendar writes, save a durable operation identity and resumable intent before invoking the system service. Embed only the minimum opaque marker needed to adopt or reconcile the result after termination.
- Define retention and deletion behavior for every new stored, synced, indexed, or exported representation, including what happens after revocation or account change.

## Skill Boundaries

- Use this skill to decide what data access and projection mean, when to request permission, what the user sees, how state degrades, and what privacy artifacts or disclosures apply.
- Pair with `apple-project-governance` to place files in the intended targets and prove effective `Info.plist`, resources, build settings, and signed entitlements.
- Pair with `apple-device-validation` to verify prompts, revocation, companion behavior, widgets, intents, live activities, and system-service behavior on a simulator or physical device.
- Pair with `apple-app-store-readiness` when the privacy policy, App Store privacy answers, account deletion, permission behavior, or public disclosures are gates in a store submission. This skill establishes their truth; the readiness skill orchestrates the submission.
- Pair with `macos-productization` for distribution certificates, hardened runtime, notarization, packaging, and release-channel requirements.

## Validation Ladder

1. Run focused tests for data mapping, deduplication, retention or deletion, typed state transitions, fallback behavior, and retry safety.
2. Exercise first-run, granted, denied, unavailable or restricted, revoked, account-mismatch, device-absence, and retry states where relevant. Verify transitions, not only static screens.
3. Confirm that permission requests occur only from an explained user context and that denial does not cause loops or hidden re-prompts.
4. Verify every applicable purpose string, entitlement, privacy manifest, resource, and projection is present in the intended target and absent from unintended targets. Use `apple-project-governance` for built-artifact proof.
5. Inspect widgets, intents, live activities, Spotlight indexes, watch or companion transfers, cloud records, and exports for data beyond their stated purpose.
6. For callable system actions, test parameter resolution, authorization, confirmation, command persistence, idempotency, result disclosure, and parity with the equivalent in-app operation separately from compiled intent metadata.
7. Reconcile actual on-device processing, off-device transfer, third-party behavior, retention, linking, and tracking with the privacy manifest and current App Store privacy details; update only what the behavior makes applicable.
8. Use `apple-device-validation` when a claim depends on a real prompt, account, hardware capability, companion device, extension lifecycle, Siri or provider routing, or system UI.

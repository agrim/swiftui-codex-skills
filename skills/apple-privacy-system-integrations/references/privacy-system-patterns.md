# Apple privacy and integration safety: playbook

## Build a data inventory, not a slogan

For each category record: source, purpose, processing location, persistent stores, remote recipients, operator access, retention, deletion trigger, and user-facing disclosure. Include credentials, diagnostic logs, derived summaries, indexes, caches, exports, and backups that affect the promise.

“Processed on device” is not equivalent to “never retained.” Apple-managed cloud storage is still a boundary crossing. A provider label or calendar participant is not a stable identity contract. Describe what the operator does and does not receive rather than making blanket claims from architecture labels.

## Distinguish five artifacts

| Artifact | What it establishes | What it does not establish |
| --- | --- | --- |
| Entitlement | Signed capability or access group | User consent or successful service access |
| Usage description | System prompt purpose text | A complete privacy inventory |
| Privacy manifest | Applicable data/API declarations | All store questionnaire answers or permission behavior |
| Store privacy details and policy | Public disclosures | Runtime enforcement or user consent by themselves |
| Feature-specific consent/permission | The relevant authorization decision | Unlimited future collection or every framework scope |

Check the current Apple required-reason API list and approved reasons for the exact behavior. Do not guess reason codes, copy a manifest unrelated to the app, or claim that one manifest covers every bundled SDK automatically. Inspect actual dependency behavior and the built archive.

## Permission state machines

Request the narrowest scope needed at the point of use. Explain the user benefit without adding manipulative pre-permission screens or repeatedly prompting after denial. Keep the core local experience usable when a supplementary integration is unavailable; an essential dependency may gate its own feature honestly.

Model only states the API can establish. For example, an empty HealthKit query is not evidence that read access was denied. Some frameworks support limited or partial access, and read/write authorization may differ. Verify current scope and status APIs before naming UI states.

Separate authorization from account readiness, device presence, background delivery, registration, requested subscription coverage, and operation completion. Granting permission does not make an asynchronous operation successful.

## Boundary-safe integration

Keep app-only truth in the canonical store and export only representations supported by the framework's semantics. Minimize widget, intent, notification, live-activity, search, and companion-device payloads. Revalidate account and authorization when a command arrives, not only when the surface was created.

Where duplicate external effects matter, persist an operation identity and reconciliation plan before crossing the boundary. A transient network error is not the same as a user permission decision. Retrying must not duplicate records or erase a successful but unacknowledged operation.

## Retention, deletion, and security

Store small secrets in the appropriate secure credential facility, not preferences or public logs. Redact diagnostics at collection; hiding them only in the UI does not remove the underlying exposure. Specify protection and accessibility requirements for sensitive files and credentials.

Define what happens after logout, revocation, account deletion, or device unlinking. Invalidate account-scoped caches, indexes, projections, and in-flight responses. Explain when an exported record remains in a user-controlled system store instead of promising deletion the app cannot guarantee.

A privacy-policy link should remain reachable after first run. Where account deletion applies, design a real initiation and completion path, not merely a logout or deactivation button. Check current platform and jurisdiction requirements for the actual product rather than treating this playbook as legal advice.

## Verification

Test permission transitions and data mapping independently from UI rendering. Inspect both successful and failed exports, pending reconciliation, stale widgets, diagnostic logs, and deletion results. Validate the signed/bundled configuration and test real accounts or devices when the framework boundary requires them. Report facts, documented constraints, recommendations, and unverified claims separately.

## Sources

- [privacy](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests) — Describing data use in privacy manifests.
- [required-reasons](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api) — Required reason APIs.
- [sdk-privacy](https://developer.apple.com/support/third-party-SDK-requirements/) — Third-party SDK requirements.
- [healthkit](https://developer.apple.com/documentation/healthkit) — HealthKit.
- [keychain](https://developer.apple.com/documentation/security/keychain-services) — Keychain services.
- [review](https://developer.apple.com/app-store/review/guidelines/) — App Review Guidelines.
- [health-authorization](https://developer.apple.com/documentation/healthkit/hkhealthstore/authorizationstatus(for:)) — HealthKit authorizationStatus(for:).
- [health-privacy](https://developer.apple.com/documentation/healthkit/protecting-user-privacy) — Protecting user privacy with HealthKit.
- [account-deletion](https://developer.apple.com/support/offering-account-deletion-in-your-app/) — Offering account deletion in your app.

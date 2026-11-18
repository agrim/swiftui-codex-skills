---
name: apple-privacy-system-integrations
description: "Audit protected data, permissions, purpose strings, privacy manifests, disclosures, retention, and deletion."
---

# Apple privacy and integration safety

## Inputs

Identify each data category, purpose, source, recipient, and dependent feature.

## Rules

- **PRIV-001 — Trace every copy.** Include local files, system stores, cloud containers, SDKs, logs, and derived data even without an app-operated server.
- **PRIV-002 — Request access at use.** Explain the purpose and request only required scopes. Display only authorization states the framework exposes.
- **PRIV-003 — Check each declaration.** Compare signed entitlements, purpose strings, bundled privacy manifests, store disclosures, and consent flows with actual behavior.
- **PRIV-004 — Handle failure by cause.** Give denial, empty results, account mismatch, revocation, and temporary unavailability their applicable recovery paths.
- **PRIV-005 — Plan retention and removal.** Specify minimum fields, protection, logs, retention, export, and deletion for each stored or transferred copy.

## Workflow

1. Trace one record across extensions, devices, and third parties.
2. Inspect the archive against current framework and SDK requirements. Implement fallback and account cleanup.

## Verify

- PRIV-002, PRIV-004: Deny or limit first-use access. Unrelated features remain usable. An empty HealthKit read reveals no permission decision.
- PRIV-004: Retry offline. The UI distinguishes pending work from completion.
- PRIV-005: Delete a record or switch accounts. Inspect caches, widgets, indexes, exports, and logs for unintended retention or disclosure.

## Output

Report flows, access decisions, declarations, deletion results, and unresolved privacy questions.

## References

- [Permission states and privacy declarations](references/privacy-system-patterns.md)
- [Data inventory across tools and system surfaces](references/integration-data-inventory.md)

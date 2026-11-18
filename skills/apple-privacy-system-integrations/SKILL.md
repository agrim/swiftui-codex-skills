---
name: apple-privacy-system-integrations
description: "Audit permissions, purpose strings, privacy manifests, disclosures, retention, and deletion."
---

# Privacy and permissions

## Inputs

Identify the data, purpose, recipient, and feature.

## Rules

- **PRIV-001 — Trace copies.** Include system stores, cloud, SDKs, logs, and derived data.
- **PRIV-002 — Ask at use.** Explain the purpose, minimize scope, and report only observable authorization states.
- **PRIV-003 — Check declarations.** Match entitlements, purpose strings, manifests, disclosures, and consent to actual use.
- **PRIV-004 — Distinguish failures.** Distinguish denial, empty results, account mismatch, revocation, and outages.
- **PRIV-005 — Manage retention.** Specify fields, protection, retention, logs, export, and deletion per copy.

## Workflow

1. Trace one record across devices and extensions. Check the signed archive against current requirements.

## Verify

- PRIV-002, PRIV-004: Limit access. Unrelated features work. Empty HealthKit reads reveal no permission decision.
- PRIV-003: Trace one data type an SDK declares as collected. Its use matches the archived manifest and published disclosures.
- PRIV-004: Retry offline. Work remains visibly pending.
- PRIV-001, PRIV-005: After deletion or an account switch, check caches, widgets, indexes, exports, and logs for exposed data.

## Output

Report flows, declarations, access, deletion, and gaps.

## References

- [Permissions and declarations](references/privacy-system-patterns.md)
- [Data inventory](references/integration-data-inventory.md)

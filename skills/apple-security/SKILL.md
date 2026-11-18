---
name: apple-security
description: "Review Keychain credentials, transport trust, deep links, imports, sandbox boundaries, and dependencies."
---

# Apple app trust boundaries and secure data

## Inputs

Identify assets, credential lifetimes, untrusted inputs, privileged actions, and supported platforms.

## Rules

- **SEC-001 — Protect credentials.** Scope Keychain access to the feature. Keep tokens, signing secrets, and private diagnostics out of source and artifacts.
- **SEC-002 — Authorize at use.** Parse routes and imports into typed values. Check the active account’s rights to the target before acting.
- **SEC-003 — Preserve transport trust.** Keep system certificate and hostname validation enabled. Scope documented transport exceptions to their intended purpose.
- **SEC-004 — Limit capabilities.** Inspect signed entitlements, access groups, and data scopes against the feature’s requirements.
- **SEC-005 — Inspect executable inputs.** Review executable dependencies and scripts. Grant access to data or credentials only when required and authorized.

## Workflow

1. Trace an external input through authorization, storage, and diagnostics.
2. Correct the failed boundary and exercise the affected command.

## Verify

- SEC-002: Malformed or duplicate route fields and another account’s ID leave stored records unchanged.
- SEC-001, SEC-004: Revoke the credential or deny sandbox access. The command fails without exposing protected data.
- SEC-001, SEC-003: Reject TLS trust. The command reports failure and logs omit secrets.

## Output

Report the asset, boundary, correction, observed rejection, and remaining risk.

## References

- [Credentials, input validation, and tool trust](references/trust-and-input.md)

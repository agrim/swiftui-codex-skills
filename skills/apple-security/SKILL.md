---
name: apple-security
description: "Review Keychain, TLS, deep links, imports, entitlements, and dependencies."
---

# App trust boundaries

## Inputs

Identify assets, untrusted inputs, and privileged actions.

## Rules

- **SEC-001 — Protect credentials.** Scope Keychain access. Exclude secrets and private diagnostics from source and artifacts.
- **SEC-002 — Authorize at use.** Parse routes and imports into typed values. Authorize the target in the current account.
- **SEC-003 — Preserve trust.** Keep system certificate and hostname checks. Scope and document exceptions.
- **SEC-004 — Limit capabilities.** Minimize signed entitlements, access groups, and data scopes.
- **SEC-005 — Review executables.** Inspect scripts and dependencies. Grant only necessary, authorized access.

## Workflow

1. Trace one input through authorization, storage, and logs. Fix and rerun the command.

## Verify

- SEC-002: Malformed or repeated fields and cross-account IDs leave records unchanged.
- SEC-001, SEC-004: Revoke credentials or sandbox access. Observe rejection without disclosure.
- SEC-005: Run a reviewed build script with only its declared inputs. It succeeds without unrelated credentials.
- SEC-001, SEC-003: Present an untrusted certificate. The request fails without logging secrets.

## Output

Report the fix, rejection, and residual risk.

## References

- [Credentials, inputs, and tool access](references/trust-and-input.md)

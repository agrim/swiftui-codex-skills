---
name: apple-security
description: "Review Keychain, TLS, deep links, imports, entitlements, and dependencies."
---

# Check who can read or change protected app data

Review a feature that handles credentials, opens incoming links, imports documents or runs build tools. Trace one operation to see who can perform it and what it exposes.

## Start here

For a link that opens a private document, identify the current account, the permitted record and the component that reads or changes it.

## How to proceed

1. **Check permission where the action runs.** Parse route or import fields into the expected types. Resolve the target against the current account before reading or writing it. <!-- SEC-002 -->
2. **Follow the credential.** Check which components can retrieve it from Keychain. Inspect source, diagnostics and distributed artifacts for unintended copies. <!-- SEC-001 -->
3. **Check the shipping connection.** Keep certificate and hostname validation intact. Trace each transport exception to the particular service that needs it. <!-- SEC-003 -->
4. **Inspect the signed app and extensions.** Narrow entitlements and access groups to the data each feature needs. <!-- SEC-004 -->
5. **Limit build tools to their inputs.** Inspect the scripts and dependencies that execute during the build. Grant only the access their authorized job requires. <!-- SEC-005 -->

## Check the result

- Try malformed or repeated fields and a valid ID from another account. The action rejects them without exposing or changing the record. <!-- SEC-002 -->
- Revoke a credential or sandbox permission, then retry. Check that the failure and its logs reveal no protected data. <!-- SEC-001 SEC-004 -->
- Present an untrusted certificate. The connection fails and the diagnostic contains no secrets. <!-- SEC-001 SEC-003 -->
- Run a reviewed build script with its declared inputs. It produces its output without unrelated credentials. <!-- SEC-005 -->

## What to report

Report the protected operation, the correction, the observed rejection and any remaining risk.

- [Check credentials, incoming data and build-tool access](references/trust-and-input.md)

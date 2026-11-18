---
name: macos-productization
description: "Prepare or verify macOS distribution, including Developer ID or Mac App Store signing, notarization, packaging, Gatekeeper, installation, and updates."
---

# macOS packaging and distribution

## Inputs

Identify channel, authorized stage, revision, version/build, bundle, nested code, signing requirements, package, and updater.

## Rules

- **MAC-001 — Select the channel.** Identify signing, sandbox, hardened runtime, packaging, and review requirements for development, internal, direct, or Mac App Store distribution.
- **MAC-002 — Inspect the deliverable.** Check identity, resources, signature, and entitlements in the exported artifact and installed copy.
- **MAC-003 — Verify the trust chain.** Inspect nested signatures, entitlements and update authenticity. Fix the source of a signing failure.
- **MAC-004 — Record each trust check.** Track signing, notarization acceptance, stapling, Gatekeeper assessment, installation, and launch separately.
- **MAC-005 — Stay within authorization.** Use credentials, submit to services, install, publish, delete, or change system settings only within the approved scope.

## Workflow

1. Inspect the supplied candidate. For an authorized repair, fix the signing or packaging step and export again.
2. Tie the artifact hash, version, release notes, service receipts, and update metadata to that export.
3. For an authorized install test, use the intended distribution path.

## Verify

- MAC-002, MAC-004: For direct download, check notarization and ticket status, assess the quarantined download, and confirm the installed app launches with expected resources and icons.
- MAC-003: For signed updates, verify metadata and payload authenticity. Invalid updates must leave the installed app and user data intact.

## Output

Report artifact hash, channel, external actions, evidence per gate, and pending checks.

## References

- [Channel, signing, and packaging checks](references/macos-productization-patterns.md)
- [Reproducing and verifying an installed release](references/distribution-reproducibility.md)

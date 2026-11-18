---
name: macos-productization
description: "Prepare or verify macOS signing, notarization, packaging, Gatekeeper, installation and updates for Developer ID or Mac App Store distribution."
---

# macOS distribution

## Inputs

Identify the channel, candidate, package, updater and authorized stage.

## Rules

- **MAC-001 — Select the channel.** Choose trust checks for the intended recipients and delivery path.
- **MAC-002 — Inspect the product.** Check identity, resources and entitlements in the export and installed copy.
- **MAC-003 — Verify trust.** Validate nested signatures and update authenticity. Repair failures at their source.
- **MAC-004 — Separate receipts.** Tie trust results to artifact and stage. Recheck affected results after repackaging.
- **MAC-005 — Bound side effects.** Use credentials, submit, install, publish, delete or change system settings only as authorized.

## Workflow

1. Inspect the candidate. After a repair, re-export and identify the new artifact.
2. Match receipts and update metadata to the shipped version and hash.

## Verify

- MAC-002, MAC-004: For notarized distribution, match acceptance to the submission and validate its stapled ticket where applicable. Assess the quarantined download and launch the installed copy with its resources.
- MAC-003: Reject invalid updates while preserving the installed app and data.
- MAC-001, MAC-005: For a Developer ID audit, verify the export’s signer and check the log for unapproved submissions.

## Output

Report channel, hash, actions and evidence or blocker per gate.

## References

- [Signing and packaging](references/macos-productization-patterns.md)
- [Installed release verification](references/distribution-reproducibility.md)

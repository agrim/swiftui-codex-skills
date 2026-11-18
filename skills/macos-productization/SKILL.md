---
name: macos-productization
description: "Prepare or verify macOS signing, notarization, packaging, Gatekeeper, installation and updates for Developer ID or Mac App Store distribution."
---

# Verify the macOS package customers will install

Use this before shipping a Mac app or when a download fails to install, launch or update. Follow the exact package from export to first launch.

## Start here

Identify the distribution channel, version, final package, updater and authorized actions. Keep the downloaded package distinguishable from a development copy already on the Mac.

## How to proceed

1. **Follow the customer’s delivery path.** Choose the checks appropriate for a Developer ID download or a Mac App Store build. <!-- MAC-001 -->
2. **Confirm which actions are approved.** Use credentials, submit, install, publish, delete files or change system settings only within the requested scope. <!-- MAC-005 -->
3. **Inspect the export and installed app.** Compare their identity, resources and signed entitlements. Check that required helpers are present. <!-- MAC-002 -->
4. **Trace trust failures to the component.** Verify nested signatures and update authenticity. Fix a rejected helper at its signing step, then export a new candidate. <!-- MAC-003 -->
5. **Match each result to its artifact.** Record what passed signing, notarization, ticket validation and Gatekeeper assessment. After repackaging, identify the final package by hash and rerun affected checks. <!-- MAC-004 -->

## Check the result

- For a notarized download, match acceptance to the submission and validate the attached ticket where applicable. Assess the quarantined download, then launch the installed copy and exercise its resources. <!-- MAC-002 MAC-004 -->
- An invalid update should leave the installed app and its data intact. For a Developer ID audit, verify the signer and confirm the log shows only approved actions. <!-- MAC-001 MAC-003 MAC-005 -->

## What to report

Identify the channel, version and package hash, then give each stage’s result or blocker.

- [Signing, entitlements and update failures](references/macos-productization-patterns.md)
- [Verifying the ZIP or installer customers receive](references/distribution-reproducibility.md)

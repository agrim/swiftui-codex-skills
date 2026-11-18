---
name: apple-privacy-system-integrations
description: "Audit permissions, purpose strings, privacy manifests, disclosures, retention, and deletion."
---

# Check what happens to personal data when access changes

Review a feature that requests permission, shares data with an SDK or promises account deletion. Trace one record to see whether the app keeps its privacy promise.

## Start here

For a workout shared with a widget, create a recognizable test record. Identify who writes it and which fields the widget needs.

## How to proceed

1. **Follow each copy.** Trace the record through the app, extensions, devices, cloud storage, SDKs, diagnostics and any summaries the feature creates. <!-- PRIV-001 -->
2. **Request access at the point of use.** Explain why the task needs the data. Ask for the narrowest useful access and keep unrelated tasks available. <!-- PRIV-002 -->
3. **Check what a failed read means.** Distinguish an outage, account switch or empty result from a known denial or revocation before offering recovery. <!-- PRIV-004 -->
4. **Compare disclosures with observed use.** Match transfers to user consent, published disclosures, and the entitlements, purpose strings and privacy manifests in the signed archive. <!-- PRIV-003 -->
5. **Define when each copy goes away.** Identify what protects it, who retains it, and which copies the app can remove after deletion. Include logs and user-controlled exports. <!-- PRIV-005 -->

## Check the result

- Limit access and complete an unrelated task. An empty HealthKit query makes no claim about read permission. An offline retry stays visibly pending. <!-- PRIV-002 PRIV-004 -->
- Trace one field that an SDK collects. Its observed use agrees with the shipped manifest and public disclosure. <!-- PRIV-003 -->
- Delete the test record, then switch accounts. Inspect caches, widgets, indexes, logs and exports against the promised deletion scope. <!-- PRIV-001 PRIV-005 -->

## What to report

Report what was collected, where it went and which copies survived deletion.

- [Diagnose permission and disclosure failures](references/privacy-system-patterns.md)
- [Follow a test record through deletion](references/integration-data-inventory.md)

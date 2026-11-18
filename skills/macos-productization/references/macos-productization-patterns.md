# Diagnosing a delivered Mac app

Start from the intended channel and the exact delivered artifact. Choose the inspection that can falsify the reported problem. An audit can inspect a supplied package without uploading, publishing or changing the machine’s trust settings.

| Symptom | Comparison that identifies the owner |
| --- | --- |
| Local copy runs, download fails | Compare the shipped hash and installed path. Assess the quarantined download, then inspect nested code named by the failure. Preserve the machine’s normal trust policy. |
| Notarization rejects a helper | Match the notary log to the submission ID and nested path. Repair that target’s signing/export step. Blanket re-signing can replace valid entitlements on other components. |
| Installed icon or resource is missing | Compare the same resource in the export, delivery container and installed copy. Repair the first stage that loses it. |
| Updater rejects a release | Match version, hash, URL and signed feed entry to the same candidate. Test an interrupted or invalid update and confirm the old app still launches with its data. |

Run an installer with privileges only within the approved scope. Inspect which paths change. An unrelated database or a machine-wide setting changing during an upgrade is a failed containment check.

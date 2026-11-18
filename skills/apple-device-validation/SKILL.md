---
name: apple-device-validation
description: "Use Xcode, Simulator and physical devices to verify rendering, upgrades, interaction and paired-device behavior on the intended build."
---

# Verify the experience on Simulator and device

Choose the proof the change needs. A screenshot can settle button truncation. A gesture, sensor reading, watch handoff or upgrade needs someone to perform the action on the relevant installation.

## Design choices

1. **Select the build and destination explicitly.** Check the Xcode scheme, configuration and runtime. Use an existing installation for an upgrade and a fresh starting state for first run. Preserve the app container when diagnosing migration or a release-only crash. <!-- SHIP-001 -->
2. **Exercise the layer that can show the defect.** Use Xcode or simctl to launch the app and capture the affected screen at the risky size and appearance. For physical input, use a device. For phone/watch changes, observe the sending action and the receiving state. <!-- SHIP-002 -->
3. **Find where the run first failed.** Check destination visibility, installation, process launch, then the app’s response. A stalled screenshot service calls for a known-good capture. An app exit calls for its crash report and the matching build’s dSYM. <!-- SHIP-003 -->

## Try it

Keep the build, destination, starting state and observed outcome together.

- For an upgrade, install over the previous version, edit an existing item, quit and reopen it. Verify the old data and new edit. <!-- SHIP-001 SHIP-002 -->
- For a rendering issue, capture the same state before and after the fix. For a device-only failure, repeat the action on that device and identify whether the app, installation or capture failed. <!-- SHIP-002 SHIP-003 -->

- [A blank list after a successful upgrade](references/an-upgrade.md)
- [Finding a broken step in an accessible journey](references/screen-review.md)
- [Capture a real screen or diagnose a device-only launch failure](references/xcode-device-run.md)

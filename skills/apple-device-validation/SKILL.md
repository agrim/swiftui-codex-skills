---
name: apple-device-validation
description: "Verify Apple app launch, rendering, interaction, hardware or paired-device behavior on a simulator or device."
---

# Verify what an Apple app actually does on a device

Use this to verify a change on a running app. A screenshot shows whether Save is visible. Activate it and reread the value after relaunch to prove the edit survived.

## Start here

Choose a behavior, expected result, build, destination and starting data. Identify actions that could affect the user’s account or files.

## How to proceed

1. **Choose an observation that answers the question.** Capture layout at the affected size. For an interaction, capture the starting state, perform the action and inspect the result. Use the receiving hardware for hardware or paired-device claims. <!-- PROOF-001 -->
2. **Protect existing data.** Use a disposable account or fixture where available. Reset, uninstall, change accounts or edit source only within the approved scope. <!-- PROOF-002 -->
3. **Identify the run.** Label logs and captures with build, destination, toolchain and test data. For batch reviews, identify each screen, state and capture revision. <!-- PROOF-003 -->
4. **Find the first blocked step.** Check pairing, provisioning, installation and launch in order as applicable. Preserve the actual error before changing the setup. <!-- PROOF-004 -->
5. **Retest the changed build.** Repeat affected checks and remove temporary fixtures. <!-- PROOF-005 -->

## Check the result

- Reopen a saved edit or inspect a delivered item on the receiving device. For layout, enable the affected accessibility setting and inspect the screen at that size. <!-- PROOF-001 -->
- If installation failed, retain the installer error and check that any reset was authorized. After a fix, confirm the new captures identify the replacement build and destination. <!-- PROOF-002 PROOF-003 PROOF-004 PROOF-005 -->

## What to report

For each behavior, report the verdict, build, destination, observation and blocked step.

- [Choosing a destination for a runtime check](references/device-validation-patterns.md)
- [Tracking reviewed screens and replacement captures](references/screen-review.md)
- [When debugger or simulator evidence is incomplete](references/debugger-and-simulator-evidence.md)

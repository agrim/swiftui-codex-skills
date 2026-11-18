---
name: apple-device-validation
description: "Verify Apple app launch, rendering, interaction, hardware or paired-device behavior on a simulator or device."
---

# Apple device validation

## Inputs

Identify the claim, candidate, fixture, available destinations and authorized actions.

## Rules

- **PROOF-001 — Match the evidence.** Use a frame for layout, an action and observed result for interaction, real hardware for hardware claims.
- **PROOF-002 — Bound side effects.** Preserve user data. Reset, uninstall, edit source or change accounts only as authorized.
- **PROOF-003 — Identify the run.** Tie artifacts and exit statuses to the build, destination, toolchain and fixture.
- **PROOF-004 — Isolate failure.** Locate the first failing prerequisite, from pairing or provisioning through launch.
- **PROOF-005 — Refresh affected proof.** Rerun checks after relevant changes and remove temporary fixtures.

## Workflow

1. Select a capable destination and run the prerequisites for this claim.
2. Exercise the transition. Record each screen and state for batch reviews.

## Verify

- PROOF-001: Inspect layout at the affected size and accessibility setting. For persistence, reread the value after relaunch. For paired delivery, observe it on the receiving device.
- PROOF-003, PROOF-005: Change the build, rerun affected checks and verify replacement receipts identify the new build and destination.
- PROOF-002, PROOF-004: On install failure, record the installer error and check reset history against authorization.

## Output

Give each claim a verdict, evidence and any blocked step.

## References

- [Destination and runtime](references/device-validation-patterns.md)
- [Screen inventory](references/screen-review.md)
- [Debugger and simulator evidence](references/debugger-and-simulator-evidence.md)

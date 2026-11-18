---
name: apple-device-validation
description: "Verify an Apple app on a simulator or device. Use for launch failures, screenshots, interaction, hardware, paired devices, and runtime evidence."
---

# Apple runtime and device validation

## Inputs

State the claim and authorization. Identify source, scheme, configuration, bundle, and fixture. Discover available devices and runtimes.

## Rules

- **PROOF-001 — Choose evidence for the claim.** Use build output for compilation, a current frame for rendering, and an observed action and result for interaction.
- **PROOF-002 — Limit side effects.** Keep uninstall, data resets, account changes, and source edits within their authorized scope.
- **PROOF-003 — Record the run.** Tie commands, exit status, artifacts, toolchain, runtime, and fixture to the exact candidate and destination.
- **PROOF-004 — Locate the failed step.** Check runtime, pairing, services, provisioning, installation, and launch before changing app code.
- **PROOF-005 — Refresh evidence after changes.** Rerun affected checks, supersede obsolete receipts, and remove temporary harness state.

## Workflow

1. Choose a destination that can demonstrate the claim. Build and run its prerequisites.
2. Exercise the transition and capture its result. For batch reviews, identify each screen, state, and capture revision.
3. Identify the first blocked step and unverified outcomes.

## Verify

- PROOF-001: For layout, inspect a frame at the affected size and accessibility setting. For persistence, read the changed value after relaunch.
- PROOF-001: For hardware or companion delivery, observe the expected result on the real device or pair.
- PROOF-003, PROOF-005: After a build change, check that evidence for each affected behavior identifies the new build and destination.

## Output

For each claim, report pass, fail, blocked, or not-run with candidate, environment, evidence, and known cause.

## References

- [Destination and runtime checks](references/device-validation-patterns.md)
- [Screen inventory and batch feedback](references/screen-review.md)
- [Debugger and simulator evidence](references/debugger-and-simulator-evidence.md)

---
name: apple-device-validation
description: "Verify a SwiftUI change on the installed build. Choose simulator captures, physical-device runs or paired-device checks to suit the defect."
---

# Verify the experience on Simulator and device

A screenshot can show that Save fits. To verify VoiceOver can activate it, perform the action on the installed build.

## Design choices

1. **Reproduce the starting state.** Select the scheme, configuration, OS and destination. Keep previous data for an upgrade and the failing container and archive for a Release-only crash. <!-- SHIP-001 -->
2. **Use the destination that can expose the failure.** Capture the layout at the affected size and appearance. Use hardware for sensors or physical input. For a watch handoff, observe both devices. <!-- SHIP-002 -->
3. **Find the first failed step.** Distinguish an invisible destination, failed install, app exit and stalled capture. For a crash, match the report’s image UUID to the archived binary and dSYM. <!-- SHIP-003 -->

## Try it

Tie each observation to its build and destination.

- For an upgrade, install over a saved favorite, edit it, quit and reopen. The old favorite and new edit must survive together. <!-- SHIP-001 SHIP-002 -->
- Repeat the visual check at the same size and appearance. If capture stalls, test the app’s responsiveness and try a known-good screen on that simulator. <!-- SHIP-002 SHIP-003 -->

- [A blank list after a successful upgrade](references/an-upgrade.md)
- [Finding a broken step in an accessible journey](references/screen-review.md)
- [Capture a real screen or diagnose a device-only launch failure](references/xcode-device-run.md)

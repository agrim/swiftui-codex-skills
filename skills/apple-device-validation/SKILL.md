---
name: apple-device-validation
description: "Evaluate an installed build against the user journey a release promises, including the transition most likely to break it."
---

# Decide if a changed experience is ready to ship

Name the promise that would make someone install this release. “My saved trips are still there after the update” calls for a different trial from “I can create a trip with VoiceOver.” Choose the build, starting state and environment that can answer that question.

## Design choices

1. **Use the starting state people will bring.** For an upgrade, prepare a previous supported build with meaningful data and preferences. For a first-run change, start fresh. Use the candidate and installation path relevant to the promise. <!-- SHIP-001 -->
2. **Follow the journey through its weakest transition.** Choose one consequential interruption, such as relaunch after saving or a focus move after dismissing a sheet. Exercise required hardware or services where the claimed behavior depends on them. <!-- SHIP-002 -->
3. **Decide which promise the candidate keeps.** Compare the end result with the promise. Tie any failure to the build and affected journey. Where a required condition is unavailable, identify the remaining trial before calling that promise verified. <!-- SHIP-003 -->

## Try it

Decide whether the release delivers the named promise on the tested destination.

- For an upgrade, open a previously saved item, edit it, quit and reopen. Record the installed builds and whether the old and new values appear where expected. <!-- SHIP-001 SHIP-002 -->
- If a feature depends on spoken focus or paired hardware, try that interaction in the relevant environment. Record the observed result or the specific claim still open. <!-- SHIP-002 SHIP-003 -->

- [A blank list after a successful upgrade](references/an-upgrade.md)
- [Finding the first broken step in an accessible journey](references/screen-review.md)

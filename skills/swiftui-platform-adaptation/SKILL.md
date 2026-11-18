---
name: swiftui-platform-adaptation
description: "Adapt SwiftUI scenes, windows, focus, and input for iOS, iPadOS, macOS, watchOS, tvOS, or visionOS."
---

# Make an app task work across Apple devices and windows

Use this when a feature works on one platform but its controls, focus or window behavior break elsewhere. Keep the outcome consistent wherever the task is shared.

## Start here

Pick one task. For example, a Mac shortcut and an iPad Save button should rename the same selected document.

## How to proceed

1. **Identify the shared operation.** Follow each control to the command that changes the record. Share that command when equivalent input should produce equivalent results. <!-- PLAT-001 -->
2. **Choose which window receives the action.** If reopening a document should recover its draft, open by document ID. Keep unrelated windows’ selections and histories independent. <!-- PLAT-002 -->
3. **Find the first unreachable action.** Try the target’s actual input. Follow focus after a dialog closes, especially if its starting row has disappeared. <!-- PLAT-003 -->
4. **Define the fallback before sharing the interface.** When a capability is unavailable, decide which part of the task can still finish and how to reach it. <!-- PLAT-004 -->
5. **Exercise the task on each target.** Build for the target, run the task, interrupt and resume it. Record which window receives the result. <!-- PLAT-005 -->

## Check the result

- Run the shared command on two targets with identical input. Compare stored results and exercise the fallback where the capability is absent. <!-- PLAT-001 PLAT-004 -->
- Select different documents in two windows. Resize one and edit by keyboard. Only its draft changes. <!-- PLAT-002 -->
- On affected targets, read and activate the watch control, regain remote focus after tvOS dismissal, or complete and exit a visionOS task. Assess spatial comfort on hardware. <!-- PLAT-003 PLAT-005 -->

## What to report

Report the destination, input, observed result and any remaining hardware checks.

- [Find the first task that fails on one platform](references/platform-patterns.md)
- [Diagnose duplicate editors and shortcuts targeting the wrong window](references/scenes-and-focus.md)

# Behavior tests, previews, and evidence: playbook

## Evidence ladder

| Claim | Minimum relevant evidence |
| --- | --- |
| Parser or reducer behavior | Executed deterministic unit test |
| SwiftUI API compiles | Build for the affected Apple target/minimum |
| State survives a save/relaunch | Disk-backed integration test or installed runtime journey |
| Button performs the action | UI interaction or equivalent behavioral integration |
| Layout does not truncate | Rendered inspection at risky sizes and states |
| VoiceOver journey works | Assistive-technology interaction plus audits where supported |
| Sensor or paired-device behavior | Relevant physical-device evidence |

## Async completions arrive out of order

Start requests A and B, wait for registration, complete B and then A. Check the final displayed record. Repeat with a late error or cancellation and check the pending indicator. For debounce, advance an injected clock across its boundary. A timeout can bound a stalled run. Only the registration or completion signal establishes the order.

During teardown, wait for the task or stream to finish and remove temporary data even if an assertion failed. Reopen a disk-backed store when the claim involves persistence across launch.

## Previews, snapshots and UI automation

- **Choose the state that exposes the defect.** A denied sensor permission, stale result, unusually long translation or narrow window can each need a different fixture. Keep preview dependencies local so staging these states cannot start a sensor or mutate real data.
- **Review a changed baseline.** Match appearance, locale, text size, content, runtime and rendering size. Inspect enough of the diff to distinguish a changed control from a changed renderer before accepting it.
- **Exercise the control.** Select it using a stable identifier and leave its human-facing label intact. Wait for the visible outcome. For VoiceOver and keyboard claims, complete the affected journey using that input. An audit can locate specific issues along the way.
- **Check the proof at handoff.** Distinguish a simulated error, an executed persistence operation and a completed device journey. Report the revision, platform and any blocked checks with the result.

## Regression probes from visual review

For a bottom-field editor, enter text, reveal the actual keyboard, reach the commit action, and recover from invalid input at a risky size. For repeated surfaces, compare the same entity and state across both contexts, including the shared component's affected appearances.

If the UI journey passes but the unit runner stalls, report both outcomes. Classify the bounded stall before retrying.

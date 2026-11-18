---
name: swiftui-state-architecture
description: "Fix SwiftUI state ownership, Observation, bindings, environment injection, row identity and scene lifetime."
---

# Keep SwiftUI edits attached to the right record

Use this when a draft disappears on refresh or a save updates the wrong row. Trace who owns the value, how long it should survive and which record it belongs to.

## Start here

Pick one edit. What should survive a redraw, dismissal, document switch or relaunch? Check the supported OS versions.

## How to proceed

1. **Choose who owns each value.** Keep drafts with their editor and selection with its window. Pass read-only values to display views. Use an enum when flags allow impossible combinations. <!-- STATE-001 -->
2. **Match the property wrapper to that owner.** A view may create its own model or follow one supplied by its parent. Choose a wrapper supporting that lifetime on each target. <!-- STATE-002 -->
3. **Keep setup out of rendering.** Tie service starts and writes to their owner so rebuilding a view cannot repeat them. <!-- STATE-004 -->
4. **Keep the draft separate from storage.** Commit on Save. Decide which actor may change shared state independently of how views observe it. <!-- STATE-005 -->
5. **Follow the record through a delayed save.** Capture its ID and edit. After the wait, look it up again. Apply the reply only if the edit is current. <!-- STATE-003 -->

## Check the result

- Change selection in one window. The other keeps its selection. Refresh the parent while typing. The draft survives without repeated setup. Replace a parent-supplied model and verify the child follows. <!-- STATE-001 STATE-002 STATE-004 -->
- Reorder, delete or re-edit during save. A late reply cannot revive a deleted row or clear a newer edit. Cancel leaves storage untouched. Save survives reopening. <!-- STATE-003 STATE-005 -->

## What to report

Identify the owner and property wrapper, supported OS versions and the transitions you verified.

- [Handle parent refreshes and document switches](references/state-patterns.md)
- [Prevent late saves from changing another row](references/observation-and-bindings.md)

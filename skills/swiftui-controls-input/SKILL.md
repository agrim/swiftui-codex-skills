---
name: swiftui-controls-input
description: "Build SwiftUI controls and forms. Resolve focus, keyboard submission, text composition, gestures, drag and drop, or duplicate commits."
---

# Make a SwiftUI form edit and save the intended value

Use this when a picker loses its selection, validation sends typing to the wrong field, or pressing Return and tapping Save creates two records.

## Start here

For a quantity field, identify the row being edited, what partial input must survive and which event saves it.

## How to proceed

1. **Match the control to its effect.** Decide whether activation selects, navigates or runs a command. Choosing a filter should leave the user on the same screen. <!-- CTRL-001 -->
2. **Isolate a styling failure.** Remove the custom style. Compare the localized label, role, focus and activation while enabled and disabled. <!-- CTRL-002 -->
3. **Trace a lost selection.** Compare picker tags with the selected value’s type and ID. Set a fallback if refresh deletes the selected item. <!-- CTRL-003 -->
4. **Focus the field that failed validation.** Give each editable row a distinct focus target. Preserve the cursor and partial input until the user finishes composing. <!-- CTRL-004 -->
5. **Send Return and Save through one command.** Prevent overlapping writes and retain drafts on failure. Offer another way to invoke a gesture-only command. <!-- CTRL-005 -->

## Check the result

- In a form with explicit Save, pick an option and refresh. The selection stays visible and storage changes only on Save. <!-- CTRL-001 CTRL-003 -->
- Submit invalid text in row two. Correct it with an input method editor without tapping. Tap Save while the Return-key submission is pending. Expect one write to row two. <!-- CTRL-004 CTRL-005 -->
- Find the localized label with VoiceOver. Invoke the control by keyboard and repeat while disabled. Only the enabled action runs. <!-- CTRL-002 -->

## What to report

Report which control and input failed, what committed the edit and which record changed.

- [Diagnose the wrong effect, a missing label or a competing gesture](references/control-patterns.md)
- [Fix validation focus and duplicate saves](references/focus-and-form-contracts.md)

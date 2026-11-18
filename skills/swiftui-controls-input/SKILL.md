---
name: swiftui-controls-input
description: "Build SwiftUI controls and forms. Resolve focus, keyboard submission, text composition, gestures, drag and drop, or duplicate commits."
---

# Controls, forms, and input

## Inputs

Record the interaction, devices, validation rules, and commit or cancel point.

## Rules

- **CTRL-001 — Match control to intent.** Prefer `Button` for commands, `NavigationLink` for navigation, and native pickers, toggles, sliders, or menus for choices and adjustments.
- **CTRL-002 — Preserve native behavior.** Start with system styles. Custom styles must retain role, enabled and pressed states, focus, keyboard support, and assistive activation.
- **CTRL-003 — Bind selection once.** Give each picker option a unique, type-matched tag. Keep selection separate from explicit Save.
- **CTRL-004 — Preserve active input.** Map focus and Submit to the intended command. Preserve the draft and text composition during validation.
- **CTRL-005 — Guard commits.** Prevent duplicate writes, retain failed drafts for retry, and offer alternatives to gesture-only commands.

## Workflow

1. Trace activation through the binding or command to its effect. Name icon-only controls.
2. Set focus order, AutoFill, dismissal, and destructive confirmation. Expose busy, invalid, and unavailable states.

## Verify

- CTRL-003: Change the picker value. Confirm one option is selected and persistence occurs at the commit point.
- CTRL-004, CTRL-005: Enter text with an input method editor. After validation fails, correct the retained draft. Press Save twice before the first save finishes. Confirm one write.
- CTRL-002: Using keyboard or VoiceOver where supported, identify the control by its full localized label, activate it when enabled, and check that disabling it blocks the command.

## Output

Report control, commit behavior, input tested, and result.

## References

- [Control selection, styles, and gestures](references/control-patterns.md)
- [Focus, validation, and editable forms](references/focus-and-form-contracts.md)

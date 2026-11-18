---
name: swiftui-controls-input
description: "Build SwiftUI controls and forms. Resolve focus, keyboard submission, text composition, gestures, drag and drop, or duplicate commits."
---

# Controls, forms, and input

## Inputs

Interaction, devices, validation, commit and cancel events.

## Rules

- **CTRL-001 — Intent.** Prefer Button for commands, NavigationLink for destinations and native controls for choices.
- **CTRL-002 — Styling.** Preserve native role, focus, pressed/disabled states, keyboard and assistive activation.
- **CTRL-003 — Selection.** Use unique, type-matched tags. Keep explicit Save separate.
- **CTRL-004 — Input.** Route focus and Submit. Preserve text composition during validation.
- **CTRL-005 — Commits.** Deduplicate writes, retain failed drafts and offer gesture alternatives.

## Workflow

1. Trace activation to the command. Label icon controls.
2. Set focus order, AutoFill, dismissal and destructive confirmation. Show busy, invalid and unavailable states.

## Verify

- CTRL-001, CTRL-003: Choose a picker option. The selection changes in place. Only the commit event updates storage.
- CTRL-004, CTRL-005: Compose with an input method editor, fail validation, then correct the retained draft. Two overlapping saves commit once.
- CTRL-002: Find the full localized label using VoiceOver or keyboard. Activation works only while enabled.

## Output

Control, commit event, input tested, observed result.

## References

- [Control choice and gestures](references/control-patterns.md)
- [Ambiguous focus and commits](references/focus-and-form-contracts.md)

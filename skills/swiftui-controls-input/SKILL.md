---
name: swiftui-controls-input
description: "Build SwiftUI controls and forms. Resolve focus, keyboard submission, text composition, gestures, drag and drop, or duplicate commits."
---

# Controls, forms, and input

## Inputs

Interaction, devices, validation, commit and cancel events.

## Rules

- **CTRL-001 — Intent.** Match the control to the intended effect on selection, history or command execution.
- **CTRL-002 — Styling.** Remove the custom style to isolate losses in role, focus or activation.
- **CTRL-003 — Selection.** When selection disappears, check tag identity and type before changing persistence.
- **CTRL-004 — Input.** Route validation to the invalid field without replacing its draft during composition.
- **CTRL-005 — Commits.** Deduplicate writes, retain failed drafts and offer gesture alternatives.

## Workflow

1. Trace touch, keyboard and assistive activation to the same command.
2. Find the first durable write. Exercise cancellation and retry around it.

## Verify

- CTRL-001, CTRL-003: Choose a picker option. The selection changes in place. Only the commit event updates storage.
- CTRL-004, CTRL-005: Compose with an input method editor, fail validation, then correct the retained draft. Two overlapping saves commit once.
- CTRL-002: Find the full localized label using VoiceOver or keyboard. Activation works only while enabled.

## Output

Control, commit event, input tested, observed result.

## References

- [Control choice and gestures](references/control-patterns.md)
- [Ambiguous focus and commits](references/focus-and-form-contracts.md)

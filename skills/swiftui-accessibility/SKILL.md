---
name: swiftui-accessibility
description: "Audit SwiftUI tasks with VoiceOver, Voice Control, keyboards, Dynamic Type, Reduce Motion, contrast, and localized layouts."
---

# Accessibility and localization

## Inputs

Record the task, destination, locale, input method, text size, and assistive settings.

## Rules

- **AX-001 — Expose actions and values.** Expose each control’s name, role, action and value. Make essential read-only values and units accessible too.
- **AX-002 — Adapt to settings.** Keep essential actions reachable as text, direction, contrast, motion, and input method change.
- **AX-003 — Provide alternatives.** Pair color, position, sound, or motion cues with accessible status. Offer an alternative to required gestures.
- **AX-004 — Group by action.** Combine related static text. Keep independent controls individually reachable in task order.
- **AX-005 — Exercise the journey.** Read, edit, submit, recover from an error, and dismiss using the relevant assistive technology.

## Workflow

1. Inspect the accessibility tree at the failing step. Correct semantics before adding hints.
2. Localize names, plurals, and formatted values. Check longer translations and mixed-direction text.
3. Repeat at the largest supported text size.

## Verify

- AX-004, AX-005: Use VoiceOver or Full Keyboard Access where supported. Reach each independent control in task order and correct an invalid entry.
- AX-001, AX-002: With Voice Control, speak the localized action’s visible title after reflow. Confirm the intended record changed.
- AX-002, AX-003: With Reduce Motion, Reduce Transparency, or increased contrast, confirm completion and error feedback remain distinguishable.

## Output

Rank barriers by impact. Report control, failing step, fix, tested settings, and outstanding hands-on checks.

## References

- [Labels, grouping, text, and contrast](references/accessibility-patterns.md)
- [Spoken commands, localization, and focus](references/assistive-and-localized-flows.md)

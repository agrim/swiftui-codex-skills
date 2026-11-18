---
name: swiftui-accessibility
description: "Audit SwiftUI tasks with VoiceOver, Voice Control, keyboards, Dynamic Type, Reduce Motion, contrast, and localized layouts."
---

# Accessibility and localization

## Inputs

Task, destination, locale, input, text size and assistive settings.

## Rules

- **AX-001 — Semantics.** Expose names, roles, actions, values and essential readouts with units.
- **AX-002 — Reach.** Keep actions reachable as text, direction, contrast, motion and input change.
- **AX-003 — Alternatives.** Supplement sensory cues with accessible status. Offer alternatives to required gestures.
- **AX-004 — Grouping.** Group static text. Preserve independent actions in task order.
- **AX-005 — Journey.** Read, edit, submit, recover and dismiss with assistive technology.

## Workflow

1. Inspect failing semantics before adding hints.
2. Localize names, plurals and values. Test long, mixed-direction text at maximum size.

## Verify

- AX-004, AX-005: Reach each action in order and correct invalid input with VoiceOver or Full Keyboard Access.
- AX-001, AX-002: After reflow, speak the visible localized title with Voice Control. Only the intended record changes.
- AX-002, AX-003: Distinguish success from error under Reduce Motion, Reduce Transparency or increased contrast.

## Output

Rank barriers by impact. Identify fixes, tested settings and outstanding checks.

## References

- [Labels, grouping and contrast](references/accessibility-patterns.md)
- [Custom dials and spoken commands](references/assistive-and-localized-flows.md)

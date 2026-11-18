---
name: swiftui-accessibility
description: "Audit SwiftUI tasks with VoiceOver, Voice Control, keyboards, Dynamic Type, Reduce Motion, contrast, and localized layouts."
---

# Accessibility and localization

## Inputs

Task, destination, locale, input, text size and assistive settings.

## Rules

- **AX-001 — Semantics.** At the blocked step, compare the announced role, value and unit with the intended action.
- **AX-002 — Reach.** After reflow, follow the same action to the same record.
- **AX-003 — Alternatives.** Remove the strongest cue or gesture. Verify the user can still detect status and act.
- **AX-004 — Grouping.** Group a row only if each independent command remains reachable in order.
- **AX-005 — Journey.** Exercise recovery from a failed submission using assistive input.

## Workflow

1. Inspect the failing element before changing its parent.
2. Repeat with long, mixed-direction text at maximum supported size.

## Verify

- AX-004, AX-005: Reach each action in order and correct invalid input with VoiceOver or Full Keyboard Access.
- AX-001, AX-002: After reflow, speak the visible localized title with Voice Control. Only the intended record changes.
- AX-002, AX-003: Distinguish success from error under Reduce Motion, Reduce Transparency or increased contrast.

## Output

Rank barriers by impact. Identify fixes, tested settings and outstanding checks.

## References

- [Labels, grouping and contrast](references/accessibility-patterns.md)
- [Custom dials and spoken commands](references/assistive-and-localized-flows.md)

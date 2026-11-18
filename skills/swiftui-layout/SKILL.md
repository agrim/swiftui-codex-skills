---
name: swiftui-layout
description: "Fix SwiftUI clipping, safe areas, scrolling, or reflow across window sizes, Dynamic Type, and right-to-left layouts."
---

# Adaptive layout and scrolling

## Inputs

Container proposal, insets, keyboard, content, text size and direction.

## Rules

- **LAY-001 — Container sizing.** Trace width-dependent clipping to the first restrictive parent.
- **LAY-002 — Essential text.** Reflow clipped labels without losing the action or draft. Justify fixed sizes.
- **LAY-003 — Geometry.** During resizing, publish changes to the value the view consumes.
- **LAY-004 — Interaction.** Keep pinned controls and underlying content reachable. Use stable row and scroll IDs.
- **LAY-005 — Primitives.** Reserve custom measurement for placement existing layouts cannot express.

## Workflow

1. Vary width and text size independently. Remove the suspect constraint and compare.
2. Choose eager or lazy rows by measured scale and required actions.

## Verify

- LAY-002, LAY-005: Try a stack first. Reflow twice mid-edit. Check focus and saved text. Name any constraint still requiring custom layout.
- LAY-001, LAY-004: At width extremes, reach the primary action with large text, long translations, RTL and keyboard visible.
- LAY-003: Resize within one width class, then cross its boundary. Expect one derived-state change.
- LAY-004: Load many rows from empty, insert before the anchor, then restore the same record.

## Output

Failing size, fix, fixed-size rationale and observed result.

## References

- [Clipping, geometry updates and custom measurement](references/layout-patterns.md)
- [Reflow, obscured rows, and scroll restoration](references/layout-and-scroll-edge-cases.md)

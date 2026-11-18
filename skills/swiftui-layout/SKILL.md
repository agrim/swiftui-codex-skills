---
name: swiftui-layout
description: "Fix SwiftUI clipping, safe areas, scrolling, or reflow across window sizes, Dynamic Type, and right-to-left layouts."
---

# Adaptive layout and scrolling

## Inputs

Container proposal, insets, keyboard, content, text size and direction.

## Rules

- **LAY-001 — Container sizing.** Size views from the container’s proposal.
- **LAY-002 — Essential text.** Reflow before truncating or shrinking. Justify fixed sizes.
- **LAY-003 — Geometry.** Publish derived values only when they change.
- **LAY-004 — Interaction.** Keep pinned controls and underlying content reachable. Use stable row and scroll IDs.
- **LAY-005 — Primitives.** Try stacks, grids, alignment, priority or fitting alternatives before custom measurement.

## Workflow

1. Locate the first frame, inset, overlay or scroll container that breaks the proposal.
2. Preserve draft ownership through reflow. Choose lazy or eager rows by behavior and measured scale.

## Verify

- LAY-002, LAY-005: Try a stack first. Reflow twice mid-edit. Check focus and saved text. Name any constraint still requiring custom layout.
- LAY-001, LAY-004: At width extremes, reach the primary action with large text, long translations, RTL and keyboard visible.
- LAY-003: Resize within one width class, then cross its boundary. Expect one derived-state change.
- LAY-004: Load many rows from empty, insert before the anchor, then restore the same record.

## Output

Failing size, fix, fixed-size rationale and observed result.

## References

- [Proposals, text, and safe areas](references/layout-patterns.md)
- [Reflow, obscured rows, and scroll restoration](references/layout-and-scroll-edge-cases.md)

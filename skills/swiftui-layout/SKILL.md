---
name: swiftui-layout
description: "Fix SwiftUI clipping, safe areas, scrolling, or reflow across window sizes, Dynamic Type, and right-to-left layouts."
---

# Adaptive layout and scrolling

## Inputs

Record container size, safe areas, keyboard state, text size, content, and layout direction.

## Rules

- **LAY-001 — Use the container proposal.** Size resizable views from available space and content. Global screen bounds can exceed the window.
- **LAY-002 — Reflow before shrinking.** Wrap or rearrange content before truncating essential text or limiting Dynamic Type. Justify fixed dimensions.
- **LAY-003 — Limit geometry updates.** Derive the needed value, such as a width class. Update state only when it changes.
- **LAY-004 — Protect interaction and identity.** An edge-to-edge background may extend under system UI. Keep controls reachable and give rows and scroll targets stable IDs.
- **LAY-005 — Choose a layout primitive.** Try stacks, grids, alignment, priority, or fitting alternatives before adding a geometry reader or custom Layout.

## Workflow

1. Locate the first frame, inset, overlay, or nested scroll view that breaks the failing proposal.
2. Choose eager or lazy containers from row semantics and measured scale. Keep draft ownership stable during reflow. Profile geometry updates if scrolling hitches.

## Verify

- LAY-002: Cross the reflow breakpoint both ways while editing. Check focus returns to the intended field and Save commits the entered text.
- LAY-001, LAY-004: At supported width extremes, check that large text, long translations, right-to-left layout, and the keyboard leave the primary action reachable.
- LAY-004: Test an empty collection, then a large one. Insert a row before the scroll anchor and confirm restoration still targets the same record ID.

## Output

Report failing size, layout change, fixed-size rationale, and rendered or measured results.

## References

- [Layout proposals, text, and safe areas](references/layout-patterns.md)
- [Fitting alternatives, stateful reflow, and scroll restoration](references/layout-and-scroll-edge-cases.md)

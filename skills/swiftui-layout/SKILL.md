---
name: swiftui-layout
description: "Fix SwiftUI clipping, safe areas, scrolling, or reflow across window sizes, Dynamic Type, and right-to-left layouts."
---

# Keep a SwiftUI screen usable as its size changes

Use this when resizing a window or enlarging text hides a control, loses a draft or jumps to the wrong row.

## Start here

Reproduce the first failure. If Save disappears, vary width, text size, language and keyboard visibility to find which change hides it.

## How to proceed

1. **Find the first restrictive frame.** Vary width and text size independently. Walk up from the clipped child, removing one fixed frame or inset at a time. <!-- LAY-001 -->
2. **Preserve the edit during reflow.** Let essential labels wrap or move actions below the field. Bind either arrangement to the same draft. <!-- LAY-002 -->
3. **Track meaningful size changes.** If toolbar controls move at one width threshold, update their state only when the window crosses it. <!-- LAY-003 -->
4. **Keep the last row reachable.** Reserve room for a wrapping bottom bar. Anchor scrolling to a stable record ID when inserting rows above it. <!-- LAY-004 -->
5. **Test a stack or grid first.** Keep custom measurement only for a placement the simpler layout cannot express. Compare eager and lazy rows at realistic volumes. <!-- LAY-005 -->

## Check the result

- Try the simpler layout. Type a draft, cross the width boundary twice and save. Focus and text survive. The toolbar state changes once per crossing. <!-- LAY-002 LAY-003 LAY-005 -->
- Reach Save at both width extremes with large text, a long right-to-left translation and the keyboard open. <!-- LAY-001 LAY-004 -->
- Populate an empty list, scroll to a record, insert rows above it and restore the same record. <!-- LAY-004 -->

## What to report

Report the failing condition, the constraint you changed, and what happened to the draft or scroll position.

- [Find the source of clipping or excessive layout updates](references/layout-patterns.md)
- [Preserve form edits and scroll position](references/layout-and-scroll-edge-cases.md)

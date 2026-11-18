---
name: swiftui-design-system
description: "Design consistent SwiftUI components with typography, color, SF Symbols, Liquid Glass, charts, and motion."
---

# Visual language, materials, and motion

## Inputs

Action hierarchy, appearances, accessibility settings, minimum OS.

## Rules

- **DES-001 — Hierarchy.** Resolve competing actions by frequency and cost of error.
- **DES-002 — Native controls.** Compare with the system control. Identify what the customization adds.
- **DES-003 — Materials.** Compare the same scrolling backdrop with and without custom glass.
- **DES-004 — Motion.** Drive completion from committed state so interrupted motion cannot strand an action.
- **DES-005 — States.** Isolate state and backdrop before changing a shared palette.

## Workflow

1. Share appearance across related surfaces. Preserve their commands and data ownership.
2. Render one record across styles and deployment targets.

## Verify

- DES-001, DES-003, DES-005: At large text sizes, identify the primary action. Check long labels on light and dark materials with increased contrast and reduced transparency. Focus, press and disable the control. Labels stay legible and disabled activation has no effect.
- DES-004: Interrupt motion, then repeat under Reduce Motion. Final state and action agree.
- DES-002: Build and render the older-target fallback. Verify the primary control’s role and activate its command.

## Output

Component, rationale, fallback, rendered states and untested cases.

## References

- [Hierarchy and shared components](references/design-patterns.md)
- [Glass, chart descriptions and motion](references/glass-charts-and-motion.md)

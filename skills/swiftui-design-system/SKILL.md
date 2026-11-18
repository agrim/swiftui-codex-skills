---
name: swiftui-design-system
description: "Design consistent SwiftUI components with typography, color, SF Symbols, Liquid Glass, charts, and motion."
---

# Visual language, materials, and motion

## Inputs

Action hierarchy, appearances, accessibility settings, minimum OS.

## Rules

- **DES-001 — Hierarchy.** Distinguish the primary action through type, spacing and placement.
- **DES-002 — Native controls.** Use system controls and chrome unless customization preserves native behavior and serves a product need.
- **DES-003 — Materials.** Favor Liquid Glass for navigation and controls. Keep content legible underneath.
- **DES-004 — Motion.** Scope transitions, preserve identity and convey completion under Reduce Motion.
- **DES-005 — States.** Check label, symbol, fill, foreground and hit area when disabled, focused or pressed.

## Workflow

1. Share appearance across related surfaces. Preserve their commands and data ownership.
2. Use semantic styles. Check API and symbol availability.

## Verify

- DES-001, DES-003, DES-005: At large text sizes, identify the primary action. Check long labels on light and dark materials with increased contrast and reduced transparency. Focus, press and disable the control. Labels stay legible and disabled activation has no effect.
- DES-004: Interrupt motion, then repeat under Reduce Motion. Final state and action agree.
- DES-002: Build and render the older-target fallback. Verify the primary control’s role and activate its command.

## Output

Component, rationale, fallback, rendered states and untested cases.

## References

- [Hierarchy and shared components](references/design-patterns.md)
- [Glass, chart descriptions and motion](references/glass-charts-and-motion.md)

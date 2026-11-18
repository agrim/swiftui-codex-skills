---
name: swiftui-design-system
description: "Design consistent SwiftUI components with typography, color, SF Symbols, Liquid Glass, charts, and motion."
---

# Visual language, materials, and motion

## Inputs

Record primary and secondary actions, appearances, accessibility settings, and deployment minimum.

## Rules

- **DES-001 — Establish hierarchy.** Use type, spacing, placement, and prominence to distinguish the primary action.
- **DES-002 — Prefer system controls and chrome.** Give each customization a product purpose and retain native interaction and accessibility.
- **DES-003 — Assign materials by role.** Prefer Liquid Glass for navigation or controls. Keep scrolling content readable behind them.
- **DES-004 — Scope motion.** Animate the intended transition, preserve identity, and communicate completion with Reduce Motion enabled.
- **DES-005 — Review the whole control.** Inspect label, symbol, fill, foreground, hit area, and disabled, focused, and pressed states together.

## Workflow

1. Compare surfaces showing the same entity. Share presentation while preserving each surface’s commands and data owner.
2. Choose semantic fonts, colors, and symbols. Check new APIs and symbols against the deployment target.

## Verify

- DES-003, DES-005: Render long labels and large text in light and dark appearances. Check legibility against the actual material background with increased contrast and reduced transparency.
- DES-004: Interrupt a transition, then repeat with Reduce Motion. Confirm the control shows the final state and offers the corresponding action.
- DES-002: For a newer visual API, build and render its older-target fallback. The same control must still perform the primary action.

## Output

Report component, rationale, fallback, rendered states, and outstanding checks.

## References

- [Hierarchy, color, typography, and shared components](references/design-patterns.md)
- [Glass, charts, and motion](references/glass-charts-and-motion.md)

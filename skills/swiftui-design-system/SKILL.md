---
name: swiftui-design-system
description: "Design consistent SwiftUI components with typography, color, SF Symbols, Liquid Glass, charts, and motion."
---

# Keep SwiftUI controls readable across themes and states

Use this when a toolbar disappears over photos, the same item looks different across screens or an animation signals Done before Save finishes.

## Start here

Render the same component and record on the affected screens. Identify the intended action and the appearance, state or OS version where it becomes unclear.

## How to proceed

1. **Choose which action should stand out.** Consider the likely next action and the cost of a wrong tap. Reuse type, spacing and information order where they convey the same meaning. <!-- DES-001 -->
2. **Compare the customization with the system control.** Identify what the customization adds. Preserve the command, accessible role and a usable fallback on the oldest supported target. <!-- DES-002 -->
3. **Test glass over scrolling content.** Scroll the same bright and dark image edges under the toolbar with and without custom glass. <!-- DES-003 -->
4. **Tie completion to the operation.** Show Done when the save commits. Interrupting motion must leave the right status and available action. <!-- DES-004 -->
5. **Find the state that loses contrast.** Compare focused, pressed and disabled controls on the failing backdrop before changing a shared color. <!-- DES-005 -->

## Check the result

- Identify the primary action at large text sizes. Read its long label in light and dark appearances with increased contrast and reduced transparency. Focus, press and disable the control. Disabled activation has no effect. <!-- DES-001 DES-003 DES-005 -->
- Interrupt a transition and repeat under Reduce Motion. Compare the final state with the saved value. <!-- DES-004 -->
- On the oldest target, verify the fallback’s role and activate its command. <!-- DES-002 -->

## What to report

Report the design choice, the appearances and fallback tested, and the observed behavior.

- [Compare hierarchy, shared components and fallback icons](references/design-patterns.md)
- [Diagnose disappearing toolbars, premature completion and stale chart descriptions](references/glass-charts-and-motion.md)

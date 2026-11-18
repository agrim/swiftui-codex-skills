---
name: apple-swiftui-native-apps
description: "Scope a SwiftUI feature or review, check native control semantics and SDK availability, and select a specialist skill."
---

# SwiftUI engineering entry point

## Inputs

Check the requested outcome, repository instructions, targets, minimum OS and Swift language mode.

## Rules

- **UI-001 — Preserve control semantics.** Choose a native control for each action, choice or link. Preserve its platform interactions and accessibility when styling it.
- **UI-002 — Check API availability.** Match the SDK declaration and Apple guidance to each target’s runtime and compiler.
- **UI-003 — Locate the owner.** Before splitting views, locate the owners of state, storage, navigation and side effects.
- **UI-004 — Honor the requested scope.** Preserve user edits. For a review, report findings. Edit, release, delete, or change accounts only within the requested scope.
- **UI-005 — Qualify findings.** Distinguish platform requirements from local conventions and design advice. Identify hypotheses and the evidence needed to resolve them.

## Workflow

1. Trace one user action from its control to the owner and any external effect.
2. Select the specialist for the failing step. Define success and the applicable failure or recovery path.
3. Apply or recommend the smallest correction. Check any diff against the requested scope.

## Verify

- UI-002: For an API change, build each affected target with its supported deployment minimum.
- UI-001: Activate a changed control using its supported input methods. Check the intended action and accessible role.
- UI-005: For a layout claim, inspect the risky size and locale. For hardware claims, reproduce on the relevant device.

## Output

Name the file and symbol, result, checks run and remaining gaps. For a review finding, include severity, reproduction, impact, correction and regression check.

## References

- [Route symptoms to specialist skills and corrections](references/correction-patterns.md)
- [Review findings and SDK modernization decisions](references/review-and-modernization.md)

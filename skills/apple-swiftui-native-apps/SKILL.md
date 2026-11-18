---
name: apple-swiftui-native-apps
description: "Scope a SwiftUI feature or review, check native controls and API availability, and select a specialist."
---

# Scope a SwiftUI change

## Inputs

Check scope, repo instructions, targets, OS minimums and Swift mode.

## Rules

- **UI-001 — Controls.** Before replacing a native control, identify the missing interaction. Styling must preserve input and accessible role.
- **UI-002 — Availability.** Accept a replacement only when affected targets support it or retain a working fallback.
- **UI-003 — Ownership.** Locate state, storage, navigation and effect owners before splitting views.
- **UI-004 — Scope.** Preserve user edits. Reviews return findings. Edit, delete, release or change accounts only as requested.
- **UI-005 — Evidence.** Classify requirements, conventions, advice and hypotheses. Name the missing proof.

## Workflow

1. Trace an action through its owner to its effect.
2. Route the failure to its specialist. Define success and recovery.
3. Recommend or apply the smallest authorized correction.

## Verify

- UI-002: Build each affected target and exercise the fallback on its oldest supported runtime.
- UI-001: Activate changed controls with supported inputs. Check action and accessible role.
- UI-003, UI-004: Name the owner behind each finding. A review leaves the reviewed code and user edits intact.
- UI-005: Check risky sizes and locales for layout, relevant devices for hardware.

## Output

Give file, symbol, result, checks and gaps. For findings add severity, reproduction, impact, correction and regression check.

## References

- [Route by symptom](references/correction-patterns.md)
- [Review and modernization](references/review-and-modernization.md)

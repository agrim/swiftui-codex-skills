---
name: apple-swiftui-native-apps
description: "Scope a SwiftUI feature or review, check native controls and API availability, and select a specialist."
---

# Find where to fix a SwiftUI feature

Use this to locate the code responsible for a SwiftUI feature before reviewing or changing it. A Save button that nobody can activate needs a different fix from one that loses edits on relaunch.

## Start here

Choose one action on an affected device. Describe the expected and actual outcome. Check project instructions, minimum OS and Swift mode.

## How to proceed

1. **Locate the first wrong result.** Follow the control through its draft, navigation or storage write. Choose the specialist for the first failing step. <!-- UI-003 -->
2. **Find what the native control cannot do.** Try the supported inputs before replacing it. If styling is enough, keep its activation behavior and accessible role. <!-- UI-001 -->
3. **Check which targets can run the fix.** Keep a working fallback on targets that lack the proposed API. <!-- UI-002 -->
4. **Stay within the request.** For reviews, give findings. For fixes, preserve existing edits and apply the smallest authorized change. Keep deletion, release and account changes within scope. <!-- UI-004 -->
5. **Choose evidence for the claim.** Distinguish a product requirement from a project convention, a recommendation or a suspected cause. Say what observation could settle it. <!-- UI-005 -->

## Check the result

- Check the control’s role and effect with each supported input. Build each affected target and exercise its oldest supported path. <!-- UI-001 UI-002 -->
- A review identifies the responsible symbol and leaves code intact. Verify layout at the failing size and locale, hardware claims on the relevant device. <!-- UI-003 UI-004 UI-005 -->

## What to report

Give the reproduction, impact, responsible code, proposed or completed change, and checks that passed or remain open.

- [Choose a specialist from the symptom](references/correction-patterns.md)
- [Review an API change without altering behavior](references/review-and-modernization.md)

# SwiftUI engineering entry point: playbook

## Route by the failure, not by the file extension

| Symptom | Primary skill | Pair when needed |
| --- | --- | --- |
| State resets, duplicate models, stale UI | `swiftui-state-architecture` | concurrency, persistence |
| Wrong screen, lost selection, deep-link failure | `swiftui-navigation` | platforms, testing |
| Truncation, keyboard overlap, rigid screen | `swiftui-layout` | accessibility, controls |
| Fake control, misleading label, focus failure | `swiftui-controls-input` | accessibility |
| Flat hierarchy, overused glass, inconsistent motion | `swiftui-design-system` | layout, platforms |
| Slow updates, hitches, memory growth | `apple-performance-cleanup` | concurrency, device validation |
| Save loss, duplicate export, offline failure | `apple-data-persistence` | networking, privacy |
| Widget, intent, watch, or health projection | `apple-system-experiences` | privacy, device validation |
| Missing target, signing resource, wrong configuration | `apple-project-governance` | release skills |

## Bound a change

For a draft editor supporting iOS 16, locate who owns the draft and who commits the note. Define what confirmation, cancellation, save failure, duplicate submission and relaunch should each leave in storage. Use the repository to resolve scope and supported targets before asking the user.

## Correct the failure mode

| Tempting shortcut | Better correction | Evidence |
| --- | --- | --- |
| Paint every button label white | Inspect style, role, tint, inherited foreground, background, and disabled state; use a tested custom style only for a real design requirement | Appearance and interaction matrix |
| Ban every AppKit/UIKit import | Encapsulate the missing platform capability in a narrow bridge with lifecycle ownership | Creation/update/teardown tests |
| Add `.id(UUID())` to force refresh | Repair observation or identity at its actual owner | Reorder, selection, and restoration tests |
| Shrink all text to fit | Reflow, shorten nonessential copy, or choose a compact layout | Accessibility text sizes and longer translations |
| Rewrite into a prescribed architecture | Extract only boundaries needed for ownership, isolation, reuse, or testing | Existing behavior preserved |
| Declare all integrations successful | Separate local commit, pending delivery, remote acknowledgement, and denied/unavailable states | Retry and interruption tests |

A component that owns both foreground and background can test contrast as a pair. Check disabled, focused and pressed states as well as semantic activation before accepting a custom style.

## Availability in a review

When a proposed fix uses a newer API, check the exact overload in the installed SDK against each affected target and language mode. Preserve the working fallback if a supported target still needs it. Record any SDK or destination you could not check. A screenshot can support a visual finding. A claim that a particular public symbol implements it needs a declaration.

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

Skill names are portable identifiers, not commands. A host may load Markdown automatically, through file reads, or through a generated bundle. No model, plugin, MCP server, or shell is mandatory.

## The implementation contract

Before nontrivial work, capture five facts: **outcome**, **scope**, **compatibility**, **state owner**, and **proof**. A one-line statement can cover them for a small fix. For a multi-surface change, enumerate the affected products and side effects. Do not turn this into an intake questionnaire when the repository already supplies the answers.

Example: “Save a local draft only after confirmation; retain iOS 16 support; the editor owns the draft, the repository owns durable notes; prove cancel, save failure, duplicate submission, and relaunch.” This is more actionable than “make the app production-ready.”

## Correct the failure mode

| Tempting shortcut | Better correction | Evidence |
| --- | --- | --- |
| Paint every button label white | Inspect style, role, tint, inherited foreground, background, and disabled state; use a tested custom style only for a real design requirement | Appearance and interaction matrix |
| Ban every AppKit/UIKit import | Encapsulate the missing platform capability in a narrow bridge with lifecycle ownership | Creation/update/teardown tests |
| Add `.id(UUID())` to force refresh | Repair observation or identity at its actual owner | Reorder, selection, and restoration tests |
| Shrink all text to fit | Reflow, shorten nonessential copy, or choose a compact layout | Accessibility text sizes and longer translations |
| Rewrite into a prescribed architecture | Extract only boundaries needed for ownership, isolation, reuse, or testing | Existing behavior preserved |
| Declare all integrations successful | Separate local commit, pending delivery, remote acknowledgement, and denied/unavailable states | Retry and interruption tests |

A system style cannot infer the contrast intent of every arbitrary custom background. A bespoke component may own foreground and background together when it provides tested contrast, disabled/focus/pressed behavior, and semantic `Button` activation. This is a scoped design decision, not permission to repaint system chrome indiscriminately.

## Source and availability procedure

For an unfamiliar or changed API, open its official symbol page and inspect the installed SDK declaration. Record the platform minimum and any compiler or feature-flag prerequisite. Distinguish a stable release, beta documentation, and a sample targeting a newer SDK. Keep an older implementation when it is correct and supported. If browsing or Xcode is unavailable, explicitly mark what remains unverified; do not invent symbols or silently raise requirements.

Apple documentation defines API contracts; the HIG provides design guidance. Local product choices can differ from a recommendation, but not erase API, accessibility, data-integrity, or authorization constraints. Apple screenshots demonstrate an experience, not the existence of a public API.

## Completion without ceremony

A useful handoff states what changed, why, what was tested against which source state, and what still needs a device or human review. Stop after delivering the authorized outcome. Do not install, publish, or change user data merely to make a checklist green.

## Sources

- [swiftui](https://developer.apple.com/documentation/SwiftUI) — SwiftUI framework overview.
- [design](https://developer.apple.com/design/human-interface-guidelines/design-principles) — HIG: Design principles.
- [button](https://developer.apple.com/documentation/SwiftUI/Button) — SwiftUI Button.
- [accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility) — HIG: Accessibility.

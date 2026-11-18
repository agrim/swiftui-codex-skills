# Coverage map

Generated from `catalog.json`; run `python3 scripts/skillctl.py docs` to update.

Select a skill for the engineering decision you face. Each folder includes its own checks and worked cases. Review provenance is available in the [source registry](sources.md).

| Skill | Scope | Platforms | Boundary |
| --- | --- | --- | --- |
| [apple-swiftui-native-apps](../skills/apple-swiftui-native-apps/SKILL.md) | Build or simplify a SwiftUI feature around one everyday task, from the first action to the result someone comes back for. | iOS, iPadOS, macOS | Feature design and the first working implementation. Start here when the main interaction is still taking shape. |
| [swiftui-platform-adaptation](../skills/swiftui-platform-adaptation/SKILL.md) | Adapt a SwiftUI task across phone, tablet or Mac while preserving the item, unfinished work and access to its actions. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Selection, navigation and access to actions across presentations, with a worked iPad resizing case. |
| [apple-data-persistence](../skills/apple-data-persistence/SKILL.md) | Design editing and persistence so people can tell what was saved, recover failed work, and keep their changes when sync is part of the feature. | iOS, iPadOS, macOS | Ownership of drafts, durable changes, and conflicts when the product promises synchronization. |
| [apple-system-experiences](../skills/apple-system-experiences/SKILL.md) | Choose what a widget, shortcut or notification should let someone see or do, including when its saved context has gone stale. | iOS, iPadOS, macOS, watchOS | Choosing a useful external entry point and preserving the app’s task and authority there. |
| [apple-performance-cleanup](../skills/apple-performance-cleanup/SKILL.md) | Find the work that delays a particular scroll, edit or launch and verify that the change improves that interaction while preserving its behavior. | iOS, iPadOS, macOS | Response time and frame delivery for a reproducible user interaction. |
| [apple-device-validation](../skills/apple-device-validation/SKILL.md) | Evaluate an installed build against the user journey a release promises, including the transition most likely to break it. | iOS, iPadOS, macOS | Product acceptance for an installed candidate, including upgrades, input and device-dependent behavior. |

## Applicability versus execution

The Platforms column describes where the engineering guidance may apply, not a list of tested destinations. The example package configures macOS 14 and iOS 17 minimums. CI is configured for macOS example execution and iOS SDK compilation; those definitions alone are not successful run receipts. Other listed platforms require their own relevant builds and runtime evidence. See the examples README and evaluation records for the precise contracts exercised.

## Deliberate limits

Select a guide when you face the product decision it describes. Use framework documentation for API mechanics and tool help for build and distribution commands. The [migration guide](skill-migration.md) explains the revised scope. The [evaluation protocol](evaluation.md) describes how to assess behavior on an app task.

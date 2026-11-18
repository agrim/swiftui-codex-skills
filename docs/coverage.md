# Coverage map

Generated from `catalog.json`; run `python3 scripts/skillctl.py docs` to update.

Select a skill for the engineering decision you face. Each folder includes its own checks and worked cases. Review provenance is available in the [source registry](sources.md).

| Skill | Scope | Platforms | Boundary |
| --- | --- | --- | --- |
| [apple-swiftui-native-apps](../skills/apple-swiftui-native-apps/SKILL.md) | Build or refine SwiftUI screens using native controls, clear action hierarchy, system styling and one owner for each interaction. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Native controls, product hierarchy and shared interaction state. The appearance depends on the built app and its supported OS versions. |
| [swiftui-platform-adaptation](../skills/swiftui-platform-adaptation/SKILL.md) | Adapt a SwiftUI task across window sizes, input methods and Apple devices while preserving selection, edits and navigation. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Navigation, focus, watch controls and continuity between windows or devices. |
| [apple-data-persistence](../skills/apple-data-persistence/SKILL.md) | Implement SwiftData or Core Data edits that respect Save and Cancel, survive relaunch and recover from failed or ambiguous writes. | iOS, iPadOS, macOS | Draft ownership, durable saves and competing edits in local or synced stores. |
| [apple-system-experiences](../skills/apple-system-experiences/SKILL.md) | Choose a widget, Live Activity or shortcut for an app task and verify its freshness, permissions and result from the system surface. | iOS, iPadOS, macOS, watchOS | Glances, live sessions and commands from Apple system surfaces. |
| [apple-performance-cleanup](../skills/apple-performance-cleanup/SKILL.md) | Use Instruments to fix a measured delay or memory problem, and simplify Swift code without losing behavior on the affected path. | iOS, iPadOS, macOS | Instruments and memory evidence for a specific user interaction. |
| [apple-device-validation](../skills/apple-device-validation/SKILL.md) | Verify a SwiftUI change on the installed build. Choose simulator captures, physical-device runs or paired-device checks to suit the defect. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Simulator, physical-device and paired-device proof for the behavior under review. |
| [apple-project-governance](../skills/apple-project-governance/SKILL.md) | Trace Xcode target, resource and entitlement problems from the source configuration to the signed app or extension that fails. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Target membership, schemes, resources and capabilities from source owner through signed product. |
| [apple-privacy-system-integrations](../skills/apple-privacy-system-integrations/SKILL.md) | Request Apple service access at the right moment, handle missing readings, and verify what gets exported, indexed or removed. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Permission UX, applicable privacy artifacts, and data handling across Apple services. Verify platform availability per integration. |
| [macos-productization](../skills/macos-productization/SKILL.md) | Verify signing, notarization, installed behavior and updates for the Mac artifact customers receive through the chosen distribution channel. | macOS | Direct, store and updater delivery of a signed Mac app. |
| [apple-app-store-readiness](../skills/apple-app-store-readiness/SKILL.md) | Verify that a specific TestFlight or App Store build delivers its listing, works for a reviewer and has reached the requested distribution stage. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Candidate identity, public-facing assets, review access and storefront readiness. Current store requirements depend on the product and region. |

## Applicability versus execution

The Platforms column describes where the engineering guidance may apply, not a list of tested destinations. The example package configures macOS 14 and iOS 17 minimums. CI is configured for macOS example execution and iOS SDK compilation; those definitions alone are not successful run receipts. Other listed platforms require their own relevant builds and runtime evidence. See the examples README and evaluation records for the precise contracts exercised.

## Deliberate limits

Select a guide for the app task and the evidence it calls for. Use the installed toolchain and current documentation for version-specific APIs and command options. The [migration guide](skill-migration.md) explains the revised scope. The [evaluation protocol](evaluation.md) describes how to assess behavior on an app task.

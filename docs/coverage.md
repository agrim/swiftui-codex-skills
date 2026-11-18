# Coverage map

Generated from `catalog.json`; run `python3 scripts/skillctl.py docs` to update.

Select a skill for the engineering decision you face. Each folder includes its own checks and worked cases. Review provenance is available in the [source registry](sources.md).

| Skill | Scope | Platforms | Boundary |
| --- | --- | --- | --- |
| [apple-swiftui-native-apps](../skills/apple-swiftui-native-apps/SKILL.md) | Design or repair a native SwiftUI feature, from the main action and state owner to toolbar controls, button contrast, and Liquid Glass. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Native controls, product hierarchy and shared interaction state. The appearance depends on the built app and its supported OS versions. |
| [swiftui-platform-adaptation](../skills/swiftui-platform-adaptation/SKILL.md) | Adapt SwiftUI navigation, focus and controls across Apple devices while keeping the selected item and unfinished task intact. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Navigation, focus, watch controls and continuity between windows or devices. |
| [apple-data-persistence](../skills/apple-data-persistence/SKILL.md) | Choose SwiftUI draft ownership and SwiftData or Core Data save boundaries so Cancel, retries and reopening preserve the right edits. | iOS, iPadOS, macOS | Draft ownership, durable saves and competing edits in local or synced stores. |
| [apple-system-experiences](../skills/apple-system-experiences/SKILL.md) | Choose and verify a WidgetKit glance, Live Activity or App Intent that reflects the app’s real state, account and actions. | iOS, iPadOS, macOS, watchOS | Glances, live sessions and commands from Apple system surfaces. |
| [apple-performance-cleanup](../skills/apple-performance-cleanup/SKILL.md) | Use Instruments to diagnose launch delays, UI hangs, scrolling hitches and retained memory, then verify the original interaction. | iOS, iPadOS, macOS | Instruments and memory evidence for a specific user interaction. |
| [apple-device-validation](../skills/apple-device-validation/SKILL.md) | Use Xcode, Simulator and physical devices to verify rendering, upgrades, interaction and paired-device behavior on the intended build. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Simulator, physical-device and paired-device proof for the behavior under review. |
| [apple-project-governance](../skills/apple-project-governance/SKILL.md) | Fix Xcode project and signing configuration when a widget, watch app, extension or shared capability builds but fails in the installed product. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Target membership, schemes, resources and capabilities from source owner through signed product. |
| [apple-privacy-system-integrations](../skills/apple-privacy-system-integrations/SKILL.md) | Integrate HealthKit, CloudKit or another Apple service with a clear permission request, useful fallback and accurate treatment of data that leaves the app. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Permission UX, applicable privacy artifacts, and data handling across Apple services. Verify platform availability per integration. |
| [macos-productization](../skills/macos-productization/SKILL.md) | Prepare or diagnose a Mac release by checking the signed app, packaging, Gatekeeper, installed icon and update path for its distribution channel. | macOS | Direct, store and updater delivery of a signed Mac app. |
| [apple-app-store-readiness](../skills/apple-app-store-readiness/SKILL.md) | Match an Xcode archive and TestFlight build to the app’s storefront promise, production services, screenshots and App Review access. | iOS, iPadOS, macOS, watchOS, tvOS, visionOS | Candidate identity, public-facing assets, review access and storefront readiness. Current store requirements depend on the product and region. |

## Applicability versus execution

The Platforms column describes where the engineering guidance may apply, not a list of tested destinations. The example package configures macOS 14 and iOS 17 minimums. CI is configured for macOS example execution and iOS SDK compilation; those definitions alone are not successful run receipts. Other listed platforms require their own relevant builds and runtime evidence. See the examples README and evaluation records for the precise contracts exercised.

## Deliberate limits

Select a guide for the app task and the evidence it calls for. Use the installed toolchain and current documentation for version-specific APIs and command options. The [migration guide](skill-migration.md) explains the revised scope. The [evaluation protocol](evaluation.md) describes how to assess behavior on an app task.

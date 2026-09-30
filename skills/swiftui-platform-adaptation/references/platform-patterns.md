# Platform-native scenes and interaction: playbook

## iOS: touch and interruptions

Use familiar hierarchical navigation, sheets for focused tasks, and safe-area-aware controls. Support keyboard presentation, orientation/window changes allowed by the app, interruption, and restoration. Permission denial should block only the dependent experience. Do not make an essential action require an undocumented gesture.

## iPadOS: a resizable workspace

Design for the actual window width rather than treating “iPad” as one large fixed canvas. Split views, sidebars, inspectors, drag/drop, keyboard shortcuts, and pointer interaction can improve substantial workflows. Test narrow and expanded presentations, external input, and multiple scenes. Keep each window's selection and draft independent when that is the intended product behavior.

## macOS: desktop ownership

Choose `WindowGroup` for multiple instances, an appropriate single-window scene for a singleton, `DocumentGroup` for documents, `Settings` for app preferences, and `MenuBarExtra` for menu-bar experiences where available. Launch and restoration behavior depends on the actual scene configuration; verify it rather than applying a universal window-opening workaround.

Use commands, menus, toolbars, sidebars, inspectors, contextual actions, and focused values to route actions to the current window. Preserve standard shortcuts, menu validation, undo, and responder behavior. A menu-bar-only app and a Dock app with a menu extra have different activation expectations; make that choice explicit. Do not unconditionally change activation policy or add AppDelegate workarounds to every app.

Keep document identity, file access, save state, and window lifecycle coherent. Use narrow AppKit interop where the public SwiftUI scene or text APIs do not meet a concrete requirement. Test first launch, reopen, last-window close, multiple windows, and Settings access.

## watchOS: glanceable and task-focused

Prioritize immediate state and the next action. Reduce copy and secondary controls before shrinking labels. Consider Crown, haptics, compact navigation, always-on behavior, limited resources, interruptions, and independent/companion roles as applicable. Do not run continuous work merely because a screen remains visible. Permission, HealthKit, connectivity, and background execution require their own contracts.

Phone and watch communicate across a delivery boundary. A phone acknowledgement does not prove the watch rendered current state. Test disconnected, delayed, duplicated, and reordered delivery, plus watch-local recovery. Keep the local useful experience explicit when the phone is absent.

## tvOS: focus from a distance

Design around focus navigation, remote activation, readable content at viewing distance, and discoverable movement between controls. Every essential element must be reachable; focus should recover predictably after data changes or dismissal. Avoid touch-only gestures, dense phone forms, and tiny targets. Use native focus behavior before custom effects. Verify the supported input hardware and remote behavior on the target runtime.

## visionOS: comfort and spatial context

Begin with windows and familiar controls; choose volumes or immersive spaces only when spatial presentation adds user value. Preserve legibility, comfortable reach and motion, clear focus/hover feedback, and safe exits. Do not assume access to raw gaze, hands, or surroundings merely because the app runs spatially. Verify the exact capabilities and permission boundaries.

Test lifecycle changes, immersion entry/exit, interruption, multiple windows, and reduced motion. Avoid copying a phone's fixed dimensions into space or anchoring distracting motion to the user's head. Simulator rendering cannot establish physical comfort or all hardware behavior.

## Platform matrix template

For each target, record: primary task, scene/container, input, state owner, API minimums, unavailable capabilities, fallback, build destination, runtime checks, and device-only gates. Share domain invariants and typed commands; specialize the presentation where the platform benefits. Keep compile-time platform checks near adapters instead of scattering them through business logic.

## Sources

- [ios](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) — HIG: Designing for iOS.
- [ipados](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados) — HIG: Designing for iPadOS.
- [macos](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos) — HIG: Designing for macOS.
- [watchos](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos) — HIG: Designing for watchOS.
- [tvos](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos) — HIG: Designing for tvOS.
- [visionos](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos) — HIG: Designing for visionOS.
- [windows](https://developer.apple.com/design/human-interface-guidelines/windows) — HIG: Windows.
- [settings](https://developer.apple.com/design/human-interface-guidelines/settings) — HIG: Settings.
- [swiftui](https://developer.apple.com/documentation/SwiftUI) — SwiftUI framework overview.

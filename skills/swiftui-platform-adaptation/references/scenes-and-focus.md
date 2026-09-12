# Scenes, desktop behavior, and focus platforms

Choose the scene model before the screen hierarchy: multiple document windows, a primary window, an auxiliary utility, settings, menu-bar UI, or spatial content have different ownership and restoration needs. Define app-wide services separately from per-scene selection, drafts, and navigation.

On macOS, keep important actions available through appropriate menus/commands and keyboard shortcuts. Route focused commands to the active window's selection rather than a global last-selected object. Test two windows editing different items, close/reopen, settings, and menu-bar-only versus ordinary app behavior. Do not force activation or change Dock presence without a product reason.

On iPad, test resizing, split layouts, keyboard/pointer input, and sidebar collapse without losing selection. On watch, design for compact, short interactions, appropriate Crown behavior, and delayed companion delivery. Do not merely scale a phone dashboard down.

On tvOS, reason about the focus engine: directional movement, stable focused identity, restoration, and discoverable actions. A view that looks tappable is not proof it can receive remote focus. On visionOS, choose window, volume, or immersive roles deliberately; respect comfort, accessibility, spatial placement, and platform-specific availability rather than adding depth everywhere.

## Shared-code boundaries

Share domain models and commands where semantics match. Adapt navigation, menus, input, focus, permissions, and lifecycle at the platform boundary. Conditional compilation should expose deliberate differences rather than hide missing features behind empty branches.

Record guidance applicability separately from tested destinations. Compiling a shared module for one platform does not prove every scene type, system surface, or input method on all platforms. Test the critical native journey and restore state under actual window/device lifecycle transitions.

## Official sources

- [HIG: Windows](https://developer.apple.com/design/human-interface-guidelines/windows).
- [HIG: Settings](https://developer.apple.com/design/human-interface-guidelines/settings).
- [HIG: Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos).
- [HIG: Designing for iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados).
- [HIG: Designing for watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos).
- [HIG: Designing for tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos).
- [HIG: Designing for visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos).

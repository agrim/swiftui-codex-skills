---
name: macos-productization
description: "Verify signing, notarization, installed behavior and updates for the Mac artifact customers receive through the chosen distribution channel."
---

# Ship a Mac app people can install and update

Inspect what the customer receives. The same app can work from Xcode and fail after a direct download, a Mac App Store install or an in-app update.

## Design choices

1. **Choose the channel’s checks.** For direct download, inspect the app and nested helpers for their Developer ID signatures, entitlements and hardened runtime. For the Mac App Store, inspect the sandbox and embedded products in the distribution archive. <!-- MAC-101 -->
2. **Follow the submitted artifact through packaging.** For Developer ID delivery, match the notary result to the submitted item. Staple where supported and verify the final download. ZIPs and DMGs take different paths. <!-- MAC-102 -->
3. **Launch the installed copy.** Check the Dock icon and a feature that needs a bundled helper or resource. For updates, start with the previous release and an existing document. <!-- MAC-103 -->

## Try it

Try the customer’s delivery channel.

- On a clean Mac or VM, download the direct release with quarantine intact. With normal Gatekeeper settings the installed app opens and the shipped helper performs its task. <!-- MAC-101 MAC-102 -->
- Update through the supported channel. The running app has the intended build and icon, and the existing document still opens. <!-- MAC-103 -->

- [The app runs from Xcode but the downloaded DMG will not open](references/downloaded-dmg.md)

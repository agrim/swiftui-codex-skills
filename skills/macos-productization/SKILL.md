---
name: macos-productization
description: "Prepare or diagnose a Mac release by checking the signed app, packaging, Gatekeeper, installed icon and update path for its distribution channel."
---

# Ship a Mac app people can install and update

Start with the file the customer receives and where they got it. A directly downloaded DMG, an app installed from the Mac App Store and an updater payload follow different trust paths.

## Design choices

1. **Choose the distribution channel first.** For direct download, inspect the Release app’s Developer ID signature, nested helpers, hardened runtime and entitlements. For the Mac App Store, inspect the distribution archive, sandbox and embedded products intended for that channel. <!-- MAC-101 -->
2. **Verify the final delivery artifact.** For direct delivery, match the notarization result to the submitted artifact, validate stapling where supported, and assess Gatekeeper on a quarantined download. Repacking or replacing a helper after signing can change what the recipient gets. <!-- MAC-102 -->
3. **Try the customer’s install and update.** Launch the installed copy, inspect its Dock or Finder icon and exercise a feature that uses an embedded helper or resource. For an updater, start at the previous shipped version and check the signed update reaches this build with user data intact. <!-- MAC-103 -->

## Try it

Use the releasable archive or download and a representative installation.

- Compare the bundle ID, version, signature, entitlements and helper in the packaged copy against the intended release. For direct distribution, check notarization and Gatekeeper on that delivery. <!-- MAC-101 MAC-102 -->
- Install or update through the chosen channel. Check the version, icon, launch and an existing user document in the installed app. <!-- MAC-103 -->

- [The app runs from Xcode but the downloaded DMG will not open](references/downloaded-dmg.md)

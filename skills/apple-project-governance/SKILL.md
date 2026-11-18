---
name: apple-project-governance
description: "Trace Xcode target, resource and entitlement problems from the source configuration to the signed app or extension that fails."
---

# Wire an Apple capability through the right Xcode targets

A widget can compile and still read an empty store. Trace one app-written value into the signed extension from the failing build.

## Design choices

1. **Edit the setting where it is defined.** Find the manifest, project, xcconfig or package that controls the setting. Regenerate when applicable. Use the failing scheme, configuration and destination. <!-- PROJECT-101 -->
2. **Check each target’s part.** The app and widget have distinct bundle IDs. To share a container, both signed products and their runtime lookups must use the intended App Group. For a missing resource, inspect target membership and the embedding phase. <!-- PROJECT-102 -->
3. **Read the effective value.** Compare resolved build settings with the archived Info.plist, resources and signed entitlements. If those agree, follow the runtime write and read before changing project settings again. <!-- PROJECT-103 -->

## Try it

Write a fresh marker so an old cached value cannot pass.

- Archive the affected configuration. Find the embedded extension, its expected resource and the intended group in both signatures. <!-- PROJECT-101 PROJECT-102 -->
- Read the app’s marker from the widget. For a paired watch, verify transfer across devices and read it on the receiver. <!-- PROJECT-103 -->

- [The app writes a value but the widget sees an empty store](references/empty-widget-store.md)

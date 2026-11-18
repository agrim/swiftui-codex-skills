---
name: apple-project-governance
description: "Fix Xcode project and signing configuration when a widget, watch app, extension or shared capability builds but fails in the installed product."
---

# Wire an Apple capability through the right Xcode targets

A widget can compile and still see an empty store. Trace the setting from the file that owns it through the app and extension Xcode actually builds.

## Design choices

1. **Edit the source of the setting.** Locate the workspace, generator manifest, project, xcconfig or Package.swift that owns the change. If a manifest generates the project, edit and regenerate it. Use the shared scheme and configuration that produce the failure. <!-- PROJECT-101 -->
2. **Follow identity into each consumer.** For shared storage, match the App Group entitlement with the suite or container name used by each process. The app and extension need distinct bundle IDs. Check resource membership, embedding and provisioning for the targets that use the capability. <!-- PROJECT-102 -->
3. **Inspect the resulting product.** Compare resolved build settings, the built Info.plist, embedded resources and signed entitlements. Then exercise one write/read across the real boundary. A correct setting in Debug may be overridden in Release. <!-- PROJECT-103 -->

## Try it

Use a value that makes a wrong target or configuration visible.

- Regenerate when applicable, select the shared scheme and build the affected configuration. Inspect the containing app and the embedded extension for the expected IDs, resource and signed group. <!-- PROJECT-101 PROJECT-102 -->
- Write a distinctive value in the installed app. Read it from the actual widget. For a paired watch, inspect the data sent across devices and the value received there. If it is absent, identify the first mismatch between source, signed product and runtime. <!-- PROJECT-103 -->

- [The app writes a value but the widget sees an empty store](references/empty-widget-store.md)

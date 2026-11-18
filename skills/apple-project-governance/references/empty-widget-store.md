# The app writes a trip but its widget reads an empty store

Start with a known trip ID. Identify the app that wrote it and the extension embedded in the installed build. The two products have different bundle IDs. An App Group shares a container on one device. Getting a trip onto a paired watch needs its own transport, such as WatchConnectivity. Where the widget reads a shared App Group, the relevant signed products and the runtime suite or container name must agree on that group.

For a workspace, compare the scheme and effective configuration with:

```sh
xcodebuild -list -workspace "$workspace"
xcodebuild -showBuildSettings -workspace "$workspace" -scheme "$scheme" -configuration Release
```

If the workspace uses a project generator, change its manifest and inspect the generated diff. Check the target’s configuration overrides, entitlement path and copy phases. Inspect a signed device archive for the exact app and extension. With paths set to those two bundles, these commands display the entitlements each signature contains:

```sh
codesign -d --entitlements - "$app"
codesign -d --entitlements - "$extension"
```

Compare the group, built Info.plists and extension membership. If the products agree, inspect the runtime suite and the written snapshot before changing the timeline provider. A Swift package dependency or Xcode group can make source visible in the editor while the extension still lacks a needed resource.

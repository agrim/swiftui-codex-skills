# The signed widget reads an empty store

Pick one trip ID written by the app. Locate the containing app and its embedded widget in the failing device archive. They have separate bundle IDs. Shared storage on one device requires the same intended App Group in both signed products and in the runtime container or suite lookup. A paired watch needs a separate data transfer.

Inspect the same workspace, shared scheme, configuration and destination that built the archive. Identify which target each block of settings describes. Use the generator manifest or target’s xcconfig when that file owns the setting.

```sh
xcodebuild -list -workspace "$workspace"
xcodebuild -showBuildSettings -workspace "$workspace" -scheme "$scheme" -configuration Release -destination 'generic/platform=iOS'
codesign -d --entitlements - "$app"
codesign -d --entitlements - "$extension"
```

Set the last two paths to the archived app and its embedded extension. Compare the signed application groups with the runtime suite. If the extension is missing, inspect embedding and target membership. If a model or asset is missing, check the built bundle that loads it, including a package resource bundle where applicable.

When the signed products agree, read the shared snapshot from the extension. A missing trip there points to the write or container lookup. A correct trip there moves the investigation to timeline selection and host rendering. Stop changing signing settings once the value has crossed that boundary.

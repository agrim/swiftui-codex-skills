# A downloaded Mac app opens but its helper fails

Use the copy installed from the customer’s download. Identify the top-level app and the embedded executable that failed. Compare each signature’s team identity and entitlements. A valid app signature can still describe a helper with the wrong entitlement or a bundle missing a required resource.

For a Developer ID app delivered on a stapled DMG, set the paths to that installed app, its helper and the final downloaded image. These checks inspect the signatures, signed permissions, stapling and execution assessment:

```sh
codesign --verify --deep --strict --verbose=2 "$app"
codesign -dv --verbose=4 "$helper"
codesign -d --entitlements - "$helper"
xcrun stapler validate "$dmg"
spctl --assess --type execute --verbose=4 "$app"
```

Match the notary record to the item submitted. For a DMG, validate its stapled ticket. For a ZIP, staple the supported enclosed item after acceptance, recreate the ZIP, then download and extract that final ZIP. Preserve quarantine and launch the installed copy on a clean test Mac or VM. Invoke the helper. Inspection alone cannot exercise that feature.

If the installed icon is wrong, trace the canonical Icon Composer or asset-catalog source through the target into the packaged app. If only an update fails, inspect the actual feed and signed payload used by the previous release, then check the running version and an existing document.

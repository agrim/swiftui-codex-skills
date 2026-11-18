# The app runs locally but the downloaded DMG will not open

Identify the version and build in the downloaded image. Inspect the app and each embedded helper that can launch. On macOS the following commands answer different questions about a direct Developer ID release. Set the paths to the app in the delivered image and the final disk image:

```sh
codesign --verify --deep --strict --verbose=2 "$app"
codesign -d --entitlements - "$app"
xcrun stapler validate "$dmg"
spctl --assess --type execute --verbose=4 "$app"
```

Verify a stapled DMG when that is the chosen notarized container. Consult the notary submission result and log for the artifact actually sent. An accepted submission does not describe a later repack. Check that the tested download retains quarantine and try the installed app under normal Gatekeeper settings. Keep the original failing build available for comparison.

If the app opens but its icon or helper differs, inspect the copy you installed. Compare the canonical Icon Composer package or asset catalog, resolved icon name, target resources and bundled helper signature. If only updates fail, check the feed’s version, payload identity and updater signature using the previous released client. A successful fresh install exercises a different path.

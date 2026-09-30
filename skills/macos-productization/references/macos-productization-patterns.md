# macOS productization and distribution: playbook

## Channel contract

| Channel | Establish before packaging |
| --- | --- |
| Local development | Development signing and local execution expectations |
| Internal distribution | Authorized recipients, installation process, and organizational requirements |
| Direct download | Developer ID trust, applicable hardened runtime and notarization, downloadable artifact behavior |
| Mac App Store | Store distribution, applicable sandbox/entitlements, archive/export and review requirements |

A DMG is a delivery container, not evidence that the contained app is signed or trusted. An updater adds its own authenticity and rollback requirements; it does not replace application signing. Consult current Apple distribution documentation for the selected path.

## Inspect before repairing

Record bundle identifier, version/build, signing identity, architectures, nested frameworks/helpers/extensions, effective entitlements, resource integrity, and source provenance. Inspect the exact artifact that users receive, not a convenient neighboring build.

For an authorized local inspection, command templates include:

```bash
codesign --verify --strict --verbose=2 Example.app
codesign --display --entitlements :- Example.app
spctl --assess --type execute --verbose=2 Example.app
xcrun stapler validate Example.app
```

Check installed tool help and platform behavior before relying on options. These commands establish different facts and have not been executed merely because they appear here. A failing staple check is not by itself a complete explanation of signing or launch failure.

Inspect nested components individually where necessary. Sign from the intended build/export pipeline with the correct identity and entitlements. Do not use `codesign --deep` as a generic signing repair: it can mask an ownership problem or assign the wrong policy to nested code.

## Notarization and delivery

Use the current supported notarization workflow only when submission is authorized. Keep credentials in approved secure storage or CI secrets, not scripts, repository files, command transcripts, or artifacts. Record the submitted artifact and service result, and inspect failure logs rather than repeatedly changing random signing flags.

Acceptance, ticket stapling, Gatekeeper assessment, and user launch are separate gates. Test the packaged/downloaded path under realistic quarantine and install conditions when authorized; a previously trusted development copy is weaker evidence. Confirm that the tested installed app is the one from the release package.

## Packaging and resources

Make packaging reproducible and reviewable. Preserve file modes, bundle structure, nested code, metadata, and required resources. Verify icon appearance in the installed app and relevant system surfaces, not only in the source asset catalog.

For installers, justify privileged operations and test their scope explicitly. Do not delete user data or change global security settings to make installation pass. Provide a safe upgrade path for existing data and clearly distinguish uninstall behavior from account or cloud-data deletion.

## Updates

Bind version/build, release notes, artifact hashes, signed update metadata, and distribution URLs to the same candidate. Authenticate updates using the chosen updater's current documented mechanism. Reject downgrade/replay or mixed-candidate behavior where the product's security contract requires it.

Test interrupted download, failed validation, install failure, relaunch, and retained user data. Do not invent an updater protocol in this skill; inspect the selected implementation and its official security guidance.

## Completion

Pair with project governance for configuration ownership and with App Store readiness for storefront/review orchestration. Report source, archive, exported bundle, package, service receipts, and installed-copy checks separately. An absent toolchain or unapproved external action is an unverified gate, not success.

## Sources

- [notarization](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution) — Notarizing macOS software before distribution.
- [distribution](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases) — Distributing your app.
- [review](https://developer.apple.com/app-store/review/guidelines/) — App Review Guidelines.
- [xcode](https://developer.apple.com/documentation/xcode) — Xcode documentation.
- [developer-id](https://developer.apple.com/developer-id/) — Signing Mac software with Developer ID.
- [notary-errors](https://developer.apple.com/documentation/security/resolving-common-notarization-issues) — Resolving common notarization issues.

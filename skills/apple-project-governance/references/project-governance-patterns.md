# Apple project governance: playbook

## Ownership matrix

| Value | Inspect the source owner | Inspect the result |
| --- | --- | --- |
| Targets and dependencies | Generator manifest, project, or Package.swift | Discovered products and build graph |
| Build/test selection | Shared schemes and CI configuration | Actual scheme and test-plan invocation |
| Capabilities | Entitlement inputs and provisioning configuration | Signed product entitlements |
| Usage descriptions | Info.plist inputs, build settings, localization | Built property list and displayed prompt |
| Assets and models | Catalogs, model files, target membership | Compiled resources in the product |
| App identity | Bundle IDs, groups, services, constants | App, extension, companion, and account configuration |

Do not assume that a file visible in the repository belongs to a target. A resolved package is not proof that the intended target links it. A generator may own only part of the project: establish its scope before deleting or regenerating everything.

## Inspect without guessing

Use the workspace when it is the build entry point; use the project when that is the repository's contract. Discover names rather than substituting a remembered scheme. Run the installed tool's help for uncertain options.

```bash
xcodebuild -version
xcodebuild -list -project Example.xcodeproj
xcodebuild -showdestinations -project Example.xcodeproj -scheme Example
xcodebuild -showBuildSettings -project Example.xcodeproj -scheme Example -configuration Debug
```

These are command templates, not commands already executed. Add the selected destination when inspecting destination-dependent settings. Avoid dumping environment-derived credentials into logs. Keep command, toolchain, exit status, and relevant output with the validation record.

`-list` establishes discovery; `-showdestinations` establishes available destinations; `-showBuildSettings` establishes resolved settings in its selected context. None of these proves runtime behavior. A successful debug simulator build does not establish release signing or device provisioning.

## Cross-product coherence

Trace identity through the main app, widgets, watch app, intents, tests, keychain groups, app groups, CloudKit containers, and associated domains that actually exist. Centralize repeated identifiers where the platform permits it, but do not hide configuration that must remain visible in entitlement or property-list files.

Preserve stable bundle identifiers and persistence keys unless migration is part of the request. Public naming, internal type names, and storage identities have different compatibility costs. Verify a renamed product's displayed name and asset pipeline without rewriting unrelated identifiers.

Maintain a canonical editable app-icon source per chosen pipeline. Confirm the compiled output and supported variants before removing older assets; a source image is not proof of installed icon appearance.

## Build settings and dependencies

Scope changes at project, target, or configuration level intentionally. Verify compiler version, language mode, strict concurrency settings, deployment minimums, supported destinations, and dependency versions separately. New compiler support does not guarantee that a runtime API exists on the deployment minimum.

Keep dependency changes reviewable: inspect package resolution, licenses, binary artifacts, target exposure, platform constraints, and privacy implications. Do not upgrade the whole graph merely to fix one configuration issue.

## Proof and failure routing

After regeneration, review the diff before debugging runtime code. A missing privacy resource or extension may be a membership defect rather than a framework bug. Inspect the built Info.plist and resource bundle when those are the claim; inspect signed entitlements when meaningful signing is present.

Classify a failing build before editing source: unknown scheme, unsupported destination, unavailable SDK/runtime, compiler error, resource processing, dependency resolution, signing, or tool service. Preserve raw error context, then fix the demonstrated owner. Repeat affected checks after source or generated state changes.

Finish with whitespace/diff checks and a concise configuration-to-product evidence table. Never describe an entitlement source file as proof of user authorization.

## Sources

- [xcode](https://developer.apple.com/documentation/xcode) — Xcode documentation.
- [distribution](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases) — Distributing your app.
- [privacy](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests) — Describing data use in privacy manifests.

# macOS Productization Playbook

Use this playbook when macOS work crosses from source configuration into an artifact a user, reviewer, store, deployment system, or updater may install or trust.

## Match Actions to the Requested Mode

| Mode | Allowed default work | Do not infer authority for |
| --- | --- | --- |
| Review or diagnose | Inspect source configuration, scripts, existing archives, built apps, packages, signatures, entitlements, metadata, and recorded service status | Editing, signing, packaging, installation, launch, credential use, notarization submission, upload, publication, deletion, or system changes |
| Implement or prepare | Make requested repository changes; build or package locally when that is an ordinary proof step | Installing or launching the result, using distribution credentials, submitting to Apple, publishing releases or update feeds, replacing an installed app, or privileged changes |
| Validate or release | Perform the explicitly requested checks or release operations and retain evidence | Unrequested channels, destructive cleanup, secret disclosure, or broader account and system changes |

Treat an explicit release request as authority only for the named release flow. Request separate approval for privileged operations and for destructive actions that could remove an installed app, preferences, caches, receipts, or user data.

## Use the Evidence Hierarchy

Project files and build settings express intent. Prove release claims against progressively stronger evidence:

1. Inspect source-owned manifests, target settings, entitlements, asset catalogs, and packaging scripts. Pair with `$apple-project-governance` when these need correction.
2. Inspect the archive or built app for its actual identity, version, build, architectures, nested code, signature, embedded entitlements, hardened runtime, sandbox state, resources, and icons.
3. Inspect the final DMG, package, archive, or update payload users will receive. Packaging success alone does not prove its contents are correct.
4. Use notarization receipts, stapling validation where supported, Gatekeeper assessment, App Store validation, or update-signature checks for the exact artifact and channel.
5. Mount, install, and launch the installed copy only when authorized. Runtime success proves a different gate from build or packaging success.

A local launch is not evidence of public Gatekeeper readiness. A valid code signature is not evidence of notarization. A successful package command is not evidence that icons, entitlements, helper tools, and embedded resources survived packaging.

## Apply the Channel Gates

### Local Development

- Identify whether the build is unsigned, ad hoc signed, or development signed and state that truthfully.
- Inspect the built identity and entitlements needed for local behavior.
- Validate the expected local launch context when requested.
- Do not describe a locally launchable or ad hoc signed app as ready for external distribution.

### Internal or Enterprise Distribution

- Record the organization's actual trust, signing, deployment, update, and install requirements instead of assuming they match public direct distribution.
- Inspect the built signature, entitlements, hardened runtime, sandbox choice, nested code, and package contents against that policy.
- Validate installation and launch in the intended managed or internal context when authorized.
- Do not claim notarization or Gatekeeper readiness unless those gates are required and independently verified.

### Direct Developer ID Distribution

- Build the release configuration from the intended commit and coherent version/build identifiers.
- Sign the app and every nested executable component with the intended Developer ID Application identity and required hardened-runtime and entitlement configuration.
- Create the reproducible final delivery artifact only after the contained app is coherent.
- Submit the exact supported delivery artifact or notarizable payload required by the release flow, retain the accepted result, and staple and validate supported artifacts where applicable.
- Assess Gatekeeper against the artifact users will receive. Keep Developer ID signing, notarization acceptance, stapling, and Gatekeeper assessment as separate recorded facts.
- Mount or install and launch the installed copy when authorized, then attach that exact artifact to matching release notes.

### Mac App Store Distribution

- Keep App Store distribution signing, provisioning, sandboxing, capabilities, export, and validation distinct from Developer ID distribution.
- Pair with `$apple-app-store-readiness` for App Store Connect metadata, public support and privacy surfaces, review information, exact-build selection, submission, and release status.
- Build and inspect the intended archive, including every app extension, helper, embedded framework, entitlement, and bundle identity.
- Validate the archive and metadata for the store workflow. Pair with `$apple-privacy-system-integrations` for privacy declarations, permission behavior, and required privacy artifacts.
- Upload or submit only when explicitly requested and authorized; record the exact archive, version, build, and resulting status.
- Do not use Developer ID signing or direct-download notarization evidence as a substitute for App Store validation.

### DMG or Installer Package Overlay

- Stage from a clean, deterministic directory and use a reproducible script rather than a hand-built archive.
- Include only intended apps, links, licenses, resources, and support files. Exclude user data, local paths, credentials, debug artifacts, and stale builds.
- Sign contained code before packaging. For direct package distribution, use the intended Developer ID Installer identity, and apply the base channel's notarization requirements to the final delivery flow.
- Mount the DMG or inspect/install the package when authorized. Verify volume or package identity, destination behavior, nested resources, helper tools, and the installed app rather than trusting the staging directory.
- Verify icon presentation from the built and packaged product. Preserve the current Apple asset pipeline; do not flatten or simplify source assets in a way that changes platform rendering.

### Sparkle or Another Update Overlay

- Keep the framework, update endpoint, feed metadata, update signature, code signature, version comparison, and artifact URL coherent.
- Protect signing keys and credentials; never print or commit private material while generating update signatures.
- Require monotonic version/build behavior appropriate to the updater and tie each feed entry to an immutable artifact and matching release notes.
- Validate the update payload independently from the appcast or feed. Test an update from a representative prior release when requested and authorized.
- Publish the artifact and feed in an order that cannot direct users to a missing, mutable, unsigned, or mismatched payload.
- Treat updater validation as an additional gate; it does not replace Developer ID, notarization, Gatekeeper, App Store, or installed-launch checks required by the base channel.

## Keep the Release Coherent

Tie together:

- source commit and clean or intentionally described working state;
- marketing version and build number;
- bundle identity, signing identity, entitlements, hardened runtime, and sandbox choice;
- app icon and embedded resources in the built product;
- archive, DMG, package, or update artifact identity and checksum when used;
- notarization, Gatekeeper, store, or updater evidence;
- release notes and every attached or published artifact.

If any element refers to a different build, stop and reconcile it before release. Do not rewrite a release claim to sound complete when the corresponding gate was not run.

## Report the Truth Precisely

Report:

- the requested mode and distribution channel;
- the exact archive, app, package, or update artifact inspected;
- the embedded identity, version/build, signature, entitlements, hardened runtime, sandbox, and icon evidence checked;
- notarization, stapling, Gatekeeper, store, packaging, updater, installation, and launch results as separate facts;
- every credentialed, external, privileged, destructive, install, launch, upload, or publish action performed;
- every gate not run, not authorized, failed, or still unverified.

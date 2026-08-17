# Project Governance Operational Playbook

Use this reference to determine who owns a project value, propagate it across products, and select evidence that proves the effective result.

## Ownership Matrix

| Concern | Inspect or edit the source owner | Prove the effective result |
|---|---|---|
| Project and target graph | Generator manifest when present; otherwise the source-controlled `.xcodeproj` or workspace composition | Regenerated diff, `xcodebuild -list`, and a target-specific build |
| Swift package products and dependencies | `Package.swift`, resolved dependency policy, or generator/project dependency declarations | Platform-compatible resolution plus link or embed membership in the consuming target |
| Shared build and test contract | Source-controlled `.xcscheme`, generator scheme declaration, and CI invocation | `xcodebuild -list`, scheme actions, test plans, and the same command shape used by CI |
| Source and resource membership | Manifest target entries or target build phases | Target-specific build plus inspection of compiled sources or built resources as appropriate |
| App icon pipeline | Canonical `.icon` package or asset catalog, generator resource entries, asset-name settings, and target membership | Compiled asset output, built-bundle icon resources, and runtime appearance through `apple-device-validation` |
| `Info.plist` values | Source plist, manifest settings, or generated-info build settings | `xcodebuild -showBuildSettings` and the built product's `Info.plist` |
| Capabilities and entitlements | Capability declaration, entitlement file, and `CODE_SIGN_ENTITLEMENTS` ownership | Resolved build setting and signed entitlements in the applicable built product |
| Bundle and service identity | Manifest or target settings plus typed app constants | Effective product identifier and consistent values in every app, extension, widget, watch product, test, and service |
| CI-only project behavior | Workflow, build script, environment, configuration, and scheme selection | Reproduce the narrow CI command or compare its explicit inputs with local evidence |

Locate the manifest or establish that none exists. Generated projects invite plausible-looking but temporary hand edits; never assume the visible `.xcodeproj` owns a value.

## Cross-Product Propagation

Before changing identity or capability configuration, inventory every app product and extension product. For each affected value, record:

- the declaring source;
- the consuming targets and configurations;
- whether each consumer needs the same value, a derived value, or no value;
- the typed runtime constant, if code also consumes it;
- the provisioning or service-side expectation; and
- the artifact that will prove the final value.

Apply this check to bundle IDs, display names, app groups, keychain groups, suite names, CloudKit containers, HealthKit identifiers, associated domains, deep links, canonical icon sources, widgets, watch products, tests, and services. Duplicated strings and competing asset sources drift easily, while an apparently successful app build can leave a companion product miswired.

## Evidence Matrix

Select the tool that answers the actual question:

| Evidence | What it proves | What it does not prove |
|---|---|---|
| Generator run plus generated diff | The source manifest can reproduce the intended project change without unexplained churn | That Xcode selects or builds the intended product |
| `xcodebuild -list` | The chosen project or workspace exposes the expected targets, configurations, and schemes | Destination availability, effective settings, or runtime behavior |
| `xcodebuild -showdestinations -scheme ...` | Xcode knows compatible destinations for that scheme | Target membership, resource inclusion, or successful compilation |
| `xcodebuild -showBuildSettings ...` | Inherited and resolved settings for an explicit project or workspace, scheme, configuration, and destination | Built resources, signed entitlements, or runtime permission behavior |
| Narrow target or scheme build | The selected graph compiles and its declared build phases execute | Correct runtime behavior or complete cross-product identity coherence |
| Built `Info.plist` inspection | The product received generated or copied property-list values | Signed capabilities or resource presence outside the plist |
| Built bundle resource inspection | The intended product contains a resource such as an asset, model, intent definition, or `PrivacyInfo.xcprivacy` | That the resource's semantics are correct |
| Signed-entitlement inspection | The applicable built executable received the entitlements used for signing | Provisioning acceptance, service behavior, or user permission semantics |
| Focused test or runtime proof | The chosen behavior works in that environment | Other schemes, configurations, destinations, or distribution channels |

Use explicit `-project` or `-workspace`, `-scheme`, `-configuration`, and destination inputs when comparing results. Otherwise, an apparently contradictory result may simply describe a different build context.

## Failure Routing

| Symptom | Inspect first |
|---|---|
| File compiles nowhere or symbols are missing only in one product | Source membership, generated target entries, and platform availability |
| Runtime cannot find an asset, model, privacy file, or intent definition | Resource build phase and built bundle contents |
| Source icon looks correct but the installed icon is absent, stale, or uses the wrong variant | Canonical icon owner, competing catalogs or packages, generated resource membership, asset-name settings, compiled bundle contents, and installation proof |
| Scheme is absent locally or in CI | Shared-scheme ownership, generated scheme declaration, workspace selection, and CI checkout |
| Build succeeds but widget, watch app, app group, or deep link fails | Cross-product identity, signed entitlements, service-side registration, and runtime proof |
| Package resolves but APIs are unavailable or binary is absent | Product selection, consuming target exposure, linkage or embedding, and deployment target |
| Local and CI results differ | Exact project or workspace, scheme, configuration, destination, toolchain, environment, and generation step |
| Xcode reports no destination or a service crash | Separate scheme compatibility from simulator, device, or Xcode-service infrastructure before editing source |

Target membership mistakes often masquerade as code defects. Shared schemes are also a hidden contract behind local tests, CI, screenshots, and device installs; inspect them whenever targets or tests change.

## Completion Contract

Finish only when:

- the upstream owner contains the intended change;
- regenerated output is reproducible and reviewed;
- intended targets include the change and unintended targets do not;
- identifiers and capabilities remain coherent across products;
- one canonical shipping icon source is wired and its compiled product is inspected when icon work is in scope;
- dependency availability and exposure are proven where relevant;
- effective build settings, built resources, built `Info.plist`, and signed entitlements are inspected as applicable; and
- project failures are distinguished from signing, permission-semantic, runtime-device, and infrastructure failures.

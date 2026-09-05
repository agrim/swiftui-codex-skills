# Apple runtime and device validation: playbook

## Evidence ladder

| Evidence | Supports | Does not establish |
| --- | --- | --- |
| Source inspection | Structure and likely behavior | Compilation or runtime success |
| Build | Compiler/linker/resource acceptance for that context | Launch, rendering, or correct interaction |
| Unit/integration test | The exercised contract under the harness | Every UI, service, or hardware path |
| Installed bundle | Delivery of the identified product | Successful launch or complete startup |
| Launch and readiness | Process and required initialization | Correct layout or durable mutation |
| Screenshot | Visible state at one captured moment | Touch, accessibility, refresh, or persistence correctness |
| Interaction/lifecycle test | The exercised transitions | Unexercised devices and external services |
| Hardware/paired-device test | The observed real boundary | Universal reliability or production-scale service behavior |

Choose the weakest sufficient evidence for the actual claim, not the easiest evidence available. A source-only review can be complete as a review while runtime behavior remains unverified.

## Tool capability, not host dependency

Use available IDE, command-line, automation, or device tools. Inspect their current help and discovered state before use; no model-specific plugin or session API is required. Record the effective project, scheme, configuration, and destination even when a wrapper chooses them for you.

For shell workflows, inspect `xcodebuild -version`, discovered schemes/destinations, and the relevant `xcrun simctl` or `xcrun devicectl` help. Do not commit device identifiers or private logs. A missing Apple toolchain is a blocked validation gate, not a reason to invent a successful build.

## Scope and safety

A request to install an app does not imply wiping the old container. Preserve data unless reset/uninstall is explicitly authorized or is clearly part of an approved destructive test. Verify that the requested bundle is installed instead of inferring installation from build output.

Do not claim uninstall cleared keychain, cloud, HealthKit, or another system-managed store. Test that store independently when its state matters. Keep signing, certificate, provisioning, and account operations separate from ordinary runtime checks.

## Comparable rendering and interaction

Capture the target screen with deterministic data, appearance, content size, locale, orientation, and window size. Include the smallest risky layout and a representative larger/adaptive layout. Inspect the image; producing a screenshot file alone is not a visual review.

Exercise disabled/loading/error states, keyboard and focus, long text, accessibility navigation, and Reduce Motion where affected. For a press/drag/focus claim, perform the interaction rather than infer it from a static screenshot.

## Persistence and system surfaces

Extend startup proof through store readiness and the first meaningful operation when persistence is in scope. Confirm the result after termination/relaunch. Record when the simulator uses a different backend or account path from a device; those are separate proof lanes.

For widgets, validate target embedding, registration, data handoff, timeline/snapshot generation, host rendering, delayed refresh, and stale states. For watch/phone flows, test both surfaces and reconnect/delivery behavior. Hardware-dependent camera, microphone, sensors, protected-data, signing, and companion behavior may require real devices; state which boundary was actually tested.

## Failure classification

Preserve raw output until you can separate compiler errors, wrong settings, unsupported destinations, unavailable runtimes, CoreSimulator services, pairing, provisioning, installation, and app failures. Do not rewrite UI to “fix” a screenshot timeout without source evidence.

A failed or blocked gate is useful information. Record the minimum next verification step, without pretending work will happen later automatically. Clean temporary fixtures and re-run affected checks after the final source change. Never hand off an older green result as proof of a newer candidate.

## Sources

- [xcode](https://developer.apple.com/documentation/xcode) — Xcode documentation.
- [testing](https://developer.apple.com/xcode/swift-testing/) — Swift Testing.
- [ui-audit](https://developer.apple.com/documentation/xcuiautomation/xcuiaccessibilityauditissue) — XCUI accessibility audits.
- [distribution](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases) — Distributing your app.

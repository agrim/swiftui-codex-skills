---
name: apple-app-store-readiness
description: "App Store product and submission readiness for iOS, iPadOS, watchOS, tvOS, visionOS, and Mac App Store apps. Use when planning, auditing, preparing, validating, or submitting a first release or update; configuring App Store Connect; reviewing rejection risks; freezing a release candidate; aligning app identity, icons, metadata, screenshots, support and privacy pages; preparing TestFlight or App Review access; or deciding which domains, services, accounts, and features must be live for review. This skill owns store-facing completeness, reviewability, metadata-to-binary coherence, and submission-gate sequencing. Pair with apple-project-governance for source configuration, apple-privacy-system-integrations for privacy and account semantics, apple-device-validation for runtime proof, and macos-productization for macOS release artifacts."
---

# Apple App Store Readiness

## Establish The Release Contract

- Identify the requested mode: plan or audit, prepare, validate, upload, submit, or release. Do not infer authority to upload, submit, change account state, purchase services, or publish from a readiness request.
- Identify every platform and product in the submission: app, watch app, extensions, App Clips, in-app purchases, subscriptions, hosted content, and companion services.
- Freeze the smallest complete release promise before auditing polish. Separate what the candidate actually delivers from later features, dormant code, development controls, placeholders, and unavailable services.
- Inspect the live repository and available App Store Connect state. Recheck current official Apple requirements, supported toolchains, regional obligations, and review guidelines; do not rely on a remembered version-specific checklist.
- Read `references/app-store-readiness-patterns.md` for the gate matrix, identity and public-surface checks, reviewability scenarios, evidence ladder, and handoff contract.

## Apply The Gates In Order

1. **Promise:** Define the core journey, supported platforms and devices, required integrations, monetization, account model, and honest v1 exclusions.
2. **Identity:** Reconcile the App Store record, public app name, bundle ID, version and build, seller or developer presentation, icons, companion products, and public website.
3. **Public surfaces:** Require real support and privacy pages, reachable services, production-safe links, and only the domains or backend capabilities the shipped experience uses.
4. **Privacy and compliance:** Pair with `apple-privacy-system-integrations` for the actual data inventory, disclosures, permission purpose, retention, deletion, account deletion, SDK behavior, and privacy artifacts.
5. **Release candidate:** Freeze an intentional source state and inspect or, when the requested mode authorizes it, build the exact candidate with a currently accepted toolchain. Pair with `apple-project-governance` to prove effective identity, resources, capabilities, and archive contents.
6. **Runtime proof:** When authorized, use TestFlight or an equivalent installed-candidate path with `apple-device-validation` for the critical journey, denial and offline paths, real hardware, companion products, and every claim screenshots or review notes depend on.
7. **Storefront and review packet:** Make metadata, screenshots, previews, age rating, pricing, availability, compliance answers, review notes, credentials, sample data, and review instructions match the exact binary.
8. **Submission and release:** Upload, submit, respond to review, or release only when explicitly authorized; record the exact build and resulting App Store Connect state.

## Release Rules

- Prefer a smaller complete release over a broad candidate with unfinished, hidden, nonfunctional, or unreviewable features. Do not add accounts, a backend, Universal Links, subscriptions, or remote services merely because a domain or App Store record exists.
- Treat App Store name availability, domain ownership, trademark or legal clearance, and social-handle availability as separate questions. Do not present one as proof of another.
- Keep the public identity coherent without gratuitously renaming stable internal types, storage keys, or bundle identifiers.
- Treat development localhost services, placeholder credentials, parked domains, staging-only data, and operator controls as release blockers when the submitted journey depends on them.
- Require a live, reproducible review path. If login, hardware, external content, or a remote service is required, provide the access, sample, instructions, and service availability App Review needs.
- Keep App Store privacy details, purpose strings, entitlements, privacy manifests, and public privacy policy distinct. Audit each applicable layer with its owning skill.
- Require both a working public privacy-policy URL and durable in-app access to the same material policy. An onboarding sheet alone is not a public URL, and a first-run-only link is not permanently accessible; prepare both before an external TestFlight build that may be reviewed against the App Review Guidelines.
- Treat screenshots and metadata as claims about the binary. Do not advertise unavailable behavior, hide material requirements, or submit imagery from a different app state or build.
- Keep TestFlight readiness, upload processing, App Review approval, and public release as separate gates.

## Completion Contract

- Report each gate as passed, failed, not applicable, not authorized, or unverified.
- Name the exact version, build, platform set, source state, archive or uploaded build, and App Store Connect state inspected.
- Separate repository inspection, build and archive proof, upload processing, TestFlight proof, physical-device proof, submission, approval, and release.
- List every remaining blocker in release order and identify its owner: product scope, project configuration, privacy, runtime, public service, storefront metadata, account administration, or Apple review.

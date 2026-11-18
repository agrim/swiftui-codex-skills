---
name: apple-app-store-readiness
description: "Audit an App Store build, prepare storefront and reviewer materials, or perform an authorized TestFlight, submission, or release stage."
---

# App Store readiness

## Inputs

Identify the release stage, approval scope, product, storefronts, candidate, account and purchase flows, dependencies, and App Store Connect records.

## Rules

- **STORE-001 — Track each stage separately.** Separate preparation, upload, processing, TestFlight, submission, approval, and release. Honor existing authorization for its candidate and stage until changed or revoked.
- **STORE-002 — Check the release promise.** Match each advertised feature and screenshot to a reachable journey in the candidate.
- **STORE-003 — Check current requirements.** Use Apple’s requirements for the current toolchain, region, data use, business model, and stage.
- **STORE-004 — Rehearse reviewer access.** Follow the review instructions with working services, links, sample data, and reviewer access. Keep credentials private.
- **STORE-005 — Identify the build.** Tie source, platforms, archive, version/build, upload receipt, and tests to one candidate.

## Workflow

1. Compare disclosures, account behavior, monetization, and metadata with the binary.
2. Prepare reviewer access and reproduce the core journey.
3. Check live state before acting. Record an existing receipt for this build, or perform the authorized stage once its prerequisites pass.

## Verify

- STORE-002: Test first launch, denied permissions, offline behavior, and applicable purchases or deletion against the storefront claim.
- STORE-004: Reach the privacy policy, support links, and advertised features using reviewer access.
- STORE-001, STORE-005: Confirm each completed external stage in App Store Connect against the selected build.

## Output

Report candidate, service evidence, and blockers in gate order. Mark each gate passed, failed, not applicable, not authorized, or unverified.

## References

- [Candidate and storefront checks](references/app-store-readiness-patterns.md)
- [Reviewer handoff and release ledger](references/review-and-release-ledger.md)

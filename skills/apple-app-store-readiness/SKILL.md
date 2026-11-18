---
name: apple-app-store-readiness
description: "Audit App Store candidates and reviewer materials, or perform an authorized TestFlight, submission, or release stage."
---

# App Store readiness

## Inputs

Identify the candidate, storefronts, requested stage, existing approval and service state.

## Rules

- **STORE-001 — Bound the action.** Reuse approval for its candidate and stage. Upload, beta distribution, submission and release are separate actions.
- **STORE-002 — Test the promise.** Trace each advertised feature and screenshot to a reachable journey.
- **STORE-003 — Check current policy.** Apply Apple’s requirements for this region, toolchain, business model and data use.
- **STORE-004 — Rehearse review.** Follow reviewer instructions against live services. Keep credentials private.
- **STORE-005 — Bind evidence.** Match revision, archive, version/build, tests and service receipts.

## Workflow

1. Reconcile disclosures, account flows and purchases with the candidate.
2. Check the selected build’s live status before performing any outstanding authorized stage.

## Verify

- STORE-002, STORE-004: From first launch, reach advertised features, support and privacy links. Exercise applicable offline, denied-permission, purchase and deletion paths against storefront claims.
- STORE-001, STORE-005: Confirm the resulting stage against this build in App Store Connect.
- STORE-003: For account creation, check the deletion flow against Apple’s current requirements for this app.

## Output

List each gate in order with evidence or blocker. Distinguish failed, unverified, unauthorized and inapplicable gates.

## References

- [Candidate and storefront checks](references/app-store-readiness-patterns.md)
- [Reviewer and release ledger](references/review-and-release-ledger.md)

# App Store readiness: playbook

## Gate order

| Gate | Required decision/evidence | Frequent failure |
| --- | --- | --- |
| Promise | Complete primary journey and honest exclusions | Future features advertised as shipped |
| Identity | Product, bundle, seller, version/build, companions | Storefront and binary disagree |
| Public surfaces | Real support/privacy links and required services | Parked domains, staging-only data, broken links |
| Privacy/account | Actual inventory, disclosures, permissions, deletion | Policy wording disconnected from behavior |
| Candidate | Intentional source and exact archive/build | Testing one binary and uploading another |
| Runtime | Critical journeys, denial/offline and device gates | Treating compile success as product readiness |
| Review packet | Access, sample data, accurate screenshots and notes | Reviewer cannot reach the core feature |
| External stages | Explicit authority and resulting service state | Calling an upload an approval or release |

Do not add accounts, subscriptions, a backend, or universal links merely because a store record or domain exists. Prefer a smaller complete experience over nonfunctional breadth.

## Current-policy review

Open the current App Review Guidelines and relevant App Store Connect help for the actual product. Recheck accepted toolchains and submission requirements at release time. Region, business model, audience, data categories, external content, and account creation can change applicable obligations.

This library provides an engineering review process, not a legal opinion or a guarantee of approval. Record which official guidance was checked and when. Do not infer trademark clearance, domain ownership, or name availability from one another.

## Truthful privacy and account behavior

Pair with the privacy skill to reconcile local processing, transfers, SDK behavior, retention, tracking/linking, permissions, and public disclosures. A purpose string, manifest, and store privacy questionnaire are different artifacts.

Keep the privacy policy reachable from the store metadata and in the app, not solely in a first-run screen. For products where account deletion is required, verify a real deletion initiation path and truthful completion/retention explanation. A logout or temporary deactivation is not automatically deletion.

## Candidate integrity

Record commit/worktree state, version/build, archive identity, export configuration, target products, and uploaded build selection. Inspect built resources, entitlements, icons, privacy artifacts, and production configuration. Ensure development controls, placeholder credentials, and staging-only dependencies do not invalidate the promised experience.

Test release-like behavior where signing, optimization, app groups, protected data, or production services differ from debug. Preserve exact-candidate evidence rather than relying on an older screenshot or unrelated simulator build.

## Reviewability and storefront

Prepare working reviewer access and clear instructions for hardware, login, external services, purchases, or non-obvious workflows. Supply sample data when required to demonstrate the feature. Avoid disclosing private production-user information or committing reviewer credentials in the repository.

Screenshots and preview text are claims. Use the actual supported experience and identify prerequisites honestly. Keep age rating, pricing, availability, purchases, support material, and privacy answers coherent with the binary. Do not hide incomplete or nonfunctional features behind misleading metadata.

## External actions and handoff

A readiness audit does not authorize upload, submission, account administration, paid services, or public release. For an authorized action, record the actual resulting service state and selected build. Processing, TestFlight availability, review submission, approval, and public availability are separate facts.

Return blockers ordered by the next gate, with an owner category such as product scope, project configuration, privacy, runtime, service, metadata, account administration, or review. An unverified gate remains unverified even when the repository looks ready.

## Reconcile a release ledger

Use one current gate table: claim, candidate/environment, latest evidence, verdict, authorization scope, and next action. Keep older receipts as history with an explicit superseded-by reference. Sort by the actual dependency, not by the order notes were written. When records conflict, inspect current source or service state; the newest prose is not automatically the strongest evidence.

For example, an earlier note says upload is unauthorized and processing unverified. A later user approval permits uploading build 12 to internal testing, and the service now reports that exact build processed. Resolve those two old blockers; do not ask for the same upload permission or upload it again. External invitations remain outside that approval. If the approved build is still absent, execute the approved upload after candidate checks instead of treating a past blocked note as a veto.

This ledger is an engineering workflow, not an Apple requirement. Record authority separately from capability: credentials, an unlocked device, or service availability can still block an authorized operation. Progress on independent preparation while the specific prerequisite is unavailable.

## Sources

- [review](https://developer.apple.com/app-store/review/guidelines/) — App Review Guidelines.
- [distribution](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases) — Distributing your app.
- [privacy](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests) — Describing data use in privacy manifests.
- [sdk-privacy](https://developer.apple.com/support/third-party-SDK-requirements/) — Third-party SDK requirements.
- [account-deletion](https://developer.apple.com/support/offering-account-deletion-in-your-app/) — Offering account deletion in your app.

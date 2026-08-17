# App Store Readiness Operational Playbook

Use this playbook to turn a repository, App Store record, and release intention into an evidence-backed submission. Requirements and accepted toolchains change; verify the current official Apple documentation before applying a time-sensitive rule.

## Match Actions To Authority

| Mode | Allowed default work | Do not infer authority for |
| --- | --- | --- |
| Plan or audit | Inspect repository state, existing artifacts, public URLs, supplied App Store Connect state, and current official requirements | Editing, account changes, purchases, uploads, submissions, publication, or release |
| Prepare | Make requested repository and public-surface changes; build and archive when ordinary verification requires them | Account-level declarations, credential use, upload, submission, pricing changes, or release |
| Validate | Exercise the named candidate through archive, TestFlight, devices, links, and review scenarios already authorized | Replacing the candidate, changing product scope, submitting, or releasing |
| Upload or submit | Perform only the named App Store Connect action for the exact authorized build and retain the resulting status | Automatic public release, unrelated account changes, or a different platform or build |
| Release | Apply the explicitly selected release method to the approved version | Unrequested phased release, pricing, availability, update, or takedown actions |

An instruction to “get ready for the App Store” is not authority to upload or submit. An instruction to submit is not automatically authority to release immediately after approval.

## Readiness Gate Matrix

| Gate | Questions to answer | Minimum evidence | Primary owner or pairing |
| --- | --- | --- | --- |
| Product promise | What exact journey, platform set, account model, monetization, integrations, and exclusions does this version promise? | Repository-grounded release scope with unfinished or later features identified | This skill; pair with UI or product work when the journey itself changes |
| Public identity | Do App Store record, app display name, bundle ID, icons, companion products, website, and version/build tell one story? | App record information plus effective built-product inspection | This skill with `apple-project-governance` |
| Public surfaces | Are support, privacy, links, email or contact, and required services reachable and truthful? | Live HTTPS checks and end-to-end link or service proof | This skill; pair with web or service tooling for implementation |
| Privacy and accounts | Do actual data handling, permissions, disclosures, policies, retention, and deletion agree? | Completed data-flow inventory and applicable artifact proof | `apple-privacy-system-integrations` |
| Binary candidate | Is there one intentional release state built with a currently accepted toolchain and coherent archive contents? | Exact archive, version/build, effective settings, bundled resources, and upload-eligibility checks | `apple-project-governance`; `macos-productization` for Mac artifacts |
| Runtime quality | Does the critical journey work on supported devices across fresh, denied, offline, interruption, and companion states? | TestFlight or equivalent installed-candidate evidence at the necessary proof level | `apple-device-validation` |
| Storefront metadata | Do descriptions, screenshots, previews, categories, ratings, pricing, availability, and compliance answers match the candidate? | Completed metadata review against the exact binary | This skill |
| Review access | Can App Review reach every material feature without guessing or using private developer state? | Working credentials or demo mode, live services, sample inputs, and precise review notes | This skill with runtime and service owners |
| Submission state | Was the intended build uploaded, processed, selected, submitted, approved, and released as authorized? | Recorded App Store Connect status for the exact version and build | This skill |

Do not collapse the matrix into “submission-ready” when any required gate remains unknown. Mark a row not applicable only after inspecting why it does not apply.

## Freeze The Release Promise

Write the candidate promise before chasing a generic rejection checklist:

- one sentence describing the core user value;
- the complete first-run-to-value journey;
- supported platforms, devices, orientations, and companion requirements;
- whether accounts, payments, subscriptions, user-generated content, protected data, remote services, or hardware are required or optional;
- behavior when permission is denied, the network is unavailable, a companion device is absent, or the account is signed out;
- features intentionally excluded from the submitted experience, plus proof that no retained control, link, remote flag, metadata claim, or development surface can expose unfinished or unreviewed behavior; and
- the exact public claims the screenshots and metadata will make.

Prefer removing or honestly gating an unfinished feature over leaving a dead control, placeholder, development panel, or unreachable workflow in the candidate. A broad codebase is not a broad release promise unless users and App Review can access the behavior.

## Identity And Record Coherence

| Identity surface | Audit | Important distinction |
| --- | --- | --- |
| App name | App Store record, installed display name, companion display names, permission copy, system metadata, support and privacy pages | App Store availability is not trademark, company-name, domain, or handle clearance |
| Bundle ID | App Store record, effective product identifier, extensions and companion relationships | Verify before the first uploaded build or another lock point described by current App Store Connect guidance |
| Version and build | Source owner, archive, uploaded build, TestFlight installation, review selection, release notes | Every upload needs a unique build identity; metadata must describe the selected build |
| Seller or developer presentation | Membership type, legal or trade-name options, regional contact obligations | This is account-level identity, not the same as the app’s display name |
| App icon | Canonical source asset, target wiring, compiled variants, marketing icon, installed appearance | A correct source design does not prove the built product contains or renders it |
| Website and domains | Canonical product URL, redirects, support and privacy paths, association files | Owning a domain does not require accounts, a backend, or Universal Links |

Preserve stable internal identifiers when they are not user-facing and changing them would risk migration or service breakage. Coherence means one public story, not a cosmetic rename of every symbol.

## App Icon Production Contract

Treat concept exploration, editable production artwork, project wiring, compiled assets, and installed presentation as different gates.

1. **Explore concepts separately.** Compare silhouette, distinctiveness, product meaning, small-size recognition, and undesirable visual or brand associations before promoting a direction into project assets.
2. **Build editable source.** Use clean independent vector or high-quality source layers on a shared canvas when the current Apple icon pipeline supports them. Keep geometry crisp and avoid baking material, refraction, specular, shadow, or appearance effects into layers that the shipping tool is expected to own.
3. **Inspect the current toolchain.** Confirm the installed Icon Composer or asset-catalog workflow, supported appearance variants, target platforms, and current Apple guidance. Do not hard-code beta-specific behavior or assume a flattened concept image is a production icon.
4. **Choose one canonical shipping source.** Store the editable `.icon` package or asset catalog in the source-owned location wired by the project. Keep exploratory checkpoints outside the shipping resource graph and remove a legacy source only after replacement is proven.
5. **Review supported variants.** Inspect light, dark, tinted, monochrome, alternate-generation, or other variants that the selected platforms and current pipeline actually use, including representative small sizes.
6. **Prove each downstream gate.** Use `apple-project-governance` for resource ownership and compiled-bundle presence, then `apple-device-validation` for installed Home Screen, launcher, Dock, or other host-surface rendering. A Composer preview, correct source file, or green build does not prove installed presentation.

If the user edits an exploratory checkpoint after integration, reconcile the intended changes into the canonical shipping source rather than silently shipping whichever similarly named file was modified last.

## Public Domain And Service Contract

Assign every public surface a real purpose:

| Surface | Required when | Proof |
| --- | --- | --- |
| Canonical product domain | The release uses a website or public policy and support surfaces | HTTPS loads reliably; canonical links and redirects preserve intended paths |
| Support page | Required by current store metadata or the release contract | Contains genuine contact and useful support information, not a parked or placeholder page |
| Privacy policy | Required by current platform or data practices | Public policy matches the real app, services, SDKs, retention, and deletion behavior |
| Universal Links or associated domains | The shipped experience opens public links or shares credentials or activities through that association | Matching entitlement and association file, valid HTTPS without prohibited redirects, installed-app link proof |
| Authentication callbacks | The shipped account flow uses web authentication | Production callback and domain association work for review accounts and do not use localhost |
| Remote API or backend | A submitted feature depends on server state or multi-user coordination | Production-safe endpoint, authorization, retention and deletion, failure behavior, and review uptime |
| Public booking, sharing, or content link | The release advertises a guest or cross-user journey | End-to-end result works outside the developer environment and communicates provisional versus final state honestly |

Use one canonical domain and treat defensive aliases as redirects when that matches the product. Do not add a backend merely to make the release look substantial. Conversely, do not describe a single-user local relay, development cloud environment, placeholder token, or localhost endpoint as production infrastructure.

## Reviewability Scenarios

| Candidate characteristic | Make reviewable by | Common incomplete state |
| --- | --- | --- |
| No account | Let the core journey start without fabricated sign-in requirements | Adding account creation only because a domain exists |
| Required login | Provide a stable demo account or complete demo mode and explain any special setup | Expiring credentials, MFA dead ends, empty accounts, or production access unavailable to review |
| Optional protected permission | Explain why and when it is requested; prove denial leaves unrelated value intact | Review is blocked at launch or purpose text does not match requested scope |
| Required hardware or companion | Give exact instructions and sample inputs; prove every portion Apple can reasonably exercise | Assuming a phone-only screenshot proves watch, accessory, sensor, or camera behavior |
| Remote service | Keep the review environment live and provide deterministic sample state | Staging endpoint, localhost, parked domain, placeholder credential, or empty service |
| User-created account | Provide an easy in-app account-deletion initiation and reconcile retained data with policy | Deactivation only, support-email-only deletion, or unmentioned retained copies |
| Purchase or subscription | Make products reviewable, explain non-obvious behavior, and keep restore and entitlement state coherent | Missing products, developer-only pricing state, inaccessible paywall path, or metadata mismatch |
| User-generated or externally supplied content | Audit moderation, reporting, rights, age-rating, privacy, and service availability against current guidelines | Hidden content paths or unreviewable server-side behavior |

Review notes should explain non-obvious prerequisites, optional permissions, demo state, hardware boundaries, external links, and the shortest path to each material feature. They should not excuse incomplete functionality.

## Storefront And Compliance Applicability Matrix

Audit every row against current App Store Connect fields, official Apple guidance, the selected territories, and the exact candidate. Requirements and terminology change; do not turn this matrix into a remembered legal or policy answer.

| Area | Audit question | Evidence or routing |
| --- | --- | --- |
| Shared app information | Are app name, subtitle, bundle ID, SKU or record identity, privacy-policy URL, and categories complete and coherent? | App Store Connect record plus built identity; route project mismatches to `apple-project-governance` |
| Platform-version metadata | Are description, keywords, support URL, marketing URL when used, version, copyright, and platform-specific fields complete? | Review each localization and platform record against the selected build |
| Screenshots and previews | Do required device families and localizations show real candidate behavior without misleading status, data, hardware, or features? | Capture coherent states from the candidate; use `apple-device-validation` for runtime proof |
| Age rating | Do content, communication, web access, health or wellness, gambling-like mechanics, user-generated content, and other applicable descriptors support the selected rating? | Current questionnaire answers plus repository and service inspection |
| Content rights and third-party services | Does the developer own or license submitted content, names, media, APIs, and service access under applicable terms? | Rights inventory and current service terms; escalate legal uncertainty rather than invent clearance |
| App privacy | Do privacy policy and App Store privacy answers match collection, linking, tracking, third parties, and on-device versus off-device behavior? | `apple-privacy-system-integrations` data-flow and disclosure audit |
| Export compliance | Does the candidate use, contain, or qualify for exemptions under the current encryption questions and documentation requirements? | Current Apple workflow and project or archive evidence; do not guess from a networking import alone |
| Regulated, medical, or specialized declarations | Does the app make health, medical, financial, children’s, location, or other regulated claims that create extra declarations or evidence? | Product claims, data paths, current Apple fields, and qualified legal or domain review when needed |
| Regional trader and contact obligations | Do selected territories require trader status, contact publication, licenses, registrations, or other regional information? | Current App Store Connect account state and official regional guidance |
| Pricing and availability | Are price, territories, tax or agreement prerequisites, pre-order state, and platform availability deliberate? | Account agreements plus App Store Connect configuration |
| In-app purchases and subscriptions | Are products submitted or approved as required, reviewable in the candidate, described accurately, restorable where applicable, and coherent with account deletion and entitlement state? | Store configuration, review path, sandbox or TestFlight evidence, and current review guidance |
| Release method | Is manual, automatic, phased, scheduled, or another current release option intentionally selected for this version? | Explicit user decision and recorded App Store Connect state |
| App Review information | Are contact details, notes, credentials, demo access, sample links or codes, and hardware or permission instructions complete and durable? | Execute the review path from a clean candidate state |

Mark a row not applicable with a reason. A missing field is not always a code defect, and the existence of a code path does not always make a storefront declaration applicable.

## Exact Candidate Evidence Ladder

1. **Repository state:** Identify the intended source commit or intentionally described working state and generated-project status.
2. **Project effect:** Prove effective bundle identities, deployment targets, versions, resources, icons, purpose strings, privacy manifests, capabilities, and companion embedding.
3. **Archive:** Inspect the exact release archive and export or validation result for every product it contains.
4. **Upload processing:** Confirm Apple accepted and processed the exact version and build; resolve warnings rather than assuming archive success is enough.
5. **TestFlight:** Install the processed build and exercise the critical path, permission states, offline behavior, lifecycle, migration, accessibility, and companion behavior that apply.
6. **Storefront proof:** Capture screenshots and previews from coherent states represented by the candidate and verify metadata against them.
7. **Review submission:** Select the exact build, provide complete review information, submit, and retain the resulting status when authorized.
8. **Release:** Record approval and apply the authorized release method; approval is not proof that public release occurred.

Use `apple-device-validation` for runtime levels and `apple-project-governance` for source-to-artifact levels. For a Mac App Store submission, also use `macos-productization` for the macOS archive, signing, sandbox, embedded-code, and export gates.

## Completion Handoff

Report:

- release promise and platform set;
- public identity and canonical domain decisions;
- exact version, build, source state, archive, and uploaded build inspected;
- each matrix gate as passed, failed, not applicable, not authorized, or unverified;
- current App Store Connect state and every external action taken;
- blockers in the order they prevent submission or release;
- the owner of each blocker; and
- every current-policy claim that still needs verification against official Apple documentation.

Do not claim “App Store ready” from a successful local build, an unsigned archive, an App Store record, a reserved name, a TestFlight upload, or a polished screenshot alone.

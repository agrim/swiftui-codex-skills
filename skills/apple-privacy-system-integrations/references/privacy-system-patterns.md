# Privacy And System Integration Operational Playbook

Use this reference for frameworks that access protected data, request permission, expose data beyond the app's primary interface, or depend on service, account, extension, or companion-device state.

## Contents

- [Integration Contract](#integration-contract)
- [Artifact Applicability Matrix](#artifact-applicability-matrix)
- [Boundary Matrix](#boundary-matrix)
- [Typed State Model](#typed-state-model)
- [Supplementary Versus Essential Behavior](#supplementary-versus-essential-behavior)
- [System Action Surface Contract](#system-action-surface-contract)
- [Truthful Projection Playbook](#truthful-projection-playbook)
- [Completion Contract](#completion-contract)

## Integration Contract

Answer these questions before implementation:

| Decision | Required articulation |
|---|---|
| User value | Explain what the integration enables in the user's language, not only the framework name |
| Data | Name exact categories, fields, precision, direction, and source of truth |
| Boundary | Identify every local store, server, cloud container, system store, index, widget, intent, activity, extension, and companion destination |
| Role | Classify the integration as supplementary or essential to the affected experience |
| Permission | Define requested scopes, request timing, system states, and recovery path |
| Purpose | Connect each access path to a visible and truthful user purpose |
| Retention and deletion | State where each representation persists, how long, who can delete it, and what revocation or account change does |
| Projection | Define the truthful subset and mapping accepted by the destination framework |
| Failure and retry | Separate user decisions, permanent unavailability, transient service failure, deduplication, and idempotency |

A framework import proves none of this contract. Complete the contract before treating an integration as complete.

Before approving public privacy copy, apply the same inventory to infrastructure ownership. Apple-hosted or vendor-hosted storage can still be an app-controlled data boundary when the app chooses the records, fields, retention, or access path. Do not turn “no developer-operated server” into “we store no data.” Prefer a bounded claim such as naming the exact data that stays on-device, is never uploaded, or is minimized for one disclosed workflow.

## Artifact Applicability Matrix

Audit every row. Change a row only when its condition applies, and record a concise not-applicable reason in the review or handoff when the omission could otherwise look accidental.
Recheck privacy-manifest and App Store disclosure applicability against current official Apple documentation instead of relying on remembered policy.

| Layer | Audit question | Update when |
|---|---|---|
| Framework code and typed state | Does the implementation request only required scope and represent real outcomes? | Access, mapping, permission, failure, or transport behavior changes |
| Identity provenance | Does the framework actually expose the stable identity being used, or is the app guessing from labels, titles, participants, or account-adjacent metadata? | Identity capture, inference, account linking, or profile-field ownership changes |
| User-facing explanation | Can the user understand the purpose, consequence, and fallback before access? | A new access path, materially different use, or different degraded behavior appears |
| `Info.plist` purpose strings | Does an Apple-protected resource require a system prompt, and does the intended target contain accurate purpose text? | A protected access path or its user-facing purpose changes |
| Entitlements and capabilities | Does the executable need authorization for the service or data class? | The integration or target requires a capability; use project governance to prove the built entitlement |
| `PrivacyInfo.xcprivacy` | Does current Apple policy require declarations for collected data, tracking domains, or required-reason API use, including relevant SDK behavior? | Actual data collection, tracking, required-reason API use, SDK composition, or applicable policy changes |
| App Store privacy details | Do current App Store Connect answers match actual collection, purpose, linking, tracking, and third-party practices across supported platforms? | On-device versus off-device behavior, retention, data use, linking, tracking, or partner behavior changes |
| Storage, retention, and deletion | Where do local, cloud, system, index, cache, and companion copies live and disappear? | A representation, destination, lifetime, account relationship, or deletion path changes |
| Settings and onboarding | Can users understand status, recover from denial, and distinguish unavailable from failed? | Request timing, state, scope, or recovery changes |
| Boundary projections | Does each widget, intent, activity, index, extension, cloud record, export, or companion payload expose only its stated subset? | A surface, field, audience, refresh policy, or destination changes |
| Tests | Which mapping, state transition, fallback, retry, and deletion claims can be automated? | Any contract row changes |

Do not manufacture no-op entitlement, purpose-string, privacy-manifest, or disclosure edits merely to make the change look complete. These are separate artifacts with separate applicability rules.

## Boundary Matrix

| Path | Treat it as | Primary risk to check |
|---|---|---|
| Local persistence | Canonical or cached app state | Retention, local protection, account separation, and deletion |
| Cloud sync | Replication between stores with conflict and account semantics | Account mismatch, deletion propagation, conflict resolution, and false local-success assumptions |
| System-store export | A mapped copy owned under another framework's semantics | Unsupported fields, duplicate writes, authorization, provenance, and truthful representation |
| Widget or live activity | A glanceable projection outside the primary app UI | Lock-screen or bystander exposure, stale content, and overbroad fields |
| App Intent or shortcut | A callable action or query exposed to system surfaces | Authentication assumptions, parameter sensitivity, result disclosure, and side effects |
| Spotlight or other index | A discoverable copy managed by a system service | Search visibility, stale entries, account changes, and deletion |
| Watch or companion transfer | A message or replicated state crossing device and process boundaries | Reachability, ordering, account identity, retries, deduplication, and counterpart absence |

Never use “sync” as a generic label for all rows. Local save, cloud sync, system export, indexing, projection, and device transfer make different promises.

Treat provider display names, system-source titles, and protected-record fields as data with their documented semantics, not as an identity API. If a workflow needs a name or address that the framework does not explicitly and stably provide, collect it at that workflow and do not overwrite a previously saved value merely because an earlier setup field was removed.

## Typed State Model

Represent the states the framework and product can distinguish. Do not collapse them into one availability boolean.

| State | Required behavior |
|---|---|
| First run or not determined | Explain value in context; request only after a meaningful user action; avoid silent launch-time prompts |
| Requesting | Prevent duplicate requests and keep the UI honest while the system owns the prompt |
| Granted | Use only approved scopes and surface current integration status |
| Denied | Preserve unaffected value, avoid automatic re-prompts, and provide a truthful settings or alternative path when useful |
| Restricted or unavailable | Explain that the capability cannot currently be used; distinguish device, framework, policy, or service limits when known |
| Revoked | Stop protected work, reconcile cached or projected state according to policy, and offer user-controlled recovery |
| Account mismatch or signed-out | Prevent cross-account mixing and define whether data waits, detaches, migrates, or is removed |
| Companion device absent or unreachable | Degrade honestly; queue only when the product contract defines durable delivery semantics |
| Transient failure or retry pending | Preserve enough operation state to retry safely, bound automatic retries as appropriate, and make duplicate work idempotent |

Permission denial and account or device unavailability are routine states, not exceptional surprises. Never use a transport retry to override a user-controlled permission decision.

## Supplementary Versus Essential Behavior

| Role | Default behavior |
|---|---|
| Supplementary integration | Keep the app's core value local and useful; use best-effort integration; show status without blocking unrelated work |
| Essential integration for one feature | Gate only that feature; explain why access is necessary; preserve navigation, account control, deletion, and unrelated value |
| Essential integration for the product contract | Explain the requirement before access; provide an honest unavailable or denied state; do not simulate success or invent fallback data |

“Local-first” and “best effort” are defaults for supplementary capabilities, not excuses to conceal an essential dependency or silently weaken a promised workflow.

## System Action Surface Contract

When the same product operation can begin in app UI, Siri, App Intents, Shortcuts, Spotlight, a model-assisted composer, or another system surface, keep interpretation and execution separate.

| Layer | Owns | Must not own independently |
| --- | --- | --- |
| UI or system adapter | Input capture, parameter resolution, surface-appropriate clarification, and result presentation | A duplicate persistence, authorization, retry, or audit implementation |
| Language or model interpretation | Producing a typed proposed command plus uncertainty or missing parameters | Direct mutation, invented identifiers, hidden permission escalation, or silent confirmation bypass |
| Typed command boundary | Validation, actor and account context, authorization, confirmation tier, idempotency, execution, persistence, retry, and audit | Surface-specific visual state or unbounded free-form intent |
| Repository or service | Canonical data mutation and truthful external projection | Deciding what a Siri phrase or UI sentence meant |
| Donation, indexing, or result projection | Minimal discoverable metadata and safe result disclosure | Broad copies of private canonical state or a second source of truth |

Apply these rules:

1. Project existing domain entities into the closest truthful App Entity or App Schema semantic. Do not maintain parallel Siri-only identities when canonical identifiers can be reused safely.
2. Prefer specific actions with typed parameters. Retain a generic app-specific action only for semantics that do not fit a supported specific operation, and keep its command vocabulary bounded.
3. Resolve ambiguous references before execution. A model may rank or propose; deterministic validation must reject invented, stale, cross-account, or unauthorized targets.
4. Apply the same confirmation, authentication, deletion, sharing, payment, and protected-data policy regardless of the initiating surface.
5. Keep retries idempotent and return truthful partial, denied, unavailable, and failed results. Do not report a successful spoken or shortcut action until the canonical command completed.
6. Minimize donated, indexed, spoken, lock-screen, and result data. Consider bystanders and device lock state separately from in-app visibility.
7. Test compiled metadata, entity resolution, command semantics and persistence, and real system routing as separate evidence levels. Pair with `apple-device-validation` for Siri, provider choice, hardware, account, or physical-device proof.

Remove obsolete catch-all intents only after the specific replacements cover their supported semantics and compiled metadata plus command behavior are both proven.

## Truthful Projection Playbook

1. Name the app's canonical record and destination representation.
2. Map only fields whose meanings match. Keep app-only details local when the destination has no truthful representation.
3. Preserve stable provenance or identifiers where the framework allows it so retries do not create duplicate exports.
4. Treat missing data as missing. Do not fabricate timestamps, quantities, categories, completion, consent, or success to satisfy an API shape.
5. Define whether destination edits flow back, are ignored, or create a conflict; export is not automatically bidirectional sync.
6. Apply retention, revocation, account-change, and deletion rules to every persisted or projected copy.
7. Test both a representative successful mapping and lossy, absent, denied, unavailable, duplicate, and retry cases.

## Completion Contract

Finish only when:

- each boundary and destination is inventoried;
- the permission and integration state model covers relevant first-run, granted, denied, unavailable, revoked, account, device, and retry paths;
- every artifact layer was audited and only applicable layers changed;
- source data maps truthfully without invented system data;
- local save, sync, export, indexing, projection, and companion transfer remain distinct;
- retention, deletion, account change, and revocation behavior are explicit;
- user-facing purpose and fallback match actual behavior; and
- focused tests and applicable built-artifact or runtime proof support the claims.

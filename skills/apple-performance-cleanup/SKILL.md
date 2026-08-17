---
name: apple-performance-cleanup
description: "Behavior-preserving cleanup and optimization of explicitly performance-sensitive Swift, SwiftUI, and Apple app code. Use when implementing or reviewing a constrained change to a hot or startup path, telemetry, parsing, persistence, rendering or invalidation, allocation or memory behavior, concurrency, a confirmed leak, or an explicitly requested whole-codebase compaction whose contract forbids stability or performance regression. Do not use for generic refactoring without a performance, memory, or explicit non-regression constraint. When hotspot discovery, trace capture, or leak diagnosis is primary, pair with a specialized performance-audit, profiling, or memgraph skill before applying cleanup."
---

# Apple Performance Cleanup

## Establish the Contract

- Confirm the path is explicitly performance- or memory-sensitive and whether the request is to review, diagnose, or change it. Do not turn an ordinary refactor into a performance project or implement a fix during a review-only request.
- Define the observable behavior contract, suspected cost, current tests, representative edge cases, and evidence needed before editing.
- Read the implementation, call sites, source formats, measurements, and debug behavior before introducing helpers. Keep cleanup narrower than a rewrite.
- Read `references/performance-cleanup-patterns.md` for the risk-to-evidence matrix, proof requirements, state semantics, and path-specific checks.
- If diagnosis is primary, pair with an available SwiftUI performance-audit, ETTrace, or memgraph workflow. Use this skill for the subsequent behavior-preserving change.

## Whole-Codebase Compaction

- Use a whole-repository protocol only when the user explicitly requests broad compaction or minimization with behavior, stability, or performance preservation. Do not expand a local cleanup into a repo-wide campaign.
- Establish a reproducible baseline before editing: intentional source state, tests, compatibility fixtures, generated-project state, release or reference artifact when useful, and comparable performance evidence. Create a commit or tag only when authorized.
- Audit the whole codebase before choosing edits. Produce a prioritized pass report that groups candidates by duplicated behavior, obsolete compatibility, generated or dead code, test redundancy, state-model duplication, and performance risk rather than walking files opportunistically.
- Execute coherent, reviewable batches from the full-pass report. Re-run the whole-repo scan after each pass so later decisions use the simplified state.
- Track production code, tests, artifacts, behavior, and runtime evidence separately. Never delete unique test scenarios, diagnostics, compatibility paths, or readable domain boundaries merely to improve a line-count metric.
- Stop when remaining reductions would weaken semantics, compatibility, observability, reviewability, or measured runtime behavior. Document the stop rule instead of forcing a target percentage.

## Change Discipline

- Preserve behavior first and improve structure second. Change code for speed only when the gain is measured or when less work follows directly from control or data flow; distinguish measured runtime proof from structural inference and do not invent a runtime number.
- Prefer tiny helper extraction, duplicated-branch removal, and source-contract tests over architecture churn.
- Treat allocations, main-thread work, logging, synchronization, persistence, and view invalidation in a hot path as costs that require justification and evidence, not as blanket prohibitions.
- Preserve distinctions among nil, zero, missing, unavailable, stale, denied, and failed states, including their fallback, caching, logging, and UI behavior.
- Avoid broad SwiftUI invalidation. Move derived values, formatting, timers, and expensive work out of `body` recomputation when evidence shows they are repeated unnecessarily.
- Treat concurrency fixes as ownership fixes, not warning suppression.
- If the user says stop, stop immediately and report what was verified versus what remains.

## Prove the Result

- Produce behavior proof and performance proof separately; one does not substitute for the other.
- Run focused tests around the exact parsing, timing, state, rendering, persistence, or concurrency contract and compare representative edge cases before and after.
- Measure launch, runtime speed, memory, leaks, or UI responsiveness under comparable conditions. If measurement is unavailable or inconclusive, say so and limit the claim.
- Pair with `$apple-device-validation` when simulator, physical-device, watch, screenshot, or runtime proof is required.
- Keep each cleanup change small enough to review and isolate it when the user asks for commits.

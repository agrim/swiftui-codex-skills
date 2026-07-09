---
name: apple-performance-cleanup
description: Behavior-preserving performance cleanup for Swift, SwiftUI, and Apple app code. Use when simplifying hot paths, startup paths, telemetry, parsing, persistence, rendering, memory behavior, concurrency, leaks, or broad code that must not regress app performance or behavior.
---

# Apple Performance Cleanup

## First Pass

- Identify the hot path, behavior contract, current tests, and measurable risk before refactoring.
- Read the current implementation and call sites before introducing helpers. Do not convert cleanup into a broad rewrite.
- Read `references/performance-cleanup-patterns.md` for startup, parsing, telemetry, rendering, persistence, concurrency, or memory-sensitive work.
- Prefer tiny helper extraction, duplicated-branch removal, and source-contract tests over architecture churn.

## Rules

- Preserve behavior first, improve structure second, improve speed only when measured or clearly implied by less work.
- Do not add allocations, main-thread work, logging, synchronization, persistence, or view invalidation inside a hot path without proof.
- Keep optional/missing data semantics intact. Cleanup often breaks edge cases by flattening nil, zero, unavailable, stale, and failed states.
- Avoid broad SwiftUI invalidation. Move derived values, formatting, timers, and expensive work out of body recomputation when needed.
- Treat concurrency fixes as ownership fixes, not warning suppression.
- If the user says stop, stop immediately and report what was verified versus what remains.

## Validation

- Run focused unit tests around the exact parsing, timing, state, or rendering contract.
- Use profiling tools when the risk is runtime speed, launch, memory, or UI responsiveness.
- Compare before/after behavior for representative edge cases.
- Keep performance cleanup commits small enough to review.

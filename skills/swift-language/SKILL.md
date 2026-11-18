---
name: swift-language
description: "Review Swift API design, value semantics, dependency injection, error handling, formatting, and compiler or language-mode migrations."
---

# Swift API design and dependency boundaries

## Inputs

Inspect callers, serialized formats, supported toolchains, and module conventions.

## Rules

- **LANG-001 — Read the call site.** Expose units, mutation, optionality, and failure at the call site. Preserve public names and stored keys across style edits.
- **LANG-002 — Encode meaningful distinctions.** Use values for snapshots and references for shared identity. Use typed IDs or enums to prevent plausible caller mistakes.
- **LANG-003 — Inject variable behavior.** Pass in the clock, ID generator, transport, or store that varies. A closure suffices for a single operation.
- **LANG-004 — Preserve error meaning.** Give absence, invalid input, cancellation, and operational failure distinct outcomes when callers recover differently. Redact private diagnostics.
- **LANG-005 — Check client compatibility.** Before retiring an API, confirm runtime availability and build its clients in each supported language mode and toolchain. Keep unrelated formatting and architecture intact.

## Workflow

1. Trace success and failure at real callers. Record preconditions, effects, and nontrivial costs.
2. Implement the smallest typed change. Keep wire formats locale-independent.

## Verify

- LANG-001, LANG-005: Build affected clients and decode a supported old fixture. Existing calls compile and decoded fields retain their values and identity.
- LANG-003: For localized instants, fix the clock and change zones. Displayed times adapt while the serialized instant stays fixed.
- LANG-004: Cancel an operation and separately submit invalid input. Check the caller can distinguish them when recovery differs.

## Output

Report changed symbols, affected callers, compatibility impact, and test results.

## References

- [API, dependency, and compatibility decisions](references/api-and-dependencies.md)

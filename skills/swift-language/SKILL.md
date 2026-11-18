---
name: swift-language
description: "Review Swift APIs, value semantics, dependency injection, errors, formatting, and toolchain migrations."
---

# Swift API design

## Inputs

Inspect callers, stored formats, and supported toolchains.

## Rules

- **LANG-001 — Clarify calls.** Expose units, mutation, optionality, and failure. Preserve public names and stored keys in style edits.
- **LANG-002 — Model distinctions.** Use values for snapshots, references for shared identity, and typed IDs to prevent mix-ups.
- **LANG-003 — Inject dependencies.** Pass in what varies, such as a clock or transport. One operation can use a closure.
- **LANG-004 — Preserve recovery.** Distinguish absence, invalid input, cancellation, and errors when recovery differs. Redact private diagnostics.
- **LANG-005 — Protect clients.** Before retiring APIs, check runtime availability, toolchains, and language modes.

## Workflow

1. Trace caller outcomes, effects, preconditions, and costs.
2. Keep wire formats locale-independent.

## Verify

- LANG-001, LANG-002, LANG-005: Build supported clients. Decode an old fixture and edit the source after taking a snapshot. The snapshot retains the fixture’s expected values and identity.
- LANG-003: Fix the clock. Switching zones changes display and preserves the serialized instant.
- LANG-004: Cancel one call and pass invalid input to another. Verify each recovery path.

## Output

Report changed symbols, callers, compatibility, and results.

## References

- [API and dependency decisions](references/api-and-dependencies.md)

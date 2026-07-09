# Project Governance Patterns

Use this reference when project identity, generated project files, target membership, schemes, or entitlements are involved.

## Failure Patterns

- Compile-only checks can miss project identity drift. A build may pass while a widget, watch app, entitlement, app group, or deep link is miswired.
- Generated project files invite accidental hand edits. If a manifest owns the project, hand edits are temporary at best and misleading at worst.
- Target membership mistakes masquerade as code bugs. Missing resources, model files, app intents, privacy files, assets, or test files can produce confusing runtime failures.
- Bundle identifiers and app-group strings tend to drift when they are duplicated across app, extensions, tests, and services.
- Shared schemes are often the hidden contract behind local tests, CI, screenshots, and device installs.

## Default Checks

- Locate the manifest or prove there is none.
- Identify all app products and extension products before changing identifiers or entitlements.
- Check generated project diffs after regeneration.
- Check shared schemes after changing targets or tests.
- Check package or dependency changes for platform availability and target exposure.
- Keep project changes separate from unrelated UI or business-logic refactors when possible.

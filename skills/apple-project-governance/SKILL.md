---
name: apple-project-governance
description: "Audit or repair Xcode and SwiftPM configuration, generated projects, target membership, resources, entitlements and settings drift."
---

# Apple project governance

## Inputs

Identify products, configurations, tracked project inputs and CI scheme.

## Rules

- **PROJ-001 — Edit the owner.** Change the generator manifest or template when it owns the project.
- **PROJ-002 — Check membership.** Check which products contain or link each changed item against its intended consumers.
- **PROJ-003 — Preserve identity.** Reconcile bundle IDs, groups, containers and domains. Migrate persistent keys deliberately.
- **PROJ-004 — Inspect effective values.** Compare resolved settings, packaged resources and signed entitlements with target requirements.
- **PROJ-005 — Locate the failure.** Identify the failing configuration, compilation, signing or infrastructure step before editing.

## Workflow

1. Trace the change from its owner to consuming targets.
2. Regenerate if needed and build affected configurations on the CI destination.

## Verify

- PROJ-001: Regenerating twice from identical inputs produces identical output.
- PROJ-002, PROJ-004: Inspect linked dependencies, Info.plist, resources and extensions in the built products.
- PROJ-003, PROJ-005: For provisioning errors, match the rejected entitlement to the profile. After storage identity changes, read pre-upgrade data.

## Output

Report owner, products, build context, inspected artifacts and blockers.

## References

- [Project and product inspection](references/project-governance-patterns.md)
- [Generated inputs and membership](references/build-and-generated-inputs.md)

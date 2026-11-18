---
name: apple-project-governance
description: "Audit or repair Xcode and Swift package configuration, generated projects, target membership, schemes, resources, entitlements, and settings drift."
---

# Apple project governance

## Inputs

Read the build instructions. Identify affected products, targets, schemes, configurations, generator inputs, dependencies, and CI commands.

## Rules

- **PROJ-001 — Edit the owning input.** For generated projects, change the manifest or template and inspect the regenerated diff.
- **PROJ-002 — Check product membership.** Verify each changed source, dependency, resource, model, privacy manifest, or extension reaches every intended product and no others.
- **PROJ-003 — Preserve durable identity.** Reconcile bundle IDs, groups, containers, domains, and shared constants. Changing a storage key requires an intentional migration.
- **PROJ-004 — Inspect effective settings.** Compare the resolved settings, bundled resources, and signed entitlements with the target’s requirements.
- **PROJ-005 — Diagnose by stage.** Distinguish configuration, compiler, signing, destination, and infrastructure failures before selecting a fix.

## Workflow

1. Trace the changed setting or file from its source owner to every consumer.
2. For a repair, edit the owner and regenerate from tracked inputs.
3. Build affected products with the CI scheme, configuration, and destination.

## Verify

- PROJ-002, PROJ-004: Confirm deployment settings and linked dependencies. Inspect the built Info.plist, resources, and extensions for intended membership.
- PROJ-001: For generator changes, rerun with identical inputs and check for an empty diff against the first output.

## Output

Report owners, affected products, build context, inspected artifacts, and build or signing blockers.

## References

- [Project ownership and product inspection](references/project-governance-patterns.md)
- [Generated inputs, toolchains, and membership](references/build-and-generated-inputs.md)

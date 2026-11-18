---
name: apple-project-governance
description: "Audit or repair Xcode and SwiftPM configuration, generated projects, target membership, resources, entitlements and settings drift."
---

# Trace an Xcode configuration problem to its source

Use this when the built app or extension lacks an expected file, capability or dependency. Find the setting responsible and fix it where the project is maintained.

## Start here

Identify the failing product, configuration, CI scheme and destination. If an extension fails only in Release, inspect its Release build.

## How to proceed

1. **Locate the first failure.** Use the log to distinguish configuration, compilation, signing and runner failures. A rejected entitlement points to the signing inputs. <!-- PROJ-005 -->
2. **Find the editable source.** Find the project, generator manifest or template that supplies the setting. Edit it and regenerate if needed. <!-- PROJ-001 -->
3. **Check the intended consumers.** List which targets need the file, package or capability. Compare that list with what each product contains or links. <!-- PROJ-002 -->
4. **Protect installed data.** Reconcile bundle IDs, groups, containers and domains before renaming anything. Plan a migration if a storage key must change. <!-- PROJ-003 -->
5. **Inspect the resulting product.** Build the affected configurations on the CI destination. Compare resolved settings, packaged resources and signed entitlements with the expected values. <!-- PROJ-004 -->

## Check the result

- For generated projects, run the generator twice with identical inputs. The second run should produce no new changes. <!-- PROJ-001 -->
- Inspect the linked dependencies, Info.plist, resources and embedded extensions. For a signing failure, match the rejected entitlement to the profile. <!-- PROJ-002 PROJ-004 PROJ-005 -->
- After a storage identity change, install over a seeded older build and verify the app and intended extension can still read their records. <!-- PROJ-003 -->

## What to report

Name the edited source, affected products and configurations, build evidence and blockers.

- [Tracing a configuration change to the installed product](references/project-governance-patterns.md)
- [Generated inputs, target membership and Release settings](references/build-and-generated-inputs.md)

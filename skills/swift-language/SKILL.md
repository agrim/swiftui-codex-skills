---
name: swift-language
description: "Review Swift APIs, value semantics, dependency injection, errors, formatting, and toolchain migrations."
---

# Change a Swift API without surprising its callers

Use this when a call is easy to misuse or when changing a type, error, or dependency could break clients or saved data.

## Start here

Find a real call that can go wrong, such as a transfer whose source and destination IDs can be swapped. Identify public callers, stored formats, and supported toolchains.

## How to proceed

1. **Read the call in context.** Make the arguments, side effects and significant costs apparent at the call site. Preserve public names and stored keys during unrelated style edits. <!-- LANG-001 -->
2. **Make important distinctions visible.** Give interchangeable-looking IDs distinct types when swapping them changes the target. Decide whether a caller should see later edits or keep a snapshot. <!-- LANG-002 -->
3. **Pass in what can vary.** Provide a fixture service for a preview or a fixed clock for a test. A single operation may need only a closure. <!-- LANG-003 -->
4. **Give callers enough information to recover.** Separate cancellation, missing data, invalid input and service failures when the next action differs. Remove private values from diagnostics. <!-- LANG-004 -->
5. **Keep existing clients working.** Check runtime availability, compiler and language modes. Keep localized display text separate from stable identifiers and serialized dates. <!-- LANG-005 -->

## Check the result

- Build client code with each supported toolchain and decode an older fixture. Take a snapshot, edit the source record, and confirm the snapshot keeps its original ID and values. <!-- LANG-001 LANG-002 LANG-005 -->
- Fix the clock and switch time zones. The displayed time changes and the serialized instant stays the same. <!-- LANG-003 -->
- Cancel one call and give another invalid input. Verify the caller takes the intended recovery path for each. <!-- LANG-004 -->

## What to report

Identify the caller that motivated the change, the compatibility checks you ran, and the behavior the caller can rely on.

- [Ambiguous IDs, dependency choices, and compatible formats](references/api-and-dependencies.md)

# Review and modernization decisions

## Evidence-first review

Rank each finding by the failure the user can encounter. Include the affected file, symbol, platform, reproduction and smallest correction. Keep a supported spelling used elsewhere out of a review that only concerns the edited control.

## Modernization record

| Field | Required decision |
| --- | --- |
| Current API | Exact overload, behavior, and callers |
| Evidence | SDK declaration, official guidance, or reproducible defect |
| Classification | Deprecated, unavailable, discouraged for this case, or simply newer alternative |
| Compatibility | Compiler, language mode, deployment minimum, and runtime availability |
| Replacement | Preserved semantics, ownership, accessibility, and fallback |
| Proof | Compile plus affected state/interaction tests |

If both APIs support the target, compare behavior before suggesting a migration. Retain a working implementation when the proposed change loses selection, alters persistence or requires raising the minimum OS beyond the brief.

## Migrating a change handler

A document switch commits the outgoing selection. When migrating its `onChange` handler, use the outgoing ID from the two-value action. Carrying over a capture of the view’s selection can commit to the incoming document instead. Keep appearance writes disabled when opening a document should leave storage untouched.

Open on A, switch to B, then recompute while B remains selected. Expect one commit to A across all three steps. For a review, report the handler and reproduction. For an authorized migration, exercise the supported fallback too.

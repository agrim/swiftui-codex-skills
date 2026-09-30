# Review and modernization decisions

## Evidence-first review

Start with the requested mode: explain, review, fix, implement, or migrate. Preserve established authorization and local conventions. Select the smallest domain skill and reference that matches the actual changed behavior; do not load every skill because the app uses SwiftUI.

For each finding, identify file/symbol, observed failure or unsupported contract, affected platform/version, minimal correction, and verification. Separate a crash/data-loss risk from an optional readability preference. Do not pad a review with deprecated-looking spellings that remain supported, speculative performance claims, or wholesale architecture substitutions.

## Modernization record

| Field | Required decision |
| --- | --- |
| Current API | Exact overload, behavior, and callers |
| Evidence | SDK declaration, official guidance, or reproducible defect |
| Classification | Deprecated, unavailable, discouraged for this case, or simply newer alternative |
| Compatibility | Compiler, language mode, deployment minimum, and runtime availability |
| Replacement | Preserved semantics, ownership, accessibility, and fallback |
| Proof | Compile plus affected state/interaction tests |

A newer API does not automatically justify migration. Keep stable code when replacement changes behavior or raises supported minimums without a product reason. Do not copy system-app private chrome based on a screenshot. Use the installed public declaration and actual destination.

## Scope the next reference

State loss belongs to ownership/identity; layout failure to measurement/proposals; poor contrast to the whole styled component; stale async work to task authority; slow builds to compiler/project diagnostics rather than runtime profiling. Framework-specific persistence issues need the matching store specialist, not a blanket preference for the newest framework.

Record what was *not* checked. A source-only audit cannot establish rendered HIG alignment, real permission prompts, or performance improvement. Keep optional tooling outside the engineering contract so another model or shell-based workflow can follow the same steps.

## Official sources

- [SwiftUI framework overview](https://developer.apple.com/documentation/SwiftUI).
- [HIG: Design principles](https://developer.apple.com/design/human-interface-guidelines/design-principles).
- [Swift API design guidelines](https://www.swift.org/documentation/api-design-guidelines/).

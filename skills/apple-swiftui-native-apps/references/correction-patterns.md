# Apple App Correction Patterns

Use this reference when starting or auditing Apple-platform app work, especially if the user says the UI feels non-native, overbuilt, junior, not minimal, not SwiftUI-native, not Jobs/Ive/Rams-level, or if a prior implementation needed repeated correction.

## Raw Scan Basis

This reference is grounded in repeated Apple-app correction patterns, not generic SwiftUI preferences. The underlying evidence came from multiple Apple-platform apps with different state, data, device, and release constraints.

Use summaries as a map, not as the evidence. When a future user asks to improve this skill, audit the current source artifacts again because new failures may have appeared after this snapshot.

## Repeated Baseline Gaps

1. Generic SwiftUI composition is not enough. The user repeatedly corrected work that had plausible SwiftUI code but weak product-state hierarchy, unclear next action, or visual clutter.
2. Native-looking is not the same as native. Trace the exact SwiftUI path: `Button`, `Menu`, toolbar placement, button style, tint, shape, foreground, and container behavior.
3. A screenshot symptom needs source tracing. Do not guess from the rendered surface; inspect the modifier chain and then re-render when visual output matters.
4. Prominent tinted controls are semantic. Using `.borderedProminent`, `.glassProminent`, or a prominent tint as decorative color can cause SwiftUI to own foreground color and hierarchy in unwanted ways.
5. Watch surfaces punish excess. Icons, labels, mixed shapes, and copied phone controls often make watch screens unreadable; protect glanceability and verify on small and large watch simulators.
6. Product flow beats app taxonomy. Repeated correction showed that feature buckets can create admin overhead, and generic tab/dashboard habits can bury the live loop the app actually exists to serve.
7. New SwiftUI APIs need runtime proof. SDK presence or interface signatures alone are not enough to replace a stable custom path.
8. Visual polish needs visual proof. Builds and unit tests do not validate typography, spacing, truncation, glass, button hierarchy, or card calmness.
9. Simulator/device tooling failures are often infrastructure. CoreSimulatorService, simdiskimaged, device visibility, and screenshot hangs can be environmental; do not rewrite app code to fix tooling.
10. Broad cleanup must stay behavior-preserving. Performance-sensitive utility work showed that simplification should use tiny helper extraction and focused tests, not broad rewrites.
11. Custom pseudo-native chrome ages badly. Prior corrections repeatedly rejected hand-built tab bars, pill clusters, aspect-ratio hacks, and custom Liquid Glass lookalikes when a platform toolbar, tab, sheet, search drawer, or button shape existed.
12. Button foreground problems are structure problems first. Repeated white/black text failures came from styles, roles, tints, parent foreground leaks, and custom filled backgrounds fighting SwiftUI's environment.
13. Small controls reveal sloppy hierarchy. Circular versus capsule controls, oversized pause buttons, watch truncation, and misplaced timers were not cosmetic; they showed unresolved role and state hierarchy.

## Corrections To Apply By Default

- Start with the user's mental model and current action, then map code. Do not start from screens, tabs, or generic feature buckets.
- Identify the one primary action, the current state, the safe escape, and rare secondary actions before styling.
- Preserve established app invariants such as a current-session execution loop or a thin user/context layer.
- Prefer shared components over visually similar duplicates. If the user says same code, extract the real owner instead of copying layout.
- Keep changes narrow when the user asks for a fix; broaden only to adjacent instances of the same root cause.
- When pause, resume, running, editing, or persisted active state is involved, audit adjacent mutations, timers, projections, watch sync, live activities, and export paths for the same state leak.
- Use native controls and styles first. If custom fill/background is required, keep the `Button` native and avoid owning text/symbol foreground unless the repo has an explicit approved contrast helper for custom non-button artwork.
- For colored start buttons, do not use prominent styles as decorative fills. Prefer a native `Button` with plain style, a single simple shape background, and no label foreground override; then inspect inherited environment if SwiftUI still resolves the wrong foreground.
- For bottom bars and toolbars, prefer native toolbar placements and system control sizing. Use custom layout only when the product interaction cannot be expressed with native placement, and then prove accessibility, motion, and geometry.
- Pair stateful controls in code. `Pause` and `Resume`, `Start Set` and `Complete Set`, active and paused home state, phone and watch projections, and crash/relaunch handling must be one state machine rather than nearby patches.
- For watchOS, design the watch surface separately. Remove copy before shrinking it, remove icons before truncating labels, prefer one obvious bottom action, and move secondary controls to a native secondary surface when possible.
- For iOS workout screens, separate workout-level state from exercise-level state: workout title/timer/chrome should not make the exercise timer or set action ambiguous.
- Verify visual changes with screenshots or device runs when the user's complaint is visual. Verify interaction changes with focused tests and, when touch/gesture matters, real device confirmation if available.
- If the user says stop or rollback, stop or rollback the disputed experiment promptly; do not keep polishing queued work.

## Useful Evidence Patterns

- Simulator/runtime debugging: full launches and logs can reveal metadata, concurrency, and persistence-store problems that are invisible in a compile-only pass.
- Active workout flows: start/complete actions need explicit state transitions; pause should freeze progression controls, automated timers, projections, and companion-device behavior, not only the visible clock.
- Native UI chrome: Liquid Glass questions must be answered by tracing exact `Menu`, toolbar, `.buttonStyle`, `.buttonBorderShape`, and modifier chains.
- Contrast/buttons: hard-coded white/black fixes are not the product lesson; the deeper lesson is to choose the correct native control structure so SwiftUI can resolve foreground correctly.
- Watch controls: copying iPhone controls onto watch creates mixed shapes, truncation, and crowded active screens; watch often needs a separate two-surface model with the main screen reserved for the current action.
- Hierarchy leaks: screenshots catch mistakes quickly, such as timer placement implying the wrong owner, icons stealing watch text space, and bright filled buttons resolving foreground incorrectly.
- Native UI work: custom tab bars, custom button ratios, and hand-built glass should be corrected toward standard Liquid Glass, platform controls, and verified screenshots.
- Search/list surfaces: matching visuals by tweaking rows is weaker than extracting shared card/search/page-stack owners.
- Search chrome: experimental toolbar behavior should stay reversible; restore stable native navigation search when verification hangs or the user asks to roll back.
- Hot-path cleanup: retain behavior and performance with focused tests and no broad refactor drift.
- macOS productization: native polish needs real app assets, proper Liquid Glass/icon treatment, signing/packaging checks, and no broad performance regressions.

## Baseline Skill Failures To Avoid

- Do not answer Apple UI requests from generic SwiftUI snippets. Start from the repo's current state and the platform role of the control.
- Do not call a surface native because it compiles with SwiftUI. Native means behavior, environment, accessibility, layout, animation, foreground resolution, and system placement all line up.
- Do not use color as a substitute for hierarchy. If the user cannot tell the next action, the flow is wrong before the palette is wrong.
- Do not solve visual complaints by adding more modifiers. First remove custom layers until the native control behavior reappears, then add only the minimum product-specific styling.
- Do not let "minimal" mean feature deletion. Minimal means preserving the core truth of the product with fewer, clearer surfaces.

---
name: apple-swiftui-native-apps
description: Native SwiftUI UI and interaction-state engineering for iOS, iPadOS, watchOS, macOS, and visionOS. Use when implementing, refactoring, reviewing, or auditing Apple-platform views, controls, button foreground ownership, toolbars, navigation, tabs, sheets, inspectors, search and list surfaces, Liquid Glass, HIG alignment, accessibility, Dynamic Type, control hierarchy, SwiftUI modernization, or app-specific interaction flows. This skill owns UI, control, navigation, accessibility, and interaction-state semantics; pair it with apple-device-validation for build, run, install, screenshot, watch, or physical-device proof. Route project configuration, privacy integrations, performance-only cleanup, App Store submission readiness, and macOS distribution to their dedicated skills unless UI behavior is also in scope.
---

# Apple SwiftUI Native Apps

## Scope And First Pass

- Own the semantic UI decision: view hierarchy, platform control, navigation and chrome, interaction state, accessibility, localization headroom, and visual role.
- Honor the user's execution boundary before acting. Treat `stop`, `rollback`, `no code changes`, and `discuss first` as hard contracts; do not continue queued edits or source-changing validation.
- When rollback is requested, promptly revert only the disputed experiment, preserve unrelated user changes, then stop and report the resulting state.
- For a planning request or no-edit request, present repository-grounded evidence and recommendations before proposing implementation; do not quietly change source.
- Inspect the live repository before deciding. Read app-local instructions such as `AGENTS.md`, `AGENT_INSTRUCTIONS.md`, and `CODEX_PROJECT_INSTRUCTIONS.md`, then inspect `project.yml`, schemes, target files, and the exact SwiftUI view and control path in scope.
- Use the product's actual nouns from current source and user context. Do not infer a domain from generic states such as pause/resume, timers, metrics, or companion-device behavior.
- Identify the user's current state, one primary next action, safe escape, and rare secondary actions before changing layout or styling.
- Trace the actual `View` tree, modifier chain, control style, toolbar placement, tint, foreground environment, accessibility path, and state mutation path. Treat a screenshot as a symptom, not source proof.
- Keep a requested fix narrow. Broaden only to adjacent instances of the same demonstrated root cause.
- Read `references/correction-patterns.md` for a new feature, broad UI audit, visual or native-control complaint, stateful cross-surface flow, or correction that has resisted a local fix.
- Use summaries only to locate evidence. Base conclusions on current source, diffs, tests, screenshots, logs, SDK declarations, and runtime output relevant to the request.
- Verify current Apple guidance, SDK declarations, and live behavior when the decision depends on recent HIG guidance, Liquid Glass, beta or newly available SwiftUI APIs, or platform-version behavior.

## Route And Pair

- Pair with `apple-device-validation` when the requested outcome includes a build-and-run, simulator rendering, screenshots, installation, watch pairing, touch or gesture proof, hardware behavior, or infrastructure triage. Define the UI claim here; prove it there.
- Route project files, targets, schemes, bundle identity, and entitlements to `apple-project-governance`.
- Route permissions, privacy artifacts, and Apple system integrations to `apple-privacy-system-integrations`; inspect the actual app graph of App Intents, widgets, watch targets, Live Activities, HealthKit, CloudKit, Spotlight, and existing services before proposing integration changes. Deepen an appropriate native integration before inventing a parallel system.
- Route startup or hot-path simplification to `apple-performance-cleanup`, and macOS signing, packaging, notarization, and release work to `macos-productization`.
- Route App Store record, storefront metadata, reviewability, TestFlight-to-submission orchestration, and public release gates to `apple-app-store-readiness`; keep UI claims and screenshot-state correctness here.

## Native Control Semantics

- Start from native SwiftUI semantics: `Button`, `Menu`, `NavigationLink`, `Picker`, `Toggle`, `Slider`, toolbar items, roles, native button styles, `controlSize`, and `buttonBorderShape`.
- Do not replace a native control with a tappable stack, gesture-only control, custom foreground layer, custom press animation, hand-built chrome, or UIKit/AppKit bridge when SwiftUI can express the behavior.
- Express mutually exclusive menu choices with one native `Picker` binding and unique type-matching tags when it fits. Do not simulate system selection with conditional checkmarks, hidden symbols, or independent row actions. Define whether selection commits immediately or through an explicit confirmation surface, then verify exactly one value and the intended commit timing.
- Place app chrome with semantic toolbar placements such as cancellation, confirmation, primary, top bar, and bottom bar. Keep content-model actions in content.
- Prefer platform navigation, tabs, sheets, inspectors, search, toolbars, and bottom bars before custom equivalents. Require a hand-built tab bar, glass island, pill cluster, or search drawer to justify how it preserves native behavior, sizing, accessibility, motion, and platform placement.
- If a native-looking control has bad geometry, first remove custom frames, padding, backgrounds, transitions, color-scheme overrides, and wrappers. Rebuild from the control, role, style, size, border shape, tint, and placement.
- Treat `controlSize` as a semantic platform request, not a fixed point-size guarantee. If a system button remains too small, inspect the runtime mapping and adjust the label's intrinsic semantic font or symbol scale before adding frames or padding; keep the system style, shape, hit target, and interaction states in control.
- Distinguish native APIs from custom drawing precisely. Native toolbar controls can coexist with custom layout, charts, rings, or timing without making the entire surface system-owned.
- Introduce UIKit/AppKit interop for an app surface only as a narrow, user-approved exception after proving native SwiftUI cannot provide the required behavior.

## Foreground, Prominence, And Hierarchy

- Treat system-resolved button foreground as non-negotiable. Let SwiftUI own text and symbol foreground for every native `Button`, including a reusable custom-filled button. Do not add `.foregroundStyle`, `.foregroundColor`, readable-foreground helpers, color-scheme overrides, or explicit label colors at either the component or screen level.
- Fix system-control contrast through the correct role, style, tint, material or background relationship, label composition, and container environment.
- For an intentionally custom reusable button, keep native `Button` semantics and let the component own its background and shape while SwiftUI continues to resolve the label foreground. Verify contrast in every supported appearance, enabled state, and interaction state; never add component-level or per-screen foreground overrides to compensate for an incompatible fill.
- Treat prominent tinted styles, including `.borderedProminent` and `.glassProminent`, as semantic. Reserve them for the true commit, save, resume, or advance action rather than using prominence as decorative fill.
- Treat a brand-colored choice or start capsule as custom presentation, not automatically as a prominent tinted button. Prefer a plain native `Button` inside one reusable component with a simple shape background and inherited or system-resolved foreground. If contrast fails, revise the fill, material, role, style, environment, or control structure rather than forcing label color.
- If foreground resolves incorrectly, inspect and correct inherited foreground and tint, role, style, parent environment, material or background, label composition, and enabled state instead of changing foreground color.
- Give each screen one obvious next action. If two controls look equally primary, resolve the workflow hierarchy before adjusting color or size.
- Make a first-run or welcome screen state the product's literal job and meaningful differentiation before listing mechanisms or features. Prefer a few truthful outcomes from the actual release over abstract category language or future-capability inventory. Keep supporting copy compact and verb-led: a shorter noun fragment is not an improvement when it no longer says what the product does.
- Align custom welcome content with the native title gutter. A bottom-pinned primary action may use the safe area without an opaque material when no scrolling separation is needed; keep forward-progression symbols after their label in logical reading order and let layout direction mirror them.
- Keep first-run setup to information and access needed for the immediate next experience. Defer preferences and workflow-specific identity to the feature that owns them instead of turning onboarding into a settings form.
- Use geometry to communicate role, not decoration. A circular run/pause control may distinguish process state beside contextual capsule actions, but its size and visual weight must match its actual priority.
- Keep labels action-specific. A selection control names the choice; configuration belongs in configuration; a live surface shows the current metric and target rather than adjacent workflow detail.
- Keep control dimensions stable across hover, press, Dynamic Type, icon presence, state changes, and longer localized labels. Wrap or scale text within that stable contract.
- Use SF Symbols when they improve recognition, and evaluate the symbol together with its container; avoid an enclosed glyph inside an already enclosed control unless the double boundary is intentional. Remove icons on watch or compact controls when they steal label space or cause truncation.

## Interaction State And Composition

- Implement paired actions through one component and one source of truth: pause/resume, begin/complete step, start/end interval, expand/collapse, or connect/disconnect. Flip label, symbol, tint, enabled state, side effects, tests, and companion projections together.
- Audit the complete mutation graph before styling a stateful surface: local state, persistence, timers, sensors, companion sync, widgets, activities, notifications or exports, lifecycle transitions, and crash/relaunch restoration.
- Preserve the product's core invariant before adding UI, such as an active-process draft, thin user/context model, route model, persistence boundary, or hot telemetry path.
- Make creation surfaces true value drafts. Opening, editing, cancelling, or terminating must not insert a placeholder model; the explicit Create or Save action owns the first persistence write.
- In persistence-backed SwiftUI apps, give broad live observations one stable owner and pass the required data into destinations and sheets. Do not attach another unfiltered query set merely because a feature view appeared, especially on a measured presentation hot path.
- Let the workflow drive information architecture. Do not let generic tabs, dashboards, or feature buckets bury the live loop the product exists to serve.
- Treat minimalism as preserving the product's core truth with fewer, clearer surfaces, not as automatic feature deletion.
- Before collapsing a workflow, name the canonical objects and lifecycle states. Remove duplicated chrome and decisions, but preserve distinctions that change persistence, side effects, cancellation, undo, history, or cross-device projection.
- Keep only information relevant to the current moment; do not leak previous-step or next-step details into the active surface.
- Extract shared local owners for repeated control structure, typography, timing, formatting, search or list rows, and chrome. Do not create visually similar one-screen copies.
- Keep views compositional and readable. Use small named `View` types for real sections instead of growing branch-heavy computed views.
- For text entry, express the intended return-key action with `submitLabel` and `onSubmit`, own focus explicitly, and support appropriate tap or scroll dismissal. Do not add a keyboard accessory merely to duplicate a native submit action.
- Do not auto-focus a modal editor merely because its first field is required. Present the editor first, let an explicit field tap start system input, keep untouched validation quiet, and provide a real blank-area or scroll dismissal path. When a compact editor intentionally uses icon-only toolbar actions, retain semantic `Label` titles and accessibility labels; do not generalize that local product choice into a rule for every toolbar.
- Apply `textContentType` only when the field's semantic contract and workflow benefit from system AutoFill; personal-information hints can surface device-owned candidates. Before replacing a hierarchy that owns focused input, clear focus and keep that hierarchy alive through a view-bound update and, when necessary, a bounded system-input teardown phase. Do not treat `Task.yield()` alone as a SwiftUI render barrier, and do not hide a teardown defect with status-bar or safe-area chrome.
- Keep direct `Form` and `List` row identity stable across loading, permission, and connection states. Change the row's accessory or status in place instead of inserting or removing structurally different rows during a transition.
- Preserve Dynamic Type, VoiceOver, Reduce Motion, light and dark appearances, layout stability, and localization headroom.
- Design watch and other compact surfaces for their own interaction model. Remove copy before shrinking it, remove icons before truncating, and move secondary actions to native secondary surfaces rather than copying the phone layout.

## Modernization And Validation

- Do not replace a stable custom path merely because a new SwiftUI API exists in the SDK. Prove semantic fit, availability, and live runtime behavior before migration.
- Treat another Apple app or first-party screenshot as evidence of interaction intent and proportion, not proof that the same public API or private system affordance is available. Verify the public declaration and actual target runtime before reproducing it; do not rebuild first-party-only chrome merely to match an image.
- Add focused behavior or source-contract tests for control, foreground, accessibility, and state rules that have regressed before.
- Sweep edited scope for hard-coded button foregrounds, parent foreground or tint leaks, fake controls, UIKit/AppKit imports, stale readable-foreground helpers, duplicate visual components, and obsolete helpers.
- Run focused source and unit tests first. Pair with `apple-device-validation` for the relevant build/run, affected screenshots across risky sizes, watch proof, or physical-device interaction confirmation.
- When validation tooling fails, classify simulator, device, signing, or service infrastructure before changing UI source.
- Finish with `git diff --check` and report exactly which UI claims were source-verified, test-verified, runtime-verified, or remain unverified.

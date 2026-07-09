---
name: apple-swiftui-native-apps
description: Native Swift and SwiftUI Apple app engineering for iOS, iPadOS, watchOS, macOS, and visionOS. Use when implementing, refactoring, reviewing, or auditing Apple-platform UI, controls, navigation, Liquid Glass, HIG alignment, SwiftUI modernization, simulator/device validation, or app-specific UX flows.
---

# Apple SwiftUI Native Apps

## First Pass

- Inspect the current repo before deciding. Read local app instructions such as `AGENT_INSTRUCTIONS.md`, `CODEX_PROJECT_INSTRUCTIONS.md`, `project.yml`, schemes, target files, and the exact SwiftUI view/control path involved.
- Read `references/correction-patterns.md` when starting a new Apple-app feature, doing a UX/UI audit, debugging a visual/native-control complaint, or making broad SwiftUI skill/style decisions.
- When improving this skill or deriving cross-project rules, use summaries only as an index. Inspect source artifacts, diffs, screenshots, logs, and tool outputs when the user asks for a thorough scan.
- Route out when another local skill is more precise: project files and entitlements to `apple-project-governance`; permissions and Apple system integrations to `apple-privacy-system-integrations`; simulator/device proof to `apple-device-validation`; hot-path cleanup to `apple-performance-cleanup`; macOS release work to `macos-productization`.
- Treat screenshots as symptoms, not proof. Trace the actual `View` tree, modifier chain, button style, toolbar placement, tint, foreground, accessibility path, and state mutation path before answering whether something is native or custom.
- Prefer XcodeBuildMCP for Apple builds, simulator runs, screenshots, and tests when available. Call `session_show_defaults` before the first build/run/test in a session.
- Verify current Apple guidance, SDK headers, or live simulator behavior when an answer depends on recent HIG, Liquid Glass, beta SwiftUI APIs, availability, or runtime behavior.

## Native Control Laws

- Start every control from native SwiftUI semantics: `Button`, `Menu`, `NavigationLink`, `Picker`, `Toggle`, `Slider`, toolbar items, roles, native button styles, control sizes, and button border shapes.
- Do not fake controls with tappable stacks, custom ink layers, custom press animations, hand-sized chrome, UIKit/AppKit bridges, or gesture-only controls when native SwiftUI can express the behavior.
- Use toolbar placements such as cancellation, confirmation, primary, top bar, and bottom bar when a control is app chrome. Use content controls only when the control is part of the content model.
- Use platform navigation, tab, sheet, inspector, toolbar, and bottom-bar APIs before custom equivalents. A hand-built tab bar, glass island, or pill cluster must prove it preserves native behavior, sizing, accessibility, and motion.
- If a native-looking control has bad geometry, first remove custom frames, padding, backgrounds, transitions, color-scheme overrides, and wrappers. Rebuild from `Button`, style, `controlSize`, `buttonBorderShape`, role, tint, and placement.
- Separate native APIs from custom drawing. A screen may contain native toolbar buttons plus custom layout/rings/timing; do not call the whole surface native just because one part is.

## Button Rules

- Let SwiftUI resolve button text and symbol foreground. Do not force button ink with `.foregroundStyle`, `.foregroundColor`, readable-foreground helpers, custom foreground colors, color-scheme overrides, or per-screen contrast patches.
- Fix button contrast by choosing the correct native role, style, tint, background relationship, and control structure. Do not patch white or black text manually.
- Treat prominent tinted styles as semantic. Use prominent styles for true current commit, resume, save, or advance actions; do not use them as decorative colored pills.
- Bright custom start-choice capsules are not prominent tinted buttons. If the product intentionally wants a bright green/yellow start capsule, use a plain native `Button` with a colored capsule background and inherited/system foreground; reserve prominent tinting for true prominent actions.
- If system foreground resolves incorrectly on a custom filled button, debug the control structure: inherited foreground/tint, button role, button style, parent environment, material/background relationship, and label composition. Do not fix by forcing white or black ink.
- Each screen should have one obvious next action. If two buttons look equally primary, question the workflow before styling around the ambiguity.
- Pair stateful actions through one control/component and one state source: pause/resume, start/complete set, start/complete rest, expand/collapse, connect/disconnect. The label, symbol, tint, enabled state, side effects, tests, and watch projection must flip together.
- Button labels should contain only information relevant to the action. Identity choice shows identity only; programming details belong in tuning; live execution shows the current live metric and target, not adjacent workflow details.
- Prefer SF Symbols when they improve recognition. Remove icons on watch or compact controls when they steal text space or cause truncation.
- Text must wrap or scale inside stable control dimensions. Do not let hover, press, dynamic type, icon presence, or longer localized labels resize the control unexpectedly.
- Use geometry to clarify role, not decoration. A circular play/pause control can distinguish session state beside contextual capsule actions, but it must not accidentally become larger or visually louder than its role.

## SwiftUI Design Discipline

- Make the workflow drive the UI. For each screen, identify the user's current state, next action, safe escape, and hidden/secondary actions before editing layout.
- Keep information relevant to the moment. Avoid showing details from the previous or next action on the current surface.
- Preserve the app's core invariant before adding UI: current-session draft, thin user model, route model, persistence boundary, or hot telemetry path.
- For stateful surfaces, audit the full mutation graph before styling: local state, persisted state, timers, sensors, watch sync, widgets, activities, notification/export paths, app lifecycle, and crash/relaunch behavior.
- Prefer shared local helpers/components for repeated control structure, typography, timing, formatting, search/list rows, and chrome. Avoid scattered one-screen overrides or visually similar duplicates.
- Keep views compositional and readable. Use small named `View` types for real sections; avoid giant branch-heavy computed views when behavior grows.
- Preserve Dynamic Type, VoiceOver, Reduce Motion, light/dark mode, layout stability, and localization headroom.
- Do not introduce UIKit/AppKit interop for app surfaces unless the user explicitly approves a narrow exception and native SwiftUI cannot do the job.
- When the user says stop, rollback, no code changes, or discuss first, treat that as a hard interaction contract. Do not continue queued edits or validation that changes source.

## Modernization Discipline

- SDK presence is not enough. Before replacing a stable custom path with a new SwiftUI API, prove the API is semantically appropriate and works in the live runtime.
- For Apple-platform audits, start with the actual app graph: targets, entitlements, App Intents, widgets, watch app, Live Activities, HealthKit, CloudKit, Spotlight, and existing services. Deepen native integrations before inventing new systems.
- When simulator, screenshot, or device tooling fails, separate infrastructure failure from app failure before changing source.
- When the user asks for planning or says no code changes, produce evidence and recommendations first. Do not quietly edit code.

## Validation

- Add focused tests or source-contract tests for any button/control/state rule that has regressed before.
- Use source sweeps for hard-coded button foregrounds, parent foreground/tint leaks, UIKit/AppKit imports, fake controls, custom readable-foreground helpers, stale helpers, and duplicate visual components before declaring a UI cleanup complete.
- Run focused tests first, then the relevant app build or simulator run. Use screenshots across affected device sizes for UI changes when layout, color, glass, typography, truncation, or watch sizing matters.
- For interaction fixes, simulator screenshots and unit tests may not be enough; use physical-device confirmation when touch, drag, gesture, or phone/watch delivery matters and the user asks for confidence.
- Distinguish app failures from simulator infrastructure failures. If CoreSimulatorService or simdiskimaged is broken, report infrastructure state before rewriting app code.
- Finish with `git diff --check` for edited repos and summarize exactly what was verified.

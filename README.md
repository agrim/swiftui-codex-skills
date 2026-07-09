# Apple Codex Skills

Public Codex skills for building better Apple-platform apps with AI coding agents.

This repository contains reusable Codex skills for Swift, SwiftUI, iOS, iPadOS, watchOS, macOS, visionOS, Xcode, native Apple UI, app privacy, simulator/device validation, and release-quality app engineering.

The goal is simple: make Codex better at creating Apple apps that feel native, behave correctly, respect platform boundaries, and survive real builds, screenshots, devices, and releases.

## Who This Is For

- Developers building Swift and SwiftUI apps with Codex or similar AI coding agents.
- Teams that want AI-generated Apple app code to stay closer to native platform conventions.
- Builders who care about app quality beyond "it compiles": UI hierarchy, privacy, entitlements, device proof, performance, packaging, and release trust.
- People creating their own public or private Codex skill libraries and looking for a practical Apple-app skill structure.

## Why These Skills Exist

General-purpose coding agents can write SwiftUI, but Apple app quality depends on details that generic code generation often misses:

- Native controls are not the same as custom views that look native.
- Button color bugs are often control-structure bugs, not palette bugs.
- Xcode project files, schemes, entitlements, bundle IDs, and generated manifests must move together.
- Permission prompts need purpose strings, privacy manifests, denied states, fallbacks, and tests.
- A successful build does not prove visual quality, watch usability, or physical-device behavior.
- Performance cleanup should preserve behavior and hot-path characteristics.
- macOS distribution needs signing, notarization, packaging, icons, and install verification.

These skills tighten those areas so Codex asks better questions before editing code.

These skills are an opinionated Apple-app layer on top of Codex's existing skills, tools, and repo-grounded coding ability. They do not replace the built-in Codex Apple skills, XcodeBuildMCP, GitHub workflows, official Apple documentation, or app-local instructions. They tighten the judgment layer Codex applies while using those foundations.

## How The Layering Works

1. **Base Codex** reads the repo, edits files, runs commands, reasons through product and engineering tradeoffs, and preserves user intent.
2. **Existing Codex skills and tools** provide general workflows such as SwiftUI implementation, Liquid Glass work, simulator control, GitHub publishing, and skill authoring.
3. **App-local instructions** preserve the specific repo's current architecture, naming, tests, product boundaries, and team decisions.
4. **These published skills** add sharper Apple-app guardrails learned from repeated implementation corrections: native control semantics, privacy completeness, project governance, real-device validation, hot-path restraint, and release hygiene.

Use the most specific skill that matches the work. Let the skill narrow the question before writing code.

## Skills

- `apple-swiftui-native-apps`: native SwiftUI Apple app engineering for iOS, iPadOS, watchOS, macOS, and visionOS, with strong defaults around platform controls, button foreground behavior, Liquid Glass, simulator/device validation, and product-state hierarchy.
- `apple-project-governance`: Xcode project, target, scheme, manifest, entitlement, and build-setting discipline.
- `apple-privacy-system-integrations`: privacy-safe Apple framework integration across permissions, data flows, manifests, and system surfaces.
- `apple-device-validation`: simulator, physical-device, watch, screenshot, and infrastructure-aware validation.
- `apple-performance-cleanup`: behavior-preserving Apple app cleanup for startup, hot paths, memory, and telemetry.
- `macos-productization`: macOS signing, packaging, notarization, app icon, release, and install hygiene.

## What These Skills Sharpen

- **Native control discipline**: prefer `Button`, `Menu`, toolbar placements, roles, system styles, and system sizing before custom tappable stacks or hand-built chrome.
- **Button foreground correctness**: fix contrast through control structure, role, style, tint, and environment instead of painting labels white or black.
- **Project coherence**: keep manifests, generated projects, targets, schemes, bundle identifiers, entitlements, app groups, and constants aligned.
- **Privacy completeness**: pair framework access with purpose strings, manifests, user explanation, permission states, fallback behavior, and tests.
- **Validation honesty**: distinguish compile proof, simulator proof, screenshot proof, physical-device proof, and infrastructure failure.
- **Performance restraint**: simplify hot paths with behavior-preserving helpers and focused tests rather than broad rewrites.
- **Release trust**: treat signing, notarization, packaging, icons, versioning, and install behavior as product quality.
- **Public hygiene**: keep published skills free of local paths, private project names, session artifacts, secrets, and device identifiers.

See [How These Skills Layer On Codex](docs/layering.md) for examples.

## Common Use Cases

- "Make this SwiftUI screen feel native instead of custom-built."
- "Audit this app for hard-coded button foreground colors and fake controls."
- "Add an Apple framework integration without missing privacy or entitlement work."
- "Validate this iPhone and watch UI with screenshots, not just a build."
- "Refactor this hot path without changing behavior or performance."
- "Prepare this macOS app for a trustworthy public release."

## Repository Contents

```text
skills/                 Published Codex skills
scripts/                Public validators and repo scanners
docs/                   Human-facing explanations and use cases
AGENTS.md               Instructions for future agents editing this repo
```

## Local Use

Clone this repository, then install a skill by copying or symlinking its folder into your Codex skills directory.

Copy example:

```bash
cp -R skills/apple-swiftui-native-apps "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Symlink example:

```bash
ln -s "$(pwd)/skills/apple-swiftui-native-apps" "${CODEX_HOME:-$HOME/.codex}/skills/apple-swiftui-native-apps"
```

## Updating

When a skill changes:

1. Edit the skill under `skills/<skill-name>/`.
2. Keep `SKILL.md` concise and put deeper guidance in `references/`.
3. Run the repository validators.
4. Commit and push the repo.
5. Keep the matching local installed skill in `~/.codex/skills` in sync.

## Validation

```bash
python3 scripts/validate_skills.py .
python3 scripts/scan_apple_repo.py /path/to/apple-app-repo
```

## License

No license has been selected yet.

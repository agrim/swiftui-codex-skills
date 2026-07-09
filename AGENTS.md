# AGENTS.md

This repository is the source of truth for published Swift/SwiftUI Codex skills.

## Rules

- Keep each skill in `skills/<skill-name>/`.
- Preserve Codex skill structure: `SKILL.md` is required; `agents/openai.yaml` is recommended; `references/` holds deeper guidance.
- Keep `SKILL.md` short, imperative, and trigger-focused. Put examples, correction patterns, and longer domain notes in reference files.
- Do not edit plugin-cache skills directly. Publish reusable changes here, then install or symlink the skill into `~/.codex/skills`.
- When updating a skill, validate YAML frontmatter and metadata before committing.
- If the skill affects active Apple-app work, update the relevant app-local instructions only when the rule is app-specific.
- Do not commit local-machine absolute paths, secrets, device identifiers, private screenshots, or user-specific filesystem details.
- Use `scripts/validate_skills.py .` before publishing.
- Keep public literature domain-neutral and example-driven. Explain the app-engineering pattern without naming private apps, local folders, devices, sessions, or users.

## Current Published Skills

- `apple-swiftui-native-apps`: default SwiftUI discipline for native Apple UI, controls, button foreground behavior, workflow hierarchy, and simulator/device validation.
- `apple-project-governance`: project files, targets, schemes, generated project state, bundle identifiers, and entitlements.
- `apple-privacy-system-integrations`: permissions, privacy manifests, HealthKit, CloudKit, App Intents, widgets, Live Activities, Spotlight, and WatchConnectivity.
- `apple-device-validation`: simulator, physical-device, watch, screenshot, install, and infrastructure-aware validation.
- `apple-performance-cleanup`: startup, hot-path, memory, telemetry, and behavior-preserving simplification work.
- `macos-productization`: macOS signing, notarization, packaging, app icons, releases, and install verification.

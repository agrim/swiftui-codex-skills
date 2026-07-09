# Apple Codex Skills

Published Codex skills for Swift, SwiftUI, and Apple-platform app work.

## Skills

- `apple-swiftui-native-apps`: native SwiftUI Apple app engineering for iOS, iPadOS, watchOS, macOS, and visionOS, with strong defaults around platform controls, button foreground behavior, Liquid Glass, simulator/device validation, and product-state hierarchy.
- `apple-project-governance`: Xcode project, target, scheme, manifest, entitlement, and build-setting discipline.
- `apple-privacy-system-integrations`: privacy-safe Apple framework integration across permissions, data flows, manifests, and system surfaces.
- `apple-device-validation`: simulator, physical-device, watch, screenshot, and infrastructure-aware validation.
- `apple-performance-cleanup`: behavior-preserving Apple app cleanup for startup, hot paths, memory, and telemetry.
- `macos-productization`: macOS signing, packaging, notarization, app icon, release, and install hygiene.

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

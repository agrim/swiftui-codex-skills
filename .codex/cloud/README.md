# Codex Cloud setup

Select `agrim/swiftui-codex-skills`. Repository maintenance works on Linux with Python 3.10+ and the standard library. No dependency installation, API credentials or running service is needed; the environment's **Install script** can remain empty after confirming `python3 --version`.

For the **Start skill**, work from the repository root, read [AGENTS.md](../../AGENTS.md), and use these existing checks for skills, catalogs or tooling:

```sh
python3 scripts/validate_skills.py .
python3 scripts/skillctl.py docs --check
python3 -m unittest discover -s tests -v
git diff --check
```

Do not install the skills into a personal host directory as part of environment setup. This checkout is the source library; its optional host adapters do not change the provider-neutral core.

Swift examples require Swift 6.0+. [CI](../../.github/workflows/validate.yml) uses macOS and Apple SDKs for the complete example suite and SwiftUI/SwiftData compilation. Cloud's Python checks do not establish Apple compilation or runtime behavior. Run the existing Apple compilation job or validate on a macOS/Xcode host when examples change.

This guidance is optional host setup documentation, not a Cloud configuration schema. Commit and push reviewed changes before GitHub-backed setup, test the prepared environment and publish it in the Cloud UI. See [the official Cloud environment guide](https://learn.chatgpt.com/docs/environments/cloud-environments).

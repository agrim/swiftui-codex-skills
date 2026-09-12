# Reproducible distribution and installed-artifact proof

Define the channel first: development, internal, Developer ID direct distribution, or Mac App Store. Signing, sandboxing, hardened runtime, notarization, packaging, update trust, and review requirements differ. A locally runnable ad-hoc app is not a notarized release.

Inspect nested executables, frameworks, extensions, helper tools, entitlements, versions, resources, and app identity in the built artifact. Do not trust source settings alone. Preserve required debug symbols and verify the product's actual architecture/platform support before claiming compatibility.

Packaging should be reproducible from source-owned inputs. Record toolchain, commit, artifact hash, version/build, signing identity category, and notarization/stapling results without disclosing private credentials. A receipt for an earlier binary does not validate a modified package.

For direct distribution, test the downloaded/quarantined installation path on an appropriate machine when authorized. Launch the installed copy, not the build-folder original. Check first launch, updates, permissions, icons, links, and removal behavior without deleting unrelated user data.

Updates need authentic metadata and artifact integrity, version ordering, failure recovery, and an intentional signing-key policy. Do not introduce an updater service solely because another project uses one. Debug injection, local paths, temporary entitlements, and developer-only helpers must not leak into shipping outputs.

Keep publication separate from preparation. A successful archive, signature check, or notarization does not authorize uploading a release or changing an account. Record exactly which artifact and gate were tested, and keep unexecuted downloaded-install and distribution-channel checks visible.

## Official sources

- [Notarizing macOS software before distribution](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution).
- [Signing Mac software with Developer ID](https://developer.apple.com/developer-id/).
- [Distributing your app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).
- [Resolving common notarization issues](https://developer.apple.com/documentation/security/resolving-common-notarization-issues).

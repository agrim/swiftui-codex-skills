# macOS Productization Patterns

Use this reference when macOS app work crosses from local build into something a user might install or trust.

## Failure Patterns

- A locally signed app can launch locally but still fail Gatekeeper distribution expectations.
- Packaging can succeed while the app icon, entitlements, helper tools, or embedded resources are wrong.
- Notarization status is often assumed from signing status; it must be checked separately.
- Release artifacts drift when version, build, commit, package, and notes are not tied together.
- Privileged cleanup or install actions can remove user state if treated casually.

## Default Checks

- What distribution channel is intended?
- What signing identity and entitlements are actually embedded?
- Is hardened runtime required and enabled?
- Is notarization required and verified?
- Does the packaged artifact install and launch?
- Do icon, version, build, and release notes match the shipped artifact?

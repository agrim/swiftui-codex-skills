# Review packets, CLI adapters, and release ledgers

Treat an external store-management CLI as a capability adapter, not a grant of account authority. Before a mutation, read current service state, reconcile the exact app/version/build and existing scoped approval, and execute only the intended stage. Avoid duplicate submissions when a previous call's result is ambiguous.

Keep a release ledger tying source, binary/archive, uploaded build, processing state, test evidence, metadata, and approval decisions. A new candidate can supersede an earlier compile or review blocker without erasing its history. The latest receipt must refer to the same candidate and stage before it clears a blocker.

Public copy, screenshots, review credentials, hardware requirements, subscriptions, support links, and privacy policy must match the submitted journey. Optimize wording for truthful discoverability, not unsupported functionality claims. Do not manufacture ratings, reviews, rankings, or expected conversion gains.

## Gate probes

Check cold first launch, login/account deletion where required, offline/denied states, purchase/restore behavior, linked services, and reviewer access. Confirm screenshots come from the intended binary/state and supported device. A polished mockup is not runtime evidence.

Recheck current regional and storefront requirements from Apple at submission time. Do not freeze a remembered fee, toolchain minimum, disclosure form, or business-model rule as permanent. Distinguish internal TestFlight, external review, App Review approval, and public release.

Report passed, failed, not applicable, not authorized, and unverified separately. A source inspection can establish preparation, not uploaded or released service state. Never embed review credentials, certificates, or API keys in the public ledger.

## Official sources

- [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/).
- [Distributing your app](https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases).
- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests).
- [Offering account deletion in your app](https://developer.apple.com/support/offering-account-deletion-in-your-app/).

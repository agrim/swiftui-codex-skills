# Data inventory across tools and system surfaces

For each data category, record origin, purpose, access scope, processing location, destination/operator, stored representations, retention, deletion, and logs. Include credentials, identifiers, derived data, caches, indexes, widgets, companion transfers, backups, and support exports—not only a developer-operated server.

Separate declarations: an entitlement enables a capability; a purpose string explains protected access; a privacy manifest describes applicable uses; storefront privacy answers describe actual collection practices. One cannot substitute for another. Recheck the current requirements when changing the data flow.

Ask permission in a meaningful user context and represent denied, restricted, revoked, unavailable, account-mismatch, empty, and transient-error states according to the specific framework. Do not fabricate a universal granted/denied API where the framework intentionally keeps read permission opaque.

An optional integration should fail without breaking unrelated local value. An essential integration should gate only its dependent journey with a clear explanation. Avoid repeated prompts and misleading “connected” labels based only on an entitlement or a successful request submission.

Diagnostic and agent tooling is also a data boundary. Screenshots, traces, build logs, memory graphs, and uploaded examples can expose private records even when app telemetry is minimal. Review and redact artifacts before sharing them or sending them to a model/tool provider.

Use synthetic fixtures for public examples. Define what happens to every representation on account switch and deletion. A deleted local row may remain in a widget snapshot or index; test those projections explicitly. Do not claim legal or privacy certification from a successful build, a checklist, or source inspection alone.

## Official sources

- [Describing data use in privacy manifests](https://developer.apple.com/documentation/bundleresources/describing-data-use-in-privacy-manifests).
- [Required reason APIs](https://developer.apple.com/documentation/bundleresources/describing-use-of-required-reason-api).
- [Third-party SDK requirements](https://developer.apple.com/support/third-party-SDK-requirements/).
- [Protecting user privacy with HealthKit](https://developer.apple.com/documentation/healthkit/protecting-user-privacy).
- [Keychain services](https://developer.apple.com/documentation/security/keychain-services).

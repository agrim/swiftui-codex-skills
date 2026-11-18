# Candidate and storefront checks

Map each advertised feature and screenshot to evidence or mark it untested. Exercise the highest-risk journey on the exact release candidate. Record the revision, archive identity, version/build, storefront and observed result.

| When the listing promises… | Probe | Evidence that changes the decision |
| --- | --- | --- |
| An account-based feature | Start with the private review instructions and an account in the described state | The verifier reaches the feature with production services and sample data. A staging-only success leaves reviewer access open. |
| A paid feature | Exercise the purchase or restore path for that storefront | The resulting entitlement unlocks the advertised behavior. |
| Offline or permission-independent use | Deny the permission or disconnect at the point the feature needs it | The observed fallback agrees with the claim. |
| Account deletion | Follow the deletion journey with disposable data, if authorized | Record how deletion starts and which outcome can be verified. A signed-out session alone proves only loss of local access. |

For a disclosure discrepancy, trace the transfer to its owner in the app or a bundled SDK. Record whether that transfer changes this storefront’s disclosure.

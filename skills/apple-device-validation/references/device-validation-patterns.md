# Choosing evidence for a runtime claim

| Claim | Evidence to accept | Common false positive |
| --- | --- | --- |
| Layout fits | Inspect the affected state at the reported size, locale and accessibility settings | A preview with short sample text |
| A control works | Operate it and observe its specific result | A screenshot showing the control |
| Data survives an upgrade | Seed the old build, install over its preserved container, then read the value in the new build | A clean-install launch |
| A widget updates | Change the source value and observe the host rendering that value | A regenerated timeline alone |
| A companion receives an action | Observe the result on the receiving device or pair, including reconnect when relevant | A sender acknowledgement |
| A notification opens the intended screen | Observe delivery and tap routing on the destination | A provider receipt or token change |

Record the candidate, fixture, runtime, destination and action for each result. A later observation supersedes a failure only for the same claim. After a change, replace affected receipts while keeping earlier results as history. For batch capture tracking, use the [screen inventory](screen-review.md).

Match the installation path to the question. Reinstallation, fresh install, restored backup and upgrade can expose different failures. Preserve existing data unless a reset is authorized. Inspect keychain, cloud or other external stores independently when the verdict depends on them. An unavailable device blocks the hardware claim while simulator checks can still proceed.

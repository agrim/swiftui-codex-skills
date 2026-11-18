# Trust-boundary failure cases

| Boundary | Exercise against the actual component | Evidence |
| --- | --- | --- |
| Incoming route or intent | Supply an unknown operation, repeated field, deleted target, or valid ID belonging to another account. | Parsing and authorization reject the input before mutation. No private record appears in the error. |
| Document import | Deny access midway through an import. | No partial write survives. Any security-scoped access the app acquired is released on exit. |
| Transport | Present an untrusted certificate to the shipping configuration. | The request fails without exposing credentials. Every shipping exception has a scoped product purpose. |
| Build dependency | Review the pinned script or plugin, then run it with only its authorized inputs. | Unrelated credentials stay unavailable throughout execution. |

## A locked-device read looks like logout

A background refresh receives `errSecInteractionNotAllowed` for a credential that requires unlock. Preserve the item and pending work. Treating the error as revocation could sign out the account or overwrite valid credentials.

Lock a device with a valid item and exercise the refresh. Unlock and retry the same query. The account resumes without a replacement item or login prompt.

# Deep links, restoration and missing history

## Back skips an intermediate screen

Trace the visible screen alongside the bound path. The discrepancy locates the first screen that restoration cannot reconstruct.

| Action | Bound path | Visible screen |
| --- | --- | --- |
| Open a folder by value | `[folder]` | Folder |
| Open its guide using a direct destination view | `[folder]` | Guide |
| Follow a value link to a document | `[folder, document]` | Document |
| Press Back | `[folder]` | Folder |

If the user expects the guide on Back, include it as a route value and repeat restoration in a fresh scene. A disposable help screen at the end of the journey can keep its direct link. When a valid route resolves only after its row appears, inspect the registration's lifetime before rebuilding the path.

## Cancel closes the presenting window

When Cancel closes the window or leaves the sheet visible, check which view acquired the dismiss action. Let the presented editor dismiss itself or let the selection owner clear its presentation. From a pushed detail, cancel an edit and check that the same window, detail and stored value remain. Reopen, fail Save and verify the draft survives for retry.

## A delayed link outlives its account

Deliver the same link during launch and again after login. Switch accounts while its record is loading. Resolve the ID against the account that will actually present the destination. Expect one authorized destination or an unavailable state. Reject malformed or unsupported links before they can trigger changes.

For saved paths, restore an older schema and remove access to one middle record. Retain the valid prefix only if it forms a useful journey. A missing record must never be silently recreated to satisfy restoration.

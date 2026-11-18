# Task ownership and stale results

Use the feature lifetime to choose a task owner. An app-wide sync must survive a row disappearing. A search for a visible query must stop publishing when its text, scope, or account changes. Measure CPU work during the reported stall before changing its executor.

## Scope changes during search

Key the view task by all inputs that determine results. Capture that snapshot for the request and end a cancelled debounce before starting the fetch. Identify the current request separately so a late reply from an earlier identical search cannot publish. Guard success, failure, and cleanup with the same identity.

1. Keep the text fixed and switch from All to Favorites during the delay. Only Favorites should reach the service.
2. Repeat after All registers with a controlled service. Complete Favorites, then return a late success for All. Favorites must keep its results. In a separate run, fail All while Favorites is loading. The old failure cannot clear the spinner or replace its error.
3. Log out before a response. Revoke publication immediately and cancel the work. Release any lock the cancellation handler needs before calling cancel.

The example suite's `SearchIntegrationTests` wait for service registration and drive completions by ID. They exercise the model and service. Exercise view restart and debounce separately when changing the SwiftUI task key.

## Reentrancy and writes

Two callers can each observe one remaining reservation before either finishes awaiting approval. Reserve the slot before suspending and release it on failure, or revalidate the remaining count at commit. Hold both approvals, then release them in reverse order. Exactly one reservation should succeed.

Revoking a request's UI authority cannot undo a remote write. If its outcome is unknown, reconcile the operation before retrying.

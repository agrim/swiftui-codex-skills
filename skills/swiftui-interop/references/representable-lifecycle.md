# Representable update and teardown failures

## An unrelated update breaks text composition

Begin composing text with an input method, then update unrelated SwiftUI state. If the adapter rewrites unchanged text, it may discard the marked range or move the cursor. Compare effective values before assigning. Exercise a programmatic change and a user edit separately. Only the user edit should write back through this binding.

## A late delegate event updates the wrong model

Mount the native view with model A, rebind the same view to B, and send an edit. Only B should change. Then dismantle the view, recreate it, and deliver a queued callback from the earlier lifetime. Check that the callback cannot change the current model and that observer and task counts return to baseline. Deferring the callback alone leaves the ownership race intact.

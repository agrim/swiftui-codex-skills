# Keep or revert a build experiment

Rerun the original workload on the final candidate. Use the same command, cache policy and destination. Report every sample, including failures, and note whether the observed difference exceeds ordinary variation.

A faster edit build that loses release symbols or ships stale generated output fails correctness. A larger clean build with reliably faster edits may be valuable if that tradeoff fits the stated goal. Record which workload benefits, which regresses and by how much.

For a failed experiment, revert only its scoped changes. Verify the restored product from the current checkout so concurrent edits and earlier green runs cannot distort the handoff.

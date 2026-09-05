# Evaluation: test the guidance, not just the formatting

## Three different claims

**Mechanical integrity:** the validator and Python tests check contracts, budgets, links, source records, routing fixtures, bundles, installation safety, and scanner behavior. Swift tests exercise the example code. These are automated and reproducible.

**Selection quality:** routing fixtures check deterministic phrase retrieval on declared examples, including no-match cases. They are not an unseen-language benchmark, semantic router, or guarantee that an agent selects the right skill.

**Behavioral effectiveness:** an agent must actually apply the guidance to an app fixture. This requires captured outputs, code changes, and the relevant build/test/runtime evidence. No multi-model behavioral result is claimed by this repository merely because its CI passes.

## Behavioral suite

`evals/scenarios.json` contains adversarial tasks, expected skill owners, must-do behaviors, prohibited shortcuts, and the evidence needed. Use them as evaluation contracts, not as examples to memorize into a scoring script. Prepare a small app/code fixture that genuinely exhibits each scenario before running the evaluation.

For each run, record the repository/fixture commit, skill revision, scenario ID, host/model and configuration, available tools, prompt, selected context, produced diff, executed checks, outputs, and reviewer decision. Do not include private app data or credentials.

Compare the same task with and without the selected skills under equivalent tool access and constraints. Randomize order where practical. Repeat tasks to expose variability, and use more than one model/host before making cross-model claims. Keep hidden variants with different names, architecture, and failure timing so keyword repetition is not rewarded.

## Scoring

Score each must-do item as satisfied, partly satisfied, absent, or unverified. Flag any prohibited shortcut independently; a critical correctness or authority violation cannot be averaged away by good prose. Evaluate the actual diff and evidence rather than whether the response repeats the rule ID.

A recommended rubric weights correctness and preserved behavior first, then compatibility, source use, scope control, accessibility/privacy where applicable, and truthful verification. Record raw judgments and disagreement rather than publishing an unexplained single “quality score.”

Compilation is not enough for visual tasks. Screenshots are not enough for focus or hardware tasks. A test fixture passing on Linux does not compile an Apple-only view. Mark blocked environments explicitly.

## Maintenance gates

A content change should preserve or improve its scenario's behavior without broadening false positives. A tooling change must pass deterministic regression tests, including malformed input and safety boundaries. A new framework needs an explicit source and coverage limit, not only its name in a checklist.

Do not publish “best,” “production-proven,” or percentage improvement claims without corresponding evidence. The repository's goal is to become a dependable reference through review, real fixtures, and honest maintenance—not to certify itself by declaration.

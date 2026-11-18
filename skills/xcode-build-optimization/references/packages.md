# Package changes that affect the measured build

Trace a slow dependency to the consuming product. Attribute resolution, host plugin or macro compilation, and target compilation separately. A package listed in a lockfile may contribute no code to the measured target.

Before splitting a module, compare the cost of a representative implementation edit with a public API edit. A split can reduce downstream recompilation while adding linking and module overhead to clean builds. Verify consumers, packaged resources and tests after the split.

If the cost belongs to a generator, change one semantic input and inspect the resulting consumer. An untracked directory present on one developer machine can hide a broken fresh build. Reproduce from tracked inputs before changing the package graph.

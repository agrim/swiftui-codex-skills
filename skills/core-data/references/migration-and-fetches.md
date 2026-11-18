# Fetches, conflicts, and migrations

- **Slow list or import.** Measure fetch count, relationship faults, and peak memory on representative data. Change batching or prefetching for the observed bottleneck. Test import memory on a dedicated context so resetting it cannot invalidate a live editor.
- **Conflicting edits.** Stage an unsaved user edit, save a different value in the background, then save the editor. Compare the final field values with the product's conflict policy. Count surviving unrelated changes as well.
- **Model upgrade.** Seed the changed relationship or optional field with distinguishable business IDs and values. Include malformed legacy rows if the importer accepted them. Reopen the migrated store twice. A fallback to an empty store can make launch appear successful while hiding every record.
- **Cloud mirroring.** Migrate a local copy first, then check a destination signed into the intended account. Exercise an account change using records with distinguishable origins.

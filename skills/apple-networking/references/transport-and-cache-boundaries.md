# Pagination, shared transfers, and image renditions

## A query changes between pages

Hold page two while changing filters. Complete the old page with success and then, in a separate run, with failure. Neither may append records or clear the new query's spinner. Preserve server ordering, deduplicate by record ID, and stop if the server repeats a cursor.

## Two views share an image download

A feed row leaves while a detail screen still needs the same photo. Share source bytes only for compatible account, representation, and cache policies. A cache-only caller cannot join a transfer that would violate its offline contract.

Register subscribers and find or start the transfer atomically. Detach a departing subscriber and finish its wait promptly. Keep the transfer for other subscribers, including intentional prefetches. When the last leaves, retire the entry and cancel the transfer. Check a callback's transfer identity before updating the cache, subscribers, or entry for its key.

Hold a fake transport while both views join. Count one start, zero transport cancellations when the row leaves, and one cancellation when the detail also leaves. Start a replacement for the same key and deliver the old completion. Only the replacement may publish. Repeat across accounts at the same URL and check that private transfers stay separate.

## One thumbnail at two scales

Request a square 60-point avatar from a sufficiently large square original at 1× and 3×. Key decoded renditions by pixel size and transformations while reusing compatible source bytes. On cold and warm paths, inspect decoded dimensions. Expect 60 and 180 pixels respectively. A small view frame can conceal a full-size decode.

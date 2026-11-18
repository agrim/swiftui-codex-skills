# A rename meets a newer edit

One window renames a saved walk while another marks it as a favorite. If the rename editor holds an entire old copy of the record and writes it back, Save can silently undo the favorite.

For independent fields, keep the record ID and the edited name in the draft. On Save, apply the name to the current record. If a save completes after a list has reordered, use that ID again before updating the row. Its former position may now belong to another walk. Closing the sheet without saving simply drops the name. Two windows editing the same name require a product choice. If overwriting would lose meaningful work, compare the revision each editor started from and let the second person keep their draft while resolving the conflict.

For an app that supports offline creation, one more boundary matters. Give the pending creation an identity that lasts across relaunch. Reuse it on retry if the service honors that identity. Otherwise look up the original result using a supported reconciliation mechanism. If the service offers neither, keep the outcome uncertain and offer recovery. A timeout alone cannot tell you whether another record should be created.

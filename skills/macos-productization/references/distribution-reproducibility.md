# Which release artifact passed?

Record the source revision, version/build, toolchain, export identity and final package hash. Keep signing, notary acceptance, ticket validation, Gatekeeper assessment, installation and launch results tied to the artifact each actually observed. A change to the package can invalidate downstream receipts.

**ZIP distribution.** The accepted submission and shipped ZIP can have different bytes after ticket stapling and repackaging. Identify the app carrying the ticket and record the new ZIP hash. Download, unpack and launch the installed copy using the intended distribution path when authorized. Testing the old ZIP or build-folder app leaves first launch unverified.

**Disk image or installer.** If the log identifies a rejected helper, link the corrected container to its own submission and service receipt. An accepted receipt for the enclosed app cannot identify that replacement container. Validate the ticket for the format the user receives. Keep the first downloaded-launch result even when an existing development copy launches successfully.

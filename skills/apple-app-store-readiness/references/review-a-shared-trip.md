# A reviewer opens a shared-trip invitation

Provide a working sample invitation or instructions to issue one. Start on a clean TestFlight installation with the intended build and a reviewer account. Open the public HTTPS link from outside the app. After sign-in, the recipient should return to the named trip. A staging-only account or expired invitation leaves the advertised journey unreviewable.

If the website opens, check domain association and the installed app’s associated-domains entitlement. If the app opens but loses the trip, inspect the route preserved across sign-in. If the recipient sees an empty inbox, follow the invitation from the sender through the service. A manual importer would hide that delivery failure.

**For a TestFlight handoff**, record the archive, bundle ID and platform. If Xcode manages build numbers during distribution, use the number actually uploaded to find the processed build and its group assignment. If an earlier upload timed out, check for that build before repeating it. A processed build can still lack group access or required external beta review. Check tester notification separately. Verify the stage requested and keep demo access in the designated review channel.

**For the listing**, open the actual support and privacy pages, exercise the production path and compare its screenshots and installed icon with the storefront assets. TestFlight purchases run in the StoreKit sandbox. Use them to check the purchase and restore flow. Check the production product’s availability separately before promising it on the storefront.

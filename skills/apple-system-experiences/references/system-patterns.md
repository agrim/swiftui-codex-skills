# Choosing what a system surface can show or change

Identify the canonical record, the smallest payload the host needs, and what happens when the record expires or changes account. For a surface that can write, identify the shared app command and its authorization check.

| Surface | Decision for this feature |
| --- | --- |
| Widget | Which facts remain useful after the displayed entry goes stale? |
| Live Activity | Which event ends the activity if the app stops running? |
| Intent | Which validated command owns the requested effect? |
| Notification | What can a locked-screen payload disclose, and where should the app resolve the rest? |
| Search | Which record ID survives indexing and can be checked again at open? |
| Watch | May a newer value replace an older one, or does every command require acknowledgement? |
| Health | Which local values map to system types and units without losing meaning? |
| Purchase | Which verified entitlement and account authorize access after restart? |

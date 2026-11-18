# API and dependency decisions

| Symptom | Scoped correction | When it earns its cost |
| --- | --- | --- |
| A caller can swap two string IDs | Give the roles distinct types or labels. | The wrong call compiles and acts on a different record. |
| A preview contacts production | Inject a fixture transport where the feature is constructed. | An external dependency varies across environments. |
| A state can be both loading and finished | Encode mutually exclusive outcomes in an enum. | The flags represent competing states. Keep independent capabilities separate. |
| A style rename breaks old documents | Preserve the stored key or decode both versions. | A released format or external caller uses the old name. |

## Searching labels and resolving identifiers

A people picker searches names but stores the selected account ID. In a fixed test locale, search for “jose” among “José” and “Josef”. Both labels should match. Give them distinct case-sensitive IDs `a7` and `A7`, select each, and verify storage receives the corresponding unchanged ID. Apply the same separation to localized dates and wire-format instants.

## Failure and compatibility

Discard an error only when the caller has the same recovery for every discarded outcome. Exercise cancellation and invalid input at the caller. Keep a failed save distinct from a successful empty response.

When replacing a public symbol, compile an external client in its supported modes. If only one runtime needs an adapter, scope it there. For generated clients, fix the owning template and compile its output.

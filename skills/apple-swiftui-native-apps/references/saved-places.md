# Choosing the first screen for Saved Places

Someone hears about a café, saves its name, and wants to find it on Saturday. They know the name before they know the street address. That makes a named list a better first screen for this version than a pin that requires coordinates.

Start with a list and a toolbar Add button. Let Add open a sheet with a name field, Save and Cancel. On Save, insert the place through the collection the list already reads. On success, dismiss the sheet and show the new row. On failure, keep the name in the editor so the person can try again. Searching or sorting a growing collection can come later.

If the real task is “show me somewhere nearby to stop on this walk,” location belongs on the first screen. You can make that call by walking through a real outing. The presence of coordinates in the data model tells you little about which screen should lead.

## When the first run becomes a settings form

Let someone save the first place with the few details they already know. Move rarely changed defaults to a secondary form. If location is useful only for “nearby,” ask when they choose it. Keep a privacy disclosure reachable from Settings after onboarding. A direction-aware Continue label should still make sense with larger type and right-to-left text.

For a modal editor, decide whether typing really is the first task. If users first need to inspect the existing place, present the sheet before focusing a field. Keep untouched fields quiet. Give Return the right next-field or done behavior and reserve explicit Save for the commit. If AutoFill lingers over the next screen, check the field’s content type, focus owner and dismissal order before adjusting safe-area padding.

For discrete numeric choices, preserve a valid old value outside the new presets until the person changes it. A native Picker can edit the draft in place. Check Cancel, keyboard submit and relaunch. A ruler in another Apple app establishes the interaction to study, not the availability of a public ruler control.

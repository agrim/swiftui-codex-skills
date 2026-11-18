# Diagnosing assistive and localized interactions

## Save works by touch but fails by voice

At large text sizes, “Save draft” moves inside a menu. In the supported command language, speak the localized visible title. If it fails, compare “Show names” with that title. “Show numbers” can establish that a control exists while leaving the name mismatch unresolved.

If the visible title already works, retain it. If custom aliases are needed, keep the localized visible title first and try both it and the alias. Dictate a draft, edit a word, open the menu by voice and save. Where two records expose Save, verify which one actually changed.

## A custom dial announces a value but cannot adjust it

Compare adjustment by touch and VoiceOver from the same starting level. A stale announcement points to value binding. An announced value that cannot be adjusted points to missing adjustable semantics. If a native styled control cannot express the interaction, bind the dial's accessibility representation to the same level, bounds and step. Limit the replacement to the dial so nearby actions remain reachable.

Adjust up and down to each limit, then move to the next control. Check the announced unit and on-screen level at both stops.

## A translation changes the wrong record

Place two similar names or mixed-direction identifiers next to localized actions. Vary the count from one to many and enlarge the text until the action moves. Check the displayed name, spoken command and stored ID independently. If a locale switch changes a persisted quantity, trace where localized display text crossed the storage boundary.

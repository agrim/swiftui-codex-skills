# Incorrect focus and early commits

## Validation focuses the wrong row

Two quantity fields share a focus value. Tapping either works, yet Save sends the correction to a different item. Give each focus target the identity of its field and record, such as `.quantity(itemID)`. Make the second quantity invalid. Submit with focus elsewhere, then type without tapping. Only that item's draft should change. Reorder the rows and repeat to distinguish correct focus from an error merely scrolled into view.

## Input that is valid only when complete

Type a partial decimal or use an input method editor to compose a word. If validation rewrites the input on every keystroke, compare the raw draft and cursor with the formatted committed value. Format at commit when intermediate text cannot be represented by the stored type. Try paste, selection replacement and AutoFill separately. Return should insert a newline in a multiline field unless the form explicitly assigns another action.

## Find the first durable write

| Event | Check |
| --- | --- |
| Open, type or change a picker | No write while the form promises explicit Save. If the chosen option disappears during refresh, show a deliberate fallback and revalidate it. |
| Submit from the keyboard and tap Save before completion | One command writes once. Failed writes keep the draft available for retry. |
| Cancel or swipe away | The editor follows its stated discard policy. Reopen the record from another surface to inspect the durable value. |

When dismissal fails only with a focused field, compare closing with and without active composition. Observe input teardown before changing the owner. A single task yield cannot prove that teardown finished.

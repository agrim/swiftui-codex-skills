# Stateful reflow and scroll position

## A reminder loses its title when Save moves

| What changes at the breakpoint? | Decision | Round-trip check |
| --- | --- | --- |
| Only the arrangement of the same editable children | Choose one layout container with the field declared once.  | Type a title, switch arrangements twice, then save. Check editing focus and stored text. |
| Width decides between genuinely different presentations | Try the widest presentation first. If the alternatives each contain an editor, bind both to one draft owner.  | Start in each presentation and save in the other. Check the longest label at the narrowest width, including when no candidate fits. |

## The last row stops under a pinned notice

A bottom notice wraps to three lines in a narrow window. Hide it and try the final row again. If the row becomes reachable, reserve the notice's measured height and remove any guessed clearance. A decorative shadow needs no reservation. Show and hide the notice with the keyboard visible. The last action should remain reachable and the gap should disappear with the notice.

## A refresh jumps away from what someone was reading

Insert a page above the visible anchor while leaving the user's finger still. Record the IDs before and after refresh. An index-based anchor moves to a neighbor. A jump to the newest item on every append can move even a correctly identified anchor. Fix the failing mechanism and define a nearby fallback for a deleted anchor.

Before replacing a list with lazy or eager rows, compare the same data volume and preserve selection, row commands and keyboard navigation. Exercise a nested scroll gesture on both axes if the replacement changes who handles scrolling.

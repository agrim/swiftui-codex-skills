---
name: apple-app-intents
description: "Add an app action to Siri or Shortcuts, or diagnose why it is missing, uses the wrong record, or fails when the app is closed."
---

# Make an app action work in Siri and Shortcuts

Use this skill to let someone run an app feature from Siri or Shortcuts. The code that exposes the feature is an `AppIntent`. For example, a “Move note” shortcut should put a packing list in the Travel folder just as the app’s Move button would.

## Start here

Try the action in the app and find the code that commits the change. If a shortcut already exists, run it with the same inputs and compare the results.

## How to proceed

1. **Expose the action to Shortcuts.** Give the intent a recognizable title and declare its inputs, such as a note and folder. Include it in the app or extension that runs it. If Shortcuts cannot find it after installation, check the build log for intent metadata extraction errors. <!-- INT-002 -->
2. **Make it work with the app closed.** Give the intent’s `perform()` method access to the current account and store before a screen opens. Use the store’s required actor or queue. If the work is queued for later, say so in the result. <!-- INT-005 -->
3. **Look up the saved choices again.** Resolve each selected record’s ID in the current account. If a selected record is gone or inaccessible, stop or ask for another choice. <!-- INT-003 -->
4. **Check permission before writing.** Show only records the person may see. If the action requires authentication or confirmation, obtain it before making changes. <!-- INT-004 -->
5. **Call the operation the app already uses.** Resolve missing inputs first. For “Move note,” ask for the folder before moving anything. If a reply is lost, check whether the move was saved before retrying. <!-- INT-001 -->

## Check the result

- Create a shortcut, add the action, choose a test note and folder, and save it. Run it with the app closed. Reopen the note and check its folder. For Siri, move it back first, invoke the spoken phrase and check the folder again. <!-- INT-002 INT-005 -->
- Switch to an account without access and run the saved shortcut. The private note’s name stays hidden and neither account’s data changes. <!-- INT-003 INT-004 -->
- Cancel a required prompt and confirm the note stays put. If the app supports retries with an operation ID, replay the same ID and verify one committed move. <!-- INT-001 INT-004 -->

## What to report

Name the action, where you ran it, and what changed in the app. If it failed, identify the last step that worked.

- [When a saved note belongs to another account or a move runs twice](references/entities-and-actions.md)

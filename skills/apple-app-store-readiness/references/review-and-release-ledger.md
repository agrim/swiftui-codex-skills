# Release decisions and conflicting receipts

Keep one row per stage and candidate. Record approval scope, current service observation, blocker and next action. Retain superseded receipts with their candidate and date. Keep reviewer credentials out of the public handoff.

**An old handoff says upload is blocked.** Later approval covers upload of build 12 and assignment to Internal QA. Check the archive and live service record. If the build already processed, carry its receipt forward and complete only the remaining group assignment. If it is absent, perform the approved upload once prerequisites pass. An ambiguous timeout calls for another state read before a retry. External invitations need their own scope. Label simulated service results explicitly.

**An external tester cannot see a processed build.** Check the exact build’s eligibility and group before changing access. An Internal Only build calls for a different candidate. For an eligible, beta-approved build, inspect whether notification is pending. Reinviting a tester solves neither a candidate mismatch nor an outstanding group distribution step. Record the service result for the authorized action.

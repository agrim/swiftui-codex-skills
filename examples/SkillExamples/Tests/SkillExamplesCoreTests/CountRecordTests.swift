import Testing
@testable import SkillExamplesCore

struct CountRecordTests {
    @Test func unknownIsDifferentFromObservedZero() throws {
        var draft = CountDraft()
        #expect(draft.observation == .unknown)
        draft.observation = .estimated(try ItemCount(0), source: "counter")
        #expect(draft.observation != .unknown)
    }

    @Test func correctedResultPreservesPlanAndObservation() throws {
        var draft = CountDraft(target: try ItemCount(12))
        draft.observation = .estimated(try ItemCount(10), source: "counter")
        let record = draft.confirm(try ItemCount(9))
        #expect(record.target?.value == 12)
        #expect(record.observation == .estimated(try ItemCount(10), source: "counter"))
        #expect(record.confirmed.value == 9)
        #expect(record.export.itemCount.value == 9)
        #expect(record.export.recordID == draft.id)
    }

    @Test func laterDraftChangesDoNotRewriteConfirmedRecord() throws {
        var draft = CountDraft(target: try ItemCount(12))
        let record = draft.confirm(try ItemCount(9))
        draft.target = try ItemCount(20)
        draft.observation = .estimated(try ItemCount(18), source: "new reading")
        #expect(record.target?.value == 12)
        #expect(record.observation == .unknown)
        #expect(record.confirmed.value == 9)
    }

    @Test func repeatHasNewIdentityAndNoObservation() throws {
        var draft = CountDraft(target: try ItemCount(12))
        draft.observation = .estimated(try ItemCount(10), source: "counter")
        let record = draft.confirm(try ItemCount(9))
        let repeated = record.repeatDraft()
        #expect(repeated.id != record.id)
        #expect(repeated.target == record.target)
        #expect(repeated.observation == .unknown)
        // A CountDraft has no confirmed value or export member.
    }

    @Test func cancellingRepeatedDraftLeavesHistoryUntouched() throws {
        let record = CountDraft(target: try ItemCount(12)).confirm(try ItemCount(9))
        let history = [record]
        var repeated: CountDraft? = record.repeatDraft()
        repeated?.target = try ItemCount(100)
        repeated = nil
        #expect(history == [record])
        #expect(history[0].confirmed.value == 9)
    }

    @Test func countsRejectNegativeValuesAndAllowConfirmedZero() throws {
        #expect(throws: ItemCount.ValidationError.negativeCount) { try ItemCount(-1) }
        let record = CountDraft().confirm(try ItemCount(0))
        #expect(record.confirmed.value == 0)
        #expect(record.export.itemCount.value == 0)
    }
}

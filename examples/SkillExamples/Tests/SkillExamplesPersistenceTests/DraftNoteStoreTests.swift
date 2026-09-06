#if canImport(SwiftData)
import Foundation
import SwiftData
import Testing
import SkillExamplesCore
@testable import SkillExamplesPersistence

private enum InjectedSaveFailure: Error { case beforeStorageWrite }

@MainActor
struct DraftNoteStoreTests {
    private func container() throws -> ModelContainer {
        try ModelContainer(for: StoredNote.self,
                           configurations: ModelConfiguration(isStoredInMemoryOnly: true))
    }

    @Test func editingAndDiscardingValueDraftDoesNotInsert() throws {
        let container = try container()
        let store = DraftNoteStore(container: container)
        var draft = NoteDraft(title: "Unsaved")
        draft.title = "Edited but canceled"
        #expect(try store.titles().isEmpty)
        #expect(!container.mainContext.hasChanges)
    }

    @Test func explicitSaveIsVisibleThroughFreshContext() throws {
        let store = DraftNoteStore(container: try container())
        let id = try store.create(NoteDraft(title: "  Saved note  "))
        #expect(try store.titles() == ["Saved note"])
        #expect(!id.uuidString.isEmpty)
    }

    @Test func validationFailureDoesNotReachSave() throws {
        var saveCalled = false
        let store = DraftNoteStore(container: try container()) { context in
            saveCalled = true
            try context.save()
        }
        #expect(throws: NoteDraft.ValidationError.emptyTitle) {
            try store.create(NoteDraft(title: " \n"))
        }
        #expect(!saveCalled)
        #expect(try store.titles().isEmpty)
    }

    @Test func injectedSaveFailureRollsBackOnlyItsOwnWriter() throws {
        let container = try container()
        container.mainContext.autosaveEnabled = false
        let unrelated = StoredNote(title: "Another editor's pending work")
        container.mainContext.insert(unrelated)
        var attemptedWriter: ModelContext?
        let store = DraftNoteStore(container: container) { writer in
            attemptedWriter = writer
            throw InjectedSaveFailure.beforeStorageWrite
        }
        let draft = NoteDraft(title: "Recoverable draft")
        #expect(throws: InjectedSaveFailure.self) { try store.create(draft) }
        let writer = try #require(attemptedWriter)
        #expect(!writer.hasChanges)
        #expect(try store.titles().isEmpty)
        #expect(draft.title == "Recoverable draft")
        #expect(container.mainContext.hasChanges)
        try container.mainContext.save()
        #expect(try store.titles() == ["Another editor's pending work"])
    }

    @Test func retryAfterPreSaveFailureCreatesOneRecord() throws {
        var shouldFail = true
        let store = DraftNoteStore(container: try container()) { writer in
            if shouldFail { throw InjectedSaveFailure.beforeStorageWrite }
            try writer.save()
        }
        let draft = NoteDraft(title: "Retry")
        #expect(throws: InjectedSaveFailure.self) { try store.create(draft) }
        shouldFail = false
        _ = try store.create(draft)
        #expect(try store.titles() == ["Retry"])
    }
}
#endif

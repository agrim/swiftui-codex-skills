#if canImport(SwiftData)
import Foundation
import SwiftData
import SkillExamplesCore

@Model
public final class StoredNote {
    public var id: UUID
    public var title: String

    public init(id: UUID = UUID(), title: String) {
        self.id = id
        self.title = title
    }
}

/// A small local-create example, not a complete persistence architecture.
/// Each commit owns its context so rollback cannot discard another editor's work.
@MainActor
public final class DraftNoteStore {
    private let container: ModelContainer
    private let save: (ModelContext) throws -> Void

    public init(container: ModelContainer) {
        self.container = container
        self.save = { try $0.save() }
    }

    /// Internal injection seam: tests can fail BEFORE a save touches storage.
    init(container: ModelContainer, save: @escaping (ModelContext) throws -> Void) {
        self.container = container
        self.save = save
    }

    public func create(_ draft: NoteDraft) throws -> UUID {
        let validated = try draft.validated()
        let writer = ModelContext(container)
        writer.autosaveEnabled = false
        let note = StoredNote(title: validated.title)
        writer.insert(note)
        do {
            try save(writer)
            return note.id
        } catch {
            writer.rollback()
            throw error
        }
    }

    /// Return values rather than letting live models escape the context owner.
    public func titles() throws -> [String] {
        let reader = ModelContext(container)
        return try reader.fetch(FetchDescriptor<StoredNote>()).map(\.title).sorted()
    }
}
#endif

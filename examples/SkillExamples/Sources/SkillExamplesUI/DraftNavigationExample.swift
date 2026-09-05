#if canImport(SwiftUI)
import SwiftUI
import SkillExamplesCore

@MainActor
public struct DraftEditor: View {
    @Environment(\.dismiss) private var dismiss
    @State private var draft: NoteDraft
    @State private var message: String?
    private let save: @MainActor (NoteDraft) throws -> Void

    public init(initial: NoteDraft = NoteDraft(), save: @escaping @MainActor (NoteDraft) throws -> Void) {
        _draft = State(initialValue: initial)
        self.save = save
    }

    public var body: some View {
        NavigationStack {
            Form {
                TextField("Title", text: $draft.title)
                if let message {
                    Text(message).foregroundStyle(.secondary)
                }
            }
            .navigationTitle("New note")
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel", role: .cancel) { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Save") {
                        do {
                            try save(draft.validated())
                            dismiss()
                        } catch NoteDraft.ValidationError.emptyTitle {
                            message = "Enter a title."
                        } catch {
                            message = "The note was not saved. Try again."
                        }
                    }
                }
            }
        }
    }
}

/// In-memory demonstration only. Production storage, async saves, restoration,
/// and multiwindow ownership require the corresponding persistence decisions.
@MainActor
public struct DraftNavigationExample: View {
    private struct Note: Identifiable {
        let id: UUID
        let title: String
    }

    @State private var notes: [Note] = []
    @State private var path: [NoteRoute] = []
    @State private var creating = false

    public init() {}

    public var body: some View {
        NavigationStack(path: $path) {
            List(notes) { note in
                NavigationLink(note.title, value: NoteRoute.detail(note.id))
            }
            .navigationTitle("Notes")
            .navigationDestination(for: NoteRoute.self) { route in
                switch route {
                case .detail(let id):
                    if let note = notes.first(where: { $0.id == id }) {
                        Text(note.title)
                    } else {
                        ContentUnavailableView("Note unavailable", systemImage: "doc")
                    }
                }
            }
            .toolbar {
                Button("New note", systemImage: "plus") { creating = true }
            }
            .sheet(isPresented: $creating) {
                DraftEditor { draft in
                    notes.append(Note(id: UUID(), title: draft.title))
                }
            }
        }
    }
}
#endif

#if canImport(SwiftData)
import Foundation
import SwiftData
import Testing

enum LabelSchemaV1: VersionedSchema {
    static var versionIdentifier: Schema.Version { Schema.Version(1, 0, 0) }
    static var models: [any PersistentModel.Type] { [Label.self] }

    @Model final class Label {
        var number: Int
        var caption: String

        init(number: Int, caption: String) {
            self.number = number
            self.caption = caption
        }
    }
}

enum LabelSchemaV2: VersionedSchema {
    static var versionIdentifier: Schema.Version { Schema.Version(2, 0, 0) }
    static var models: [any PersistentModel.Type] { [Label.self] }

    @Model final class Label {
        var number: Int
        @Attribute(originalName: "caption") var title: String
        var detail: String?

        init(number: Int, title: String) {
            self.number = number
            self.title = title
        }
    }
}

enum LabelMigrationPlan: SchemaMigrationPlan {
    static var schemas: [any VersionedSchema.Type] { [LabelSchemaV1.self, LabelSchemaV2.self] }
    static var stages: [MigrationStage] {
        [.lightweight(fromVersion: LabelSchemaV1.self, toVersion: LabelSchemaV2.self)]
    }
}

@MainActor
struct DiskMigrationTests {
    private func openStore(at url: URL, version: any VersionedSchema.Type,
                           plan: (any SchemaMigrationPlan.Type)? = nil) throws -> ModelContainer {
        let schema = Schema(versionedSchema: version)
        let configuration = ModelConfiguration(schema: schema, url: url, cloudKitDatabase: .none)
        return try ModelContainer(for: schema, migrationPlan: plan, configurations: [configuration])
    }

    @Test func renamedValuesSurviveUpgradeAndSecondOpen() throws {
        let files = FileManager.default
        let directory = files.temporaryDirectory.appendingPathComponent(UUID().uuidString)
        try files.createDirectory(at: directory, withIntermediateDirectories: false)
        defer { try? files.removeItem(at: directory) }
        let url = directory.appendingPathComponent("Labels.store")

        try autoreleasepool {
            let container = try openStore(at: url, version: LabelSchemaV1.self)
            let writer = ModelContext(container)
            writer.insert(LabelSchemaV1.Label(number: 2, caption: "West"))
            writer.insert(LabelSchemaV1.Label(number: 1, caption: "East"))
            try writer.save()
        }

        let byNumber = FetchDescriptor<LabelSchemaV2.Label>(sortBy: [SortDescriptor(\.number)])
        try autoreleasepool {
            let container = try openStore(at: url, version: LabelSchemaV2.self, plan: LabelMigrationPlan.self)
            let writer = ModelContext(container)
            let labels = try writer.fetch(byNumber)
            #expect(labels.map(\.number) == [1, 2])
            #expect(labels.map(\.title) == ["East", "West"])
            #expect(labels.allSatisfy { $0.detail == nil })
            let first = try #require(labels.first)
            first.detail = "Updated after migration"
            try writer.save()
        }

        try autoreleasepool {
            let container = try openStore(at: url, version: LabelSchemaV2.self, plan: LabelMigrationPlan.self)
            let reader = ModelContext(container)
            let labels = try reader.fetch(byNumber)
            #expect(labels.map(\.number) == [1, 2])
            #expect(labels.map(\.title) == ["East", "West"])
            #expect(labels.map(\.detail) == ["Updated after migration", nil])
        }
    }
}
#endif

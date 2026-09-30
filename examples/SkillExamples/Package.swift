// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SkillExamples",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "SkillExamplesCore", targets: ["SkillExamplesCore"]),
        .library(name: "SkillExamplesUI", targets: ["SkillExamplesUI"]),
        .library(name: "SkillExamplesPersistence", targets: ["SkillExamplesPersistence"])
    ],
    targets: [
        .target(name: "SkillExamplesCore"),
        .target(name: "SkillExamplesUI", dependencies: ["SkillExamplesCore"]),
        .target(name: "SkillExamplesPersistence", dependencies: ["SkillExamplesCore"]),
        .testTarget(name: "SkillExamplesCoreTests", dependencies: ["SkillExamplesCore"]),
        .testTarget(name: "SkillExamplesPersistenceTests", dependencies: ["SkillExamplesPersistence", "SkillExamplesCore"])
    ]
)

// swift-tools-version: 6.0
import PackageDescription

let package = Package(
    name: "SkillExamples",
    platforms: [.macOS(.v14), .iOS(.v17)],
    products: [
        .library(name: "SkillExamplesCore", targets: ["SkillExamplesCore"]),
        .library(name: "SkillExamplesUI", targets: ["SkillExamplesUI"])
    ],
    targets: [
        .target(name: "SkillExamplesCore"),
        .target(name: "SkillExamplesUI", dependencies: ["SkillExamplesCore"]),
        .testTarget(name: "SkillExamplesCoreTests", dependencies: ["SkillExamplesCore"])
    ]
)

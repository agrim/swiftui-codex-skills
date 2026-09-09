from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import scan_apple_repo as scanner
import skillctl
import skilllib
import validate_skills


class FrontmatterTests(unittest.TestCase):
    def test_json_quoted_description(self):
        result = skilllib.frontmatter('---\nname: example\ndescription: "Use: a \\"quoted\\" value"\n---\n'.replace('\\\\', '\\'))
        self.assertEqual(result["description"], 'Use: a "quoted" value')

    def test_duplicate_key_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            skilllib.frontmatter('---\nname: one\nname: two\ndescription: x\n---\n')

    def test_missing_description_rejected(self):
        with self.assertRaises(ValueError):
            skilllib.frontmatter('---\nname: example\n---\n')

    def test_multiline_yaml_profile_rejected(self):
        with self.assertRaises(ValueError):
            skilllib.frontmatter('---\nname: example\ndescription: |\n  text\n---\n')

    def test_unknown_key_rejected(self):
        with self.assertRaises(ValueError):
            skilllib.frontmatter('---\nname: example\ndescription: text\nallowed-tools: shell\n---\n')

    def test_crlf_supported(self):
        self.assertEqual(skilllib.frontmatter('---\r\nname: example\r\ndescription: text\r\n---\r\n')["name"], "example")

    def test_ambiguous_plain_scalar_rejected(self):
        with self.assertRaises(ValueError):
            skilllib.frontmatter('---\nname: example\ndescription: this: that\n---\n')


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", ".build", "__pycache__", ".build-ios"))

    def test_repository_valid_without_vendor_metadata(self):
        for path in self.root.glob("skills/*/agents"):
            shutil.rmtree(path)
        self.assertEqual(validate_skills.validate(self.root), [])

    def test_duplicate_json_key_rejected(self):
        (self.root / "catalog.json").write_text('{"schema_version":1,"schema_version":1}')
        self.assertTrue(any("duplicate" in e for e in validate_skills.validate(self.root)))

    def test_unknown_source_rejected(self):
        data = skilllib.catalog(self.root)
        data["skills"][0]["sources"].append("missing-source")
        (self.root / "catalog.json").write_text(json.dumps(data))
        self.assertTrue(any("unknown source" in e for e in validate_skills.validate(self.root)))

    def test_unreviewed_source_cannot_claim_date(self):
        data = skilllib.source_registry(self.root)
        data["sources"][0]["status"] = "reference-only"
        (self.root / "sources.json").write_text(json.dumps(data))
        self.assertTrue(any("must not claim" in e for e in validate_skills.validate(self.root)))

    def test_word_budget_enforced(self):
        path = self.root / "skills/apple-swiftui-native-apps/SKILL.md"
        path.write_text(path.read_text() + "\n" + "extra " * 700)
        self.assertTrue(any("exceeds 650" in e for e in validate_skills.validate(self.root)))

    def test_review_scope_cannot_upgrade_discovery_source(self):
        data = skilllib.source_registry(self.root)
        source = next(item for item in data["sources"] if item["status"] == "reference-only")
        source["review_scope"] = "A purported review without content inspection"
        (self.root / "sources.json").write_text(json.dumps(data))
        self.assertTrue(any("review_scope requires" in e for e in validate_skills.validate(self.root)))

    def test_broken_link_rejected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[Broken](no-such-file.md)\n")
        self.assertTrue(any("broken local link" in e for e in validate_skills.validate(self.root)))

    def test_stale_generated_docs_rejected(self):
        (self.root / "docs/coverage.md").write_text("stale\n")
        self.assertTrue(any("stale" in e for e in validate_skills.validate(self.root)))

    def test_unlisted_skill_rejected(self):
        (self.root / "skills/unlisted").mkdir()
        self.assertTrue(any("directories and catalog differ" in e for e in validate_skills.validate(self.root)))

    def test_missing_reference_rejected(self):
        (self.root / "skills/swift-concurrency/references/concurrency-patterns.md").unlink()
        self.assertTrue(validate_skills.validate(self.root))

    def test_reference_traversal_rejected(self):
        data = skilllib.catalog(self.root)
        data["skills"][0]["references"] = ["../../README.md"]
        (self.root / "catalog.json").write_text(json.dumps(data))
        self.assertTrue(any("unsafe relative path" in e for e in validate_skills.validate(self.root)))

    def test_vendor_invocation_in_core_rejected(self):
        path = self.root / "skills/swift-concurrency/SKILL.md"
        path.write_text(path.read_text() + "\nRequire XcodeBuildMCP for all work.\n")
        self.assertTrue(any("vendor-specific" in e for e in validate_skills.validate(self.root)))

    def test_duplicate_rule_id_rejected(self):
        path = self.root / "skills/swift-concurrency/SKILL.md"
        path.write_text(path.read_text() + "\n- **UI-001 — Duplicate.** Bad rule identity.\n")
        self.assertTrue(any("duplicate rule ID" in e for e in validate_skills.validate(self.root)))

    def test_invalid_catalog_shape_is_diagnostic(self):
        (self.root / "catalog.json").write_text('{"schema_version":1,"skills":[null]}')
        self.assertTrue(validate_skills.validate(self.root))

    def test_external_source_host_rejected(self):
        data = skilllib.source_registry(self.root)
        data["sources"][0]["url"] = "https://example.invalid/not-primary"
        (self.root / "sources.json").write_text(json.dumps(data))
        self.assertTrue(any("primary-source" in e for e in validate_skills.validate(self.root)))


class PortableToolsTests(unittest.TestCase):
    def test_routing_contracts(self):
        for case in skilllib.read_json(ROOT / "evals/routing.json")["cases"]:
            with self.subTest(query=case["query"]):
                actual = [item["id"] for item in skillctl.route(ROOT, case["query"])]
                for expected in case["expected"]:
                    self.assertIn(expected, actual)
                if not case["expected"]:
                    self.assertEqual(actual, [])

    def test_behavioral_contracts_reference_existing_skills(self):
        known = {item["id"] for item in skilllib.catalog(ROOT)["skills"]}
        scenarios = skilllib.read_json(ROOT / "evals/scenarios.json")["scenarios"]
        self.assertEqual(len({s["id"] for s in scenarios}), len(scenarios))
        for scenario in scenarios:
            self.assertTrue(set(scenario["skills"]) <= known)
            for field in ("prompt", "skills", "must_do", "must_not", "evidence"):
                self.assertTrue(scenario[field])
            if "fixture" in scenario:
                self.assertTrue(skilllib.safe_path(ROOT / "evals", scenario["fixture"]).is_file())

    def test_bundle_is_deterministic_and_self_contained(self):
        names = ["swiftui-navigation", "swift-concurrency"]
        text = skillctl.bundle(ROOT, names)
        self.assertEqual(text, skillctl.bundle(ROOT, names))
        self.assertNotIn("](references/", text)
        self.assertIn('<a id="swift-concurrency-reference-1"></a>', text)
        self.assertIn("https://developer.apple.com/", text)

    def test_entrypoint_bundle_explains_missing_playbook(self):
        text = skillctl.bundle(ROOT, ["swiftui-navigation"], True)
        self.assertIn("not included", text)
        self.assertNotIn("](#swiftui-navigation-reference", text)

    def test_multiple_references_remain_locatable_in_both_bundle_modes(self):
        text = skillctl.bundle(ROOT, ["apple-device-validation"])
        self.assertIn('<a id="apple-device-validation-reference-2"></a>', text)
        self.assertNotIn("](references/", text)
        entry = skillctl.bundle(ROOT, ["apple-device-validation"], True)
        self.assertIn("screen review workflow (not included", entry)
        self.assertNotIn("](#apple-device-validation-reference", entry)

    def test_unknown_skill_rejected(self):
        with self.assertRaises(ValueError):
            skillctl.bundle(ROOT, ["invented-skill"])

    def test_duplicate_selection_rejected(self):
        with self.assertRaises(ValueError):
            skillctl.bundle(ROOT, ["swiftui-navigation"] * 2)

    def test_safe_path_rejects_escape_and_absolute(self):
        for relative in ("../escape", "/absolute", "a/../b", "a\\b", "a//b"):
            with self.subTest(path=relative), self.assertRaises(ValueError):
                skilllib.safe_path(ROOT, relative)

    def test_installer_dry_run_and_refusal(self):
        with tempfile.TemporaryDirectory() as directory:
            # Canonicalize our own temporary fixture; keep real destination
            # symlinks rejected by the installer on every platform.
            destination = Path(directory).resolve()
            names = ["swiftui-navigation"]
            self.assertEqual(skillctl.install(ROOT, names, destination, True), names)
            self.assertEqual(list(destination.iterdir()), [])
            skillctl.install(ROOT, names, destination)
            self.assertTrue((destination / names[0] / "SKILL.md").is_file())
            with self.assertRaisesRegex(ValueError, "overwrite"):
                skillctl.install(ROOT, names, destination)

    def test_installer_preflights_all_targets(self):
        with tempfile.TemporaryDirectory() as directory:
            destination = Path(directory).resolve()
            (destination / "swift-concurrency").mkdir()
            with self.assertRaises(ValueError):
                skillctl.install(ROOT, ["swiftui-navigation", "swift-concurrency"], destination)
            self.assertFalse((destination / "swiftui-navigation").exists())

    def test_symlink_destination_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "real").mkdir()
            (root / "link").symlink_to(root / "real", target_is_directory=True)
            with self.assertRaises(ValueError):
                skillctl.install(ROOT, ["swiftui-navigation"], root / "link")

    def test_bundle_output_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "bundle.md"
            target.write_text("keep")
            with contextlib.redirect_stderr(io.StringIO()):
                status = skillctl.main(["bundle", "swiftui-navigation", "--output", str(target)])
            self.assertEqual(status, 2)
            self.assertEqual(target.read_text(), "keep")

    def test_cli_limit_invalid(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(skillctl.main(["route", "swiftui", "--limit", "0"]), 2)


class ScannerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return path

    def test_comments_and_strings_are_not_code_findings(self):
        self.write("View.swift", '// .id(UUID())\n/* outer /* Task.detached {} */ try! x() */\nlet a = ".onTapGesture { }"\nlet b = #".id(UUID())"#\nlet c = """\nTask.detached {}\n"""\n')
        self.assertEqual(scanner.scan(self.root)["findings"], [])

    def test_imports_are_not_blanket_errors(self):
        self.write("Bridge.swift", "import UIKit\nimport AppKit\nstruct Bridge: UIViewRepresentable {}\n")
        self.assertEqual(scanner.scan(self.root)["findings"], [])

    def test_line_numbers_survive_multiline_masking(self):
        self.write("View.swift", '/* hidden\ncomment */\nview\n.id(\n UUID()\n)\n')
        finding = scanner.scan(self.root)["findings"][0]
        self.assertEqual((finding["rule"], finding["line"]), ("volatile-identity", 4))

    def test_informational_findings_do_not_fail_by_default(self):
        self.write("View.swift", 'Text("Hello").foregroundStyle(.white)\n')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(scanner.main([str(self.root)]), 0)
            self.assertEqual(scanner.main([str(self.root), "--fail-on", "info"]), 1)

    def test_warning_threshold(self):
        self.write("View.swift", 'view.id(UUID())\n')
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(scanner.main([str(self.root)]), 0)
            self.assertEqual(scanner.main([str(self.root), "--fail-on", "warning"]), 1)

    def test_credential_is_redacted_in_json(self):
        token = "gh" + "p_" + "A" * 30
        self.write("secret.txt", token)
        result = scanner.scan(self.root)
        self.assertNotIn(token, json.dumps(result))
        self.assertEqual(result["findings"][0]["severity"], "error")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(scanner.main([str(self.root), "--format", "json"]), 1)
        self.assertNotIn(token, output.getvalue())

    def test_ignored_directory_and_symlinks_not_followed(self):
        self.write(".build/Generated.swift", "view.id(UUID())")
        outside = self.root / "outside.swift"
        outside.write_text("view.id(UUID())")
        scan_root = self.root / "repo"
        scan_root.mkdir()
        (scan_root / "link.swift").symlink_to(outside)
        (scan_root / ".build").mkdir()
        (scan_root / ".build/generated.swift").write_text("view.id(UUID())")
        self.assertEqual(scanner.scan(scan_root)["findings"], [])

    def test_ignored_name_in_parent_does_not_hide_repository(self):
        root = self.root / "build/project"
        root.mkdir(parents=True)
        (root / "View.swift").write_text("view.id(UUID())")
        self.assertEqual(len(scanner.scan(root)["findings"]), 1)

    def test_binary_and_large_files_reported(self):
        (self.root / "binary").write_bytes(b"\x00\xff")
        (self.root / "large").write_bytes(b"x" * (scanner.MAX_BYTES + 1))
        self.assertEqual(len(scanner.scan(self.root)["skipped"]), 2)

    def test_invalid_root_has_error_exit(self):
        with contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(scanner.main([str(self.root / "missing")]), 2)

    def test_raw_multiline_and_escaped_quote_masking(self):
        text = 'let x = ##"""\n.id(UUID())\n"""##\nlet y = "a\\\" .id(UUID())"\nview.id(UUID())'
        self.write("View.swift", text)
        findings = scanner.scan(self.root)["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["line"], 5)

    def test_deterministic_output(self):
        self.write("Z.swift", "try! operation()")
        self.write("A.swift", "Task.detached {}")
        self.assertEqual(scanner.scan(self.root), scanner.scan(self.root))
        self.assertEqual(scanner.scan(self.root)["findings"][0]["path"], "A.swift")


if __name__ == "__main__":
    unittest.main()

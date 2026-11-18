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
    def test_description_requires_json_quotes(self):
        with self.assertRaisesRegex(ValueError, "description must be a JSON-quoted"):
            skilllib.frontmatter("---\nname: example\ndescription: plain text\n---\n")


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", ".build", "__pycache__", ".build-ios"))

    def test_extensionless_file_reports_redacted_findings(self):
        credential = "github_" + "pat_" + "A" * 24
        machine_path = "/" + "Users/example/private-file"
        (self.root / "probe").write_text(f"{credential}\n{machine_path}\n")
        self.assertCountEqual(validate_skills.validate(self.root), [
            "probe: possible credential; content redacted",
            "probe: local-machine path; content redacted",
        ])

    def test_broken_link_rejected(self):
        path = self.root / "README.md"
        path.write_text(path.read_text() + "\n[Broken](no-such-file.md)\n")
        self.assertTrue(any("broken local link" in e for e in validate_skills.validate(self.root)))

    def test_reference_traversal_rejected(self):
        data = skilllib.catalog(self.root)
        data["skills"][0]["references"] = ["../../README.md"]
        (self.root / "catalog.json").write_text(json.dumps(data))
        self.assertTrue(any("unsafe relative path" in e for e in validate_skills.validate(self.root)))

    def test_duplicate_rule_id_rejected(self):
        path = self.root / "skills/swift-concurrency/SKILL.md"
        path.write_text(path.read_text().replace("## Rules\n", "## Rules\n\n- **UI-001 — Duplicate.** Bad rule identity.\n"))
        self.assertTrue(any("duplicate rule ID" in e for e in validate_skills.validate(self.root)))

    def test_contract_exports_complete_entries_or_reports_an_error(self):
        skills = ["swift-concurrency", "swiftui-testing"]
        args = ["--repo", str(self.root), "contract", *skills]
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(skillctl.main(args), 0)
        data = json.loads(output.getvalue())
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual([s["id"] for s in data["skills"]], skills)
        for skill in data["skills"]:
            folder = self.root / "skills" / skill["id"]
            text = (folder / "SKILL.md").read_text()
            self.assertIn(f'\n# {skill["title"]}\n', text)
            for rule in skill["rules"]:
                self.assertIn("- **{id} — {title}** {instruction}".format(**rule), text)
            for check in skill["verify"]:
                self.assertIn(f"- {', '.join(check['rule_ids'])}: {check['check']}", text)
            for ref in skill["references"]:
                self.assertIn("- [{label}]({path})".format(**ref), text)

        path = self.root / "skills" / skills[-1] / "SKILL.md"
        original = path.read_text()
        other_rule = data["skills"][0]["rules"][0]["id"]
        path.write_text(original.replace("## Verify\n", f"## Verify\n- {other_rule}: Wrong skill.\n"))
        output, errors = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(errors):
            self.assertEqual(skillctl.main(args), 2)
        self.assertIn("rule IDs from this skill", errors.getvalue())
        self.assertEqual(output.getvalue(), "")
        path.write_text(original.replace("## Rules\n", "## Rules\n\n- **TEST-999 — Repeat.** Run again.\n"))
        self.assertIn(f"{skills[-1]}: no verification check for TEST-999", validate_skills.validate(self.root))


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

    def test_bundle_includes_selected_references_and_locates_the_rest(self):
        text = skillctl.bundle(ROOT, ["apple-device-validation"])
        anchor = "apple-device-validation-reference-2"
        self.assertIn(f'<a id="{anchor}"></a>', text)
        self.assertIn(f"](#{anchor})", text)
        self.assertNotIn("](references/", text)
        path = "skills/apple-device-validation/references/screen-review.md"
        entry = skillctl.bundle(ROOT, ["apple-device-validation"], True)
        self.assertIn(f"`{path}`", entry)
        self.assertNotIn("](#apple-device-validation-reference", entry)
        partial = skillctl.bundle(ROOT, ["apple-device-validation"], references=[path])
        self.assertIn(f"](#{anchor})", partial)
        self.assertIn(f'<a id="{anchor}"></a>', partial)
        self.assertNotIn('<a id="apple-device-validation-reference-1">', partial)
        self.assertIn((ROOT / path).read_text().strip(), partial)
        with self.assertRaisesRegex(ValueError, "outside selected skills"):
            skillctl.bundle(ROOT, ["apple-security"], references=[path])

    def test_bundle_output_does_not_overwrite(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "bundle.md"
            target.write_text("keep")
            with contextlib.redirect_stderr(io.StringIO()):
                status = skillctl.main(["bundle", "swiftui-navigation", "--output", str(target)])
            self.assertEqual(status, 2)
            self.assertEqual(target.read_text(), "keep")


class ScannerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)

    def test_warning_threshold(self):
        (self.root / "View.swift").write_text("view.id(UUID())\n")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(scanner.main([str(self.root)]), 0)
            self.assertEqual(scanner.main([str(self.root), "--fail-on", "warning"]), 1)

    def test_credential_is_redacted_in_json(self):
        token = "gh" + "p_" + "A" * 30
        (self.root / "secret.txt").write_text(token)
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(scanner.main([str(self.root), "--format", "json"]), 1)
        self.assertNotIn(token, output.getvalue())
        self.assertEqual(json.loads(output.getvalue())["findings"][0]["rule"], "possible-credential")

    def test_ignored_directory_and_symlinks_not_followed(self):
        outside = self.root / "outside.swift"
        outside.write_text("view.id(UUID())")
        scan_root = self.root / "repo"
        scan_root.mkdir()
        (scan_root / "link.swift").symlink_to(outside)
        (scan_root / ".build").mkdir()
        (scan_root / ".build/generated.swift").write_text("view.id(UUID())")
        self.assertEqual(scanner.scan(scan_root)["findings"], [])

    def test_raw_multiline_and_escaped_quote_masking(self):
        text = 'let x = ##"""\n.id(UUID())\n"""##\nlet y = "a\\\" .id(UUID())"\nview.id(UUID())'
        (self.root / "View.swift").write_text(text)
        findings = scanner.scan(self.root)["findings"]
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["line"], 5)


if __name__ == "__main__":
    unittest.main()

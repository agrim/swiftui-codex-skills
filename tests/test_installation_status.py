from __future__ import annotations

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skillctl
from skill_installation import RECEIPT, fingerprint, installation_status


class InstallationStatusTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / "repo"
        self.repo.mkdir()
        self.name = "swiftui-navigation"
        self.source = self.repo / "skills" / self.name
        shutil.copytree(ROOT / "skills" / self.name, self.source)
        shutil.copyfile(ROOT / "catalog.json", self.repo / "catalog.json")
        self.dest = self.base / "installed"
        self.dest.mkdir()
        self.target = self.dest / self.name

    def install(self):
        skillctl.install(self.repo, [self.name], self.dest)

    def status(self):
        return installation_status(self.repo, [self.name], self.dest)[0]

    def test_receipt_matches_copied_bytes_without_machine_paths(self):
        self.install()
        receipt = json.loads((self.target / RECEIPT).read_text())
        self.assertEqual(receipt["files"], fingerprint(self.source))
        self.assertEqual(receipt["source"], {"commit": None, "skill_dirty": None})
        self.assertNotIn(str(self.base), (self.target / RECEIPT).read_text())
        self.assertEqual(self.status()["state"], "current")

    def test_three_way_comparison_retains_local_edits(self):
        self.install()
        local = self.target / "local.md"
        local.write_text("local work")
        self.assertEqual(self.status()["state"], "local-changed")
        (self.source / "upstream.md").write_text("incoming work")
        result = self.status()
        self.assertEqual(result["state"], "both-changed")
        self.assertEqual(result["changes"]["installed_only"], ["local.md"])
        self.assertEqual(result["changes"]["source_only"], ["upstream.md"])
        self.assertEqual(local.read_text(), "local work")

    def test_source_change_and_deletion_do_not_write_destination(self):
        self.install()
        before = fingerprint(self.target, installed=True)
        receipt = (self.target / RECEIPT).read_bytes()
        (self.source / "SKILL.md").write_text("new source")
        (self.source / "references/navigation-patterns.md").unlink()
        result = self.status()
        self.assertEqual(result["state"], "source-changed")
        self.assertEqual(result["changes"]["modified"], ["SKILL.md"])
        self.assertEqual(result["changes"]["installed_only"], ["references/navigation-patterns.md"])
        self.assertEqual(fingerprint(self.target, installed=True), before)
        self.assertEqual((self.target / RECEIPT).read_bytes(), receipt)

    def test_same_change_on_both_sides_still_matches_source(self):
        self.install()
        for folder in [self.source, self.target]:
            (folder / "extra.md").write_text("same change")
        result = self.status()
        self.assertEqual(result["state"], "both-changed")
        self.assertTrue(result["matches_source"])

    def test_untracked_copy_does_not_invent_provenance(self):
        shutil.copytree(self.source, self.target)
        self.assertEqual(self.status()["state"], "untracked")
        self.assertTrue(self.status()["matches_source"])
        (self.target / "SKILL.md").write_text("unknown origin")
        self.assertEqual(self.status()["state"], "untracked")
        self.assertFalse(self.status()["matches_source"])
        self.assertFalse((self.target / RECEIPT).exists())

    def test_missing_status_and_dry_run_leave_no_receipt(self):
        self.assertEqual(self.status()["state"], "missing")
        skillctl.install(self.repo, [self.name], self.dest, True)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_symlink_destination_and_ancestor_are_rejected(self):
        alias = self.base / "alias"
        alias.symlink_to(self.dest, target_is_directory=True)
        child = self.dest / "child"
        child.mkdir()
        for dest in [alias, alias / "child"]:
            with self.subTest(dest=dest), self.assertRaises(ValueError):
                skillctl.install(self.repo, [self.name], dest)
            with self.assertRaises(ValueError):
                installation_status(self.repo, [self.name], dest)
        self.assertEqual(list(child.iterdir()), [])

    def test_symlink_receipt_is_not_followed(self):
        self.install()
        p = self.target / RECEIPT
        p.unlink()
        p.symlink_to(self.repo / "catalog.json")
        with self.assertRaisesRegex(ValueError, "symlink"):
            self.status()

    def test_malformed_receipt_is_diagnostic_and_preserved(self):
        self.install()
        p = self.target / RECEIPT
        p.write_text('{"schema_version": 99}')
        with self.assertRaisesRegex(ValueError, "receipt"):
            self.status()
        self.assertEqual(p.read_text(), '{"schema_version": 99}')

    def test_source_cannot_supply_reserved_receipt(self):
        (self.source / RECEIPT).write_text("untrusted receipt")
        with self.assertRaisesRegex(ValueError, "reserved"):
            self.install()
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_changed_copy_is_left_untracked_not_falsely_receipted(self):
        write_receipt = skillctl.write_receipt
        def changed_before_receipt(target, name, files, identity):
            (target / "SKILL.md").write_text("changed during copying")
            write_receipt(target, name, files, identity)
        with patch.object(skillctl, "write_receipt", side_effect=changed_before_receipt):
            with self.assertRaisesRegex(ValueError, "differs from preflight"):
                self.install()
        self.assertTrue((self.target / "SKILL.md").is_file())
        self.assertFalse((self.target / RECEIPT).exists())

    def test_cli_json_and_name_only_diff(self):
        self.install()
        (self.target / "private-note.md").write_text("do not print this content")
        output = io.StringIO()
        args = ["--repo", str(self.repo), "status", self.name, "--dest", str(self.dest)]
        with contextlib.redirect_stdout(output):
            self.assertEqual(skillctl.main(args + ["--json"]), 0)
        self.assertEqual(json.loads(output.getvalue())[0]["state"], "local-changed")
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(skillctl.main(args + ["--diff"]), 0)
        self.assertIn("private-note.md", output.getvalue())
        self.assertNotIn("do not print this content", output.getvalue())


if __name__ == "__main__":
    unittest.main()

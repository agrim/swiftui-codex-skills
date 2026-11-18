import contextlib
import hashlib
import io
import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skillctl
from skill_installation import RECEIPT, installation_status, write_receipt


class InstallationTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.repo = Path(temp.name).resolve()
        self.dest = self.repo / "installed"
        self.dest.mkdir()
        self.names = ["swiftui-navigation", "swift-concurrency"]
        shutil.copyfile(ROOT / "catalog.json", self.repo / "catalog.json")
        for name in self.names:
            shutil.copytree(ROOT / "skills" / name, self.repo / "skills" / name)
        self.source = self.repo / "skills" / self.names[0]
        self.target = self.dest / self.names[0]

    def status(self):
        return installation_status(self.repo, self.names[:1], self.dest)[0]

    def test_dry_run_then_install_records_copied_bytes(self):
        self.assertEqual(self.status()["state"], "missing")
        self.assertEqual(skillctl.install(self.repo, self.names, self.dest, dry_run=True), self.names)
        self.assertEqual(list(self.dest.iterdir()), [])
        skillctl.install(self.repo, self.names, self.dest)
        for name in self.names:
            with self.subTest(name=name):
                target = self.dest / name
                entry = (target / "SKILL.md").read_bytes()
                self.assertEqual(entry, (self.repo / "skills" / name / "SKILL.md").read_bytes())
                receipt = json.loads((target / RECEIPT).read_text())
                self.assertEqual(receipt["files"]["SKILL.md"], hashlib.sha256(entry).hexdigest())
        self.assertEqual(self.status()["state"], "current")

    def test_existing_install_preserves_edits_and_blocks_entire_batch(self):
        existing = self.dest / self.names[1]
        existing.mkdir()
        entry = existing / "SKILL.md"
        entry.write_text("local changes")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            skillctl.install(self.repo, self.names, self.dest)
        self.assertFalse(self.target.exists())
        self.assertEqual(entry.read_text(), "local changes")

    def test_missing_reference_in_later_skill_blocks_entire_batch(self):
        (self.repo / "skills" / self.names[1] / "references/concurrency-patterns.md").unlink()
        with self.assertRaisesRegex(ValueError, "reference"):
            skillctl.install(self.repo, self.names, self.dest)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_rejects_symlinks_in_source_or_destination_ancestry(self):
        alias = self.repo / "alias"
        alias.symlink_to(self.repo, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            skillctl.install(self.repo, self.names, alias / self.dest.name)
        (self.source / "external").symlink_to(self.repo / "catalog.json")
        with self.assertRaisesRegex(ValueError, "symlink"):
            skillctl.install(self.repo, self.names, self.dest)
        self.assertEqual(list(self.dest.iterdir()), [])

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX FIFO support")
    def test_rejects_special_file_before_copying(self):
        os.mkfifo(self.source / "stream")
        with self.assertRaisesRegex(ValueError, "special file"):
            skillctl.install(self.repo, self.names, self.dest)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_status_compares_local_and_source_edits_without_replacing_either(self):
        skillctl.install(self.repo, self.names[:1], self.dest)
        installed = self.target / "SKILL.md"
        installed.write_text("private local draft")
        self.assertEqual(self.status()["state"], "local-changed")
        source = self.source / "SKILL.md"
        source.write_text("published revision")
        status = self.status()
        self.assertEqual(status["state"], "both-changed")
        self.assertEqual(status["changes"]["modified"], ["SKILL.md"])
        self.assertFalse(status["matches_source"])

        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = skillctl.main(["--repo", str(self.repo), "status", self.names[0],
                                  "--dest", str(self.dest), "--diff"])
        self.assertEqual(code, 0)
        self.assertIn("SKILL.md", output.getvalue())
        self.assertNotIn("private local draft", output.getvalue())
        self.assertEqual(installed.read_text(), "private local draft")
        self.assertEqual(source.read_text(), "published revision")

    def test_legacy_install_has_no_claim_of_origin(self):
        shutil.copytree(self.source, self.target)
        status = self.status()
        self.assertEqual(status["state"], "untracked")
        self.assertTrue(status["matches_source"])
        self.assertFalse((self.target / RECEIPT).exists())

    def test_matching_an_upstream_edit_keeps_the_original_install_baseline(self):
        skillctl.install(self.repo, self.names[:1], self.dest)
        (self.source / "SKILL.md").write_text("new edition")
        self.assertEqual(self.status()["state"], "source-changed")
        (self.target / "SKILL.md").write_text("new edition")
        status = self.status()
        self.assertTrue(status["matches_source"])
        self.assertEqual(status["state"], "both-changed")

    def test_changed_bytes_cannot_receive_an_original_receipt(self):
        skillctl.install(self.repo, self.names[:1], self.dest)
        path = self.target / RECEIPT
        original = json.loads(path.read_text())
        path.unlink()
        (self.target / "SKILL.md").write_text("changed since preflight")
        with self.assertRaisesRegex(ValueError, "differs from preflight"):
            write_receipt(self.target, self.names[0], original["files"], original["source"])
        self.assertEqual(self.status()["state"], "untracked")


if __name__ == "__main__":
    unittest.main()

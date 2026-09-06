from __future__ import annotations

import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import skillctl


class InstallationPreflightTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        base = Path(self.temporary.name).resolve()
        self.repo = base / "repo"
        self.destination = base / "installed"
        self.destination.mkdir()
        self.names = ["swiftui-navigation", "swift-concurrency"]
        self.repo.mkdir()
        shutil.copyfile(ROOT / "catalog.json", self.repo / "catalog.json")
        for name in self.names:
            shutil.copytree(ROOT / "skills" / name, self.repo / "skills" / name)
        self.second = self.repo / "skills" / self.names[1]

    def assert_rejected_before_copy(self):
        for dry_run in (False, True):
            with self.subTest(dry_run=dry_run), self.assertRaises(ValueError):
                skillctl.install(self.repo, self.names, self.destination, dry_run)
            self.assertEqual(list(self.destination.iterdir()), [])

    def test_missing_later_source_does_not_install_first(self):
        shutil.rmtree(self.second)
        self.assert_rejected_before_copy()

    def test_missing_entrypoint_does_not_install_first(self):
        (self.second / "SKILL.md").unlink()
        self.assert_rejected_before_copy()

    def test_invalid_frontmatter_does_not_install_first(self):
        (self.second / "SKILL.md").write_text("not a skill")
        self.assert_rejected_before_copy()

    def test_wrong_identity_does_not_install_first(self):
        p = self.second / "SKILL.md"
        p.write_text(p.read_text().replace("name: swift-concurrency", "name: other"))
        self.assert_rejected_before_copy()

    def test_missing_reference_does_not_install_first(self):
        (self.second / "references/concurrency-patterns.md").unlink()
        self.assert_rejected_before_copy()

    def test_reference_directory_is_not_a_file(self):
        p = self.second / "references/concurrency-patterns.md"
        p.unlink()
        p.mkdir()
        self.assert_rejected_before_copy()

    def test_nested_symlink_does_not_install_first(self):
        (self.second / "extra.md").symlink_to(self.repo / "catalog.json")
        self.assert_rejected_before_copy()

    @unittest.skipUnless(hasattr(os, "mkfifo"), "requires POSIX FIFO support")
    def test_special_file_does_not_hang_copy(self):
        os.mkfifo(self.second / "stream")
        self.assert_rejected_before_copy()

    def test_empty_selection_rejected(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            skillctl.install(self.repo, [], self.destination)
        with self.assertRaisesRegex(ValueError, "at least one"):
            skillctl.bundle(self.repo, [])

    def test_successful_preflight_copies_all_selected_skills(self):
        self.assertEqual(skillctl.install(self.repo, self.names, self.destination), self.names)
        for name in self.names:
            self.assertEqual((self.destination / name / "SKILL.md").read_bytes(),
                             (self.repo / "skills" / name / "SKILL.md").read_bytes())


if __name__ == "__main__":
    unittest.main()

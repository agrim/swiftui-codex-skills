"""Exercise the build helper with a temporary project and an injected runner."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import apple_build


class BuildTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        (self.root / "My App.xcodeproj").mkdir()
        self.config = {"schema_version": 1, "project": "My App.xcodeproj", "scheme": "My App; Beta",
                       "configuration": "Debug", "destination": "generic/platform=iOS Simulator"}
        self.output = self.root / "evidence"
        self.runner = Mock()

    def run_build(self, authorized=True):
        return apple_build.execute(self.root, self.config, "build", self.output,
                                   authorized=authorized, runner=self.runner)

    def test_build_requires_opt_in(self):
        with patch.object(subprocess, "run") as runner:
            plan = apple_build.plan(self.root, self.config)
            runner.assert_not_called()
        self.assertEqual(plan["status"], "planned")
        with self.assertRaises(ValueError):
            self.run_build(authorized=False)
        self.runner.assert_not_called()
        self.assertEqual(sorted(p.name for p in self.root.iterdir()), ["My App.xcodeproj"])

    def test_build_refuses_existing_evidence(self):
        self.output.mkdir()
        log = self.output / "build.log"
        log.write_text("earlier run")
        with self.assertRaises(ValueError):
            self.run_build()
        self.runner.assert_not_called()
        self.assertEqual(log.read_text(), "earlier run")

    def test_project_cannot_escape_build_root(self):
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other).resolve() / "Other.xcodeproj"
            outside.mkdir()
            alias = self.root / outside.name
            alias.symlink_to(outside, target_is_directory=True)
            self.config["project"] = alias.name
            with self.assertRaises(ValueError):
                self.run_build()
        self.runner.assert_not_called()
        self.assertFalse(self.output.exists())

    def test_failed_build_records_command_diagnostics_and_exit_code(self):
        def failed(command, *, stdout, **kwargs):
            self.assertFalse(kwargs.get("shell", False))
            stdout.write("compile failed\n")
            return subprocess.CompletedProcess(command, 65)

        self.runner.side_effect = failed
        result = self.run_build()
        command = self.runner.call_args.args[0]
        self.assertEqual(command[1:5], ["-project", "My App.xcodeproj", "-scheme", "My App; Beta"])
        self.assertEqual(result["command"], command)
        self.assertEqual((result["status"], result["exit_code"]), ("failed", 65))
        self.assertEqual((self.output / "build.log").read_text(), "compile failed\n")
        self.assertEqual(json.loads((self.output / "result.json").read_text()), result)

    def test_timeout_retains_partial_diagnostics(self):
        def timed_out(command, *, stdout, timeout, **kwargs):
            stdout.write("started compiling\n")
            raise subprocess.TimeoutExpired(command, timeout)

        self.runner.side_effect = timed_out
        result = self.run_build()
        self.assertEqual((result["status"], result["exit_code"]), ("timed-out", None))
        self.assertEqual((self.output / "build.log").read_text(), "started compiling\n")


class BenchmarkTests(unittest.TestCase):
    def test_failed_attempts_are_reported_and_excluded_from_timings(self):
        contract = {key: "fixture" for key in
                    ("source", "toolchain", "destination", "configuration", "workload", "cache_policy")}
        samples = [{"phase": "no-op", "seconds": seconds, "exit_code": code}
                   for seconds, code in [(1, 0), (3, 0), (8, 0), (0.5, 65)]]
        summary = apple_build.summarize({"schema_version": 1, "contract": contract, "samples": samples})
        phase, = summary["phases"]
        self.assertEqual((phase["failed_count"], phase["sample_count"]), (1, 4))
        self.assertEqual((phase["min_seconds"], phase["median_seconds"], phase["max_seconds"]), (1, 3, 8))
        self.assertFalse(phase["meets_reporting_minimum"])


if __name__ == "__main__":
    unittest.main()

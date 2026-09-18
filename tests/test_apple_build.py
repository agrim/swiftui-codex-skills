"""No Apple tools or network required; exercise the executor through a fake."""
from __future__ import annotations

import copy
import importlib.util
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


class BuildContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / "My App.xcodeproj").mkdir()
        self.config = {"schema_version": 1, "project": "My App.xcodeproj", "scheme": "My App",
                       "configuration": "Debug", "destination": "generic/platform=iOS Simulator"}
        self.runner = Mock(return_value=subprocess.CompletedProcess([], 0))

    def run_build(self, **kwargs):
        return apple_build.execute(self.root, self.config, "build", self.root / "evidence",
                                   authorized=True, runner=self.runner, **kwargs)

    def test_plan_does_not_execute_or_write(self):
        before = list(self.root.iterdir())
        with patch.object(subprocess, "run", side_effect=AssertionError("must not run")):
            result = apple_build.plan(self.root, self.config)
        self.assertEqual(result["status"], "planned")
        self.assertEqual(before, list(self.root.iterdir()))

    def test_command_preserves_spaces_as_single_arguments(self):
        result = apple_build.plan(self.root, self.config)
        self.assertEqual(result["command"][2], "My App.xcodeproj")
        self.assertEqual(result["command"][4], "My App")

    def test_metacharacters_are_not_a_shell(self):
        self.config["scheme"] = "App; echo not-a-command"
        self.run_build()
        args, kwargs = self.runner.call_args
        self.assertIn("App; echo not-a-command", args[0])
        self.assertNotIn("shell", kwargs)

    def test_requires_explicit_authorization_before_writes(self):
        with self.assertRaises(ValueError):
            apple_build.execute(self.root, self.config, "build", self.root / "evidence", authorized=False,
                                runner=self.runner)
        self.assertFalse((self.root / "evidence").exists())
        self.runner.assert_not_called()

    def test_rejects_missing_project(self):
        self.config["project"] = "Missing.xcodeproj"
        with self.assertRaises(ValueError): self.run_build()
        self.runner.assert_not_called()

    def test_rejects_two_selectors(self):
        self.config["workspace"] = "App.xcworkspace"
        with self.assertRaises(ValueError): apple_build.plan(self.root, self.config)

    def test_rejects_path_escape(self):
        for path in ("../My App.xcodeproj", "/My App.xcodeproj", "./My App.xcodeproj"):
            with self.subTest(path=path):
                self.config["project"] = path
                with self.assertRaises(ValueError): apple_build.plan(self.root, self.config)

    def test_rejects_symlink_project(self):
        (self.root / "Alias.xcodeproj").symlink_to(self.root / "My App.xcodeproj", target_is_directory=True)
        self.config["project"] = "Alias.xcodeproj"
        with self.assertRaises(ValueError): apple_build.plan(self.root, self.config)

    def test_rejects_unknown_config_and_option_values(self):
        config = dict(self.config, extra_flags="-allowProvisioningUpdates")
        with self.assertRaises(ValueError): apple_build.plan(self.root, config)
        for bad in ("", "-allowProvisioningUpdates", "App\nOther", None, True):
            with self.subTest(bad=bad):
                config = dict(self.config, scheme=bad)
                with self.assertRaises(ValueError): apple_build.plan(self.root, config)

    def test_rejects_bool_schema_and_unavailable_actions(self):
        with self.assertRaises(ValueError): apple_build.plan(self.root, dict(self.config, schema_version=True))
        for action in ("clean", "archive", "install", "publish"):
            with self.subTest(action=action):
                with self.assertRaises(ValueError): apple_build.plan(self.root, self.config, action)

    def test_workspace_is_supported_without_guessing(self):
        (self.root / "All.xcworkspace").mkdir()
        config = dict(self.config); del config["project"]; config["workspace"] = "All.xcworkspace"
        self.assertEqual(apple_build.plan(self.root, config)["command"][1], "-workspace")

    def test_no_output_overwrite(self):
        (self.root / "evidence").mkdir()
        (self.root / "evidence" / "user.txt").write_text("keep")
        with self.assertRaises(ValueError): self.run_build()
        self.assertEqual((self.root / "evidence" / "user.txt").read_text(), "keep")

    def test_success_keeps_command_and_raw_output(self):
        def fake(command, **kwargs):
            kwargs["stdout"].write("raw diagnostics\n")
            return subprocess.CompletedProcess(command, 0)
        self.runner.side_effect = fake
        result = self.run_build()
        self.assertEqual(result["status"], "completed")
        self.assertEqual((self.root / "evidence" / "build.log").read_text(), "raw diagnostics\n")
        stored = json.loads((self.root / "evidence" / "result.json").read_text())
        self.assertEqual(stored, result)
        self.assertIn("Process result only", result["claim"])

    def test_failure_is_not_hidden(self):
        self.runner.return_value = subprocess.CompletedProcess([], 65)
        result = self.run_build()
        self.assertEqual((result["status"], result["exit_code"]), ("failed", 65))

    def test_timeout_retains_log_and_reports_no_exit_code(self):
        self.runner.side_effect = subprocess.TimeoutExpired(["xcodebuild"], 1)
        result = self.run_build(timeout=1)
        self.assertEqual(result["status"], "timed-out")
        self.assertIsNone(result["exit_code"])
        self.assertTrue((self.root / "evidence" / "build.log").exists())

    def test_missing_tool_is_not_success(self):
        self.runner.side_effect = FileNotFoundError("absent")
        result = self.run_build()
        self.assertEqual(result["status"], "launch-failed")
        self.assertEqual(result["launch_error"], "FileNotFoundError")

    def test_bad_timeout_is_rejected_before_creation(self):
        for value in (0, -1, float("nan"), float("inf"), True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError): self.run_build(timeout=value)
        self.assertFalse((self.root / "evidence").exists())


class BenchmarkTests(unittest.TestCase):
    def artifact(self):
        return {"schema_version": 1, "contract": {key: "fixture" for key in
                ("source", "toolchain", "destination", "configuration", "workload", "cache_policy")},
                "samples": [{"phase": "no-op", "seconds": n, "exit_code": 0} for n in [1, 3, 8]]}

    def test_median_and_spread_not_fastest_only(self):
        phase = apple_build.summarize(self.artifact())["phases"][0]
        self.assertEqual((phase["median_seconds"], phase["min_seconds"], phase["max_seconds"]), (3, 1, 8))

    def test_failed_samples_remain_visible(self):
        data = self.artifact(); data["samples"].append({"phase": "no-op", "seconds": 0.5, "exit_code": 65})
        phase = apple_build.summarize(data)["phases"][0]
        self.assertEqual(phase["failed_count"], 1)
        self.assertEqual(phase["sample_count"], 4)
        self.assertFalse(phase["meets_reporting_minimum"])

    def test_all_failures_produce_null_timing_not_zero(self):
        data = self.artifact()
        for sample in data["samples"]: sample["exit_code"] = 65
        self.assertIsNone(apple_build.summarize(data)["phases"][0]["median_seconds"])

    def test_phases_are_separate(self):
        data = self.artifact(); data["samples"].append({"phase": "clean", "seconds": 30, "exit_code": 0})
        phases = apple_build.summarize(data)["phases"]
        self.assertEqual(len(phases), 2)
        self.assertFalse(phases[0]["meets_reporting_minimum"])

    def test_nonfinite_bool_and_negative_samples_rejected(self):
        for number in (-1, float("nan"), float("inf"), True, "1"):
            with self.subTest(number=number):
                data = self.artifact(); data["samples"][0]["seconds"] = number
                with self.assertRaises(ValueError): apple_build.summarize(data)

    def test_incomplete_contract_and_empty_samples_rejected(self):
        data = self.artifact(); del data["contract"]["cache_policy"]
        with self.assertRaises(ValueError): apple_build.summarize(data)
        data = self.artifact(); data["samples"] = []
        with self.assertRaises(ValueError): apple_build.summarize(data)

    def test_extra_sample_fields_and_bool_exit_rejected(self):
        data = self.artifact(); data["samples"][0]["task_seconds"] = 100
        with self.assertRaises(ValueError): apple_build.summarize(data)
        data = self.artifact(); data["samples"][0]["exit_code"] = False
        with self.assertRaises(ValueError): apple_build.summarize(data)


if __name__ == "__main__":
    unittest.main()

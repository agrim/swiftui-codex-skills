"""Provenance is a contract, not a generated claim that every source was read."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import upstream_audit as audit
from skillctl import route


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "upstreams.json").read_text())

    def test_real_registry_and_generated_document(self):
        audit.validate(ROOT, self.data)
        self.assertEqual(audit.render(self.data), (ROOT / "docs/ecosystem.md").read_text())

    def test_duplicate_id_rejected(self):
        self.data["resources"].append(copy.deepcopy(self.data["resources"][0]))
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_unknown_skill_rejected(self):
        self.data["resources"][0]["maps_to"] = ["not-a-real-skill"]
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_empty_mapping_rejected(self):
        self.data["resources"][0]["maps_to"] = []
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_duplicate_mapping_rejected(self):
        self.data["resources"][0]["maps_to"] *= 2
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_non_string_mapping_is_rejected(self):
        self.data["resources"][0]["maps_to"] = [{}]
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_discovery_does_not_get_review_date(self):
        self.data["resources"][0]["status"] = "discovery-only"
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_review_requires_date(self):
        self.data["resources"][0].pop("reviewed")
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_bad_or_future_date_rejected(self):
        for value in ["2026-02-30", "2999-01-01", "2026-9-12", False]:
            with self.subTest(value=value):
                data = copy.deepcopy(self.data); data["inventory_date"] = value
                with self.assertRaises(ValueError): audit.validate(ROOT, data)

    def test_review_cannot_postdate_inventory(self):
        self.data["resources"][0]["reviewed"] = "2999-01-01"
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_unknown_status_rejected(self):
        self.data["resources"][0]["status"] = "fully-certified"
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_unknown_relation_rejected(self):
        self.data["resources"][0]["relation"] = "endorsed-by-apple"
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_credential_or_insecure_url_rejected(self):
        for value in ["http://example.com", "https://user:password@example.com", "file:///etc/hosts", "https://example.com/a b"]:
            with self.subTest(value=value):
                data = copy.deepcopy(self.data); data["resources"][0]["url"] = value
                with self.assertRaises(ValueError): audit.validate(ROOT, data)

    def test_blob_requires_full_hash_and_path(self):
        for value in ["latest", "abc123", None]:
            data = copy.deepcopy(self.data); data["resources"][0]["blob_sha"] = value
            with self.assertRaises(ValueError): audit.validate(ROOT, data)

    def test_remote_receipt_path_rejects_traversal(self):
        for value in ["../SKILL.md", "/absolute/SKILL.md", "skills\\SKILL.md"]:
            data = copy.deepcopy(self.data); data["resources"][0]["path"] = value
            with self.assertRaises(ValueError): audit.validate(ROOT, data)

    def test_missing_article_limitation_rejected(self):
        self.data["article"]["limitation"] = ""
        with self.assertRaises(ValueError): audit.validate(ROOT, self.data)

    def test_generated_output_deterministic(self):
        self.assertEqual(audit.render(self.data), audit.render(copy.deepcopy(self.data)))

    def test_all_current_plugin_entrypoints_accounted_for(self):
        ios = [r for r in self.data["resources"] if r["id"].startswith("openai-ios-")]
        mac = [r for r in self.data["resources"] if r["id"].startswith("openai-macos-")]
        self.assertEqual(len(ios), 9); self.assertEqual(len(mac), 11)
        self.assertTrue(all(r.get("blob_sha") for r in ios + mac))

    def test_all_six_build_specialists_accounted_for(self):
        rows = [r for r in self.data["resources"] if r["url"].endswith("/Xcode-Build-Optimization-Agent-Skill")]
        self.assertEqual(len(rows), 6)
        self.assertTrue(all(r["maps_to"] == ["xcode-build-optimization"] for r in rows))

    def test_directory_links_do_not_claim_reading(self):
        for row in self.data["resources"]:
            if row["relation"] == "directory-discovery":
                self.assertEqual(row["status"], "discovery-only")
                self.assertNotIn("reviewed", row)


class EcosystemRoutingTests(unittest.TestCase):
    def test_specialist_routes(self):
        fixtures = json.loads((ROOT / "evals/ecosystem-routing.json").read_text())
        for case in fixtures["cases"]:
            with self.subTest(query=case["query"]):
                matches = [item["id"] for item in route(ROOT, case["query"], 3)]
                self.assertIn(case["expected"], matches)


if __name__ == "__main__":
    unittest.main()

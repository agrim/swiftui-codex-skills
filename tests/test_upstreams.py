"""Check the public claims and file links in the provenance map."""
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import upstream_audit as audit
from skillctl import route


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / "upstreams.json").read_text())
        self.row = {
            "id": "example", "url": "https://github.com/example/project",
            "relation": "supporting-source", "status": "excerpt-reviewed",
            "scope": "Example file", "maps_to": ["swiftdata"], "reviewed": self.data["inventory_date"],
            "path": "skills/File #1.md", "blob_sha": "a" * 40, "commit_sha": "b" * 40,
        }
        self.data["resources"] = [self.row]

    def test_pin_links_to_the_reviewed_file(self):
        audit.validate(ROOT, self.data)
        url = f'{self.row["url"]}/blob/{self.row["commit_sha"]}/skills/File%20%231.md'
        self.assertIn(f']({url})', audit.render(self.data))
        del self.row["commit_sha"]
        audit.validate(ROOT, self.data)
        legacy = audit.render(self.data)
        self.assertIn(self.row["blob_sha"], legacy)
        self.assertNotIn("/blob/", legacy)

    def test_branch_name_cannot_pin_a_review(self):
        self.row["commit_sha"] = "main"
        with self.assertRaisesRegex(ValueError, "commit SHA"):
            audit.validate(ROOT, self.data)

    def test_discovery_cannot_claim_a_review_date(self):
        self.row["status"] = "discovery-only"
        with self.assertRaisesRegex(ValueError, "must not claim content review"):
            audit.validate(ROOT, self.data)

    def test_source_credentials_cannot_enter_published_url(self):
        self.row["url"] = "https://user:password@github.com/example/project"
        with self.assertRaisesRegex(ValueError, "credential-free"):
            audit.validate(ROOT, self.data)


class EcosystemRoutingTests(unittest.TestCase):
    def test_specialist_routes(self):
        fixtures = json.loads((ROOT / "evals/ecosystem-routing.json").read_text())
        for case in fixtures["cases"]:
            with self.subTest(query=case["query"]):
                matches = [item["id"] for item in route(ROOT, case["query"], 3)]
                self.assertIn(case["expected"], matches)


if __name__ == "__main__":
    unittest.main()

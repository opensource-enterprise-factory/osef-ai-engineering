import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from retrieve import load_corpus, retrieve, terms

CORPUS = Path(__file__).resolve().parents[1] / "data" / "synthetic-documents.json"


class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.docs = load_corpus(CORPUS)

    def test_rh_isolation(self):
        results = retrieve(self.docs, "RH", "réclamation virement congés formation", 10)
        self.assertTrue(all(not r["id"].startswith("OP-") for r in results))

    def test_operations_isolation(self):
        results = retrieve(self.docs, "OPERATIONS", "congés réclamation formation", 10)
        self.assertTrue(all(not r["id"].startswith("RH-") for r in results))

    def test_shared_docs(self):
        for group in ("RH", "OPERATIONS"):
            ids = [r["id"] for r in retrieve(self.docs, group, "support formation incident", 10)]
            self.assertIn("COM-002", ids)

    def test_citation(self):
        hit = retrieve(self.docs, "OPERATIONS", "virement", 3)[0]
        self.assertEqual(hit["citation"], f'{hit["id"]}@{hit["version"]}')

    def test_no_match(self):
        self.assertEqual(retrieve(self.docs, "RH", "zyxxyabcword", 3), [])

    def test_no_authorization(self):
        self.assertEqual(retrieve(self.docs, "ADMIN", "congés", 3), [])
        with self.assertRaises(ValueError):
            retrieve(self.docs, "", "congés", 3)

    def test_bad_top_k(self):
        with self.assertRaises(ValueError):
            retrieve(self.docs, "RH", "congés", 0)

    def test_unicode(self):
        self.assertIn("réclamation", terms("RÉCLAMATION !"))

    def test_duplicate_document(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "corpus.json"
            target.write_text(json.dumps(self.docs + [self.docs[0]]), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "Duplicate"):
                load_corpus(target)

    def test_acl_applied_before_scoring(self):
        baseline = retrieve(self.docs, "RH", "congés formation", 10)
        extra = {"id":"OP-NEW","title":"congés formation","version":"1.0","text":"congés formation","allowed_groups":["OPERATIONS"]}
        self.assertEqual(baseline, retrieve(self.docs + [extra], "RH", "congés formation", 10))


if __name__ == "__main__":
    unittest.main()

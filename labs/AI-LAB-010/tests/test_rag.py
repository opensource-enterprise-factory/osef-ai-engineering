import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from rag import load_docs, rank, answer, tokens


class BaselineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.docs = load_docs()

    def test_accent_tokens(self):
        self.assertIn("reclamation", tokens("réclamation"))

    def test_ops_retrieval(self):
        results = rank("réclamation virement", "OPERATIONS", self.docs)
        self.assertEqual(results[0]["id"], "OPS-001")

    def test_hr_retrieval(self):
        results = rank("attestation travail", "RH", self.docs)
        self.assertEqual(results[0]["id"], "RH-002")

    def test_acl_rh_never_ops(self):
        for q in ("virement réclamation", "ticket opérationnel", "congé"):
            self.assertTrue(all("RH" in d["groups"] for d in
                                rank(q, "RH", self.docs)))

    def test_acl_ops_never_hr(self):
        for q in ("attestation travail", "demande congé", "sécurité"):
            self.assertTrue(all("OPERATIONS" in d["groups"] for d in
                                rank(q, "OPERATIONS", self.docs)))

    def test_access_denied_scenario(self):
        response = answer("réclamation virement", "RH", self.docs)
        self.assertEqual(response["status"], "no_authorized_evidence")
        self.assertFalse(response["citations"])

    def test_answer_citations(self):
        response = answer("réclamation virement", "OPERATIONS", self.docs)
        self.assertEqual(response["citations"][0]["id"], "OPS-001")
        self.assertEqual(response["mode"], "extractive_baseline_not_llm")

    def test_unknown_question(self):
        response = answer("xylophone thermonucléaire", "RH", self.docs)
        self.assertEqual(response["status"], "no_authorized_evidence")

    def test_duplicate_id_fails(self):
        from tempfile import NamedTemporaryFile
        import json
        with NamedTemporaryFile(mode="w+", suffix=".json", encoding="utf-8") as f:
            json.dump([self.docs[0], self.docs[0]], f)
            f.flush()
            with self.assertRaises(ValueError):
                load_docs(f.name)

    def test_blank_group_fails(self):
        with self.assertRaises(ValueError):
            rank("bonjour", "", self.docs)

    def test_all_citations_are_authorized(self):
        for group in ("RH", "OPERATIONS"):
            for q in ("congé", "réclamation", "travail", "ticket"):
                hits = rank(q, group, self.docs)
                self.assertTrue(all(group in d["groups"] for d in hits))


if __name__ == "__main__":
    unittest.main()

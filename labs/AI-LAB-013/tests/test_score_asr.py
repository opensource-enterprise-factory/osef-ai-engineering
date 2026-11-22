import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from score_asr import edit_distance, normalize, score_rows


class ScoreASRTests(unittest.TestCase):
    def test_normalize_accents_and_punctuation(self):
        self.assertEqual(normalize("  ÉCOLE,  d'Abidjan! "), "école d abidjan")

    def test_distance(self):
        self.assertEqual(edit_distance(["bonjour", "monsieur"], ["bonjour"]), 1)
        self.assertEqual(edit_distance("chat", "chat"), 0)

    def test_exact_score(self):
        rows = [{"sample_id": "1", "reference": "Bonjour Abidjan",
                 "hypothesis": "bonjour abidjan", "variety": "synthetic",
                 "consent_confirmed": "yes"}]
        score = score_rows(rows)
        self.assertEqual(score["scores"]["all"]["wer"], 0)
        self.assertEqual(score["scores"]["all"]["cer"], 0)

    def test_deletion(self):
        rows = [{"sample_id": "1", "reference": "bonjour à tous",
                 "hypothesis": "bonjour tous", "variety": "synthetic",
                 "consent_confirmed": "yes"}]
        result = score_rows(rows)["scores"]["all"]
        self.assertAlmostEqual(result["wer"], 1 / 3)

    def test_duplicate_rejected(self):
        row = {"sample_id": "x", "reference": "a", "hypothesis": "a",
               "variety": "test", "consent_confirmed": "yes"}
        with self.assertRaises(ValueError):
            score_rows([row, row])

    def test_missing_consent_rejected(self):
        with self.assertRaises(ValueError):
            score_rows([{"sample_id": "1", "reference": "a",
                         "hypothesis": "a", "consent_confirmed": "no"}])

    def test_empty_reference_rejected(self):
        with self.assertRaises(ValueError):
            score_rows([{"sample_id": "1", "reference": "",
                         "hypothesis": "a", "consent_confirmed": "yes"}])

    def test_empty_dataset_rejected(self):
        with self.assertRaises(ValueError):
            score_rows([])


if __name__ == "__main__":
    unittest.main()

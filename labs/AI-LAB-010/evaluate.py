#!/usr/bin/env python3
"""Evaluation of synthetic, predeclared retrieval questions only."""
import json
from pathlib import Path
from rag import load_docs, rank

ROOT = Path(__file__).resolve().parent


def evaluate():
    questions = json.loads((ROOT / "evaluation.json").read_text(encoding="utf-8"))
    corpus = load_docs()
    correct = 0
    for sample in questions:
        hits = rank(sample["question"], sample["group"], corpus, limit=3)
        passed = any(d["id"] == sample["expected_id"] for d in hits)
        correct += passed
        print(("PASS" if passed else "FAIL") + " " + sample["expected_id"])
    if not questions:
        raise ValueError("empty evaluation")
    print("Recall@3 on synthetic test set: {}/{} = {:.1%}".format(
        correct, len(questions), correct / len(questions)))
    return correct == len(questions)


if __name__ == "__main__":
    raise SystemExit(0 if evaluate() else 1)

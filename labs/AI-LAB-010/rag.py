#!/usr/bin/env python3
"""AI-LAB-010: offline, lexical, ACL-filtered retrieval baseline, not an LLM."""
import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "synthetic_docs.json"
TERMS = {"le", "la", "les", "de", "des", "du", "un", "une", "et",
         "est", "en", "sur", "pour", "dans", "comment", "quelle",
         "quel", "quelles", "quels", "au", "aux", "à", "que",
         "qui", "doit", "on", "il", "elle", "nos", "notre"}


def tokens(s):
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return [t for t in re.findall(r"[a-z0-9]+", s) if t not in TERMS]


def load_docs(path=DATA_PATH):
    docs = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(docs, list) or not docs:
        raise ValueError("corpus must be a nonempty list")
    ids = set()
    for d in docs:
        if not isinstance(d, dict) or not all(
            isinstance(d.get(k), str) and d[k].strip()
            for k in ("id", "title", "text", "version")
        ):
            raise ValueError("invalid document")
        if d["id"] in ids:
            raise ValueError("duplicate document id")
        ids.add(d["id"])
        if not isinstance(d.get("groups"), list) or not d["groups"] or any(
            not isinstance(g, str) or not g for g in d["groups"]
        ):
            raise ValueError("invalid ACL")
    return docs


def rank(query, group, docs, limit=3):
    if not isinstance(group, str) or not group:
        raise ValueError("a test access group is required")
    if not query.strip():
        return []
    # Fail closed: authorization is checked BEFORE ranking and before passing text to answer().
    allowed = [d for d in docs if group in d["groups"]]
    query_terms = tokens(query)
    if not query_terms:
        return []
    q = set(query_terms)
    doc_tokens = [tokens(d["title"] + " " + d["text"]) for d in allowed]
    document_frequency = Counter(t for ts in doc_tokens for t in set(ts))
    results = []
    for doc, ts in zip(allowed, doc_tokens):
        tf = Counter(ts)
        score = sum((1.0 + math.log(tf[t])) *
                    math.log(1 + (len(allowed) + 1) / (1 + document_frequency[t]))
                    for t in q if tf[t])
        if score > 0:
            results.append((score, doc["id"], doc))
    results.sort(key=lambda x: (-x[0], x[1]))
    return [doc for _, _, doc in results[:limit]]


def answer(query, group, docs=None):
    docs = load_docs() if docs is None else docs
    results = rank(query, group, docs)
    if not results:
        return {"status": "no_authorized_evidence", "answer":
                "Aucune information pertinente dans les documents autorisés.",
                "citations": [], "mode": "extractive_baseline_not_llm"}
    # Explicit extractive answer: no LLM, no false claim of reasoning or synthesis.
    first = results[0]
    return {"status": "found", "answer": first["text"],
            "citations": [{"id": d["id"], "title": d["title"],
                           "version": d["version"]} for d in results],
            "mode": "extractive_baseline_not_llm"}


def main():
    p = argparse.ArgumentParser(description="OSEF offline ACL retrieval demonstration")
    p.add_argument("--group", choices=("RH", "OPERATIONS"), required=True,
                   help="Simulated group for testing; NOT authentication")
    p.add_argument("--question", required=True)
    p.add_argument("--corpus", type=Path, default=DATA_PATH)
    args = p.parse_args()
    print(json.dumps(answer(args.question, args.group, load_docs(args.corpus)),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

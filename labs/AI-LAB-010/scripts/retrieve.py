#!/usr/bin/env python3
"""Offline standard-library document retrieval demo with group-based ACLs.

Not an LLM or a production authorization system.
"""
import argparse
import json
import math
import re
import unicodedata
from collections import Counter
from pathlib import Path


def terms(text):
    normalized = unicodedata.normalize("NFKC", text).casefold()
    return re.findall(r"[^\W_]+", normalized, flags=re.UNICODE)


def load_corpus(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list) or not data:
        raise ValueError("Corpus must be a non-empty JSON array")
    ids = set()
    for doc in data:
        if not isinstance(doc, dict) or not all(k in doc for k in ("id", "title", "version", "text", "allowed_groups")):
            raise ValueError("Each document needs id,title,version,text,allowed_groups")
        if not all(isinstance(doc[k], str) and doc[k].strip() for k in ("id", "title", "version", "text")):
            raise ValueError("Document text fields must be non-empty strings")
        if doc["id"] in ids:
            raise ValueError("Duplicate document id")
        ids.add(doc["id"])
        groups = doc["allowed_groups"]
        if not isinstance(groups, list) or not groups or not all(isinstance(g, str) and g.strip() for g in groups):
            raise ValueError("allowed_groups must be a non-empty list of group names")
    return data


def retrieve(docs, group, query, top_k=3):
    if not isinstance(group, str) or not group.strip():
        raise ValueError("An authenticated group is required")
    if not isinstance(query, str) or not terms(query):
        return []
    if not isinstance(top_k, int) or top_k < 1:
        raise ValueError("top_k must be positive")
    # Authorization filter precedes scoring: unauthorized documents never reach ranking/results.
    authorized = [d for d in docs if group in d["allowed_groups"]]
    if not authorized:
        return []
    query_words = Counter(terms(query))
    counts = [Counter(terms(d["text"] + " " + d["title"])) for d in authorized]
    doc_freq = Counter(w for c in counts for w in c)
    n = len(authorized)
    results = []
    for doc, frequency in zip(authorized, counts):
        score = sum(
            min(q_count, frequency[word]) * (math.log((n + 1) / (doc_freq[word] + 1)) + 1)
            for word, q_count in query_words.items() if word in frequency
        )
        if score > 0:
            results.append({
                "id": doc["id"], "title": doc["title"], "version": doc["version"],
                "passage": doc["text"], "score": round(score, 5),
                "citation": f'{doc["id"]}@{doc["version"]}'
            })
    results.sort(key=lambda r: (-r["score"], r["id"]))
    return results[:top_k]


def main():
    parser = argparse.ArgumentParser(description="AI-LAB-010 lot 1: ACL-filtered document retrieval, no LLM")
    parser.add_argument("--corpus", default=str(Path(__file__).resolve().parents[1] / "data" / "synthetic-documents.json"))
    parser.add_argument("--group", required=True, choices=["RH", "OPERATIONS"])
    parser.add_argument("--query", required=True)
    parser.add_argument("--top-k", type=int, default=3)
    args = parser.parse_args()
    try:
        results = retrieve(load_corpus(args.corpus), args.group, args.query, args.top_k)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        parser.error(str(error))
    print(json.dumps({"group": args.group, "query": args.query, "results": results}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

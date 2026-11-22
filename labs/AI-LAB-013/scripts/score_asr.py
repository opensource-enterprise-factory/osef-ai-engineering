#!/usr/bin/env python3
"""Score transcriptions already produced by an ASR system; no model inference."""
import argparse
import csv
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path


REQUIRED = {"sample_id", "reference", "hypothesis", "variety", "consent_confirmed"}


def normalize(value):
    value = unicodedata.normalize("NFKC", value).lower()
    value = "".join(ch if ch.isalnum() or ch.isspace() else " " for ch in value)
    return " ".join(value.split())


def edit_distance(left, right):
    previous = list(range(len(right) + 1))
    for index, left_item in enumerate(left, start=1):
        current = [index]
        for j, right_item in enumerate(right, start=1):
            current.append(min(
                current[-1] + 1,
                previous[j] + 1,
                previous[j - 1] + (left_item != right_item),
            ))
        previous = current
    return previous[-1]


def score_rows(rows):
    totals = defaultdict(lambda: {"samples": 0, "word_errors": 0,
                                  "reference_words": 0, "char_errors": 0,
                                  "reference_chars": 0})
    seen = set()
    count = 0
    for row in rows:
        count += 1
        sample_id = (row.get("sample_id") or "").strip()
        if not sample_id or sample_id in seen:
            raise ValueError("missing or duplicate sample_id on row {}".format(count))
        seen.add(sample_id)
        if (row.get("consent_confirmed") or "").strip().lower() != "yes":
            raise ValueError("consent not confirmed on row {}".format(count))
        ref = normalize(row.get("reference") or "")
        hyp = normalize(row.get("hypothesis") or "")
        if not ref:
            raise ValueError("empty reference on row {}".format(count))
        group = (row.get("variety") or "").strip() or "unspecified"
        word_errors = edit_distance(ref.split(), hyp.split())
        char_errors = edit_distance(ref, hyp)
        for key in ("all", "variety:" + group):
            entry = totals[key]
            entry["samples"] += 1
            entry["word_errors"] += word_errors
            entry["reference_words"] += len(ref.split())
            entry["char_errors"] += char_errors
            entry["reference_chars"] += len(ref)
    if not count:
        raise ValueError("empty dataset")
    result = {}
    for key in sorted(totals):
        values = totals[key]
        result[key] = dict(values)
        result[key]["wer"] = values["word_errors"] / values["reference_words"]
        result[key]["cer"] = values["char_errors"] / values["reference_chars"]
    return {"status": "scoring_only_no_inference", "normalization": "NFKC_lowercase_punctuation_to_spaces",
            "scores": result}


def main():
    parser = argparse.ArgumentParser(description="Score consented ASR transcripts")
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path, help="JSON file (otherwise stdout)")
    args = parser.parse_args()
    try:
        with args.input.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            if not reader.fieldnames or not REQUIRED.issubset(reader.fieldnames):
                raise ValueError("required CSV fields: " + ", ".join(sorted(REQUIRED)))
            result = score_rows(reader)
        content = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
        if args.output:
            args.output.write_text(content, encoding="utf-8")
        else:
            print(content, end="")
    except (OSError, ValueError, csv.Error) as exc:
        print("ERROR: " + str(exc), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

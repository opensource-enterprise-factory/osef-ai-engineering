#!/usr/bin/env python3
"""Collect release metadata from official GitHub upstream repositories.

No LLM-generated facts, no secrets, no third-party package dependency.
The output is a *candidate* watch report, requiring human verification.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import pathlib
import sys
import urllib.error
import urllib.request

PROJECTS = {
    "Models & inference": ["vllm-project/vllm", "ollama/ollama", "huggingface/transformers"],
    "Data & MLOps": ["mlflow/mlflow", "huggingface/datasets", "langchain-ai/langchain"],
    "AI infrastructure": ["kserve/kserve", "ray-project/ray"],
    "AI security": ["protectai/llm-guard"],
}
BASE = pathlib.Path(__file__).resolve().parents[1]
UTC = dt.timezone.utc


def releases(repo: str) -> list[dict]:
    url = "https://api.github.com/repos/" + repo + "/releases?per_page=10"
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "osef-ai-watch/1.0",
               "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=20) as response:
        return json.load(response)


def generate(now: dt.datetime | None = None) -> tuple[pathlib.Path, int]:
    now = now or dt.datetime.now(UTC)
    start = now - dt.timedelta(hours=48)
    seen = set()
    found = []
    errors = []
    for category, repos in PROJECTS.items():
        for repo in repos:
            try:
                items = releases(repo)
                for item in items:
                    if item.get("draft") or item.get("prerelease"):
                        continue
                    when_str = item.get("published_at")
                    link = item.get("html_url")
                    if not when_str or not link or link in seen:
                        continue
                    when = dt.datetime.fromisoformat(when_str.replace("Z", "+00:00"))
                    if start <= when <= now:
                        seen.add(link)
                        found.append((when, category, repo, item.get("tag_name", ""), link))
            except (urllib.error.URLError, TimeoutError, ValueError, KeyError, json.JSONDecodeError) as exc:
                errors.append((repo, type(exc).__name__))
    found.sort(reverse=True)
    date = now.date().isoformat()
    out = BASE / "watch" / now.strftime("%Y") / now.strftime("%m") / (date + "-candidates.md")
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# OSEF AI Watch — candidates " + date,
        "",
        "> Collecte automatique de métadonnées upstream ; **non vérifiée éditorialement**.",
        "> Les entrées ne sont ni des recommandations de production ni une preuve de conformité OSAID.",
        "",
        "- Exécution UTC : " + now.strftime("%Y-%m-%d %H:%M"),
        "- Fenêtre : dernières 48 heures",
        "- Source : API GitHub Releases des dépôts officiels listés dans le script",
        "",
        "## Publications détectées",
        "",
    ]
    if found:
        for when, category, repo, tag, link in found:
            lines += ["- **" + category + "** — [" + repo + " " + tag + "](" + link + ")"
                      + " — publication " + when.strftime("%Y-%m-%d %H:%M UTC")]
    else:
        lines.append("Aucune release stable détectée sur les projets surveillés pendant cette fenêtre.")
    lines += ["", "## Contrôles avant publication", "",
              "- [ ] Consulter chaque source primaire et noter les changements réellement importants",
              "- [ ] Vérifier le type d'ouverture et la licence par version, sans confusion open weights / open source AI",
              "- [ ] Évaluer les impacts Data, infrastructure, sécurité et business pour l'Afrique francophone",
              "- [ ] Proposer les issues, labs, meetups ou contributions justifiés",
              "- [ ] Distinguer faits vérifiés, analyses et hypothèses", "",
              "## Couverture et limites", "",
              "Ce collecteur couvre seulement les releases GitHub des projets configurés. "
              "Il ne remplace pas une veille mondiale sur les publications scientifiques, "
              "les jeux de données, les politiques publiques, les fournisseurs cloud, "
              "les entreprises et communautés d'Afrique francophone.",
              ""]
    if errors:
        lines += ["### Erreurs de collecte (à investiguer)", ""]
        for repo, kind in errors:
            lines.append("- " + repo + ": " + kind)
        lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    return out, len(found)


if __name__ == "__main__":
    path, count = generate()
    print(f"{path.relative_to(BASE)} : {count} releases")

# AI-LAB-010 — Baseline retrieval documentaire avec ACL (22 novembre 2026)

**État :** première implémentation de laboratoire, à approuver via PR. Ce jalon n'est **pas encore un RAG complet** : aucun embedding ni LLM, aucun serveur web, aucun SSO, aucune garantie de sécurité production. Son but est de prouver et tester une chaîne **question → recherche lexicale filtrée par ACL → extrait sourcé** sans réseau ni dépendance externe.

## Objectif
Montrer un assistant documentaire **extractif** sur des procédures totalement fictives. Il s'agit de la base technique avant ingestion PDF/Word, index vectoriel et modèle génératif.

## Reproduire sur Python 3.10+
```bash
cd labs/AI-LAB-010
python3 rag.py --group OPERATIONS --question "Comment traiter une réclamation de virement ?"
python3 rag.py --group RH --question "Comment traiter une réclamation de virement ?"
python3 -m unittest discover -s tests -v
python3 evaluate.py
```

Aucune bibliothèque tierce, aucun secret, aucun fichier audio/document réel. La commande `--group` **simule** une appartenance, ce n'est **pas** une authentification : toute personne peut choisir le groupe en ligne de commande. Ne pas exposer l'outil à des données confidentielles.

## Données de laboratoire
- `data/synthetic_docs.json` : 6 procédures fictives, groupes RH / OPERATIONS et quelques documents communs ; toutes les procédures sont imaginaires et n'ont aucune valeur réglementaire.
- `evaluation.json` : 4 questions fictives dont les documents attendus sont définis.
- `rag.py` : tokenisation/normalisation, recherche pondérée dans les **seuls** documents autorisés, citation document/version et absence de réponse sans recouvrement.
- `evaluate.py` : Recall@3 sur le jeu synthétique uniquement.
- `tests/test_rag.py` : contrôles fonctionnels, ACL et erreurs de saisie.

## Architecture actuelle
```text
Question + groupe *simulé*
         |
       ACL avant retrieval ──> Documents synthétiques autorisés
         |
      Recherche lexicale pondérée
         |
      Extrait exact de la source + document/version
```

**Limites importantes :** le score est lexical, donc les synonymes et reformulations peuvent échouer ; il n'existe aucun filtrage sémantique, aucun modèle génératif, aucun contrôle IAM/SSO ni isolation de tenant déployée. Une recherche avec recouvrement lexical retourne éventuellement une source insuffisante ; les résultats doivent être revus. Tests ACL sur données fictives ne prouvent pas sécurité production.

## Mesures
`evaluate.py` affiche Recall@3 uniquement sur quatre exemples synthétiques. Ne pas généraliser le score à des documents réels, à des langues africaines ou à une performance produit. Latence, mémoire et coût doivent faire l'objet de benchmarks reproductibles ultérieurs ; aucun résultat chiffré de production n'est revendiqué.

## Roadmap vers un vrai RAG
- [ ] Charger PDF/Word et chunks avec citations de passage/page, versions et suppression.
- [ ] Ajouter un backend embeddings/index vectoriel, comparaison au baseline lexical.
- [ ] Intégrer un serveur LLM dont la licence et les poids sont vérifiés par version.
- [ ] Tester fidélité des réponses, abstention et résistance aux injections de prompt.
- [ ] Brancher SSO/IAM réel, contrôle d'accès **au retrieval** et isolation des locataires ; audit sécurité.
- [ ] Mesurer latence p50/p95, consommation CPU/RAM/GPU et TCO.
- [ ] Reproduire sur VM Ubuntu et ouvrir une PR évaluée par un autre ingénieur.

## Business OSEF
Ce lab appuie l'offre [Enterprise Knowledge AI](../../business/enterprise-knowledge/README.md), le [meetup #20](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/20) et le [funnel commercial](../../business/funnel/README.md) **après** validation technique, sans se présenter comme déploiement client.

## Sécurité et nettoyage
Aucun service persistant ni accès réseau. Supprimer les fichiers de cache Python après test avec `find . -type d -name __pycache__ -prune -exec rm -rf {} +` uniquement depuis ce répertoire de lab ; vérifier le chemin avant suppression.

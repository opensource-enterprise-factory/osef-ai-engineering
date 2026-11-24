# AI-LAB-010 — Lot 1 : recherche documentaire, ACL et citations

**Statut :** prototype de laboratoire soumis à revue, sans modèle IA génératif. Corpus entièrement fictif. Ce lot n'inclut ni embeddings, ni interface web, ni identité SSO. Il n'est **pas destiné à la production**.

## Fonctionnement
Corpus synthétique → **filtrage des documents autorisés** → recherche lexicale simple → passages et références `document-id@version`.

Le groupe `--group` est un **paramètre simulé et non authentifié**. Ne pas exposer cette CLI en service réseau : la sécurité d'un système réel nécessite une identité vérifiée côté serveur et une autorisation contrôlée à chaque requête.

## Prérequis
Python 3.10 ou plus récent, sans bibliothèque tierce. Aucune connexion réseau ni aucun GPU.

## Exécution depuis la racine du dépôt
```bash
python3 labs/AI-LAB-010/scripts/retrieve.py --group OPERATIONS --query "réclamation de virement"
python3 labs/AI-LAB-010/scripts/retrieve.py --group RH --query "congés annuels"
python3 labs/AI-LAB-010/scripts/retrieve.py --group RH --query "réclamation de virement"
python3 -m unittest discover -s labs/AI-LAB-010/tests -v
```

Le résultat est un JSON contenant le groupe simulé, la question et les passages classés. Chaque passage comporte une référence documentaire et un score lexical. Aucun score ne représente une mesure de qualité du RAG ou de précision métier.

## Critères de recette du lot 1
- [ ] Tests automatiques exécutés avec succès sur une autre machine et en CI GitHub.
- [ ] Un profil RH ne reçoit aucun document `OP-*`.
- [ ] Un profil OPERATIONS ne reçoit aucun document `RH-*`.
- [ ] Les documents communs restent accessibles aux deux profils.
- [ ] Les citations portent identifiant/version et les requêtes sans correspondance renvoient zéro résultat.
- [ ] Le relecteur confirme l'absence de documents réels, de secrets et de données personnelles.

## Limites
Corpus de seulement **6 documents** pour amorcer le lab (objectif ultérieur 20 à 50), recherche par mots et non sémantique, document entier utilisé comme passage, ACL de démonstration sans authentification, pas de suppression ni de révocation dynamique, citations sans numéro de page, pas de génération de réponses ni de métriques de latence/qualité de production.

## Étapes suivantes
Après revue : corpus synthétique plus riche ; séparation des passages ; authentification et autorisation effectives ; tests de révocation ; index vectoriel/embeddings si adaptés ; modèle génératif et abstention ; évaluation quality/security/performance documentée.

**Issues associées :** [AI-LAB-010 #14](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14) et [AI-BIZ-006 #31](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/31).

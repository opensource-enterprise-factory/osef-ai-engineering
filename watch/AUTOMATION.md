# Publication automatique de candidats (GitHub Actions)

La tâche ChatGPT quotidienne de synthèse, lorsqu'elle est active, est **distincte** de ce collecteur GitHub.

## Ce qui est automatisé
- Workflow `.github/workflows/ai-watch.yml` programmé à 08:15 UTC (cron GitHub Actions, susceptible de retards).
- Exécution de `scripts/ai_watch.py` sans dépendances tierces.
- Lecture des releases stables de dépôts GitHub officiellement configurés, sur les dernières 48 heures.
- Création d'une fiche **candidats non vérifiés** dans `watch/YYYY/MM/`.
- Création d'une Pull Request de revue. Aucun auto-merge.

## Mise en service
1. Dans Settings > Actions > General du dépôt, autoriser les Actions GitHub si nécessaire.
2. Autoriser GitHub Actions à créer des Pull Requests et vérifier les permissions du jeton GITHUB_TOKEN.
3. Lancer manuellement le workflow une première fois avec **Run workflow**.
4. Examiner le journal, vérifier que la PR est proposée et faire relire la fiche.
5. Si GitHub bloque l'ouverture des PR, le workflow signale une erreur : ne pas prétendre que la publication est opérationnelle.

## Limites
- Ce n'est pas une veille exhaustive : seules les releases de la liste du script sont collectées.
- Une PR ne prouve ni sécurité, ni qualité, ni licence, ni conformité OSAID.
- Les thèmes Africa, Business et Data au-delà des releases doivent être enrichis manuellement ou par des collecteurs supplémentaires avec sources primaires.
- Les horaires GitHub Actions peuvent dériver ; n'en déduire aucune garantie SLA.
- Aucun accès aux données client, à une API payante ou à des secrets supplémentaires n'est nécessaire.

## Revue humaine
Compléter une fiche validée à partir de [TEMPLATE](TEMPLATE.md), puis créer une issue lab / meetup / business si pertinent.

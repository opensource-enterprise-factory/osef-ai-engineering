# 03 — Protocole d'acceptation, qualité et sécurité

**Aucune valeur cible n'est présentée ici comme résultat.** Les seuils doivent être fixés avec le client **avant** le POC.

## Jeu d'évaluation
- Au moins un ensemble de questions factuelles vérifiables par source.
- Questions sans réponse dans le corpus : le système doit pouvoir exprimer l'incertitude.
- Questions avec documents périmés, contradictoires ou supprimés.
- Deux groupes fictifs (A, B) avec accès disjoints ; un groupe n'a jamais droit aux passages du second.
- Données synthétiques et réponses de référence, versionnées et sans informations personnelles.

## Mesures
| Dimension | Mesure | Condition d'acceptation proposée |
|---|---|---|
| Retrieval | recall@k / MRR selon protocole | seuil négocié, score réel publié |
| Citations | correspondance passage-source | vérification manuelle sur échantillon |
| Qualité | exactitude / fidélité à la source | grille humaine, désaccords conservés |
| Confidentialité | fuite de passages inter-groupes | **aucune fuite dans le corpus de test défini** |
| Refus | réponse hors documentation | taux et erreurs détaillés |
| Performance | latence p50/p95, erreurs, débit | seuil dépendant du matériel et du cas d'usage |
| Coût | infra + ingénierie + support | hypothèses et facture/mesures distinctes |
| Résilience | indisponibilité index/modèle et reprise | reprise selon runbook et objectif du POC |
| Cycle documentaire | suppression + nouvelle indexation | anciennes données non accessibles aux utilisateurs tests |

## Tests de sécurité obligatoires
1. Authentification et contrôle d'accès **au retrieval**, tests croisés A/B.
2. Marqueurs synthétiques pour vérifier qu'aucune réponse ne révèle les ressources interdites.
3. Injection de prompt dans un document fictif ; vérifier que l'instruction non fiable ne donne pas de privilège.
4. Logs : pas de données sensibles ou de secrets, rotation/redaction vérifiées.
5. Dépendances et modèles : empreintes et licences enregistrées par version.
6. Tests de mise à jour, retrait des droits et suppression d'un document.

## Go / No-Go
**GO** seulement si aucune fuite n'est observée dans les scénarios de contrôle définis, si la qualité et la latence atteignent les seuils négociés, et si les risques résiduels sont acceptés par des décideurs habilités. L'absence de fuite observée ne prouve pas l'absence absolue de vulnérabilité.

**NO-GO** si contrôle d'accès uniquement dans un prompt, erreurs de source non maîtrisées, sortie de données sans droits, ou support promis sans capacité.

## Livrable de recette
Tableau des tests, versions, jeux de données, configuration, preuves, incidents et décisions. Les noms et données du client demeurent dans son espace privé.

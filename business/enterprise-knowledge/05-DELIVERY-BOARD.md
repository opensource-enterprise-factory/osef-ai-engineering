# 05 — Organisation d'équipe, RACI et tableau de livraison

**Rôles proposés, non attribués :** responsable commercial (BIZ), référent AI/Data (AI), responsable sécurité (SEC), responsable exploitation (OPS), sponsor client (CLI). Les responsabilités contractuelles finales doivent être approuvées.

## Matrice RACI indicative
| Activité | BIZ | AI | SEC | OPS | CLI |
|---|---|---|---|---|---|
| Qualification et budget | R | C | I | I | A |
| Définir les données et droits | C | R | C | I | A |
| Architecture et prototype | I | A/R | C | C | C |
| Tests sécurité / conformité technique | I | R | A | C | C |
| SLA, monitoring et exploitation | C | C | C | A/R | C |
| Recette fonctionnelle et décision de production | C | R | C | C | A |

**RACI :** R = réalise, A = décide/valide, C = consulté, I = informé. Le schéma est une proposition, non un mandat à la place du client.

## Backlog prêt à déléguer
| Ordre | Livrable | Issue existante | Owner |
|---|---|---|---|
| 1 | Valider persona, cas d'usage et conditions de découverte | [#31](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/31) | À désigner |
| 2 | Définir corpus synthétique, ACL et tests de recherche | [#14](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14) | À désigner |
| 3 | Réaliser démo reproductible (non encore réalisée) | [#14](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14) | À désigner |
| 4 | Vérifier isolation, secrets, injection de prompt | [#15](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15) | À désigner |
| 5 | Construire coûts et proposition de service | [#33](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/33) | À désigner |
| 6 | Présenter au moins 5 entretiens ciblés (objectif, non résultat) | [#32](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/32) | À désigner |

## Routine hebdomadaire
- Lundi ou créneau retenu : 30 min revue business + 30 min revue technique.
- Identifier blocages, dépendances et revues PR, sans merge sans approbation.
- Statut des tâches : À faire / En cours / En revue / Validé / Bloqué.
- Mesures : entretiens réellement tenus, POC acceptés, labs reproduits, coûts direct observés. « Non mesuré » par défaut.

## Critères avant un rendez-vous DSI
- Démo contrôlée prête ou clairement annoncée comme prototype non exécuté.
- Argumentaire ciblé sur problème métier, pas sur le prestige d'un modèle.
- Preuves, limites et responsabilités disponibles.
- Prochaine action proposée : diagnostic borné, non engagement de production.

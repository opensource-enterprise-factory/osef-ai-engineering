# OSEF AI Engineering

Engineering ouvert, reproductible et orienté entreprise pour l'écosystème IA en Afrique francophone.

> **Statut** : programme en construction. Les propositions de labs, benchmarks et offres ne constituent pas des résultats validés.

## Périmètre
- **Open Models** : distinguer Closed AI, Open Weights, Open Code, Open Data et **Open Source AI** selon l'[OSAID 1.0](https://opensource.org/ai/open-source-ai-definition). Vérifier chaque version et licence, sans assimiler automatiquement poids ouverts à Open Source.
- **Data** : gouvernance, ingestion, qualité, RAG, provenance, jeux de données africains légalement utilisables.
- **Infrastructure** : GPU, CPU, réseau, stockage, Kubernetes et serving.
- **Platforms** : MLOps, LLMOps, inference, observabilité et résilience.
- **Security** : accès, isolation, évaluation des risques, tests de sécurité et conformité.
- **Business** : coûts, tarification, offres managées, partenariats cloud providers.
- **Community** : meetups, documentation et contributions upstream.

## Navigation
| Répertoire | Objet |
|---|---|
| [watch/](watch/README.md) | Protocole de veille quotidienne |
| [models/](models/README.md) | Taxonomie et évaluations |
| [data/](data/README.md) | AI Data Engineering |
| [infrastructure/](infrastructure/README.md) | Compute et déploiement |
| [platforms/](platforms/README.md) | MLOps / LLMOps |
| [security/](security/README.md) | AI Security |
| [labs/](labs/README.md) | Labs AI-001 à AI-006 |
| [meetups/](meetups/README.md) | Programme de rencontres |
| [business/](business/README.md) | Chaîne de valeur et offres B2B |
| [upstream/](upstream/README.md) | Contributions externes |

## Règles d'ingénierie
1. Chaque lab doit être reproductible, documenté, vérifiable, traçable et sans secrets embarqués.
2. Préférer les jeux de données synthétiques ou explicitement autorisés, jamais de données client réelles dans ce dépôt public.
3. Identifier les licences et versions exactes des dépendances et modèles.
4. Appliquer les principes Twelve-Factor lorsque pertinents (configuration externalisée, logs, stateless, environnements).
5. Aucun chiffre de benchmark, promesse de conformité ou affirmation commerciale sans protocole, preuves et limites.
6. Revoir les contributions via pull request et tests ; ne pas pousser directement un résultat non validé comme « prêt pour la production ».

## Programme de départ
- AI-001 : licences, artefacts et Open Source AI Definition.
- AI-002 : serving et benchmark des ressources.
- AI-003 : pipeline RAG, évaluation et qualité des données.
- AI-004 : LLMOps, observabilité, régression et rollback.
- AI-005 : tests de sécurité et contrôles d'accès.
- AI-006 : coûts et modèle économique Private AI.

**Cadrage stratégique** : [OSEF-AI-STRAT-001](https://github.com/opensource-enterprise-factory/opensource-enterprise-factory.github.io/issues/13).

**OSEF** : https://osef.africascaler.com

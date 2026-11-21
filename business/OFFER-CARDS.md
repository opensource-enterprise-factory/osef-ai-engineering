# Fiches commerciales candidates — OSEF AI

> Versions de travail : offres non lancées et prix non déterminés. Les services sont à contractualiser après capacité réelle et contrôle des licences.

## 1. OSEF AI Data Foundation
**Client :** DSI, CDO, équipes Data. **Problème :** documents et données non fiabilisés pour les cas d'usage IA.
**Diagnostic :** inventaire sources, permissions, qualité, résidence, critères métier.
**Pilote :** pipeline RAG avec corpus de démonstration autorisé, évaluation retrieval et fidélité, documentation.
**Production :** ingestion, supervision, contrôles d'accès, politique de mise à jour, support.
**Mesures :** couverture documentaire, erreurs, latence p95, coût unitaire, incidents.
**Liens :** [AI-LAB-010](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14).

## 2. OSEF Private AI Platform
**Client :** DSI et cloud provider. **Problème :** exécuter un modèle sans dépendance exclusive à une API tierce.
**Diagnostic :** modèles/versions/licences, volume de requêtes, architecture, contraintes sécurité.
**Pilote :** inference API, authentification, quotas, observabilité, load test, rollback.
**Production :** MLOps/LLMOps, SLA, patching, escalade, facturation.
**Mesures :** p95, tokens/s, utilisation GPU, disponibilité, coût par requête.
**Liens :** [AI-LAB-008](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/12), [AI-LAB-012](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/16).

## 3. OSEF AI Trust & Operations
**Client :** RSSI, Risk, DSI. **Problème :** risques des assistants, agents et données.
**Diagnostic :** politiques, flux de données, accès, journaux, modèle de menaces.
**Pilote :** tests défensifs d'injection de prompt, permissions, isolation, réponses incident.
**Production :** contrôle continu, régressions, remédiations et documentation.
**Mesures :** tests passés, temps de détection/remédiation, exceptions approuvées.
**Liens :** [AI-LAB-011](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15).

## 4. AI Infrastructure Engineering
**Client :** opérateurs cloud, ESN, datacenters. **Problème :** dimensionnement et coûts d'inférence.
**Livrables :** architecture de référence CPU/GPU, benchmark sur matériel autorisé, supervision, pratiques d'exploitation.
**Mesures :** coût par million tokens, p95, disponibilité, efficacité de la capacité.

## 5. Industry AI Solutions
**Client :** banques, assureurs, télécoms. **Problème :** automatisation documentée de processus à faible risque.
**Livrables :** pilote sur données synthétiques, validation métier et plan de gouvernance ; aucune promesse d'homologation.

## 6. AI Training & Advisory
**Client :** DSI, ingénieurs, OSPO. **Livrables :** atelier, formation et lab privé reproduit ; évaluation des compétences et guide de transfert.

## Questions obligatoires avant proposition commerciale
1. Quel cas d'usage et quel gain mesurable ?
2. Où sont les données et qui a le droit d'y accéder ?
3. Quel budget, calendrier et sponsor ?
4. Quels volumes, métriques de qualité et latence cible ?
5. Quels critères d'acceptation d'un POC ?
6. Qui porte coûts cloud/GPU, responsabilité, SLA et sécurité ?
7. Quelles restrictions des licences des modèles/datasets ?

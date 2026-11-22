# 02 — Architecture cible et backlog MVP

## Architecture logique

```text
Collaborateur ──> UI ──> SSO/Identity ──> API RAG ──> Requête autorisée
                                             │
                            ┌────────────────┴─────────────────┐
                            ▼                                  ▼
                    Retriever/ACL                       Service d'inférence
                            │                                  │
                      Index vectoriel                         │
                            │                                  │
                      Passages sourcés ───────> Génération + citations
                            │
                       Sources originales

Administrateur autorisé ──> Ingestion ──> parsing ──> classification/ACL
                                           │
                                      embeddings/index
```

**Point de sécurité non négociable :** les autorisations doivent être appliquées **avant** la remise de passages au modèle. Un filtre uniquement dans le prompt ne constitue pas un contrôle d'accès.

## Stack candidate, à fixer par PR après audit
- Document extraction : Python + Apache Tika pour formats pris en charge ; respecter restrictions sur fichiers et formats.
- Index/recherche : PostgreSQL + pgvector ou OpenSearch ; vérifier fonctions et contrôle d'accès requis.
- Orchestration RAG : Haystack ou implémentation Python minimale, versionnée.
- Modèle d'embeddings et modèle de génération : sélection via AI-001, licence/version, langue, empreinte mémoire, exigences de privacy.
- Identité : intégration IAM existante ; compte de test local uniquement pour prototype isolé.
- Observabilité : OpenTelemetry, Prometheus/Grafana selon besoin, sans journaliser les documents sensibles.

## Backlog MVP (aucune fonctionnalité implémentée par ce document)
- [ ] Corpus synthétique de 20–50 documents versionnés avec identifiants, ACL et dates.
- [ ] Deux groupes fictifs et une ressource réservée à chaque groupe.
- [ ] Extraction et segmentation déterministes, avec liens vers fichier/page/passage.
- [ ] Recherche avec filtre d'ACL au niveau du retriever.
- [ ] Génération avec citations vérifiables et réponse « information insuffisante ».
- [ ] Suppression et réindexation effectives d'un document.
- [ ] Export des métriques retrieval, qualité, p95, tokens et coût d'inférence si applicable.
- [ ] Tests d'échec de moteur, document malformé, index indisponible et rétablissement.
- [ ] Procédure Docker/VM Ubuntu reproductible, secrets hors dépôt.

## Principes 12-Factor applicables
Configuration par environnement, dépendances déclarées, journaux structurés sans secrets, processus stateless là où pertinent, reproductibilité et séparation build/release/run.

## Réversibilité
Inventaire des formats exportables : documents sources (selon droits), métadonnées/ACL, index reconstructible, modèles et versions, scripts de réindexation, procédures de suppression et backup/restore.

## Liens
[AI-LAB-010](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14) ; [AI-LAB-011](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15).

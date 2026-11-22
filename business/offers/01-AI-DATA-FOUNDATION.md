# Offre OSEF AI Data Foundation — Enterprise Knowledge AI

> **Version :** 22 novembre 2026 · **Statut :** offre candidate à qualifier commercialement, non annoncée comme disponible · **Priorité :** P1 : première offre à qualifier. Les exemples sont fictifs et ne sont pas des références clients.

## 1. Proposition de valeur
**Acheteurs et bénéficiaires :** DSI, CDO, directions opérations, RH et conformité (banques, assurances, télécoms, ESN, entreprises multisites).

**Problème à résoudre :** Les informations nécessaires aux collaborateurs sont dispersées entre GED, PDF, Word, ERP et intranets ; les accès et les versions ne sont pas toujours harmonisés.

**Bénéfice à démontrer :** Accès plus rapide à la documentation, respect des droits et meilleure traçabilité, à démontrer par un pilote ; aucune promesse de gain de productivité sans mesure.

**Exemple illustratif (non déployé) :** Un service interne recherche une procédure de réclamation ; l'assistant retrouve les passages autorisés, fournit une réponse citée et permet la vérification humaine. Les erreurs et refus d'accès sont mesurés.

## 2. Parcours de livraison et livrables
### Phase A — Diagnostic / cadrage contractuel
1. Cartographier les documents, sources et droits existants.
2. Identifier 20 à 50 questions représentatives et leurs réponses documentées.
3. Vérifier propriété, provenance, conservation, localisation et mises à jour.

**Livrables attendus :** note de cadrage, inventaire des sources et contraintes, hypothèses de coût et risques, critères d'acceptation du pilote.

### Phase B — POC payant et borné
1. Corpus autorisé, synthétique si possible ; extraction et indexation ; retrieval et génération avec citations.
2. SSO/IAM ou identité de test, isolation par utilisateur/dossier et test de suppression de document.
3. Mesure de retrieval@k, fidélité des réponses, p95, taux de refus et coût par requête.

**Livrables attendus :** architecture de test, scripts et versions, démonstration documentée, résultats mesurés ou limites, décision go/no-go explicite.

### Phase C — Production (seulement après acceptation)
1. Pipelines de synchronisation contrôlés, versioning des index et suppression effective.
2. Surveillance, sauvegardes et restauration, gestion d'incidents, contrôle des habilitations.
3. Revue périodique qualité et base de connaissances, formation et transfert de compétences.

**Livrables attendus :** architecture revue, sécurité et droits, runbooks, supervision, support et réversibilité selon contrat.

## 3. Technologies ouvertes candidates
Apache Tika / Python ; PostgreSQL+pgvector ou OpenSearch ; Haystack ou LangChain ; modèles autorisés et serveur d'inférence adapté ; Keycloak/IAM existant ; OpenTelemetry. Choix et licences à qualifier.

**Règle :** vérifier modèle, poids, code, datasets, licences et restrictions **par version** ; « poids ouverts » ne signifie pas nécessairement « Open Source AI » selon OSAID 1.0. La stack proposée n'a pas été auditée comme solution intégrée OSEF.

## 4. Critères de succès / KPI
Retrieval@k, précision des citations, fidélité évaluée humainement, fuite entre corpus (objectif zéro aux tests définis), latence p95, taux d'erreurs, coût par requête.

Comparer à une situation de référence documentée. N'annoncer ni économies, ni précision, ni sécurité ni satisfaction client avant mesure.

## 5. Périmètre et exclusions
Aucune ingestion de documents sans droits ; pas d'accès inter-clients ; aucune décision bancaire automatisée ; pas de garantie d'absence d'hallucinations.

Le lieu de traitement, les flux transfrontaliers, la confidentialité, la propriété des livrables et les garanties sont à examiner selon la juridiction et le contrat.

## 6. Modèle de revenus
Diagnostic au forfait → POC payé sur corpus borné → intégration au projet → contrat de maintenance mensuel ; refacturation cloud selon contrat.

**Politique commerciale :** prix seulement après étude du coût direct, des responsabilités et des contraintes client. Fourchettes **exploratoires** dans [le catalogue](../COMMERCIAL-CATALOGUE.md). Aucune vente ni partenariat présumé.

## 7. Préparation commerciale
- [ ] Sponsor et décideur identifiés dans un CRM **privé** (aucun nom ou email dans GitHub public).
- [ ] Problème métier, volume, budget, calendrier et coût du statu quo documentés.
- [ ] Architecture, données, provenance, licences et responsabilités examinées.
- [ ] Démonstration reproductible et résultats réellement obtenus.
- [ ] Devis avec livrables, exclusions, critères d'acceptation, coûts et taxes selon pays.
- [ ] Capacité support et SLA réellement tenables ; clauses revues juridiquement.
- [ ] Décision de lancement prise et tracée, sinon offre maintenue au stade pilote.

## 8. Veille → Lab → Meetup → Business
- **Labs :** [AI-LAB-010 #14](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14), [AI-LAB-011 #15](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15).
- **Meetups :** [AI-MEETUP-005 #20](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/20).
- **Issues business :** [AI-BIZ-002 #23](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/23), [AI-BIZ-006 #31](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/31).
- **Docs transversaux :** [Plan 90 jours](../GO-TO-MARKET-90D.md), [Playbook DSI](../DSI-SALES-PLAYBOOK.md), [Modèles devis/support](../QUOTE-AND-SUPPORT-TEMPLATES.md), [Routine et KPI](../SALES-OPERATING-RHYTHM.md).

## 9. Sources méthodologiques
- [OSI — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Linux Foundation Research — State of Commercial Open Source 2026](https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source)

Les sources soutiennent les critères généraux de gouvernance, d'ouverture et de business Open Source ; **elles ne valident pas les prix, la demande locale ni les performances d'OSEF**.

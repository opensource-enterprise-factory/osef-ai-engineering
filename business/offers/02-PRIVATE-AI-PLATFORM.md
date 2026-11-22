# Offre OSEF Private AI Platform — hébergement et exploitation

> **Version :** 22 novembre 2026 · **Statut :** offre candidate à qualifier commercialement, non annoncée comme disponible · **Priorité :** P1/P2 : après validation d'un pilote technique. Les exemples sont fictifs et ne sont pas des références clients.

## 1. Proposition de valeur
**Acheteurs et bénéficiaires :** DSI, CTO, entreprises réglementées, ESN et fournisseurs cloud.

**Problème à résoudre :** Les organisations veulent intégrer des modèles IA dans leur SI sans dépendre exclusivement d'une API extérieure et souhaitent des coûts, droits d'accès, disponibilité et versions maîtrisés.

**Bénéfice à démontrer :** Contrôle opérationnel des modèles et flux ; capacité de support et de réversibilité mesurée, sans prétendre automatiquement à la souveraineté juridique ou à la conformité sectorielle.

**Exemple illustratif (non déployé) :** Une assurance déploie une API d'inférence privée pour assister les gestionnaires ; l'API est authentifiée, observée et intégrée à une application métier de test.

## 2. Parcours de livraison et livrables
### Phase A — Diagnostic / cadrage contractuel
1. Volumétrie, p95 visée, usage simultané, exigences disponibilité et durée de conservation.
2. Architecture client/cloud et responsabilités d'exploitation, localisation et sous-traitants.
3. Inventaire des modèles, versions, licences et restrictions d'utilisation commerciale.

**Livrables attendus :** note de cadrage, inventaire des sources et contraintes, hypothèses de coût et risques, critères d'acceptation du pilote.

### Phase B — POC payant et borné
1. Choisir modèle et moteur compatibles ; déployer sur VM ou Kubernetes selon volumétrie.
2. Installer API Gateway, authentification, quotas, logs minimisés et métriques.
3. Test de charge, incidents simulés, stratégie de rollback et coût de revient.

**Livrables attendus :** architecture de test, scripts et versions, démonstration documentée, résultats mesurés ou limites, décision go/no-go explicite.

### Phase C — Production (seulement après acceptation)
1. Runbooks de patch, versions et sécurité ; CI/CD/PR et gestion des secrets.
2. SLA, gestion des incidents, sauvegardes, capacité et réversibilité contractualisés.
3. Revues mensuelles performances, qualité, coût, risques et conformité.

**Livrables attendus :** architecture revue, sécurité et droits, runbooks, supervision, support et réversibilité selon contrat.

## 3. Technologies ouvertes candidates
vLLM, llama.cpp ou Ollama selon compatibilité ; Kubernetes/KServe lorsque justifiés ; Keycloak/SSO, Prometheus/Grafana/OpenTelemetry ; IaC/Ansible. Vérifier versions, maturité, licences et infrastructure.

**Règle :** vérifier modèle, poids, code, datasets, licences et restrictions **par version** ; « poids ouverts » ne signifie pas nécessairement « Open Source AI » selon OSAID 1.0. La stack proposée n'a pas été auditée comme solution intégrée OSEF.

## 4. Critères de succès / KPI
Débit, latence p50/p95, time-to-first-token, VRAM/RAM, disponibilité mesurée, coût par requête / million de tokens, délais de rétablissement.

Comparer à une situation de référence documentée. N'annoncer ni économies, ni précision, ni sécurité ni satisfaction client avant mesure.

## 5. Périmètre et exclusions
Pas d'achat ou de garantie GPU OSEF sans contrat ; pas de SLA 24/7 sans astreinte financée ; hébergement privé ne prouve ni souveraineté ni conformité.

Le lieu de traitement, les flux transfrontaliers, la confidentialité, la propriété des livrables et les garanties sont à examiner selon la juridiction et le contrat.

## 6. Modèle de revenus
Audit + installation/intégration + exploitation managée mensuelle + optimisations et mises à jour ; partenariat cloud possible après signature.

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
- **Labs :** [AI-LAB-008 #12](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/12), [AI-LAB-012 #16](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/16).
- **Meetups :** [AI-MEETUP-003 #18](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/18), [AI-MEETUP-007 #22](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/22).
- **Issues business :** [AI-BIZ-003 #24](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/24), [AI-BIZ-004 #25](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/25).
- **Docs transversaux :** [Plan 90 jours](../GO-TO-MARKET-90D.md), [Playbook DSI](../DSI-SALES-PLAYBOOK.md), [Modèles devis/support](../QUOTE-AND-SUPPORT-TEMPLATES.md), [Routine et KPI](../SALES-OPERATING-RHYTHM.md).

## 9. Sources méthodologiques
- [OSI — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Linux Foundation Research — State of Commercial Open Source 2026](https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source)

Les sources soutiennent les critères généraux de gouvernance, d'ouverture et de business Open Source ; **elles ne valident pas les prix, la demande locale ni les performances d'OSEF**.

# Offre OSEF AI Infrastructure Engineering — performance et coût

> **Version :** 22 novembre 2026 · **Statut :** offre candidate à qualifier commercialement, non annoncée comme disponible · **Priorité :** P2 : provider et DSI dotés d'infrastructure. Les exemples sont fictifs et ne sont pas des références clients.

## 1. Proposition de valeur
**Acheteurs et bénéficiaires :** Cloud providers, hébergeurs, DSI, ESN et responsables plateformes/SRE.

**Problème à résoudre :** Le coût et la capacité des plateformes IA sont mal compris : modèles incompatibles, GPU sous-utilisés, mémoire insuffisante, latence et coût réseau/stockage.

**Bénéfice à démontrer :** Dimensionnement fondé sur mesures de charge, arbitrage entre performance, coût, sécurité et résilience ; économies non promises sans preuve.

**Exemple illustratif (non déployé) :** Un provider veut ajouter un service d'inférence à son catalogue ; OSEF mesure ce qui fonctionne sur ses machines existantes, puis propose une architecture et un runbook de support.

## 2. Parcours de livraison et livrables
### Phase A — Diagnostic / cadrage contractuel
1. Inventorier GPU/CPU, VRAM, stockage, réseau, stack de virtualisation/Kubernetes et coûts réels.
2. Choisir 2 ou 3 profils de charge et engagements métier.
3. Déterminer responsabilités cloud/OSEF/client et résidence des données.

**Livrables attendus :** note de cadrage, inventaire des sources et contraintes, hypothèses de coût et risques, critères d'acceptation du pilote.

### Phase B — POC payant et borné
1. Benchmark versions de moteurs et modèles compatibles, quantification et concurrency.
2. Instrumenter CPU/GPU, mémoire, bande passante, cache, latence, incidents et consommation énergétique si instrumentée.
3. Tester charge nominale, pic, panne partielle et récupération.

**Livrables attendus :** architecture de test, scripts et versions, démonstration documentée, résultats mesurés ou limites, décision go/no-go explicite.

### Phase C — Production (seulement après acceptation)
1. Automatiser déploiements, observabilité, capacité et rollback.
2. Optimiser allocations, cache/stockage, tests de performance lors des montées de version.
3. Formaliser catalogue managé, SLA et plans de croissance avant co-vente.

**Livrables attendus :** architecture revue, sécurité et droits, runbooks, supervision, support et réversibilité selon contrat.

## 3. Technologies ouvertes candidates
Kubernetes, KServe, vLLM, llama.cpp, Valkey pour certains caches applicatifs, OpenTelemetry/Prometheus/Grafana, Terraform/Ansible selon contexte ; aucune promesse de compatibilité des GPU sans test.

**Règle :** vérifier modèle, poids, code, datasets, licences et restrictions **par version** ; « poids ouverts » ne signifie pas nécessairement « Open Source AI » selon OSAID 1.0. La stack proposée n'a pas été auditée comme solution intégrée OSEF.

## 4. Critères de succès / KPI
Coût par million de tokens, tokens/s, latence p95, VRAM, débit réseau, consommation, taux d'utilisation, rétablissement après incident.

Comparer à une situation de référence documentée. N'annoncer ni économies, ni précision, ni sécurité ni satisfaction client avant mesure.

## 5. Périmètre et exclusions
Ne pas présenter une PR upstream comme une fonctionnalité stable ; ne pas assimiler cache applicatif Valkey à cache KV de LLM sans architecture spécifique ; OSEF n'achète pas par défaut les GPU.

Le lieu de traitement, les flux transfrontaliers, la confidentialité, la propriété des livrables et les garanties sont à examiner selon la juridiction et le contrat.

## 6. Modèle de revenus
Audit de capacité → benchmark facturé → plateforme déployée → optimisation et opérations managées ; white-label et partage de revenus uniquement négociés.

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
- **Labs :** [AI-LAB-008 #12](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/12), [AI-LAB-009 #13](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/13).
- **Meetups :** [AI-MEETUP-003 #18](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/18), [AI-MEETUP-004 #19](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/19).
- **Issues business :** [AI-BIZ-004 #25](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/25), [AI-BIZ-003 #24](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/24).
- **Docs transversaux :** [Plan 90 jours](../GO-TO-MARKET-90D.md), [Playbook DSI](../DSI-SALES-PLAYBOOK.md), [Modèles devis/support](../QUOTE-AND-SUPPORT-TEMPLATES.md), [Routine et KPI](../SALES-OPERATING-RHYTHM.md).

## 9. Sources méthodologiques
- [OSI — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Linux Foundation Research — State of Commercial Open Source 2026](https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source)

Les sources soutiennent les critères généraux de gouvernance, d'ouverture et de business Open Source ; **elles ne valident pas les prix, la demande locale ni les performances d'OSEF**.

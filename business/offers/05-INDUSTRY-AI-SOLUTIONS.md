# Offre OSEF Industry AI Solutions — applications métiers sectorielles

> **Version :** 22 novembre 2026 · **Statut :** offre candidate à qualifier commercialement, non annoncée comme disponible · **Priorité :** P2/P3 : un vertical après validation de la fondation. Les exemples sont fictifs et ne sont pas des références clients.

## 1. Proposition de valeur
**Acheteurs et bénéficiaires :** Directeurs métiers et DSI des banques, assurances, télécoms, services et entreprises multisites.

**Problème à résoudre :** Les équipes veulent résoudre un problème opérationnel concret — procédures, réclamations, analyse de dossier, support, investigation assistée — plutôt qu'acheter une technologie IA abstraite.

**Bénéfice à démontrer :** Application et intégration à un workflow métier, tests de qualité et ROI mesuré sur l'usage défini ; décisions sensibles conservées sous contrôle humain.

**Exemple illustratif (non déployé) :** Assistant de support interne ; transcription et aide à l'agent de centre d'appels ; préparation de synthèses de dossiers assurantiels ; investigation humaine assistée à partir d'alertes de fraude.

## 2. Parcours de livraison et livrables
### Phase A — Diagnostic / cadrage contractuel
1. Cartographier un processus métier borné et ses coûts actuels.
2. Identifier données, systèmes d'intégration, autorisations et validations métier.
3. Établir tests d'acceptation métier et besoins sectoriels/juridiques.

**Livrables attendus :** note de cadrage, inventaire des sources et contraintes, hypothèses de coût et risques, critères d'acceptation du pilote.

### Phase B — POC payant et borné
1. Prototyper sur données fictives/autorisées et contrôler les réponses.
2. Construire connecteurs en mode lecture seule d'abord, contrôle d'accès et journalisation.
3. Évaluer exactitude métier, temps de traitement, taux de corrections humaines, erreurs et cas hors périmètre.

**Livrables attendus :** architecture de test, scripts et versions, démonstration documentée, résultats mesurés ou limites, décision go/no-go explicite.

### Phase C — Production (seulement après acceptation)
1. Revue risques et responsabilités de l'application, circuit humain de validation.
2. Tests de régression et déploiement par étapes avec rollback.
3. Formation utilisateurs, support, amélioration du workflow et revues de performance.

**Livrables attendus :** architecture revue, sécurité et droits, runbooks, supervision, support et réversibilité selon contrat.

## 3. Technologies ouvertes candidates
RAG, modèles d'extraction et ASR à licence vérifiée, API d'entreprise, moteurs de workflow ; selon le secteur, intégration à outils paiement/fraude open source uniquement après revue licences, conformité et sécurité.

**Règle :** vérifier modèle, poids, code, datasets, licences et restrictions **par version** ; « poids ouverts » ne signifie pas nécessairement « Open Source AI » selon OSAID 1.0. La stack proposée n'a pas été auditée comme solution intégrée OSEF.

## 4. Critères de succès / KPI
Précision par cas métier, taux d'escalade humaine, temps de résolution, incidents, latence, coûts, satisfaction sur échantillon mesuré.

Comparer à une situation de référence documentée. N'annoncer ni économies, ni précision, ni sécurité ni satisfaction client avant mesure.

## 5. Périmètre et exclusions
Aucune décision automatique de crédit/paiement/fraude ou conformité sans autorisation et analyse spécifiques ; aucune promesse d'homologation par régulateur.

Le lieu de traitement, les flux transfrontaliers, la confidentialité, la propriété des livrables et les garanties sont à examiner selon la juridiction et le contrat.

## 6. Modèle de revenus
Conseil métier et cadrage → POC par cas d'usage → intégration applicative → contrat d'évolution et de support.

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
- **Labs :** [AI-LAB-010 #14](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14), [AI-LAB-013 #27](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/27).
- **Meetups :** [AI-MEETUP-005 #20](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/20), [AI-MEETUP-008 #28](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/28).
- **Issues business :** [AI-BIZ-002 #23](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/23), [AI-BIZ-006 #31](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/31).
- **Docs transversaux :** [Plan 90 jours](../GO-TO-MARKET-90D.md), [Playbook DSI](../DSI-SALES-PLAYBOOK.md), [Modèles devis/support](../QUOTE-AND-SUPPORT-TEMPLATES.md), [Routine et KPI](../SALES-OPERATING-RHYTHM.md).

## 9. Sources méthodologiques
- [OSI — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Linux Foundation Research — State of Commercial Open Source 2026](https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source)

Les sources soutiennent les critères généraux de gouvernance, d'ouverture et de business Open Source ; **elles ne valident pas les prix, la demande locale ni les performances d'OSEF**.

# Offre OSEF AI Trust & Security — sécurisation et gouvernance

> **Version :** 22 novembre 2026 · **Statut :** offre candidate à qualifier commercialement, non annoncée comme disponible · **Priorité :** P1/P2 : complément transverse aux déploiements. Les exemples sont fictifs et ne sont pas des références clients.

## 1. Proposition de valeur
**Acheteurs et bénéficiaires :** RSSI, DSI, responsables risques, audit interne, cloud providers et directions conformité.

**Problème à résoudre :** Les systèmes IA peuvent révéler des informations, exécuter des actions non autorisées ou dépendre de modèles/datasets mal documentés ; l'organisation manque de preuves de maîtrise des risques.

**Bénéfice à démontrer :** Risques documentés, contrôles testés et procédure de remédiation vérifiable ; pas de certification ou homologation promise.

**Exemple illustratif (non déployé) :** Une banque souhaite contrôler qu'un agent connecté à une base documentaire ne traverse pas les périmètres d'accès et n'exécute pas d'action non autorisée via ses outils.

## 2. Parcours de livraison et livrables
### Phase A — Diagnostic / cadrage contractuel
1. Identifier données, composants, versions, flux, fournisseurs, utilisateurs et outils disponibles à l'agent.
2. Construire modèle de menaces, exigences métier et politique de sécurité.
3. Vérifier licences des poids, code et datasets ; localiser les données et accès.

**Livrables attendus :** note de cadrage, inventaire des sources et contraintes, hypothèses de coût et risques, critères d'acceptation du pilote.

### Phase B — POC payant et borné
1. Tests défensifs sur environnement autorisé et données fictives : injections de prompt, isolement, exfiltration simulée.
2. Politiques d'accès minimales, authentification/rotation, contrôles de sortie et observabilité.
3. Rapport de constats avec reproductibilité, gravité argumentée et remédiations.

**Livrables attendus :** architecture de test, scripts et versions, démonstration documentée, résultats mesurés ou limites, décision go/no-go explicite.

### Phase C — Production (seulement après acceptation)
1. Tests de non-régression après mise à jour modèles et prompts.
2. Surveillance des actions, réponse à incident, revue périodique fournisseurs, secrets et permissions.
3. Registre des risques, procédures d'escalade, revue des preuves et gouvernance.

**Livrables attendus :** architecture revue, sécurité et droits, runbooks, supervision, support et réversibilité selon contrat.

## 3. Technologies ouvertes candidates
Référentiels NIST AI RMF, OWASP LLM Top 10, OSI OSAID 1.0 ; IAM/SSO ; outils de journaux et observabilité ; tests propres aux applications. Ce sont des aides à la démarche, pas un label de certification.

**Règle :** vérifier modèle, poids, code, datasets, licences et restrictions **par version** ; « poids ouverts » ne signifie pas nécessairement « Open Source AI » selon OSAID 1.0. La stack proposée n'a pas été auditée comme solution intégrée OSEF.

## 4. Critères de succès / KPI
Contrôles exécutés et passés/échoués, couverture des chemins critiques, violations d'isolation, incidents, délai de remédiation, taux de régression.

Comparer à une situation de référence documentée. N'annoncer ni économies, ni précision, ni sécurité ni satisfaction client avant mesure.

## 5. Périmètre et exclusions
Aucune attestation de conformité automatique, aucun pentest hors mandat, aucune collecte de données réelles en dépôt public.

Le lieu de traitement, les flux transfrontaliers, la confidentialité, la propriété des livrables et les garanties sont à examiner selon la juridiction et le contrat.

## 6. Modèle de revenus
Audit ponctuel → correction/renforcement au projet → suivi périodique et tests de non-régression sous contrat.

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
- **Labs :** [AI-LAB-011 #15](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15), [AI-LAB-007 #11](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/11).
- **Meetups :** [AI-MEETUP-006 #21](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/21), [AI-MEETUP-002 #17](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/17).
- **Issues business :** [AI-BIZ-005 #26](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/26).
- **Docs transversaux :** [Plan 90 jours](../GO-TO-MARKET-90D.md), [Playbook DSI](../DSI-SALES-PLAYBOOK.md), [Modèles devis/support](../QUOTE-AND-SUPPORT-TEMPLATES.md), [Routine et KPI](../SALES-OPERATING-RHYTHM.md).

## 9. Sources méthodologiques
- [OSI — Open Source AI Definition 1.0](https://opensource.org/ai/open-source-ai-definition)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Linux Foundation Research — State of Commercial Open Source 2026](https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source)

Les sources soutiennent les critères généraux de gouvernance, d'ouverture et de business Open Source ; **elles ne valident pas les prix, la demande locale ni les performances d'OSEF**.

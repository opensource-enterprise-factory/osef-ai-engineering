# OSEF AI — Business Model & Positionnement (proposition)

**Établi :** 21 novembre 2026. **Statut :** hypothèses à valider, aucune vente, marge, capacité GPU ni partenariat confirmé par ce document.

## Positionnement
OSEF comme **Open Source AI Engineering & Managed Services Partner** pour les entreprises, banques, assurances, ESN, télécommunications et cloud providers d'Afrique francophone. Ne pas supposer que tous les modèles à poids ouverts sont Open Source AI.

## Chaîne de valeur / opportunités
| Couche | Besoin client | Activité OSEF | Modèle de revenus candidat |
|---|---|---|---|
| Data | qualité, gouvernance, données exploitables | audit, pipelines, RAG, évaluation | forfait intégration + maintenance |
| Models | choisir modèle/licence adaptée | audit Open Weights/OSAID, évaluation | audit + adaptation |
| Infra | déployer sans surdimensionnement | sizing GPU/CPU, Kubernetes, observabilité | projet + exploitation |
| Platform | SLA, cycle de vie et résilience | serving, LLMOps, sauvegarde, rollback | support et services managés |
| Security | réduire risques et fuites | auth, isolation, red teaming défensif, conformité | audit + suivi |
| Applications | cas d'usage mesurables | assistants, RAG, workflow, applications de fraude | pilote + intégration |

## Offres initiales à qualifier
1. **AI Data Foundation** : diagnostic, corpus autorisé, pipeline, gouvernance et RAG ; commencer par un pilote.
2. **Private AI Platform** : installation privée / cloud partenaire, modèles autorisés, API, monitoring, coûts et runbooks.
3. **AI Trust & Operations** : revue de licences, contrôles, isolation, disponibilité, suivi.
4. **AI Infrastructure Engineering** : sizing et optimisation d'une infrastructure existante, sans achat de GPU par OSEF en phase initiale.
5. **Industry AI Solutions** : cas d'usage métiers, avec métriques et validation métier.
6. **AI Training & Advisory** : formations et labs privatifs, programme DSI/OSPO.

## Un parcours commercial type
**Veille sourcée → Lab reproductible → Meetup éducatif → Qualification DSI / CTO → Diagnostic payant ou cadrage contractuel → POC avec critères d'acceptation → Déploiement → Contrat de support.**

Un meetup n'est pas une qualification commerciale automatique. Éviter d'utiliser des données sensibles ou des noms de clients dans le dépôt public.

## Pricing à construire (aucun tarif publié)
- **Audit** : effort estimé × taux journalier + frais justifiés.
- **Projet** : charge de travail et dépendances + provision de risques négociée.
- **Managé** : charge infra + GPU/CPU + stockage + observabilité + astreintes/SLA + sécurité + marge cible.
- **Usage** : coût fixe/volume prévu + coût variable par requête ou million de tokens + marge de risque, sous réserve de mesure.

### Paramètres nécessaires pour une offre
Taille des modèles ; licence exacte ; résidence des données ; disponibilité ; utilisateurs simultanés ; requêtes/tokens par jour ; p95 cible ; coût des instances ; prix de l'électricité si auto-hébergement ; coûts d'ingénierie/support ; exigence de réversibilité.

## Priorités 90 jours (hypothèses)
- **J1–30** : choisir 2 personas DSI / cloud provider, conduire au moins 5 entretiens, figer 2 cas d'usage, rédiger la fiche AI Data Foundation.
- **J31–60** : reproduire AI-LAB-010 et AI-LAB-012, mesurer coût/latence/qualité, construire démonstration.
- **J61–90** : présenter 2 offres pilotes à partenaires prospects, négocier périmètre et responsabilités, mesurer conversion et retour.

## Règles de validation
- Pas de tarifs ni de prévisions présentés comme des faits sans hypothèses sourcées.
- Pas d'affirmation de conformité OSAID, légale ou réglementaire sans audit par version / juridiction.
- Pas d'affiliation avec cloud provider sans accord.
- Contrat : confidentialité, propriété des données, responsabilités, licences, sécurité, SLA et plan de sortie.

## Sources
- Linux Foundation Research, *The State of Commercial Open Source 2026* : https://www.linuxfoundation.org/research/2026-state-of-commercial-open-source
- NIST AI RMF : https://www.nist.gov/itl/ai-risk-management-framework
- OSI Open Source AI Definition : https://opensource.org/ai/open-source-ai-definition
- OSEF AI Watch partenariat : ../watch/2026/11/AI-WATCH-20261121-03.md
- Issue de pilotage : https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/8

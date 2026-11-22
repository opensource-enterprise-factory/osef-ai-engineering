# Catalogue commercial OSEF AI — versions pilotes

**Ce document est un brouillon d'offre**, sans engagement public de disponibilité ni prix contractuel. Tous les montants sont en **FCFA (XOF), hors taxes et frais externes**, hypothèses à confirmer après 5 à 10 entretiens commerciaux et calcul des coûts directs. Ne sont **pas** des prix moyens du marché.

## Offre 1 — Enterprise Knowledge AI (priorité)
**Promesse conditionnelle :** donner aux collaborateurs un accès contrôlé à une base documentaire, avec réponses citées et possibilités de vérification humaine.

**Acheteurs cibles :** DSI, direction opérations, RH, conformité.
**Périmètre diagnostic :** cartographie des sources, classification et droits d'accès, qualité des documents, critères de succès et contraintes de sécurité.
**POC :** corpus autorisé (synthétique par défaut), ingestion, index/retrieval, citation de sources, limites explicites, tests de non-fuite entre périmètres et mesure de la qualité.
**Production (à contractualiser) :** connecteurs, gestion des identités, journalisation, mise à jour et suppression documentaire, sauvegardes, support.
**Exclusions par défaut :** ingestion non autorisée de documents clients, génération de décisions réglementaires automatisées, garantie d'exactitude parfaite.
**Mesures d'acceptation :** jeu de questions métier validé ; qualité retrieval/réponses ; p95 ; isolation ; tests de mise à jour et suppression.
**Labs :** [AI-LAB-010](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/14) et [AI-LAB-011](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15).

## Offre 2 — Private AI Platform
**Acheteurs cibles :** DSI, CTO, providers, entreprises à exigences particulières.
**Diagnostic :** volume de requêtes, localisation des données, versions et licences modèles, SLA demandé, coûts infrastructure.
**POC :** serveur d'inférence, authentification, quotas, télémétrie, déploiement reproductible, test de panne.
**Production :** correctifs, gestion des secrets, rotation, observabilité, escalade, réversibilité et maintenance.
**Exclusions :** investissement GPU pris en charge par OSEF et homologation réglementaire, sauf disposition contractuelle distincte.
**Mesures :** débit, temps de première réponse, latence p95, coûts par requête, disponibilité.
**Labs :** [AI-LAB-008](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/12), [AI-LAB-012](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/16).

## Offre 3 — AI Trust & Operations
**Acheteurs cibles :** RSSI, DSI, direction risques.
**Diagnostic :** flux et provenance des données, licences, IAM, journaux, prompt injection, dépendances, modèle de menace.
**Livraison :** rapport de risques priorisés, plan de remédiation, tests défensifs, runbooks, suivi si mandaté.
**Exclusions :** certification et attestation de conformité non autorisées.
**Mesures :** couverture des contrôles testés, remédiations vérifiées, délais d'incidents, risques résiduels.
**Lab :** [AI-LAB-011](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/15).

## Tarifs indicatifs à tester — aucune vente confirmée
| Service | Fourchette de validation commerciale | Conditions |
|---|---:|---|
| Diagnostic initial | 1–3 M FCFA | Périmètre et durée bornés |
| POC RAG | 3–8 M FCFA | Données autorisées, critères d'acceptation |
| Déploiement Private AI | 8–25 M FCFA | Infrastructure cloud/GPU hors forfait sauf devis |
| Support / exploitation | 0,5–3 M FCFA/mois | SLA, heures et volumes à préciser |
| Audit sécurité IA | 2–6 M FCFA | Référentiel et périmètre fixés |
| Formation intra-entreprise | 0,75–2,5 M FCFA/session | Participants et durée définis |

**Formule de prix à chiffrer** = charge ingénieur + infrastructure + licences/fournisseurs + sécurité + support/SLA + risques opérationnels + marge cible. Distinguer HT/TTC et TVA selon pays, contrats et fiscalité applicables.

## Go / No Go avant signature
- [ ] Cas d'usage et sponsor identifiés
- [ ] Données et droits d'usage documentés
- [ ] Licences des modèles et composants vérifiées **par version**
- [ ] Coûts directs et marge calculés avec hypothèses datées
- [ ] Livrables, exclusions et acceptation décrits
- [ ] Clauses de confidentialité, responsabilité, sécurité et sortie revues
- [ ] Capacité d'exploitation et SLA vérifiés ; sinon prestation limitée au pilote

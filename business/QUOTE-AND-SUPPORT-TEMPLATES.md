# OSEF AI — Modèles de devis, lettre de mission et support

**Brouillons non contractuels.** À adapter par un juriste compétent dans le pays du client avant usage. Aucun SLA, certification, clause RGPD locale, pénalité ou fiscalité n'est présumé applicable.

## A. Devis type — Diagnostic / POC
| Champ | Valeur à remplir |
|---|---|
| Référence / date | [DEVIS-XXXX] / [date] |
| Prestataire / client | [raison sociale et identifiants — **hors GitHub public**] |
| Objet | [ex. diagnostic RAG privé] |
| Périmètre | [nombre de sources, utilisateurs tests, environnements] |
| Hors périmètre | [données non autorisées, production, infrastructure non prévue] |
| Durée / planning | [jalons contractuels] |
| Livrables | [architecture, rapport, scripts, documentation] |
| Acceptation | [tests, qualité, approbation, délais de revue] |
| Coût ingénierie | [jours × taux HT validé] |
| Infrastructure | [volume × prix vérifié, refacturé ou fourni par client] |
| Déplacements et sous-traitants | [si applicables] |
| Taxes | [à déterminer selon juridiction] |
| Total | [calcul approuvé] |
| Paiement | [jalons et conditions négociés] |
| Validité du devis | [date] |

### Exemple ARITHMÉTIQUE fictif, sans valeur de marché
5 jours × 300 000 FCFA/jour = **1 500 000 FCFA de main-d'œuvre HT**, avant hébergement, taxes, risques et autres frais. Ce n'est pas un devis envoyé, accepté ou exécuté.

## B. Structure d'une lettre de mission POC
1. Parties et représentants autorisés.
2. Objet, contexte et définitions : données, modèle/version, environnement, service.
3. Périmètre, exclusions, livrables, jalons, responsabilités et critères d'acceptation.
4. Sécurité, accès, confidentialité, droits sur données et documents ; gestion des sous-traitants.
5. Droits de propriété intellectuelle, composants et licences Open Source/poids ouverts.
6. Environnement d'hébergement, flux transfrontaliers et contraintes sectorielles à analyser.
7. Conditions financières, facturation, taxes, frais externes et contrôle du dépassement.
8. Résiliation, restitution/suppression, sauvegarde et réversibilité.
9. Responsabilité, garanties limitées, incidents, force majeure, droit applicable et règlement des litiges — **à négocier juridiquement**.
10. Validation et signatures.

## C. Annexe de support managé (SLA à NÉGOCIER)
| Élément | À déterminer avant engagement |
|---|---|
| Service couvert | [API, pipeline, monitoring, connecteurs, stockage] |
| Heures de couverture | [jours/heures/fuseau] |
| Disponibilité visée | [valeur à contractualiser, méthode de mesure] |
| Incident P1/P2/P3 | [définitions et délais de prise en charge/rétablissement distincts] |
| Dépendances tierces | [cloud provider, réseau, modèles et exclusions] |
| Maintenance planifiée | [fenêtres, préavis, procédures] |
| Escalade et astreinte | [équipes réellement mobilisables] |
| Sécurité et accès | [IAM, journaux, secrets, remédiation] |
| Réversibilité | [export, durée, suppression, test de restauration] |
| Revue mensuelle | [SLA réellement mesuré, incidents, capacités, coût] |

## D. Checklist pré-signature
- [ ] Validation juridique locale, données et conformité sectorielle.
- [ ] Coût de revient et marge revus.
- [ ] Licence de chaque modèle et dépendance vérifiée par version.
- [ ] Capacité opérationnelle réelle validée, ressources financées.
- [ ] Contrat prestataire-cloud-client et RACI signés le cas échéant.
- [ ] Données, documents et signatures conservés dans un système privé.

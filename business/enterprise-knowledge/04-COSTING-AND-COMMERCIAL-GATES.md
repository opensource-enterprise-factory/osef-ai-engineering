# 04 — Coût de revient, devis et contrats

## Principe
La facturation se construit **sur coût observé et effort estimé**, puis acceptation d'un périmètre. Les prix FCFA discutés dans le catalogue sont des **fourchettes hypothétiques** et ne prouvent aucune volonté d'achat du marché.

## Modèle de coût (tous montants dans la même devise)
```text
COUT_POC =
  jours_cadrage * TJM_cadrage
+ jours_ingestion * TJM_data
+ jours_app * TJM_dev
+ jours_securite * TJM_securite
+ jours_tests * TJM_qa
+ cout_cpu_gpu_test + stockage + reseau + logiciels_tiers
+ cout_support_poc + deplacements + provision_risques_documentee

COUT_MENSUEL =
  compute_cpu_gpu + stockage + reseau + observabilite
+ support_astreinte + maintenance + securite
+ amortissement_projet_selon_contrat + couts_tiers

PRIX_CIBLE = COUT_DIRECT / (1 - marge_contributive_cible)
```

Le calcul suppose un taux de marge contributive cible **strictement inférieur à 100 %**. Fiscalité, frais généraux, fonds de roulement et coûts commerciaux doivent être pris en compte séparément ; la marge contributive n'est pas le bénéfice net.

## Hypothèses à renseigner dans un dossier privé
- Volumes documents, utilisateurs, requêtes/tokens, pics et croissance.
- Temps ingénieur par rôle et capacité réelle.
- Tarifs vérifiés CPU/GPU/hébergement + estimation des dépassements.
- Coût support / horaires / astreintes et responsabilités des tiers.
- Licences, conditions d'usage, données/résidence/assurance et réversibilité.

## Trois scénarios
| Scénario | Volume | Infrastructure | Risque à tester |
|---|---|---|---|
| Faible | à mesurer | CPU ou petite instance | latence et qualité |
| Moyen | à mesurer | GPU partagé ou dédié selon charge | coûts à l'usage |
| Fort | à mesurer | capacité réservée et redondance | SLA et support |

## Proposition commerciale en quatre étapes
1. **Diagnostic payé** : périmètre, livrables et validation écrits.
2. **POC payé** : corpus et test bornés, paiement et acceptation par jalons.
3. **Déploiement** : intégration à IAM, sauvegardes, sécurité, transfert et recette.
4. **Support managé** : forfait mensuel, périmètre exact, horaires réels, SLA négocié.

## Gates contractuels
- [ ] Droit de traiter les documents, règles de sécurité et hébergement approuvés.
- [ ] Licences des modèles/code/datasets auditées.
- [ ] Coût complet et hypothèses internes vérifiés.
- [ ] Devis écrit, critères de recette, exclus et gestion des changements.
- [ ] Responsabilités OSEF/cloud/client, incidents, réversibilité et paiement négociés.
- [ ] Validation juridique adaptée au pays / secteur du client.

**Aucun devis d'un client réel ni montant négocié ne doit être publié dans ce dépôt.**

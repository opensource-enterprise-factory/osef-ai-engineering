# Partner playbook — Private AI pour cloud providers africains

**Hypothèse d'alliance, non partenariat existant.**

## Répartition envisageable
| Domaine | Cloud provider | OSEF | Entreprise cliente |
|---|---|---|---|
| Data center, GPU, réseau, stockage | Fourniture/contrat | Spécifications techniques | Choix capacité |
| Serving, Kubernetes, LLMOps | Selon accords | Intégration, exploitation | Exigences |
| Modèles et licences | Conditions catalogue | Audit technique et sélection | Approbation usage |
| Données et privacy | Sécurité infra | Configuration traitement | Gouvernance, consentement, droits |
| Facturation et support | Quote-part à négocier | Runbook et niveau support défini | Paiement / gestion incidents |
| SLA et incident | Selon contrat | Selon contrat | Selon contrat |

**Chaque responsabilité doit être contractualisée. Aucune partie ne peut être considérée responsable automatiquement.**

## Modèles commerciaux à tester
- **Referral / apport d'affaires** : rémunération sous conditions contractuelles.
- **Co-sell** : offre conjointe et partage des responsabilités.
- **White label** : service opéré par OSEF sous marque partenaire.
- **Marketplace** : service managé intégré au catalogue provider.
- **Support/Ops contract** : OSEF intervient en intégrateur sans revendre le calcul.

## POC de référence
Assistant documentaire RAG multi-tenant sur données synthétiques avec API d'inférence, observabilité, comptes séparés et quotas. Mesurer utilisation, sécurité, latence, coût; tester incident, backup, rollback et réversibilité.

## Discovery partenaire
- Capacité GPU/CPU réellement disponible et facturation ?
- Interconnexions, résidence des données, sauvegarde et réseau ?
- Kubernetes/VM, gestion des secrets, logs, IAM ?
- SLA, astreinte, réversibilité et conditions de support ?
- Restriction sur modèles, licences et hébergement ?
- Scénario de partage de revenus, facture client et gestion de TVA selon juridiction ?

## Gates
**G0** intérêt et sponsor → **G1** due diligence technique, juridique et coût → **G2** POC sur données synthétiques → **G3** proposition commerciale validée → **G4** lancement contractualisé.

Liens : [AI-LAB-012](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/16), [AI-MEETUP-007](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/22).

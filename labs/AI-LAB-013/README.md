# AI-LAB-013 — Évaluer une transcription ASR (français d'Afrique)

**Statut : kit de préparation soumis à revue, aucun modèle ni fichier audio exécuté.**

Ce premier jalon apporte un **outil d'évaluation standard-library** calculant WER et CER à partir d'un CSV de transcriptions de référence et de prédictions. Ce n'est **pas un connecteur à Rumble-2-Flash**, ni un benchmark de ses performances. Les deux lignes d'exemple sont totalement fictives, ne portent sur aucune voix réelle, et ne sont pas des résultats scientifiques.

## Objet et traçabilité
- Veille : [AI-WATCH-20261122-02](../../watch/2026/11/AI-WATCH-20261122-02.md)
- Cadrage : [issue #27](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/27)
- Meetup candidat : [issue #28](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/28)
- Business hypothétique : [AI-BIZ-002 #23](https://github.com/opensource-enterprise-factory/osef-ai-engineering/issues/23)

## Démarrage — VM Ubuntu ou laptop
Prérequis : Python >= 3.10. Aucune bibliothèque externe, pas de téléchargement de poids, pas d'accès réseau requis.

```bash
cd labs/AI-LAB-013
python3 scripts/score_asr.py --input examples/synthetic-transcripts.csv --output /tmp/osef-ai-lab013-score.json
python3 -m unittest discover -s tests -v
```

**Colonnes du CSV :** `sample_id`, `reference`, `hypothesis`, `variety`, `consent_confirmed`. Les prédictions (`hypothesis`) doivent provenir ultérieurement d'une inférence exécutée sur des audios autorisés et explicitement associés à un identifiant.

**Mesures :** WER (distance de Levenshtein sur les mots / nombre de mots de référence), CER (même distance sur caractères normalisés / nombre de caractères de référence), macro-moyennes non calculées : les scores globaux sont **micro-agrégés**, et un score par `variety` est fourni. Normalisation transparente : NFKC, minuscules, ponctuation remplacée par des espaces, espaces regroupés ; conserver les accents.

**Fail closed :** échec si identifiant vide/dupliqué, colonnes manquantes, consentement non confirmé (doit valoir `yes`), transcription de référence vide, ou jeu de données vide. Le champ `consent_confirmed` est une **déclaration de l'opérateur et ne constitue pas une vérification juridique**.

## Phases suivantes, non implémentées
1. Auditer droits des modèles, provenance et consentements de corpus.
2. Ajouter un adaptateur d'inférence versionné (Reson8/Rumble-2-Flash et référence choisie), compatible avec une machine de test.
3. Associer transcriptions à leurs métadonnées de matériel/version/latence et mesurer CPU/GPU/RAM.
4. Exécuter une évaluation aveugle sur des variétés francophones consenties, analyser les erreurs ; ne pas publier les voix ni transcriptions identifiantes.
5. Rapporter scores réels, intervalles d'incertitude et limites. Ne jamais confondre résultats des auteurs avec mesures OSEF.

## Sécurité et qualité
- Utiliser uniquement des données synthétiques pour la démonstration publique.
- Aucun audio ni donnée privée dans Git ; gérer les données réelles hors dépôt avec autorisations explicites.
- Une amélioration WER/CER ne démontre pas à elle seule la qualité d'un produit ou son adéquation réglementaire.
- L'analyse comparative doit figer versions de modèle, moteur et matériel.

## Critères d'acceptation de ce premier jalon
- [ ] Tests unitaires et exemple exécutés avec succès sur Python 3.10+
- [ ] Validation et normalisation documentées
- [ ] Aucun score de modèle inventé, aucun audio ni secret
- [ ] Relecture d'un ingénieur OSEF, merge uniquement après approbation

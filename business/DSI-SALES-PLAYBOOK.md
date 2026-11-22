# OSEF AI — Playbook de découverte commerciale DSI / CTO

## Message de positionnement (30 secondes)
« OSEF accompagne les entreprises d'Afrique francophone dans l'adoption de solutions IA fondées sur des composants ouverts. Nous intervenons sur la préparation des données, le déploiement privé, la sécurité et l'exploitation. Nous commençons par un cas d'usage et des critères mesurables, avant tout engagement de production. »

## Questions de découverte (ne pas collecter les réponses personnelles dans GitHub public)
1. Quel processus coûte actuellement le plus de temps ou génère des erreurs ?
2. Qui utilisera l'assistant ou la plateforme, et combien de fois par jour ?
3. Quelles sources documentaires ou applications sont concernées ? Qui détient les droits ?
4. Où doivent rester les données, les journaux et les sauvegardes ?
5. Quelle intégration SSO/IAM, archivage et auditabilité est nécessaire ?
6. Quelles sont les attentes de qualité, de délai de réponse et de disponibilité ?
7. Qui est responsable de la décision métier quand l'IA se trompe ?
8. Quel budget approximatif, sponsor décisionnaire et fenêtre de projet ?
9. L'entreprise préfère-t-elle son infrastructure, un cloud partenaire, ou une API tierce autorisée ?
10. Quels critères justifieraient le passage d'un diagnostic au POC puis à la production ?

## Diagnostic proposé — structure
- Hypothèses de valeur métier et ligne de base mesurable.
- Périmètre, sources, risques et acteurs concernés.
- Architecture et 2 options de déploiement au minimum.
- Estimation TCO avec prix sourcés et zones incertaines.
- Plan POC, critères d'acceptation, conditions de réversibilité.
- Proposition de support éventuel.

## Objections fréquentes / réponses prudentes
**« Où est le support ? »** Contrat avec SLA et plages de service explicitement définis ; ne pas promettre 24/7 sans équipe financée.
**« Et si le modèle disparaît ? »** Auditer licences, portabilité, versions, dépendances et documenter une stratégie de remplacement ; pas de garantie absolue.
**« Nos données sont-elles souveraines ? »** La réponse dépend de l'hébergement, des flux, des sauvegardes, de l'administration, des sous-traitants et des contrats ; audit préalable.
**« Est-ce toujours gratuit car Open Source ? »** Les licences sont distinctes des coûts de calcul, intégration, maintenance et support.
**« Où sont vos références ? »** Présenter uniquement des labs OSEF effectivement testés et des projets clients autorisés. Les travaux en draft ne sont pas des références de production.

## Du meetup à la vente
- Invitons les DSI à discuter d'un **problème métier**, non à écouter une publicité.
- Proposer un échange exploratoire volontaire et respecter le consentement de contact.
- Qualifier le besoin ; devis de diagnostic uniquement si cadrage partagé.
- Résultats et témoignages client publiés seulement avec autorisation écrite.

## Modèle de mail de premier contact
Objet : Échange DSI à DSI — adoption pragmatique de l'IA ouverte

Bonjour,

Chez OSEF, nous étudions comment les entreprises d'Afrique francophone peuvent mettre en place des assistants documentaires privés et des plateformes IA maintenables, avec des critères de qualité, de sécurité et de coûts mesurables.

Seriez-vous disponible pour un échange de 20 minutes afin de comprendre vos enjeux et vous présenter un protocole de laboratoire reproductible ? Il ne s'agit pas de présumer d'un projet ni d'un partenariat.

Cordialement,
Équipe OSEF
https://osef.africascaler.com

## Livrables
Compte rendu anonymisé dans le reporting public ; toutes les données d'identification et négociations exclusivement dans un espace privé habilité.

# Bibliotheque


## Expliquez pourquoi l’authentification ne suffit pas pour sécuriser

un endpoint et à quoi servent les permissions.
L’authentification vérifie l’identité de l’utilisateur (qui es-tu ?).
Mais cela ne suffit pas : une fois identifié, il faut aussi contrôler ce que l’utilisateur a le droit de faire.

Les permissions servent à définir les actions autorisées pour chaque utilisateur (as-tu le droit de faire cette action ?).
Exemples :

Un utilisateur authentifié peut lire, mais pas modifier certaines données.
Seuls les admins peuvent supprimer des objets.
En résumé :

Authentification = identification
Permissions = autorisation d’accès/action
Les deux sont nécessaires pour une API vraiment sécurisée.
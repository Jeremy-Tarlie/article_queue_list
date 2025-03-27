# Stacks and Queue - Gestion des Articles

Ce projet est une application en ligne de commande qui utilise des structures de données comme les files d'attente (Queue) et les piles (Stack) pour gérer des articles récupérés depuis une API. L'utilisateur peut lire des articles, consulter l'historique des articles lus, et naviguer dans un menu interactif.

---

## Fonctionnalités

- **Récupération des articles** :

  - Les articles sont récupérés depuis l'API [Currents API](https://currentsapi.services/).
  - Les articles sont stockés dans une file d'attente pour être lus dans l'ordre.

- **Menu interactif** :

  - **Option 1** : Lire un article de la file d'attente.
  - **Option 2** : Afficher le dernier article lu depuis l'historique.
  - **Option 3** : Quitter l'application.

- **Gestion des données** :
  - Les articles lus sont ajoutés à une pile (historique).
  - Les articles non lus restent dans la file d'attente.

---

## Prérequis

- Python 3.8 ou supérieur
- [pip](https://pip.pypa.io/en/stable/) pour installer les dépendances
- Une clé API pour [Currents API](https://currentsapi.services/)

---

## Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/stacksAndQueue.git
   cd stacksAndQueue
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Configurez votre clé API :
   - Créez un fichier .env à la racine du projet.
   - Ajoutez votre clé API dans le fichier .env :

```bash
       API_KEY=VotreCleAPI
```

--

## Utilisation

1. Lancez l'application :

```bash
       python main.py
```

2. Suivez les instructions dans le menu interactif :

   - Option 1 : Lire un article de la file d'attente.
   - Option 2 : Afficher le dernier article lu depuis l'historique.
   - Option 3 : Quitter l'application.

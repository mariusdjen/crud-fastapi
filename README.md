
# Application CRUD avec FastAPI 🚀

Ce projet est une API CRUD (Create, Read, Update, Delete) développée avec **FastAPI** et **Uvicorn**. Il permet de gérer des données de manière simple et rapide grâce à une interface de documentation interactive. Les données sont stockées dans **Airtable**, une base de données flexible.

## Fonctionnalités 🌟

- **Créer** une ressource dans Airtable
- **Lire** les ressources stockées dans Airtable
- **Mettre à jour** une ressource existante dans Airtable
- **Supprimer** une ressource dans Airtable
- Documentation interactive disponible via Swagger UI et Redoc

## Prérequis 🛠️

Pour exécuter ce projet, vous devez avoir :

- **Python 3.7 ou plus récent** : [Télécharger Python](https://www.python.org/downloads/)
- **Uvicorn** pour démarrer le serveur
- **Pip** : installé avec Python
- **Un compte Airtable** et une **API Key** pour interagir avec Airtable
- **Une base Airtable** avec un **Table Name** et des champs appropriés (par exemple, `firstName`, `lastName`, `email`, etc.)

## Installation 🚧

1. Clonez le dépôt GitHub :

   ```bash
   git clone https://github.com/mariusdjen/crud-fastapi.git
   cd crud-fastapi

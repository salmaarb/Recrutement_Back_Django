# Recrutement_Back_Django
#  API de Recrutement - Django REST Framework

Ce projet est une API de gestion de recrutement développée avec **Django** et **Django REST Framework**, permettant de gérer deux types d'utilisateurs : **candidats** et **recruteurs**.

## 📁 Structure du Projet

Le projet est organisé en deux applications principales :

- candidats: pour gérer les données des candidats (profil, CV, expériences, etc.)
- recruteurs : pour gérer les recruteurs et leurs offres d'emploi.
🛠 Exemple de structure des fichiers

api-recrutement/
│
|--- candidats/
│   ├--- models.py
│   ├--- views.py
│   ├--- serializers.py
│   └---urls.py
│
├--- recruteurs/
│   ├--- models.py
│   ├--- views.py
│   ├--- serializers.py
│   └--- urls.py
│
├---RecrutementBackDjango/
│   ├--- settings.py
│   ├--- urls.py
│   └--- wsgi.py
│
├--- manage.py
└---requirements.txt
## 🔧 Technologies utilisées

- Python 3.13.3
- Django 5.2.1
- Django REST Framework
- drf-yasg (Swagger pour la documentation)
- PostgreSQL 
- Git pour le versionnement

## 📦 Installation locale

### 1. Cloner le projet

```bash
git clone https://github.com/salmaarb/Recrutement_Back_Django.git
cd RecrutementBackDjango


### 2. Créer un environnement virtuel
```bash
python -m venv venv
source   venv\Scripts\activate
### 3.Installer les dependances

pip install -r requirements.txt

###🛠 Configuration de la base de données PostgreSQL
Avant de lancer les migrations, assure-toi que :
PostgreSQL est installé sur ta machine.

-- 1. Créer la base de données
CREATE DATABASE recrutement_db;

-- 2. Créer un utilisateur avec mot de passe
ALTER USER postgres WITH PASSWORD 'admin';
postgres est l'utilisateur par defaut 
-- 3. Donner tous les privilèges sur la base à cet utilisateur
GRANT ALL PRIVILEGES ON DATABASE recrutement_db TO postgres;

##ou bien tu peux configuré ces informations dans RecrutementBackDjango/settings.py selon tes donnees local :
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recrutement_db',
        'USER': 'votre_utilisateur',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 4. Appliquer les migrations

python manage.py makemigrations

python manage.py migrate

### 5. Lancer le serveur

python manage.py runserver

📌 Points d’accès API
Méthode	URL	Description
GET	/api/candidats/	Liste des candidats
POST	/api/candidats/	Ajouter un nouveau candidat
GET	/api/recruteurs/	Liste des recruteurs
POST	/api/recruteurs/	Ajouter un nouveau recruteur
GET	/api/swagger/	Interface Swagger (API docs)
GET	/api/redoc/	Interface ReDoc (API docs)

📚 Documentation Swagger
Accède à la documentation interactive via Swagger :

➡️ http://localhost:8000/api/swagger/
➡️ http://localhost:8000/api/redoc/ 
Tu verras une interface lisible et interactive qui montre toute la structure d API (routes, champs, méthodes, descriptions…).

👤 Auteur
Arbaoui Salma
📧 Contact : [salma.arbaoui15@gmail.com]

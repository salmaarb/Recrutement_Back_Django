# Recrutement_Back_Django
#  API de Recrutement - Django REST Framework

Ce projet est une API de gestion de recrutement développée avec **Django** et **Django REST Framework**, permettant de gérer deux types d'utilisateurs : **candidats** et **recruteurs**.

## 📁 Structure du Projet

Le projet est organisé en deux applications principales :

- candidats: pour gérer les données des candidats (profil, CV, expériences, etc.)
- recruteurs : pour gérer les recruteurs et leurs offres d'emploi.
### 🛠 structure de Projet

RecrutementBackDjango/
│
|--- candidats/
│   ├--- models.py
│   ├--- views.py
│   ├--- serializers.py
│   └----urls.py
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

git clone https://github.com/salmaarb/Recrutement_Back_Django.git

### 3.Installer les dependances

pip install -r requirements.txt

###### 🛠 Configuration de la base de données PostgreSQL
Avant de lancer les migrations, assure-toi que :
PostgreSQL est installé sur ta machine.

### -- 1. Créer la base de données
CREATE DATABASE recrutement_db;

### -- 2. Créer un utilisateur avec mot de passe
ALTER USER postgres WITH PASSWORD 'admin';
postgres est l'utilisateur par defaut 
### -- 3. Donner tous les privilèges sur la base à cet utilisateur
GRANT ALL PRIVILEGES ON DATABASE recrutement_db TO postgres;

## voici la configuration de la base de donnee dans le projet dans settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'recrutement_db',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 4. Appliquer les migrations

python manage.py makemigrations

python manage.py migrate

### 5. Lancer le serveur

python manage.py runserver

# 📌 Points d’accès API
Méthode	URL	Description
GET	/api/candidats/	Liste des candidats
POST	/api/candidats/	Ajouter un nouveau candidat
GET	/api/candidats/{id}	candidat by id
PUT	/api/candidats/{id}	 modifier candidat by id
DELETE	/api/candidats/{id}	 supprimer candidat by id

GET	/api/recruteurs/	Liste des recruteurs
GET	/api/recruteurs/voir-tous-les-candidats/	voir Liste des candidats
GET	/api/recruteurs/ajouter-favori/	ajouter candidat au favori
POST	/api/recruteurs/	Ajouter un nouveau recruteur
GET	/api/recruteurs/{id}	recruteur by id
PUT	/api/recruteurs/{id}	 modifier recruteur by id
DELETE	/api/recruteurs/{id}	 supprimer recruteur by id


GET	/api/swagger/	Interface Swagger (API docs)
GET	/api/redoc/	Interface ReDoc (API docs)

# 📚 Documentation Swagger
Accède à la documentation interactive via Swagger :

➡️ http://localhost:8000/api/swagger/
➡️ http://localhost:8000/api/redoc/ 
Tu verras une interface lisible et interactive qui montre toute la structure d API (routes, champs, méthodes, descriptions…).

# 👤 Auteur
Arbaoui Salma
📧 Contact : [salma.arbaoui15@gmail.com]

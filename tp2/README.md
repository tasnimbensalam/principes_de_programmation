# Application de Gestion des Étudiants (Client API REST)

Ce projet est une application PHP simple structurée selon une architecture de séparation des responsabilités (Services, Vues, Configuration). Elle consomme une API REST externe pour récupérer et afficher une liste d'étudiants.

##  Structure du Projet

L'organisation des fichiers suit une logique modulaire pour faciliter la maintenance :

* **`apirest.php`** : Point d'entrée de l'application. Il initialise la configuration, appelle le service et charge la vue.
* **`config/`** : Contient `config.php` pour définir les constantes globales comme l'URL de base de l'API.
* **`services/`** : Contient `StudentService.php`, responsable de la logique de récupération des données (appels API).
* **`views/`** : Contient `students.php`, responsable de l'affichage HTML des données.
* **`assets/`** : Contient les fichiers statiques, notamment `style.css` pour la mise en forme.

## Installation et Configuration

### 1. Prérequis
* Un serveur Web (Apache/Nginx) avec **PHP 7.4+** installé.
* L'extension PHP `allow_url_fopen` doit être activée pour permettre l'utilisation de `file_get_contents` sur des URLs.

### 2. Configuration de l'API
Ouvre le fichier `config/config.php` et modifie l'URL pour correspondre à ton serveur d'API :
```php
define('API_BASE_URL', '[http://127.0.0.1:5000](http://127.0.0.1:5000)');
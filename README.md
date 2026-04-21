# Principes de Programmation — Master 1 Informatique (S2)

Ce dépôt rassemble l'ensemble des travaux pratiques et projets réalisés dans le cadre de l'unité d'enseignement **"Principes de Programmation"** à l'Institut Galilée. L'objectif est de maîtriser les architectures de services web, la manipulation de données et la conteneurisation.

---

##  Structure du Répertoire

* **`app/`** : Client PHP structuré (Services/Vues) consommant une API REST.
* **`tp1/` & `tp2/`** : Implémentation de Services Web **SOAP** avec JAX-WS en Java.
* **`docker/`** : Études sur la persistance (Volumes), les réseaux et l'orchestration de conteneurs.

---

##  Notions Fondamentales

### 1. Communication et Services Web
Nous avons étudié les deux méthodes majeures d'échange de données entre applications :

* **API REST (Representational State Transfer)** : 
    * Utilise le protocole **HTTP** et des méthodes standard (GET, POST, PUT, DELETE).
    * Privilégie le format **JSON** pour sa légèreté.
    * *Exemple projet* : Récupération de listes d'étudiants via `file_get_contents` en PHP.
* **SOAP (JAX-WS)** : 
    * Protocole basé sur **XML**.
    * Utilise un contrat **WSDL** pour définir strictement les méthodes (ex: `convertir`, `somme`).
    * *Exemple projet* : Serveur Java utilisant `@WebService` et `Endpoint.publish()`.

### 2. Manipulation des Données
Le passage d'un langage de programmation à un flux réseau nécessite deux étapes clés :
* **Sérialisation** : Transformer un objet ou une structure de données en un format transmissible (JSON ou XML).
* **Désérialisation** : Reconstruire l'objet d'origine à partir du format reçu pour pouvoir le manipuler dans le code.

### 3. Architecture Logicielle
* **Interface & Contrat** : Définition d'un contrat entre les parties de l'application pour permettre un **couplage faible**.
* **Séparation des responsabilités** : Utilisation de **Services** (logique métier) distincts des **Vues** (affichage HTML/CSS).

---

## Conteneurisation avec Docker

Une partie importante du cours a été dédiée à la gestion des environnements via Docker :

* **Gestion du stockage** : 
    * *Bind Mounts* : Liaison directe pour le développement en temps réel.
    * *Volumes* : Persistance des données gérée par Docker (ex: pour MySQL).
* **Réseaux Docker** :
    * **Bridge** : Réseau par défaut.
    * **Custom Network** : Création de réseaux isolés avec **DNS interne** permettant aux conteneurs de communiquer par leur nom (ex: le client PHP contactant l'API).
* **Orchestration** : Utilisation de **Docker Compose** pour gérer plusieurs services simultanément.

---

##  Technologies & Outils

| Technologie | Usage |
| :--- | :--- |
| **Java (JAX-WS)** | Développement de Services Web SOAP. |
| **PHP 7.4+** | Consommation d'API REST et rendu dynamique. |
| **Docker** | Isolation, déploiement et réseaux. |
| **CSS** | Mise en forme des interfaces de gestion. |

---

## Installation rapide

1.  **Serveur SOAP** : Lancer `Application.java` pour exposer le service sur `http://localhost:8080/`.
2.  **Client REST** : Configurer l'URL de l'API dans `config/config.php` et lancer via un serveur PHP (Apache).
3.  **Docker** : Pour tester les réseaux personnalisés :
    ```bash
    docker network create mon-reseau
    docker run -d --name api --network mon-reseau alpine sleep 1000
    ```

---
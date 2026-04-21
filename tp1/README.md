# Serveur de Service Web SOAP (JAX-WS)

Ce projet Java implémente un service web utilisant le protocole **SOAP**, basé sur les spécifications **JAX-WS** (Java API for XML Web Services). Il permet d'exposer des méthodes métier via un serveur HTTP intégré.

##  Fonctionnalités du Service

Le service `MonserviceWeb` propose les opérations suivantes :

* **Conversion** : Une méthode `convertir` qui prend un montant (`mt`) et retourne sa valeur multipliée par 0.9.
* **Somme** : Une méthode `somme` qui additionne deux nombres réels, dont l'un est défini par le paramètre `@WebParam` nommé `parametre1`.

## Structure du Code

* **`Application.java`** : Contient la méthode principale (`main`). Elle utilise la classe `Endpoint` pour publier et déployer le service web sur l'URL locale `http://localhost:8080/`.
* **`MonserviceWeb.java`** : Définit le service web avec l'annotation `@WebService`. Il précise également un `targetNamespace` personnalisé (`http://www.polytech.fr`) pour la structure XML.

## 🚀 Déploiement et Accès

### 1. Lancement du Serveur
Exécute la classe `Application.java`. Une fois lancé, tu devrais voir le message suivant dans la console :
> "Déploiment réussi ! Le service web est déployé"

### 2. Consulter le WSDL
Le fichier de description du service (**WSDL**), nécessaire pour que les clients puissent consommer le service, est généré automatiquement par JAX-WS. Tu peux y accéder via ton navigateur à l'adresse suivante :
`http://localhost:8080/?wsdl`

## Notes Techniques

* **JAX-WS** : Utilisé pour la gestion des annotations et du protocole SOAP.
* **SOAP** : Protocole basé sur XML pour l'échange d'informations structurées.
* **Annotations** : Utilisation de `@WebMethod` pour renommer les opérations et `@WebParam` pour personnaliser les paramètres dans le message SOAP.
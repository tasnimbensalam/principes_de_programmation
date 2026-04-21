#  Docker — Notes de cours

---

##  1. Les types de stockage (Volumes)

Docker propose trois types principaux de stockage persistant.

### A. Bind Mounts (montages liés)

Relient directement un dossier de la machine hôte à un dossier dans le conteneur. Les modifications sont visibles en temps réel des deux côtés.

**Caractéristiques :**
- Dépend du système de fichiers hôte
- Risque de sécurité si mal configuré

```bash
docker run -v /chemin/hote:/chemin/conteneur image
```

> `source` = chemin sur la machine hôte  
> `destination` = chemin dans le conteneur

**Exemple :**
```bash
docker run -it -v /home/user/projets:/app alpine sh
# Tout changement dans /home/user/projets se reflète dans /app
```

---

### B. Volumes gérés par Docker (recommandés)

Volumes entièrement gérés par Docker, stockés dans `/var/lib/docker/volumes/`.

**Caractéristiques :**
- Indépendants du système hôte
- Plus sûrs et facilement sauvegardables

```bash
# Créer un volume
docker volume create monvolume

# L'utiliser dans un conteneur
docker run -v monvolume:/chemin/dans/conteneur image
```

**Commandes utiles :**
```bash
docker volume ls                   # Liste les volumes
docker volume inspect monvolume    # Affiche les infos en JSON
docker volume rm monvolume         # Supprime un volume
```

**Exercice de persistance :**
```bash
# 1. Lancer un conteneur avec le volume
docker run -it -v monvolume:/data alpine sh

# 2. Créer un fichier dans le volume
echo "hello" > /data/test.txt

# 3. Supprimer le conteneur
docker rm -f <id_conteneur>

# 4. Relancer un conteneur avec le même volume
docker run -it -v monvolume:/data alpine sh
# → test.txt est toujours là !
```

---

### C. tmpfs (mémoire uniquement — Linux)

Stockage temporaire en RAM uniquement.

**Caractéristiques :**
- Très rapide
- Aucune trace sur le disque
- Données perdues à l'arrêt du conteneur

```bash
docker run --tmpfs /chemin image
```

---

##  2. Exemple concret — Persistance d'une base de données

### MySQL

```bash
# Créer le volume
docker volume create mysql_data

# Lancer MySQL avec le volume
docker run -d \
  --name mysql \
  -e MYSQL_ROOT_PASSWORD=pass \
  -v mysql_data:/var/lib/mysql \
  mysql:8
```

Ensuite :
1. Créer une base de données et y insérer des données
2. Arrêter le conteneur
3. Relancer un nouveau conteneur en partageant le même volume
4. Vérifier que les données sont toujours accessibles

### PostgreSQL

Reproduire la même démarche avec l'image `postgres` et le chemin de données `/var/lib/postgresql/data`.

---

##  3. Dockerfile

### Qu'est-ce qu'un Dockerfile ?

Un Dockerfile automatise la création d'images Docker. Sans lui, il faudrait configurer chaque conteneur manuellement (installer des paquets, copier des fichiers…). Avec lui, Docker fait tout ça automatiquement pour produire une image réutilisable.

### Structure générale

| Instruction | Rôle |
|---|---|
| `FROM` | Choisir l'image de base |
| `RUN` | Exécuter une commande dans l'image |
| `COPY` | Copier un fichier ou dossier local dans l'image |
| `WORKDIR` | Définir le dossier de travail |
| `EXPOSE` | Documenter le port exposé |
| `CMD` / `ENTRYPOINT` | Commande lancée au démarrage du conteneur |

### Exemple — API REST avec Flask

**Emplacement :** le `Dockerfile` doit être au même niveau que le dossier `src`.

```dockerfile
# Image Python officielle légère
FROM python:3.12-slim

# Répertoire de travail dans le conteneur
WORKDIR /app

# Installation de Flask
RUN pip install flask

# Copie du fichier source
COPY app.py .

# Documentation du port utilisé
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
```

**Build et run :**
```bash
docker build -t mon-app .
docker run -p 4900:5000 mon-app
```

---

##  4. Publier son image sur Docker Hub

```bash
# Se connecter
docker login

# Tagger l'image avec son username
docker tag mon-app votre_username/mon-app:1

# Pousser l'image
docker push votre_username/mon-app:1
```

---

##  5. Docker Compose

Docker Compose permet de gérer plusieurs services en même temps. Par exemple, un service PHP qui aurait besoin d'une API REST peut être orchestré via un fichier `docker-compose.yml`.

>  Penser à inclure `<M1>` si nécessaire pour éviter les suppressions involontaires.

---

##  6. Gestion des réseaux

### Réseau bridge (par défaut)

Réseau utilisé automatiquement par Docker pour tous les conteneurs.

```bash
docker run -d --name web nginx
docker network inspect bridge
```

---

### Réseau host

Le conteneur partage directement le réseau de la machine hôte. Pas d'IP Docker, pas d'isolation réseau.

```bash
docker run --network host nginx
```

---

### Réseau none

Le conteneur est totalement isolé : aucune communication réseau possible.

```bash
docker run --network none -it alpine sh

# Test à l'intérieur du conteneur :
ping www.google.com
#  Aucune réponse : le conteneur ne peut ni envoyer ni recevoir de données.
```

---

### Réseau personnalisé

Créer son propre réseau isolé avec DNS interne automatique.

```bash
# Créer le réseau
docker network create monreseau

# Lancer des conteneurs dans ce réseau
docker run -d --name site --network monreseau nginx
docker run -d --name api  --network monreseau alpine sleep 1000

# Tester la communication par nom (DNS interne Docker)
docker exec -it site ping api
```

---

### Connecter / déconnecter un conteneur

```bash
# Ajouter un conteneur à un réseau
docker network connect monreseau site

# Le retirer du réseau
docker network disconnect monreseau site
```

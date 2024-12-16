# Utiliser une image de base Python
FROM python:3.10-slim

# Installer les dépendances nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip à la dernière version
RUN pip install --upgrade pip

# Créer un répertoire de travail
WORKDIR /

# Copier les fichiers du projet
COPY . /

# Exposer le port utilisé par le serveur
EXPOSE 5002

# Définir la commande de lancement
CMD ["python", "server.py"]
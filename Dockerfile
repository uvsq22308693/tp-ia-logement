# 1. Image de base légère avec Python
FROM python:3.9-slim

# 2. Dossier de travail dans le conteneur
WORKDIR /app

# 3. Copier et installer les bibliothèques
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copier tout le reste (code + modèle .pkl)
COPY . .

# 5. Ouvrir les ports (5000 pour Flask, 8501 pour Streamlit)
EXPOSE 5000
EXPOSE 8501

# 6. Lancer l'API et l'Interface en même temps
CMD python app.py & streamlit run interface.py --server.port 8501 --server.address 0.0.0.0
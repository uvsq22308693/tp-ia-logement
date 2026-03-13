# 1. Image Python
FROM python:3.9-slim

# 2. Dossier de travail
WORKDIR /app

# 3. Installation des outils
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copie de ton code
COPY . .

# 5. On expose le port (pour la forme)
EXPOSE 10000

# 6. ON LANCE LES DEUX : Flask en fond (&) et Streamlit sur le port de Render ($PORT)
CMD python app.py & streamlit run interface.py --server.port $PORT --server.address 0.0.0.0
import streamlit as st
import requests

st.title("Estimation de prix immobilier 🏠")

# Création du formulaire
surface = st.number_input("Surface (m²)", value=50)
pieces = st.slider("Nombre de pièces", 1, 10, 3)
distance = st.number_input("Distance du centre (km)", value=5)
etage = st.number_input("Étage", value=1)
annee = st.number_input("Année de construction", value=2010)

if st.button("Estimer le prix"):
    payload = {
        "surface": surface,
        "pieces": pieces,
        "distance_centre": distance,
        "etage": etage,
        "annee_construction": annee
    }
    # Appel à l'API
    response = requests.post("http://localhost:5000/predict", json=payload)
    resultat = response.json()
    
    st.success(f"Le prix estimé est de : {resultat['prix_estime']} €")
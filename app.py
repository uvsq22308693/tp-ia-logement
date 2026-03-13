from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Charger le modèle au démarrage
model = joblib.load("model_logement.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    
    # Transformer les données reçues en DataFrame pour le modèle
    df_input = pd.DataFrame([data])
    
    # Faire la prédiction
    prediction = model.predict(df_input)
    
    return jsonify({'prix_estime': round(float(prediction[0]), 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
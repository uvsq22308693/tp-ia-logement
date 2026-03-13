import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor

import joblib


print("\nAffichage du contenu du fichier logements \n")
df = pd.read_csv("logements.csv")
print(df)

print("\nAffichage des 5 premieres lignes du tableau\n")
print(df.head())
print("\nAffichage des nombre de ligne non null\n")
print(df.info())
print("\nAffichage des statistiques\n")
print(df.describe())

print("\nAffichage des nombre de données vide et dupliquer\n")
print(df.isnull().sum())
print(df.duplicated().sum())

plt.scatter(df["surface"], df["prix"])

plt.xlabel("Surface")
plt.ylabel("Prix")

plt.title("Relation entre la surface et le prix")

plt.show()

X = df[["surface","pieces","distance_centre","etage","annee_construction"]]

y = df["prix"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)
print("Score sur les données d'entraînement :", train_score)
print("Score sur les données de test        :", test_score)

predictions = model.predict(X_test)

resultats = pd.DataFrame({
    "prix_reel": y_test.values,
    "prix_predit": predictions
})

print(resultats)

mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("MSE :", mse)
print("R2 :", r2)

nouveau_logement = pd.DataFrame({
    "surface":[150],
    "pieces":[2],
    "distance_centre":[2],
    "etage":[4],
    "annee_construction":[2022]
})

prediction = model.predict(nouveau_logement)

print("Prix estimé :", prediction[0])


models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(random_state=42),
    "KNN Regressor": KNeighborsRegressor(n_neighbors=3)
}

for name, model in models.items():
    print("\n----------------------------------")
    print("Algorithme :", name)

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    train_score2 = model.score(X_train, y_train)
    test_score2 = model.score(X_test, y_test)
    print("Score sur les données d'entraînement :", train_score2)
    print("Score sur les données de test        :", test_score2)

    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)

    print("MSE :", mse)
    print("R2 :", r2)


# Exemple : On décide de ré-entraîner et sauvegarder spécifiquement la Random Forest
final_model = RandomForestRegressor(random_state=42)
final_model.fit(X_train, y_train)

joblib.dump(final_model, "model_logement.pkl")
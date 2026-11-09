import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
df = pd.read_csv("daten/reifen.csv")
X = df[["marke", "km", "druck_bar", "temperatur_c"]]
y = df["profiltiefe_mm"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
def erstelle_pipeline(modell):
 """Pipeline: Marke in Zahlen umwandeln, dann Modell trainieren."""
 vorverarbeitung = ColumnTransformer(
 [("marke", OneHotEncoder(), ["marke"])],
 remainder="passthrough",
 )
 return Pipeline([("prep", vorverarbeitung), ("model", modell)])
# Zwei Modelle vergleichen
modelle = {
 "Lineare Regression": LinearRegression(),
 "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
}
for name, modell in modelle.items():
 pipe = erstelle_pipeline(modell)
 pipe.fit(X_train, y_train)
 vorhersage = pipe.predict(X_test)
 mae = mean_absolute_error(y_test, vorhersage)
 r2 = r2_score(y_test, vorhersage)
 print(f"{name}: MAE = {mae:.3f} mm, R² = {r2:.3f}")
# Bestes Modell auf allen Daten trainieren und eine neue Vorhersage machen
final = erstelle_pipeline(RandomForestRegressor(n_estimators=200, random_state=42))
final.fit(X, y)
neuer_reifen = pd.DataFrame([{
 "marke": "Marke A",
 "km": 30000,
 "druck_bar": 2.0,
 "temperatur_c": 30,
}])
print(f"\nVorhersage Profiltiefe: {final.predict(neuer_reifen)[0]:.2f} mm")
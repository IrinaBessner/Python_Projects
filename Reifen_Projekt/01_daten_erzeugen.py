import numpy as np
import pandas as pd
from pathlib import Path
Path("daten").mkdir(exist_ok=True)
Path("ausgabe").mkdir(exist_ok=True)
rng = np.random.default_rng(42) # Zufallsgenerator mit fester Startzahl, damit alles reproduzierbar ist
n = 300
marke = rng.choice(["Marke A", "Marke B"], size=n)
km = rng.uniform(0, 60000, n)
druck = rng.normal(2.3, 0.15, n)
temperatur = rng.normal(25, 6, n)
# Marke B verschleißt etwas stärker
rate = np.where(marke == "Marke A", 0.00011, 0.00013)
# Niedriger Druck und hohe Temperatur beschleunigen den Verschleiß
druck_faktor = 1 + 0.8 * np.maximum(2.3 - druck, 0)
temp_faktor = 1 + 0.4 * (temperatur - 25) / 10
profil = 8.0 - rate * km * druck_faktor * temp_faktor + rng.normal(0, 0.15, n)
profil = np.clip(profil, 0, 8.0)
df = pd.DataFrame({
 "marke": marke,
 "km": km.round(0),
 "druck_bar": druck.round(2),
 "temperatur_c": temperatur.round(1),
 "profiltiefe_mm": profil.round(2),
})
df.to_csv("daten/reifen.csv", index=False)
print(df.head())
print(f"{len(df)} Datensätze gespeichert.")

import pandas as pd
df = pd.read_csv("daten/reifen.csv")
print(df.head())
df.info()
print(df.describe().round(2))
# Neue Spalte: Verschleiß je 1000 km (nur Reifen mit mehr als 1000 km)
df = df[df["km"] > 1000].copy()
df["verschleiss_pro_1000km"] = (8.0 - df["profiltiefe_mm"]) / df["km"] * 1000
# Gruppierte Auswertung nach Marke
kennzahlen = df.groupby("marke").agg(
 anzahl=("km", "size"),
 mittlere_km=("km", "mean"),
 mittlere_profiltiefe=("profiltiefe_mm", "mean"),
 mittlerer_verschleiss=("verschleiss_pro_1000km", "mean"),
).round(3)
print("\nKennzahlen je Marke:\n", kennzahlen)
# Filter: Reifen mit zu niedrigem Druck (unter 2,0 bar)
niedriger_druck = df[df["druck_bar"] < 2.0]
print(f"\nReifen mit Druck unter 2,0 bar: {len(niedriger_druck)}")
# Sortierung: die 5 am stärksten verschlissenen Reifen
print("\nTop 5 Verschleiß:\n", df.nlargest(5, "verschleiss_pro_1000km")[["marke", "km", "profiltiefe_mm"]])
# Ergebnis speichern
kennzahlen.to_csv("ausgabe/kennzahlen.csv")
df.to_csv("ausgabe/auswertung.csv", index=False)
print("\nDateien in 'ausgabe' gespeichert.")

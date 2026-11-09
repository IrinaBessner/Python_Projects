import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv("daten/reifen.csv")
fig, achsen = plt.subplots(1, 3, figsize=(16, 5))
# Diagramm 1: Streudiagramm Profiltiefe über Laufleistung
for marke, gruppe in df.groupby("marke"):
 achsen[0].scatter(gruppe["km"], gruppe["profiltiefe_mm"], s=12, alpha=0.6, label=marke)
achsen[0].axhline(1.6, color="red", linestyle="--", label="Mindestprofil 1,6 mm")
achsen[0].set_title("Profiltiefe über Laufleistung")
achsen[0].set_xlabel("Kilometer")
achsen[0].set_ylabel("Profiltiefe (mm)")
achsen[0].legend()
achsen[0].grid(alpha=0.3)
# Diagramm 2: Histogramm des Reifendrucks
achsen[1].hist(df["druck_bar"], bins=20, color="steelblue", edgecolor="white")
achsen[1].axvline(2.0, color="red", linestyle="--", label="Grenze 2,0 bar")
achsen[1].set_title("Verteilung Reifendruck")
achsen[1].set_xlabel("Druck (bar)")
achsen[1].set_ylabel("Anzahl")
achsen[1].legend()
# Diagramm 3: Balken mit mittlerer Profiltiefe je Marke
mittel = df.groupby("marke")["profiltiefe_mm"].mean()
balken = achsen[2].bar(mittel.index, mittel.values, color=["#4C72B0", "#DD8452"])
achsen[2].bar_label(balken, fmt="%.2f mm")
achsen[2].set_title("Mittlere Profiltiefe je Marke")
achsen[2].set_ylabel("mm")
plt.tight_layout()
plt.savefig("ausgabe/diagramme.png", dpi=150)
plt.show()
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import curve_fit
df = pd.read_csv("daten/reifen.csv")
df["verlust"] = 8.0 - df["profiltiefe_mm"]
# 1) t-Test: unterscheiden sich die Marken beim Verschleiß?
a = df.loc[df["marke"] == "Marke A", "verlust"]
b = df.loc[df["marke"] == "Marke B", "verlust"]
t, p = stats.ttest_ind(a, b, equal_var=False)
print(f"t-Test: t = {t:.3f}, p = {p:.4f}")
print("Ergebnis:", "signifikanter Unterschied" if p < 0.05 else "kein signifikanter Unterschied")
# 2) Lineare Regression: Verlust in Abhängigkeit von km
reg = stats.linregress(df["km"], df["verlust"])
print(f"\nSteigung: {reg.slope * 1000:.3f} mm je 1000 km")
print(f"R² = {reg.rvalue ** 2:.3f}")
# 3) Kurvenanpassung mit eigenem Modell: verlust = k * km^n
def modell(km, k, n):
 return k * km ** n
params, _ = curve_fit(modell, df["km"], df["verlust"], p0=[1e-4, 1.0], maxfev=10000)
print(f"\nKurvenanpassung: k = {params[0]:.6f}, n = {params[1]:.3f}")
# Vorhersage für 30.000 km
vorhersage = modell(30000, *params)
print(f"Erwarteter Verlust nach 30.000 km: {vorhersage:.2f} mm")
print(f"Erwartete Profiltiefe: {8.0 - vorhersage:.2f} mm")

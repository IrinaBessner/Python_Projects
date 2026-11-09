import numpy as np
# Messreihe eines einzelnen Reifens
km = np.array([0, 10000, 20000, 30000, 40000, 50000])
profil = np.array([8.0, 7.1, 6.3, 5.4, 4.6, 3.9])
# Verschleiß je Intervall, ohne for-Schleife
verschleiss = -np.diff(profil)
km_schritt = np.diff(km)
rate_pro_1000km = verschleiss / km_schritt * 1000
print("Verschleiß je Intervall (mm):", verschleiss)
print("Verschleiß je 1000 km:", rate_pro_1000km.round(3))
print("Mittelwert:", rate_pro_1000km.mean().round(3), "mm")
print("Maximum:", rate_pro_1000km.max().round(3), "mm")
# Vektorisierte Rechnung: Restprofil über der gesetzlichen Grenze
restprofil = profil - 1.6
print("Restprofil über 1,6 mm:", restprofil)
# Geschätzte Restlaufleistung für den letzten Messwert
restlaufleistung_km = restprofil[-1] / rate_pro_1000km.mean() * 1000
print("Geschätzte Restlaufleistung (km):", round(restlaufleistung_km))
# Matrix-Beispiel: Form und Umformen
matrix = np.arange(12).reshape(3, 4)
print("Matrix:\n", matrix)
print("Form:", matrix.shape, "Spaltenmittel:", matrix.mean(axis=0))

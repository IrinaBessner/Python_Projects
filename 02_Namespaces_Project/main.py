
# 1. Imports: Namen werden in den globalen Namespace geladen
import math                         #Name math zeigt aus dem 
from math import floor              #Name "floor" existiert direkt im globalen Namespace      
from mein_modul import begruessung  #Import eines eigenen Moduls
import mein_modul                  # Ganzes Modul als Namespace-Objekt

print("=== 1. Module und Namespaces ===")
print(math.floor(3.7))                 # 3, Zugriff über das Modul
print(floor(3.7))                      # 3, direkter Zugriff
print(begruessung())                   # Hallo aus dem Modul mein_modul!
print(mein_modul.MODUL_NAME)           # Zugriff auf Attribut im Modul-Namespace



# 2. Globaler Namespace
x = "global"                           # Global
print("\n=== 2. Globaler Namespace ===")
print("x" in globals())                # True
print(globals()["x"])                  # global

# ==========================================================
# 3. LEGB-Regel mit verschachtelten Funktionen
def aussen():
    x = "enclosing"                    # Enclosing
    def innen():
        x = "local"                    # Local
        print("innen:", x)             # local
    innen()
    print("aussen:", x)                # enclosing
print("\n=== 3. LEGB ===")
aussen()
print("global:", x)                   # global

# ==========================================================
# 4. Zugriff auf Globales aus einer Funktion (nur lesend)
def zeige_global():
    print("zeige_global sieht:", x)    # Python liest x aus dem globalen Namespace
print("\n=== 4. Lesender Zugriff ===")
zeige_global()

# ==========================================================
# 5. Änderung mit global
def aendere_global():
    global x                           # Ohne global würde hier eine neue lokale Variable entstehen
    x = "geaendert"
print("\n=== 5. global ===")
aendere_global()
print("x nach aendere_global:", x)     # geaendert

# ==========================================================
# 6. Änderung mit nonlocal
def zaehler():
    count = 0
    def erhoehe():
        nonlocal count                 # Verweis auf den Enclosing-Namespace
        count += 1
        return count
    return erhoehe
print("\n=== 6. nonlocal ===")
z = zaehler()
print(z(), z(), z())                   # 1 2 3

# ==========================================================
# 7. Shadowing: Namen werden überschrieben
print("\n=== 7. Shadowing ===")
def floor(x):                          # Überschreibt den importierten floor
    return "eigene Funktion"
print(floor(3.7))                      # eigene Funktion
print(math.floor(3.7))                 # 3, das Modul bleibt unverändert

# ==========================================================
# 8. Namespaces untersuchen
print("\n=== 8. Namespaces untersuchen ===")
print("floor in math:", "floor" in dir(math))         # True
print("hasattr(math, 'floor'):", hasattr(math, "floor"))
def lokale_namen_demo():
    a = 1
    b = 2
    print("locals():", locals())       # {'a': 1, 'b': 2}
lokale_namen_demo()

# ==========================================================
# 9. NameError: Name existiert nicht im Namespace
print("\n=== 9. NameError ===")
try:
    print(unbekannt)                   # Name ist nirgends definiert
except NameError as fehler:
    print("Fehler:", fehler)           # name 'unbekannt' is not defined
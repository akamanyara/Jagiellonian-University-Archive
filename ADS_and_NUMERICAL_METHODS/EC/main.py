import matplotlib.pyplot as plt
import numpy as np

# Wczytanie danych z pliku
dane = []
with open("dane.txt", "r", encoding="utf-8") as f:
    for linia in f:
        # Zmiana przecinków na kropki (format PL → EN)
        cz, we, wy, stosunek, faza = map(lambda x: float(x.replace(",", ".")), linia.strip().split(";"))
        dane.append((cz, stosunek, faza))

# Rozdzielenie na osobne listy
czestotliwosc = [x[0] for x in dane]
amplituda = [x[1] for x in dane]
przesuniecie = [x[2] for x in dane]

# Charakterystyka amplitudowa
plt.figure(figsize=(10, 5))
plt.plot(czestotliwosc, amplituda, 'bo-', label="Uwy/Uwe")
plt.xlabel("Częstotliwość [kHz]")
plt.ylabel("Wzmocnienie (Uwy/Uwe)")
plt.title("Charakterystyka amplitudowa")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Charakterystyka fazowa
plt.figure(figsize=(10, 5))
plt.plot(czestotliwosc, przesuniecie, 'ro-', label="Przesunięcie fazowe [°]")
plt.xlabel("Częstotliwość [kHz]")
plt.ylabel("Przesunięcie fazowe [°]")
plt.title("Charakterystyka fazowa")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

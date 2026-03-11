import numpy as np

INF = float('inf')

def wczytaj_graf(plik):
    with open(plik, 'r') as f:
        linie = f.readlines()
    
    V = int(linie[0].strip()) 
    D = np.full((V, V), INF) 

    for i in range(V):
        D[i][i] = 0

    for linia in linie[1:]:
        u, v, w = map(int, linia.strip().split())
        D[u][v] = w 

    return D, V

def floyd_warshall(D, V):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if D[i][k] != INF and D[k][j] != INF:
                    D[i][j] = min(D[i][j], D[i][k] + D[k][j])
    return D

def wypisz_macierz(D):
    V = len(D)
    print("Macierz najkrótszych odległości:")
    print("    " + "  ".join(f"{j:>3}" for j in range(V)))
    for i in range(V):
        print(f"{i:>2} " + " ".join(f"{(D[i][j] if D[i][j] < INF else 'INF'):>4}" for j in range(V)))

plik = "grafZadanie.txt"
D, V = wczytaj_graf(plik)
D = floyd_warshall(D, V)
wypisz_macierz(D)

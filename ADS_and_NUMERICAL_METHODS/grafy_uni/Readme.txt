UWAGA.
Przykładowe projekty są utworzone w Visual Studio, przez co jest generowane dużo dodatkowych plików. Gdyby ktoś używał innego kompilatora (np. gcc) istotne jest by skupić się na kilku plikach niezbędnych do odpalenia projektu.

GrafMacierzPEGAZ
GrafMacierz.cpp - tu jest metoda Main z testami
Graf.h
Graf.cpp -ten plik trzeba opracować implementując metody z Graf.h


Projekt GrafListaSasiedztwaPEGAZ:
GrafListaSasiedztwa.cpp  - tu jest metoda Main z testami
Graf.h
Graf.cpp - ten plik trzeba opracować implementując metody z Graf.h
edge.h
edge.cpp

DODANE: 

Graf.cpp dla obu implementacji !

kompilacja jaka testowalem: 

g++ -std=c++11  -o GrafMacierz GrafMacierz.cpp Graf.cpp edge.cpp
podobnie dla listysasiedztwa
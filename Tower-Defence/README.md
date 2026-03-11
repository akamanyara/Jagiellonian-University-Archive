# Tower Defense Game in Python
Author: Jakub Pawlusek
Version: 0.1v

Projekt jest implementacją klasycznej gry strategicznej typu "Tower Defense" w języku Python. Celem gracza jest obrona bazy przed falami przeciwników poprzez strategiczne rozmieszczanie wież obronnych. Gra wykorzystuje bibliotekę graficzną `pygame` do renderowania grafiki oraz obsługi interakcji z użytkownikiem.
Jest to obecnie wczesna wersja - w przyszłości mam plan rozbudowywać ją o ulepszenia wiezyczek, UI, etc.

## Spis treści
1. [Wymagania i Instalacja](#wymagania-i-instalacja)
2. [Uruchomienie](#uruchomienie)
3. [Zasady Gry i Sterowanie](#zasady-gry-i-sterowanie)
4. [Zastosowane Algorytmy](#zastosowane-algorytmy)
5. [Struktura Projektu](#struktura-projektu)

---

## Wymagania i Instalacja

Do działania gry wymagany jest zainstalowany interpreter **Python 3.x**.

### Wymagane biblioteki
Jedyną zewnętrzną biblioteką jest `pygame`. Można ją zainstalować za pomocą komendy:

```bash
pip install pygame
```
--- 

## Uruchomienie

1. Upewnij się, że wszystkie pliki źródłowe (main.py, enemy.py, tower.py, settings.py) znajdują się w tym samym katalogu.

2. Otwórz terminal (konsolę) w folderze projektu.

3. Uruchom grę komendą:

```bash
python game/main.py
```

--- 

# Zasady Gry i Sterowanie
Cel gry: Celem gracza jest obrona bazy przed nadchodzącymi falami przeciwników. Gracz przegrywa, gdy jego punkty życia (HP) spadną do zera.

### Mechanika:

Złoto: Za każdego pokonanego przeciwnika gracz otrzymuje złoto.

Wieże: Złoto służy do kupowania wież, które automatycznie atakują wrogów w swoim zasięgu.

Fale: Przeciwnicy nadchodzą w zdefiniowanych turach (falach).

### Sterowanie:
Klawisz             Akcja,Funkcja

LPM (Panel boczny), Wybór wieży ze sklepu
LPM (Mapa),         Postawienie wybranej wieży
PPM,                Anulowanie budowania wieży lub sprzedanie wiezy
SPACJA,             Rozpoczęcie kolejnej fali przeciwników

### Dostosowanie fal przeciwników:

W pliku settings.py w miejscu kodu:

WAVES = [
    ["basic", "basic", "basic", "basic"], # wave 1
    ["basic", "basic", "fast", "basic"], # wave 2
    ["basic", "tank", "fast", "fast", "fast"], # wave 3
    ["basic", "tank", "fast", "fast", "fast", "basic", "tank", "fast", "fast", "fast"] # wave 4
    # to be continued...
]

mozna dodawac fale - ile sie chce (obecnie jest 20) 
wystarczy iść podobnym schematem jak powyzej

### Dostosowanie trudności:
W pliku settings.py mozemy znalezc `TOWER_DATA` oraz `ENEMY_DATA`.
Tam są zawarte dane co do typu i statystyk wiezyczek oraz przeciwników.

W przyszłości będą się pojawiać PATCHe w celu dokładniejszego zbalansowania gry, aby była mozliwa do przejścia ale równiez
nie za łatwa (bo gra łatwa to gra nudna)

Jeśli chce się osobiście balansować grę to mozna to właśnie zrobić przez zmiany w pliku `settings.py`.
--- 

# Zastosowane Algorytmy
W projekcie wykorzystano następujące rozwiązania algorytmiczne:

### 1. Ruch przeciwników (Interpolacja Wektorowa)
Przeciwnicy nie poruszają się po prostych liniach X/Y, lecz wykorzystują wektory do nawigacji między punktami kontrolnymi (`waypoints`). 
Pozwala to na płynny ruch w dowolnym kierunku.

**Zasada działania:**
1. Obliczamy wektor różnicy między aktualną pozycją a celem.
2. Normalizujemy wektor (długość = 1), aby uzyskać sam kierunek.
3. Mnożymy przez prędkość (`speed`).

*Fragment z pliku `enemy.py`:*
```python
def move(self):
    target_point = self.path[self.target_index]
    target_vector = pygame.math.Vector2(target_point)
    
    direction_vector = target_vector - self.position
    distance = direction_vector.length() 
    
    # Jeśli wróg jest daleko od punktu, poruszamy go w stronę celu
    if distance > 0:
        direction_vector = direction_vector.normalize()
        self.position += direction_vector * self.speed
```

### 2. Wykrywanie celów (Dystans Euklidesowy)
Wieże muszą w każdej klatce gry decydować, czy zaatakować przeciwnika. 
Algorytm sprawdza odległość od środka wieży do każdego przeciwnika na mapie.

***Zasada działania:***
Wykorzystujemy metodę distance_to biblioteki Pygame, która oblicza odległość w linii prostej (przeciwprostokątna). 
Jeśli odległość jest mniejsza niż promień zasięgu (range_radius) i wieża jest przeładowana, następuje atak.

**Fragment z pliku `tower.py`:**
```python
def attack(self, enemies_group):
    # Sprawdzenie cooldownu
    if self.cooldown_timer > 0:
        self.cooldown_timer -= 1
        return None
    
    # Pętla po wszystkich wrogach
    for enemy in enemies_group:
        tower_position = pygame.math.Vector2(self.rect.center)
        enemy_position = enemy.position
        
        distance = tower_position.distance_to(enemy_position)
        
        # Sprawdzenie czy wróg jest w zasięgu
        if distance <= self.range_radius:
            enemy.health_points -= self.damage
            self.cooldown_timer = self.attack_speed
            return enemy.rect.center
```

### 3. Zarządzanie falami (Kolejka FIFO)
System spawnowania wrogów opiera się na kolejce (First In, First Out). 
Lista typów przeciwników jest wczytywana z ustawień, a następnie przeciwnicy są "zdejmowani" 
z listy jeden po drugim w określonych odstępach czasu.

**Zasada działania:** 
Gra sprawdza aktualny czas (pygame.time.get_ticks()). 
Jeśli różnica między czasem obecnym a czasem ostatniego spawnu jest większa niż opóźnienie (spawn_delay), 
funkcja pop(0) pobiera pierwszego wroga z listy i usuwa go z kolejki.

**Fragment z pliku `main.py`:**
```python
if len(wave_queue) > 0:
    if (current_time - last_spawn_time) > spawn_delay:
        # Pobierz pierwszego wroga z kolejki i usuń go z listy
        enemy_type = wave_queue.pop(0)
        
        # Stwórz instancję wroga
        new_enemy = create_enemy(enemy_type)
        enemies_group.add(new_enemy)
        
        # Zaktualizuj czas ostatniego spawnu
        last_spawn_time = current_time
```
--- 

# Struktura Projektu
Projekt został podzielony na moduły zgodnie z zasadami OOP:

- main.py - Główny plik uruchomieniowy. Zawiera pętlę gry (Game Loop), obsługę zdarzeń (mysz/klawiatura) oraz renderowanie grafiki.

- enemy.py - Klasa Enemy. Odpowiada za logikę poruszania się, rysowanie paska zdrowia oraz statystyki wroga.

- tower.py - Klasa Tower. Odpowiada za mechanikę namierzania, strzelania i zarządzania czasem przeładowania (cooldown).

- settings.py - Plik konfiguracyjny. Zawiera stałe globalne, definicje mapy (PATH), statystyki wież (TOWER_DATA) oraz konfigurację fal (WAVES).
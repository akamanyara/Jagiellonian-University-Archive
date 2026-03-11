# Project Manager - Aplikacja do zarządzania zadaniami

Prosta aplikacja webowa umożliwiająca tworzenie projektów oraz przypisywanie do nich zadań (To-Do List). 
Projekt realizowany w ramach zaliczenia przedmiotu Techniki WWW.

## Technologie

* **Backend:** Node.js, Express.js
* **Baza danych:** SQLite (plik `manager.db` tworzony automatycznie)
* **Frontend:** HTML, CSS, JavaScript (Fetch API)

## Funkcjonalności

1.  **Zarządzanie Projektami:**
    * Dodawanie nowych projektów (Formularz w modalu).
    * Wyświetlanie listy projektów (Dashboard).
    * Usuwanie projektów (Jednoczesne usuwanie powiązanych zadań).
2.  **Zarządzanie Zadaniami:**
    * Dodawanie zadań do konkretnego projektu.
    * Oznaczanie zadań jako wykonane.
    * Dynamiczne odświeżanie widoków bez przeładowania strony.

## Instalacja i Uruchomienie

Aby uruchomić projekt na lokalnej maszynie, wykonaj następujące kroki:

1.  **Sklonuj lub pobierz projekt.**
2.  **Zainstaluj zależności:**
    Otwórz terminal w folderze projektu i wpisz:
    ```bash
    npm install
    ```
3.  **Uruchom serwer:**
    ```bash
    node server.js
    ```
4.  **Otwórz w przeglądarce:**
    Wejdź na adres: [http://localhost:3000](http://localhost:3000)

## Struktura Projektu

* `models/` - Konfiguracja bazy danych SQLite.
* `public/` - Pliki frontendowe (HTML, CSS, JS).
* `routes/` - Endpointy API (Backend).
* `server.js` - Główny plik serwera.

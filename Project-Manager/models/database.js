const sqlite3 = require('sqlite3').verbose();
const path = require('path');

// ustawiamy sciezke do pliku z baza danych
const dbPath = path.resolve(__dirname, '../manager.db');
// wychodzimy z models do katalogu glownego

// tworzymy polaczenie z baza
const db = new sqlite3.Database(dbPath, (err) => {
    if (err) {
        console.error('Błąd połączenia z bazą danych: ', err.message);
    } else {
        console.log('Połączono z bazą danych');

        // obsluga kluczy obcych (pod kaskadowe usuwanie)
        db.run('PRAGMA foreign_keys = ON')
        initDb();
    }
});

// tworzenie tabeli
function initDb() {
    db.serialize(() => {
        // 1. projekty: id, nazwa, opis, data_utworzenia
        db.run(`CREATE TABLE IF NOT EXISTS projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )`);

        // 2. zadania
        db.run(`CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_id INTEGER,
            content TEXT NOT NULL,
            is_done INTEGER DEFAULT 0,
            FOREIGN KEY(project_id) REFERENCES projects(id) ON DELETE CASCADE
        )`);

        console.log('Tabele gotowe')
    });
}

// eksportowanie obiektu db
module.exports = db;
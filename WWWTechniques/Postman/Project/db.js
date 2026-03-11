const sqlite3 = require("sqlite3").verbose();

const db = new sqlite3.Database("./cats.db", (err) => {
    if (err) {
        console.error("Błąd połączenia z bazą SQLite:", err.message);
    } else {
        console.log("Połączono z bazą SQLite (cats.db).");
    }
});

db.serialize(() => {
    db.run(`
    CREATE TABLE IF NOT EXISTS cats (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      Name TEXT NOT NULL,
      Age INTEGER,
      AdoptionStatus TEXT,
      Race TEXT,
      Owner TEXT NOT NULL
    )
  `);
});

module.exports = db;
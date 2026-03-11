const express = require('express');
const path = require('path');
const db = require('./db');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

// MIDDLEWARE WALIDACYJNY
const validateCatData = (req, res, next) => {
    const { Name, Age, Owner } = req.body;

    // 1. Sprawdzenie czy pola istnieją (zakładamy że Name i Owner są wymagane)
    if (!Name || !Owner) {
        return res.status(400).json({ error: "Brak wymaganych pól: Name oraz Owner" });
    }

    // 2. Walidacja czy Owner to email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(Owner)) {
        return res.status(400).json({ error: "Pole 'Owner' musi być poprawnym adresem email!" });
    }

    // Jeśli wszystko ok, idziemy do właściwej funkcji (endpointu)
    next();
};

// --- ENDPOINTY ---

// POBIERZ WSZYSTKIE KOTY
app.get("/cats", (request, response) => {
    db.all("SELECT * FROM cats", [], (err, rows) => {
        if (err) {
            response.status(500).json({ error: err.message });
            return;
        }
        // Zwracamy pustą tablicę lub dane - status 200 jest ok nawet jak puste
        return response.json(rows);
    });
});

// POBIERZ KOTA PO ID
app.get("/cats/:id", (request, response) => {
    const id = request.params.id;
    
    db.get("SELECT * FROM cats WHERE id = ?", [id], (err, row) => {
        if (err) {
            return response.status(500).json({ error: err.message });
        }
        if (!row) {
            return response.status(404).json({ error: "Cat not found!" });
        }
        return response.json(row);
    });
});

// DODAJ KOTA (Używamy tutaj naszego Middleware validateCatData)
app.post("/cats", validateCatData, (request, response) => {
    // Pobieramy dane zgodne z kolumnami w bazie ze zdjęcia
    const { Name, Age, AdoptionStatus, Race, Owner } = request.body;

    const sql = "INSERT INTO cats (Name, Age, AdoptionStatus, Race, Owner) VALUES (?, ?, ?, ?, ?)";
    const params = [Name, Age, AdoptionStatus || "NotAdopted", Race, Owner];

    db.run(sql, params, function (err) {
        if (err) {
            return response.status(500).json({ error: err.message });
        }

        return response.json({
            message: "Cat added successfully!",
            id: this.lastID
        });
    });
});

app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
});
// endpointy dla projektow
const express = require('express');
const router = express.Router();
const db = require('../models/database');

// 1. Pobierz wszystkie projekty (GET /api/projects)
router.get('/', (req,res) => {
    const sql = 'SELECT * FROM projects ORDER BY created_at DESC';
    db.all(sql, [], (err, rows) => {
        if (err) return res.status(500).json({error: err.message});
        res.json(rows);
    });
});

// 2. Dodaj nowy projekt (POST /api/projects)
router.post('/', (req, res) => {
    const {name, description} = req.body;

    // walidacja - nazwa jest wymagana
    if (!name) { 
        return res.status(400).json({ error: 'nazwa projektu wymagana'});
    }

    const sql = 'INSERT INTO projects (name, description) VALUES (?,?)';
    // tutaj zamiast => uzywamy function() zeby miec dostep do this.ID
    db.run(sql, [name, description], function (err) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ id: this.lastID, name, description});
    });
});

// 3. Usun projekt (DELETE /api/projects/:id)
router.delete('/:id', (req, res) => {
    const sql = 'DELETE FROM projects WHERE id = ?';
    db.run(sql, req.params.id, function (err) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ message: 'usunieto projekt', changes: this.changes});
    });
});

// 4. pobierz zadania dla projektu
router.get('/:id/tasks', (req, res) => {
    const sql = 'SELECT * FROM tasks WHERE project_id = ?';
    db.all(sql, [req.params.id], (err, rows) => {
        if (err) return res.status(500).json({ error: err.message });
        res.json(rows);
    });
});

// 5. Pobierz projekt po id (GET /api/projects/:id)
router.get('/:id', (req, res) => {
    const sql = 'SELECT * FROM projects WHERE id = ?';
    db.get(sql, [req.params.id], (err, row) => {
        if (err) return res.status(500).json({ error: err.message });
        if (!row) return res.status(404).json({ error: "Projekt nie istnieje" });
        res.json(row);
    });
});

module.exports = router;
// endpointy dla taskow
const express = require('express');
const router = express.Router();
const db = require('../models/database');

// dodaj zadanie (post /api/tasks)
router.post('/', (req,res) => {
    const {content, project_id} = req.body;

    if (!content || !project_id) {
        return res.status(400).json({error: 'tresc i id projektu sa wymagane'});
    }

    const sql = 'INSERT INTO tasks (content, project_id) VALUES (?, ?)';
    db.run(sql, [content, project_id], function (err) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({id: this.lastID, content, project_id, is_done: 0});
    });
});

// edytuj status zadania (patch /api/tasks/:id)
router.patch('/:id', (req,res) => {
    const {is_done} = req.body;
    const sql = 'UPDATE tasks SET is_done = ? WHERE id = ?';

    db.run(sql, [is_done, req.params.id], function (err) {
        if (err) return res.status(500).json({error: err.message});
        res.json({message: "zaktualizowano zadanie", changes: this.changes});
    });
});

// usuwanie zadania (DELETE /api/tasks/:id)
router.delete('/:id', (req, res) => {
    const sql = 'DELETE FROM tasks WHERE id = ?';
    db.run(sql, req.params.id, function (err) {
        if (err) return res.status(500).json({ error: err.message });
        res.json({ message: "Usunięto zadanie", changes: this.changes });
    });
});

module.exports = router;
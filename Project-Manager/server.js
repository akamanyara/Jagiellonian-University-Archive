require('dotenv').config();
const express = require('express');
const cors = require('cors');
const path = require('path');

// Import bazy
const db = require('./models/database');

// Import routerów
const projectsRoutes = require('./routes/projects');
const tasksRoutes = require('./routes/tasks');

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, 'public'))); // pod pliki frontendowe

// Podpięcie ścieżek API
app.use('/api/projects', projectsRoutes);
app.use('/api/tasks', tasksRoutes);

// Middleware do obsługi błędów
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).json({
        error: 'Wystąpił wewnętrzny błąd serwera',
        message: err.message
    });
});

// Uruchomienie serwera
app.listen(PORT, () => {
    console.log(`Serwer działa na http://localhost:${PORT}`);
});
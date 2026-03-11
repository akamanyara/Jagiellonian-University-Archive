const apiUrl = '/api/projects';
const projectsContainer = document.getElementById('projects-container');
const modal = document.getElementById('modal');
const addBtn = document.getElementById('addProjectBtn');
const closeBtn = document.querySelector('.close-btn');
const form = document.getElementById('addProjectForm');

// 1. POBIERANIE PROJEKTOW PRZY STARCIE
document.addEventListener('DOMContentLoaded', fetchProjects);

async function fetchProjects() {
    try {
        const res = await fetch(apiUrl);
        const projects = await res.json();
        renderProjects(projects);
    } catch (err) {
        console.error("Błąd pobierania:", err);
        projectsContainer.innerHTML = '<p>Błąd wczytywania danych.</p>';
    }
}

// 2. GENEROWANIE KAFELKOW
function renderProjects(projects) {
    projectsContainer.innerHTML = '';

    if (projects.length === 0) {
        projectsContainer.innerHTML = '<p>Brak projektów. Dodaj pierwszy projekt</p>';
        return;
    }

    projects.forEach(project => {
        const card = document.createElement('div');
        card.className = 'project-card';
        card.innerHTML = `
            <div onclick="location.href='project-details.html?id=${project.id}'">
                <h3>${project.name}</h3>
                <p>${project.description || 'Brak opisu'}</p>
                <small>Utworzono: ${new Date(project.created_at).toLocaleDateString()}</small>
            </div>
            <button class="btn-danger" onclick="deleteProject(event, ${project.id})">Usuń</button>
        `;
        projectsContainer.appendChild(card);
    });
}

// 3. DODAWANIE PROJEKTU (POST)
form.addEventListener('submit', async (e) => {
    e.preventDefault() // stop przeladowania strony

    const name = document.getElementById('projectName').value;
    const description = document.getElementById('projectDesc').value;

    const res = await fetch(apiUrl, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, description})
    });

    if (res.ok) {
        modal.style.display = 'none'; // zamknij popup
        form.reset(); // clear formularza
        fetchProjects(); // odswiez liste
    } else {
        alert('Błąd dodawania projektu');
    }
});

// 4. USUWANIE PROJEKTU
async function deleteProject(event, id) {
    event.stopPropagation(); // unikniecie klikniecia w karte
    if (!confirm('Czy napewno chcesz usunac ten projekt?')) return;

    await fetch(`${apiUrl}/${id}`, { method: 'DELETE' });
    fetchProjects(); // odswiez liste
}

// obsluga modala

if (addBtn && modal) {
    addBtn.addEventListener('click', () => {
        modal.style.display = 'flex'; // zeby okno bylo na srodku
    });
}

window.addEventListener('click', (e) => {
    if (e.target === modal) {
        modal.style.display = 'none';
    }
});
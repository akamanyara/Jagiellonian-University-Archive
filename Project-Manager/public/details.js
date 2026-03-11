// pobieramy id z adresu
const params = new URLSearchParams(window.location.search);
const projectId = params.get('id');

const titleElement = document.getElementById('project-title');
const taskInput = document.getElementById('taskInput');
const addTaskBtn = document.getElementById('addTaskBtn');
const tasksList = document.getElementById('tasks-list');

if (!projectId) window.location.href = 'index.html';

// pobieranie danych projektu i zadan
document.addEventListener('DOMContentLoaded', () => {
    fetchProjectDetails();
    fetchTasks();
});

// pobieranie nazwy projektu
async function fetchProjectDetails() {
    const res = await fetch(`/api/projects/${projectId}`);
    if (res.ok) {
        const data = await res.json();
        titleElement.textContent = data.name;
    } else {
        titleElement.textContent = "Błąd wczytywania projektu";
    }
}

// pobieranie listy taskow
async function fetchTasks() {
    const res = await fetch(`/api/projects/${projectId}/tasks`);
    const tasks = await res.json();
    renderTasks(tasks);
}

// wyswietlanie zadan
function renderTasks(tasks) {
    tasksList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = `task-item ${task.is_done ? 'task-done' : ''}`;
        
        li.innerHTML = `
            <div class="task-content">
                <input type="checkbox" class="task-checkbox" 
                    ${task.is_done ? 'checked' : ''} 
                    onchange="toggleTask(${task.id}, this.checked)">
                <span>${task.content}</span>
            </div>
            <button class="btn-delete-task" onclick="deleteTask(${task.id})">&times;</button>
        `;
        tasksList.appendChild(li);
    });
}

// usuwanie zadania
window.deleteTask = async (id) => {
    if (!confirm("Czy na pewno chcesz usunąć to zadanie?")) return;

    await fetch(`/api/tasks/${id}`, {
        method: 'DELETE'
    });
    
    fetchTasks(); // Odśwież listę po usunięciu
};

// dodawanie nowego zadania
addTaskBtn.addEventListener('click', async () => {
    const content = taskInput.value;
    if (!content) return;

    await fetch('/api/tasks', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content, project_id: projectId })
    });

    taskInput.value = ''; // wyczyść pole
    fetchTasks(); // ddśwież listę
});

// zmien status zadania 
window.toggleTask = async (id, isDone) => {
    await fetch(`/api/tasks/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ is_done: isDone ? 1 : 0 })
    });
    fetchTasks();
};


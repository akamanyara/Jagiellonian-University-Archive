async function loadCats() {
    const res = await fetch("/cats");
    const cats = await res.json();

    const list = document.getElementById("catList");
    list.innerHTML = "";

    cats.forEach(c => {
        const li = document.createElement("li");
        // Wyświetlamy dane zgodnie z kolumnami bazy
        li.textContent = `${c.id}. ${c.Name} (Lat: ${c.Age}, Właściciel: ${c.Owner})`;
        list.appendChild(li);
    });
}

async function addCat() {
    const Name = document.getElementById("name").value;
    const Age = document.getElementById("age").value;
    const Owner = document.getElementById("owner").value;
    const Race = document.getElementById("race").value;
    const AdoptionStatus = document.getElementById("status").value;

    const res = await fetch("/cats", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ Name, Age, Owner, Race, AdoptionStatus })
    });

    if (!res.ok) {
        // Tu wyświetli się błąd z naszego middleware (np. że email jest zły)
        const errData = await res.json();
        alert("Błąd: " + errData.error);
        return;
    }

    // Czyścimy pola
    document.getElementById("name").value = "";
    document.getElementById("age").value = "";
    document.getElementById("owner").value = "";
    
    loadCats();
}

async function getCatById() {
    const id = document.getElementById("searchId").value;
    if (!id) return;

    const res = await fetch(`/cats/${id}`);
    const out = document.getElementById("singleCat");

    if (!res.ok) {
        out.textContent = "Nie znaleziono!";
        return;
    }

    const cat = await res.json();
    out.textContent = JSON.stringify(cat, null, 2);
}
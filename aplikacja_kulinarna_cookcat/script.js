const DEFAULT_IMG = "widelec.png";

const initialRecipes = [
    {
        id: 1,
        name: "Kremowa Zupa z Dyni",
        type: "Obiad",
        difficulty: "Łatwy",
        time: 45,
        portions: 4,
        img: "widelec.png",
        desc: "Aksamitna zupa krem z pieczonej dyni z dodatkiem imbiru i mleka kokosowego. Idealna na chłodne jesienne dni.",
        ingredients: [
            {name: "Dynia Hokkaido", qty: 1, unit: "kg"}, 
            {name: "Cebula", qty: 1, unit: "szt"}, 
            {name: "Czosnek", qty: 2, unit: "szt"},
            {name: "Imbir świeży", qty: 10, unit: "g"},
            {name: "Bulion warzywny", qty: 750, unit: "ml"},
            {name: "Mleczko kokosowe", qty: 200, unit: "ml"}
        ],
        steps: [
            "Dynię pokrój w kostkę (nie musisz obierać Hokkaido).", 
            "Cebulę i czosnek posiekaj i zeszklij w garnku na oliwie.", 
            "Dodaj dynię i starty imbir, smaż chwilę.", 
            "Zalej gorącym bulionem i gotuj ok. 20 minut do miękkości.",
            "Zblenduj zupę na gładki krem.",
            "Dodaj mleczko kokosowe, dopraw solą i pieprzem."
        ],
        owner: "Elżbieta1984",
        reviews: [
            {user: "Ania_K", rating: 5, text: "Wyszła przepyszna! Dodałam grzanki."},
            {user: "Marek", rating: 4, text: "Trochę za ostra, dałem za dużo imbiru."}
        ]
    },
    {
        id: 2,
        name: "Amerykańskie Pancakes",
        type: "Śniadanie",
        difficulty: "Średni",
        time: 20,
        portions: 2,
        img: "pancake.png",
        desc: "Puszyste, mięciutkie placuszki idealne na słodkie śniadanie. Najlepiej smakują z syropem klonowym i borówkami.",
        ingredients: [
            {name: "Mąka pszenna", qty: 1.5, unit: "szkl"}, 
            {name: "Jajko", qty: 1, unit: "szt"}, 
            {name: "Mleko", qty: 1.25, unit: "szkl"},
            {name: "Masło roztopione", qty: 3, unit: "łyżki"},
            {name: "Proszek do pieczenia", qty: 3, unit: "łyżeczki"},
            {name: "Cukier", qty: 1, unit: "łyżka"}
        ],
        steps: [
            "Wymieszaj suche składniki (mąka, cukier, proszek, sól) w misce.", 
            "Wlej mleko, jajko i roztopione masło. Wymieszaj krótko, tylko do połączenia składników.", 
            "Rozgrzej patelnię (bez tłuszczu lub z minimalną ilością).",
            "Nakładaj porcje ciasta, smaż aż pojawią się bąbelki, wtedy przewróć na drugą stronę.",
            "Smaż na złoty kolor."
        ],
        owner: "leniwiec512",
        reviews: []
    },
    {
        id: 3,
        name: "Spaghetti Carbonara",
        type: "Obiad",
        difficulty: "Trudny",
        time: 25,
        portions: 2,
        img: "carbonara.png",
        desc: "Klasyczny włoski przepis. Żadnej śmietany! Tylko jajka, ser Pecorino, guanciale i dużo pieprzu.",
        ingredients: [
            {name: "Makaron Spaghetti", qty: 200, unit: "g"}, 
            {name: "Guanciale lub Boczek", qty: 100, unit: "g"}, 
            {name: "Jajka (żółtka)", qty: 3, unit: "szt"},
            {name: "Ser Pecorino Romano", qty: 50, unit: "g"},
            {name: "Świeży pieprz", qty: 1, unit: "łyżeczka"}
        ],
        steps: [
            "Boczek pokrój w paski i wytop na patelni na chrupko.", 
            "W miseczce wymieszaj żółtka z drobno startym serem i dużą ilością pieprzu.", 
            "Ugotuj makaron al dente w osolonej wodzie.",
            "Wrzuć makaron na patelnię z boczkiem (zostaw trochę wody z gotowania!). Wymieszaj.",
            "Zdejmij patelnię z ognia. Odczekaj chwilę.",
            "Wlej masę jajeczną, energicznie mieszając, aby powstał kremowy sos (uważaj, żeby nie zrobiła się jajecznica!). W razie potrzeby dodaj wody z makaronu."
        ],
        owner: "śliwka123",
        reviews: [
            {user: "Włoch_z_Polski", rating: 5, text: "Bravissimo! Prawdziwy przepis."}
        ]
    },
    {
        id: 4,
        name: "Brownie z Fasoli",
        type: "Deser",
        difficulty: "Łatwy",
        time: 60,
        portions: 8,
        img: "widelec.png",
        desc: "Zdrowsza wersja popularnego ciasta. Wilgotne, mocno czekoladowe i bezglutenowe. Nie czuć smaku fasoli!",
        ingredients: [
            {name: "Czerwona fasola (puszka)", qty: 1, unit: "szt"}, 
            {name: "Banan dojrzały", qty: 1, unit: "szt"}, 
            {name: "Jajka", qty: 2, unit: "szt"},
            {name: "Kakao", qty: 2, unit: "łyżki"},
            {name: "Ksylitol lub cukier", qty: 0.5, unit: "szkl"},
            {name: "Olej", qty: 1, unit: "łyżka"},
            {name: "Proszek do pieczenia", qty: 1, unit: "łyżeczka"}
        ],
        steps: [
            "Fasolę bardzo dokładnie opłucz na sitku.", 
            "Zblenduj wszystkie składniki na gładką, jednolitą masę.", 
            "Przelej masę do małej keksówki wyłożonej papierem.",
            "Piecz w 180 stopniach przez ok. 40-45 minut.",
            "Krój dopiero po całkowitym wystudzeniu."
        ],
        owner: "FitMarta_90",
        reviews: []
    }
];

class CookCatApp {
    constructor() {
        this.recipes = JSON.parse(localStorage.getItem('cc_recipes_final_v1')) || initialRecipes;
        this.user = JSON.parse(localStorage.getItem('cc_user_final_v1')) || null;
        this.tempIngredients = [];
        this.tempSteps = [];
        this.editingId = null; 
        this.init();
    }

    init() {
        window.onpopstate = (event) => {
            if (event.state) {
                if (event.state.recipeId) {
                    this.showDetails(event.state.recipeId, false);
                } else if (event.state.view) {
                    this.navigate(event.state.view, false);
                }
            } else {
                this.navigate('home', false);
            }
        };

        const hash = window.location.hash;
        if (hash.startsWith('#recipe-')) {
            const id = parseInt(hash.split('-')[1]);
            if (!isNaN(id)) {
                 this.showDetails(id, false);
            }
        } else {
            this.navigate(hash.replace('#', '') || 'home', false);
        }
        
        this.updateUIAuth();
        this.toggleAuthMode('login'); // Domyślny tryb logowania
    }

    navigate(viewId, addToHistory = true) {
        if ((viewId === 'favorites' || viewId === 'add' || viewId === 'my-recipes') && !this.user) {
            this.showNotification("Wymagane logowanie!", "warning");
            this.navigate('profile', true);
            document.getElementById('auth-msg').innerText = "Zaloguj się, aby uzyskać dostęp do tej sekcji.";
            document.getElementById('auth-msg').style.color = "var(--danger)";
            return;
        }

        if (addToHistory) {
            history.pushState({ view: viewId }, null, `#${viewId}`);
        }

        document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(el => el.classList.remove('active'));

        const target = document.getElementById(viewId + '-view') || document.getElementById('home-view');
        target.classList.add('active');
        
        const navMap = {'home':'nav-home', 'favorites':'nav-fav', 'add':'nav-add', 'profile':'nav-profile', 'my-recipes':'nav-my'};
        if(navMap[viewId]) document.getElementById(navMap[viewId]).classList.add('active');

        if(viewId === 'home') this.renderRecipes();
        else if(viewId === 'favorites') this.renderRecipes(); // Używamy renderRecipes do obsługi szukania
        else if(viewId === 'my-recipes') this.renderRecipes();
        else if(viewId === 'add') {
            if(!this.editingId) this.resetForm();
        }

        window.scrollTo(0, 0);
    }

    resetFiltersAndGoHome() {
        document.getElementById('search-input').value = '';
        this.editingId = null; 
        this.navigate('home');
    }

    createCard(r) {
        const isFav = this.user && this.user.favorites && this.user.favorites.includes(r.id);
        const isMine = this.user && r.owner === this.user.name;
        const { avg, count } = this.getRating(r);

        let diffColor = 'var(--diff-easy)';
        if(r.difficulty === 'Średni') diffColor = 'var(--diff-med)';
        if(r.difficulty === 'Trudny') diffColor = 'var(--diff-hard)';

        const div = document.createElement('div');
        div.className = 'card';
        div.innerHTML = `
            <div class="fav-btn ${isFav?'active':''}" onclick="event.stopPropagation(); app.toggleFav(${r.id})" title="Ulubione"><i class="fas fa-star"></i></div>
            ${isMine ? `
                <div class="delete-btn" onclick="event.stopPropagation(); app.deleteRecipe(${r.id})" title="Usuń"><i class="fas fa-trash"></i></div>
                <div class="edit-btn" onclick="event.stopPropagation(); app.editRecipe(${r.id})" title="Edytuj"><i class="fas fa-pencil-alt"></i></div>
            ` : ''}
            <img src="${r.img || DEFAULT_IMG}" class="card-img" onerror="this.onerror=null;this.src='${DEFAULT_IMG}';">
            <div class="card-body">
                <span class="card-badge">${r.type}</span>
                <div class="card-title">${r.name}</div>
                <div style="font-size:0.9rem; color:#666; display:flex; justify-content:space-between;">
                    <span><i class="fas fa-clock"></i> ${r.time} min</span>
                    <span style="font-weight:700; color:${diffColor}">${r.difficulty}</span>
                </div>
                ${count > 0 ? `<div class="rating-stars">${this.renderStars(avg)} <span class="rating-count">(${count})</span></div>` : ''}
            </div>
        `;
        div.onclick = () => this.showDetails(r.id);
        return div;
    }

    editRecipe(id) {
        const r = this.recipes.find(item => item.id === id);
        if(!r) return;

        this.editingId = id; 
        this.tempIngredients = [...r.ingredients];
        this.tempSteps = [...r.steps];

        document.getElementById('form-title').innerText = "Edytuj Przepis";
        document.getElementById('new-name').value = r.name;
        document.getElementById('new-type').value = r.type;
        document.getElementById('new-diff').value = r.difficulty;
        document.getElementById('new-time').value = r.time;
        document.getElementById('new-portions').value = r.portions;
        document.getElementById('new-desc').value = r.desc;
        
        this.renderQueue('ing');
        this.renderQueue('step');

        this.navigate('add');
        this.showNotification("Tryb edycji włączony", "info");
    }

    submitRecipe(e) {
        e.preventDefault();
        
        const actionName = this.editingId ? "zapisać zmiany" : "dodać ten przepis";
        if(!confirm(`Czy na pewno chcesz ${actionName}? Anuluj, aby wrócić do edycji.`)) {
            return; 
        }

        if(this.tempIngredients.length === 0 || this.tempSteps.length === 0) return this.showNotification("Dodaj składniki i kroki!", "warning");
        
        const time = parseInt(document.getElementById('new-time').value);
        const portions = parseInt(document.getElementById('new-portions').value);

        if(isNaN(time) || time <= 0) return this.showNotification("Czas musi być liczbą dodatnią!", "warning");
        if(isNaN(portions) || portions <= 0 || !Number.isInteger(portions)) return this.showNotification("Liczba porcji musi być liczbą naturalną!", "warning");

        const fileInput = document.getElementById('new-img-file');
        
        const save = (imgSrc) => {
            const recipeData = {
                id: this.editingId || Date.now(), 
                name: document.getElementById('new-name').value,
                type: document.getElementById('new-type').value,
                difficulty: document.getElementById('new-diff').value,
                time: time,
                portions: portions,
                img: imgSrc,
                desc: document.getElementById('new-desc').value,
                ingredients: this.tempIngredients,
                steps: this.tempSteps,
                owner: this.user.name,
                reviews: this.editingId ? (this.recipes.find(r=>r.id===this.editingId).reviews) : []
            };

            if(this.editingId) {
                const idx = this.recipes.findIndex(r => r.id === this.editingId);
                this.recipes[idx] = recipeData;
                this.showNotification("Przepis zaktualizowany!", "success");
            } else {
                this.recipes.push(recipeData);
                this.showNotification("Przepis dodany!", "success");
            }

            localStorage.setItem('cc_recipes_final_v1', JSON.stringify(this.recipes));
            this.resetFiltersAndGoHome();
        };

        if(fileInput.files[0]) {
            const reader = new FileReader();
            reader.onload = (ev) => save(ev.target.result);
            reader.readAsDataURL(fileInput.files[0]);
        } else {
            let oldImg = null;
            if(this.editingId) {
                const oldR = this.recipes.find(r=>r.id===this.editingId);
                oldImg = oldR.img;
            }
            save(oldImg); 
        }
    }

    getRating(recipe) {
        if (!recipe.reviews || recipe.reviews.length === 0) return { avg: 0, count: 0 };
        const sum = recipe.reviews.reduce((a, b) => a + b.rating, 0);
        return { avg: sum / recipe.reviews.length, count: recipe.reviews.length };
    }
    renderStars(rating) {
        let html = '';
        for (let i = 1; i <= 5; i++) {
            if (rating >= i) html += '<i class="fas fa-star"></i>';
            else if (rating >= i - 0.5) html += '<i class="fas fa-star-half-alt"></i>';
            else html += '<i class="far fa-star"></i>';
        }
        return html;
    }
    
    // ZMIANA: Kontekstowe renderowanie (filtracja)
    renderRecipes() {
        const type = document.getElementById('filter-type').value;
        const diff = document.getElementById('filter-diff').value;
        const time = document.getElementById('filter-time').value;

        // Ustalenie kontekstu (gdzie jesteśmy)
        let targetGridId = 'recipe-grid';
        let baseList = this.recipes;
        let search = document.getElementById('search-input').value.toLowerCase(); // domyślny input

        const activeView = document.querySelector('.view-section.active');
        
        if (activeView && activeView.id === 'favorites-view') {
            targetGridId = 'favorites-grid';
            baseList = this.recipes.filter(r => this.user && this.user.favorites && this.user.favorites.includes(r.id));
            search = document.getElementById('fav-search-input').value.toLowerCase();
        } else if (activeView && activeView.id === 'my-recipes-view') {
            targetGridId = 'my-recipes-grid';
            baseList = this.recipes.filter(r => this.user && r.owner === this.user.name);
            search = document.getElementById('my-search-input').value.toLowerCase();
        }

        const filtered = baseList.filter(r => {
             return r.name.toLowerCase().includes(search) &&
                   (type === 'all' || r.type === type) &&
                   (diff === 'all' || r.difficulty === diff) &&
                   (!time || r.time <= parseInt(time));
        });

        const grid = document.getElementById(targetGridId);
        if(!grid) return; // zabezpieczenie
        grid.innerHTML = '';
        
        if(filtered.length === 0) {
            grid.innerHTML = '<div style="grid-column:1/-1; text-align:center; padding:50px; color:#888;">Nic tu nie ma... 🐱</div>';
        } else {
            filtered.forEach(r => grid.appendChild(this.createCard(r)));
        }

        // Dodanie kafelka "Dodaj" tylko na stronie głównej
        if(targetGridId === 'recipe-grid' && !search && type==='all') {
             const addCard = document.createElement('div');
             addCard.className = 'add-card';
             addCard.innerHTML = '<i class="fas fa-plus" style="font-size:3rem; margin-bottom:10px;"></i><h3>Dodaj przepis</h3>';
             addCard.onclick = () => this.navigate('add');
             grid.appendChild(addCard);
        }
    }

    deleteRecipe(id) {
        if(!confirm("Czy na pewno chcesz usunąć ten przepis?")) return;
        this.recipes = this.recipes.filter(r => r.id !== id);
        localStorage.setItem('cc_recipes_final_v1', JSON.stringify(this.recipes));
        if(this.user.favorites) {
            this.user.favorites = this.user.favorites.filter(fid => fid !== id);
            this.saveUser();
        }
        this.showNotification("Przepis usunięty.", "success");
        this.renderRecipes();
    }

    showDetails(id, addToHistory = true) {
        const r = this.recipes.find(i => i.id === id);
        if(!r) return;
        this.currentRecipeForCalc = r;
        const view = document.getElementById('recipe-view');
        const { avg, count } = this.getRating(r);

        const isFav = this.user && this.user.favorites && this.user.favorites.includes(r.id);

        let diffColor = '#666';
        if(r.difficulty === 'Średni') diffColor = 'var(--diff-med)';
        if(r.difficulty === 'Trudny') diffColor = 'var(--diff-hard)';
        if(r.difficulty === 'Łatwy') diffColor = 'var(--diff-easy)';

        if(addToHistory) {
            history.pushState({ view: 'recipe', recipeId: id }, null, `#recipe-${id}`);
        }

        document.querySelectorAll('.view-section').forEach(el => el.classList.remove('active'));
        view.classList.add('active');
        window.scrollTo(0, 0); 

        const ingRows = r.ingredients.map(ing => `<tr><td style="font-weight:600;">${ing.name}</td><td><span class="calc-qty" data-base="${ing.qty}">${ing.qty}</span> ${ing.unit}</td></tr>`).join('');
        const stepsList = r.steps ? r.steps.map((s, i) => `<li><span class="step-num">${i+1}.</span><span>${s}</span></li>`).join('') : '<li>Brak instrukcji</li>';
        
        let reviewsHtml = '';
        if(count > 0) {
             // ZMIANA: Możliwość usuwania własnych opinii
             reviewsHtml = r.reviews.map((rev, idx) => {
                const isMyReview = this.user && rev.user === this.user.name;
                return `
                <div class="review-item">
                    <div class="review-header" style="display:flex; justify-content:space-between; align-items:center;">
                        <div>
                            <span class="review-user" style="font-weight:bold;">${rev.user}</span>
                            <span style="color:var(--accent); margin-left:10px;">${this.renderStars(rev.rating)}</span>
                        </div>
                        ${isMyReview ? `<button class="btn-small btn-danger" onclick="app.deleteReview(${r.id}, ${idx})" style="padding:2px 8px; font-size:0.7rem; width:auto; margin:0;">Usuń</button>` : ''}
                    </div>
                    <div style="margin-top:5px;">${rev.text}</div>
                </div>
            `}).join('');
        } else {
            reviewsHtml = '<p style="padding:20px; color:#999; text-align:center;">Brak opinii. Bądź pierwszy!</p>';
        }

        // ZMIANA: Poprawiony przycisk Wróć, przycisk Ulubione
        view.innerHTML = `
            <div class="recipe-detail">
                <img src="${r.img || DEFAULT_IMG}" class="detail-img" onerror="this.onerror=null;this.src='${DEFAULT_IMG}';">
                <div class="detail-content">
                    <button class="btn btn-small" onclick="window.history.back()" style="margin-bottom:20px; width:auto;">&larr; Wróć</button>
                    
                    <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:10px;">
                        <h1>${r.name}</h1>
                        <button class="btn btn-small" onclick="app.toggleFav(${r.id})" style="width:auto; background: ${isFav ? 'var(--accent)' : '#eee'}; color: ${isFav ? '#fff' : '#555'};">
                            <i class="${isFav ? 'fas' : 'far'} fa-star"></i> ${isFav ? 'Ulubiony' : 'Do ulubionych'}
                        </button>
                    </div>
                    
                    <div style="display:flex; gap: 20px; margin-bottom: 20px; color: #666; font-size: 1rem; margin-top:10px;">
                        <span><i class="fas fa-clock"></i> ${r.time} min</span>
                        <span><i class="fas fa-utensils"></i> ${r.type}</span>
                        <span style="color:${diffColor}; font-weight:700;">${r.difficulty}</span>
                    </div>

                    <div style="margin-bottom:15px; color:#666;">
                        Autor: <b>${r.owner || 'Nieznany'}</b> | 
                        <span style="color:var(--accent)">${count > 0 ? this.renderStars(avg) : ''}</span> 
                        ${count > 0 ? `(${avg.toFixed(1)} / 5)` : ''}
                    </div>
                    <p>${r.desc || 'Brak opisu.'}</p>
                    
                    <div class="calculator-box">
                        <i class="fas fa-calculator" style="font-size:1.5rem; color:var(--primary);"></i>
                        <div>
                            <label style="font-weight:600;">Przelicz porcje:</label>
                            <input type="number" id="calc-portions" value="${r.portions}" min="1" step="1" style="width:60px; padding:5px;" onchange="app.recalcPortions(this.value)">
                        </div>
                        <div style="font-size:0.9rem; color:#666;">(Domyślna ilość porcji: ${r.portions})</div>
                    </div>

                    <h3>Składniki</h3>
                    <table class="ing-table">${ingRows}</table>

                    <h3 style="margin-top:30px;">Przygotowanie</h3>
                    <ul class="step-list">${stepsList}</ul>

                    <div class="reviews-section">
                        <h3>Opinie (${count})</h3>
                        ${reviewsHtml}
                        <div style="background:#f9f9f9; padding:20px; border-radius:10px; margin-top:20px;">
                             <h4>Dodaj Opinię</h4>
                             <div style="margin:10px 0;">
                                 <label>Ocena: </label>
                                 <select id="review-rating" style="padding:5px;">
                                     <option value="5">5 gwiazdek</option>
                                     <option value="4">4 gwiazdki</option>
                                     <option value="3">3 gwiazdki</option>
                                     <option value="2">2 gwiazdki</option>
                                     <option value="1">1 gwiazdka</option>
                                 </select>
                             </div>
                             <textarea id="review-text" class="form-input" rows="2" placeholder="Jak smakowało?"></textarea>
                             <button class="btn btn-small" onclick="app.addReview(${r.id})">Dodaj opinię</button>
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    recalcPortions(newVal) {
        const parsed = parseInt(newVal);
        if(isNaN(parsed) || parsed < 1) return;
        
        const factor = parsed / this.currentRecipeForCalc.portions;
        document.querySelectorAll('.calc-qty').forEach(span => {
            const base = parseFloat(span.getAttribute('data-base'));
            if(!isNaN(base)) span.innerText = (Math.round(base * factor * 100) / 100);
        });
        // ZMIANA: Powiadomienie
        this.showNotification(`Przeliczono składniki dla ${parsed} porcji`, "info");
    }

    addReview(id) {
        if (!this.user) {
            return this.showNotification("Musisz się zalogować, aby dodać opinię!", "warning");
        }

        const text = document.getElementById('review-text').value;
        const rating = parseFloat(document.getElementById('review-rating').value);
        if(!rating) return;
        const recipe = this.recipes.find(r => r.id === id);
        if(!recipe.reviews) recipe.reviews = [];
        
        if(recipe.reviews.some(r => r.user === this.user.name)) {
            return this.showNotification("Możesz dodać tylko jedną opinię!", "warning");
        }

        recipe.reviews.push({ user: this.user.name, rating: rating, text: text });
        localStorage.setItem('cc_recipes_final_v1', JSON.stringify(this.recipes));
        this.showNotification("Opinia dodana!", "success");
        this.showDetails(id, false); // false, żeby nie dodawać historii
    }

    // ZMIANA: Funkcja usuwania opinii
    deleteReview(recipeId, reviewIdx) {
        if(!confirm("Usunąć opinię?")) return;
        const r = this.recipes.find(i => i.id === recipeId);
        if(r && r.reviews) {
            r.reviews.splice(reviewIdx, 1);
            localStorage.setItem('cc_recipes_final_v1', JSON.stringify(this.recipes));
            this.showNotification("Opinia usunięta", "success");
            this.showDetails(recipeId, false);
        }
    }

    resetForm() {
        this.editingId = null;
        document.getElementById('form-title').innerText = "Stwórz Przepis";
        document.querySelector('#add-view form').reset();
        this.tempIngredients = [];
        this.tempSteps = [];
        this.renderQueue('ing');
        this.renderQueue('step');
    }

    addIngredientToQueue() {
        const name = document.getElementById('ing-name').value;
        const qty = document.getElementById('ing-qty').value;
        const unit = document.getElementById('ing-unit').value;
        if(!name || !qty) return this.showNotification("Podaj nazwę i ilość!", "warning");
        this.tempIngredients.push({ name, qty: parseFloat(qty), unit });
        document.getElementById('ing-name').value = '';
        document.getElementById('ing-qty').value = '';
        document.getElementById('ing-unit').value = ''; // reset selecta
        this.renderQueue('ing');
    }

    addStepToQueue() {
        const desc = document.getElementById('step-desc').value;
        if(!desc) return;
        this.tempSteps.push(desc);
        document.getElementById('step-desc').value = '';
        this.renderQueue('step');
    }

    renderQueue(type) {
        const list = document.getElementById(type + '-queue');
        const data = type === 'ing' ? this.tempIngredients : this.tempSteps;
        list.style.display = data.length ? 'block' : 'none';
        list.innerHTML = '';
        data.forEach((item, i) => {
            const li = document.createElement('li');
            li.className = 'queue-item';
            const txt = type === 'ing' ? `<b>${item.name}</b>: ${item.qty} ${item.unit}` : `${i+1}. ${item}`;
            li.innerHTML = `<span>${txt}</span><i class="fas fa-trash remove-icon" onclick="app.removeFromQueue('${type}', ${i})"></i>`;
            list.appendChild(li);
        });
    }

    removeFromQueue(type, idx) {
        if(type === 'ing') this.tempIngredients.splice(idx, 1);
        else this.tempSteps.splice(idx, 1);
        this.renderQueue(type);
    }

    toggleFilterModal() { document.getElementById('filter-modal').classList.toggle('active'); }
    applyFilters() { this.renderRecipes(); this.toggleFilterModal(); }
    clearFilters() {
        document.getElementById('filter-type').value='all';
        document.getElementById('filter-diff').value='all';
        document.getElementById('filter-time').value='';
        this.renderRecipes();
        this.toggleFilterModal();
    }
    
    // ZMIANA: Obsługa przełączania trybów logowania/rejestracji
    toggleAuthMode(mode) {
        const btnLogin = document.getElementById('btn-mode-login');
        const btnReg = document.getElementById('btn-mode-register');
        const actionBtn = document.getElementById('auth-action-btn');
        const emailGroup = document.getElementById('email-group');

        if (mode === 'login') {
            btnLogin.style.background = 'var(--primary)';
            btnLogin.style.color = 'white';
            btnReg.style.background = '#ccc';
            btnReg.style.color = '#333';
            emailGroup.style.display = 'none';
            actionBtn.innerText = 'Zaloguj się';
            actionBtn.onclick = () => app.login();
        } else {
            btnReg.style.background = 'var(--primary)';
            btnReg.style.color = 'white';
            btnLogin.style.background = '#ccc';
            btnLogin.style.color = '#333';
            emailGroup.style.display = 'block';
            actionBtn.innerText = 'Zarejestruj się';
            actionBtn.onclick = () => app.register();
        }
    }

    checkInputs() {
        const l = document.getElementById('login-user').value;
        const p = document.getElementById('login-pass').value;
        if(!l || !p) {
            this.showNotification("Podaj login i hasło!", "warning");
            return null;
        }
        return { l, p };
    }

    login() {
        const creds = this.checkInputs();
        if(!creds) return;
        
        const db = JSON.parse(localStorage.getItem('cc_users_db_final')) || {};
        
        if(db[creds.l]) {
            if(db[creds.l].pass === creds.p) {
                this.user = db[creds.l];
                this.saveUser();
                this.updateUIAuth();
                this.showNotification("Zalogowano pomyślnie", "success");
                this.navigate('home');
            } else {
                this.showNotification("Błędne hasło!", "warning");
            }
        } else {
            this.showNotification("Użytkownik nie istnieje. Zarejestruj się.", "warning");
        }
    }

    register() {
        const creds = this.checkInputs();
        if(!creds) return;

        const db = JSON.parse(localStorage.getItem('cc_users_db_final')) || {};

        if(db[creds.l]) {
            this.showNotification("Taki użytkownik już istnieje!", "warning");
        } else {
            const newUser = { name: creds.l, pass: creds.p, favorites: [] };
            db[creds.l] = newUser;
            localStorage.setItem('cc_users_db_final', JSON.stringify(db));
            this.user = newUser;
            this.saveUser();
            this.updateUIAuth();
            this.showNotification("Konto utworzone! Zalogowano.", "success");
            this.navigate('home');
        }
    }

    logout() {
        this.user = null;
        localStorage.removeItem('cc_user_final_v1');
        this.updateUIAuth();
        this.showNotification("Wylogowano");
        this.navigate('home');
    }
    updateUIAuth() {
        const isLogged = !!this.user;
        document.getElementById('auth-panel').style.display = isLogged ? 'none' : 'block';
        document.getElementById('user-panel').style.display = isLogged ? 'block' : 'none';
        document.getElementById('nav-profile').classList.toggle('user-active', isLogged);
        document.getElementById('nav-my').style.display = isLogged ? 'block' : 'none';
        if(isLogged) document.getElementById('username-display').innerText = this.user.name;
    }
    saveUser() {
        localStorage.setItem('cc_user_final_v1', JSON.stringify(this.user));
        const db = JSON.parse(localStorage.getItem('cc_users_db_final')) || {};
        db[this.user.name] = this.user;
        localStorage.setItem('cc_users_db_final', JSON.stringify(db));
    }
    toggleFav(id) {
        if(!this.user) return this.showNotification("Musisz się zalogować!", "warning");
        if(!this.user.favorites) this.user.favorites = [];
        const idx = this.user.favorites.indexOf(id);
        if(idx > -1) {
            this.user.favorites.splice(idx, 1);
            this.showNotification("Usunięto z ulubionych");
        } else {
            this.user.favorites.push(id);
            this.showNotification("Dodano do ulubionych", "success");
        }
        this.saveUser();
        // Zostajemy na tym samym widoku, ale odświeżamy stan przycisku
        if(document.getElementById('recipe-view').classList.contains('active')) {
             this.showDetails(id, false); 
        } else {
             this.renderRecipes();
        }
    }
    showNotification(msg, type='normal') {
        const n = document.getElementById('notification');
        n.innerText = msg;
        n.className = 'notification show ' + type;
        setTimeout(() => n.className = 'notification', 3000);
    }
}
const app = new CookCatApp();
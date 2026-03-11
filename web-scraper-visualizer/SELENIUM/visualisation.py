import json
import re
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import pandas as pd

with open("books.json", encoding="utf-8") as f:
    books = json.load(f)

print(f"Wczytano rekordów: {len(books)}")

def extract_year(text):
    match = re.search(r"\b(1[89]\d{2}|20\d{2})\b", text)
    return int(match.group(1)) if match else None

def normalize_lang(token):
    unwanted = {"więcej", "mniej", "pokaż", "wszystko", "hide", "all", "everything"}
    token = token.lower().strip()
    token = re.sub(r'\s+', ' ', token)
    for suffix in ["...", "…", "more"]:
        if token.endswith(suffix):
            token = token[:-len(suffix)].strip()
    langs = token.split()
    return [lang for lang in langs if lang and lang not in unwanted]

# 1) FALA ZAINTERESOWANIA
years = []
for b in books:
    for k, v in b.items():
        if "data" in k.lower() or "rok" in k.lower():
            y = extract_year(v)
            if y: years.append(y)
            break

if years and min(years) >= 1976:
    bins = list(range(1976, 2026, 5))
    labels = [f"{bins[i]}–{bins[i+1]-1}" for i in range(len(bins)-1)]
else:
    bins = [1800,1850,1875,1900,1925,1950,1975,2000,2025]
    labels = ["1800–1850","1851–1875","1876–1900","1901–1925","1926–1950","1951–1975","1976–2000","2001–2025"]

counts = [0]*(len(bins)-1)
for y in years:
    for i in range(len(bins)-1):
        if bins[i] <= y < bins[i+1]:
            counts[i] += 1
            break

plt.figure(figsize=(10,6))
plt.bar(labels, counts, color="skyblue")
plt.title("Liczba publikacji na przestrzeni lat")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("wykres1_fala_zainteresowania.png")
plt.show()

# 2) JĘZYKI
lang_counts = defaultdict(int)
for b in books:
    raw = b.get("Język", "")
    for tok in re.split(r"[,;/\n]", raw):
        langs = normalize_lang(tok)
        for lang in langs:
            lang_counts[lang] += 1

if lang_counts:
    plt.figure(figsize=(7,7))
    plt.pie(lang_counts.values(), labels=lang_counts.keys(), autopct="%1.1f%%", startangle=140)
    plt.axis("equal")
    plt.title("Rozkład języków publikacji")
    plt.tight_layout()
    plt.savefig("wykres2_jezyki.png")
    plt.show()
else:
    print("Brak danych językowych.")

# 3) GATUNKI W DEKADACH
records = []
for b in books:
    year = extract_year(b.get("Data publikacji", "") or b.get("Rok wydania", ""))
    if not year:
        continue
    decade = (year // 10) * 10
    genres = b.get("Gatunek", "").split("\n")
    for g in genres:
        g = g.strip()
        if g:
            records.append({"Dekada": f"{decade}-{decade+9}", "Gatunek": g})

if records:
    df = pd.DataFrame(records)
    pt = df.pivot_table(index="Dekada", columns="Gatunek", aggfunc="size", fill_value=0)
    pt = pt.reindex(sorted(pt.index, key=lambda x: int(x.split("-")[0])))
    pt.plot(kind="bar", stacked=True, figsize=(12,6))
    plt.xticks(rotation=45)
    plt.title("Gatunki utworów w dekadach")
    plt.tight_layout()
    plt.savefig("wykres3_gatunki_dekady.png")
    plt.show()
else:
    print("Brak danych do wykresu gatunków.")

# 4) LICZBA STRON
pages_data = []
for b in books:
    author = b.get("Twórca", "").lower()
    if "murakami" in author:
        pages_text = b.get("Opis fizyczny", "")
        match = re.search(r"(\d{2,4})\s*s\.", pages_text)
        if match:
            title = b.get("Tytuł", "Nieznany tytuł")
            pages = int(match.group(1))
            pages_data.append((title, pages))

if pages_data:
    titles, pages = zip(*pages_data)
    plt.figure(figsize=(12, 6))
    plt.barh(titles, pages, color="seagreen")
    plt.xlabel("Liczba stron")
    plt.title("Liczba stron książek Harukiego Murakamiego")
    plt.tight_layout()
    plt.savefig("wykres4_liczba_stron.png")
    plt.show()
else:
    print("Brak danych o liczbie stron.")

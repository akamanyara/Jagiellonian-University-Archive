import json
import csv
import re
from time import sleep
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'more hide.*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'Pokaż wszystko.*', '', text, flags=re.IGNORECASE)
    text = ' '.join(dict.fromkeys(text.strip().split()))
    parts = list(dict.fromkeys(text.strip().split('/')))
    return ' / '.join([p.strip() for p in parts if p.strip()])

driver = webdriver.Safari()

urls = [
    f'https://katalogi.bn.org.pl/discovery/search?query=any,contains,Haruki%20Murakami&tab=LibraryCatalog&search_scope=NLOP_IZ_NZ&vid=48OMNIS_NLOP:48OMNIS_NLOP&offset={(i - 1) * 10}'
    for i in range(1, 9)
]

all_books = []

for page_num, url in enumerate(tqdm(urls, desc="Przetwarzanie stron"), 1):
    driver.get(url)
    sleep(2)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.list-item-wrapper h3 a'))
        )
    except Exception as e:
        print(f"Błąd ładowania listy książek na stronie {url}: {e}")
        continue

    book_links = [box.get_attribute('href') for box in driver.find_elements(By.CSS_SELECTOR, '.list-item-wrapper h3 a')]
    print(f"📄 Strona {page_num}: znaleziono {len(book_links)} książek.")

    for book_link in tqdm(book_links, desc=f"Książki na stronie {page_num}", leave=False):
        driver.get(book_link)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#details .section-body .layout-row'))
            )
        except Exception as e:
            print(f"Błąd ładowania szczegółów książki {book_link}: {e}")
            continue

        book = {'link': book_link}

        details = driver.find_elements(By.CSS_SELECTOR, '#details .section-body .layout-row')
        for detail in details:
            try:
                name = detail.find_element(By.CSS_SELECTOR, '.flex-gt-xs-25.flex-gt-sm-20.flex').text.strip()
                value = detail.find_element(By.CSS_SELECTOR, '.item-details-element-container.flex').text.strip()
                name = clean_text(name)
                value = clean_text(value)
                book[name] = value
            except Exception as e:
                print(f"Błąd przy zbieraniu danych szczegółowych: {e}")

        all_books.append(book)

driver.quit()

with open('books.json', 'w', encoding='utf-8') as f:
    json.dump(all_books, f, ensure_ascii=False, indent=2)
print("✅ Dane zapisane do books.json")

if all_books:
    keys = set().union(*(book.keys() for book in all_books))
    with open('books.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(all_books)
    print("✅ Dane zapisane do books.csv")
else:
    print("⚠️ Brak danych do zapisania w CSV")

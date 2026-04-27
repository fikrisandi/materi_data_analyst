# Week 3 · Day 1 AM
# Web Scraping — Mengambil Data dari Website

> **Tujuan:** Setelah modul ini kamu paham web scraping basics, bisa pakai `requests` + `BeautifulSoup` untuk scrape website static, paham etika scraping, dan tahu kapan pakai Selenium.
>
> **Estimasi:** 3 jam.

---

## 1. Apa itu Web Scraping & Kapan Dipakai?

**Web scraping** = ekstrak data dari website secara otomatis. DA pakai scraping saat:

- Data yang dibutuhkan **ada di website** tapi tidak punya API
- Tracking harga kompetitor (e-commerce monitoring)
- Aggregate review/rating produk
- Berita, artikel, blog post (content analysis)
- Job postings (analisis pasar kerja)

### Kapan **TIDAK** Pakai Scraping?

1. Kalau ada **API resmi** — selalu prefer API (Day 1 PM)
2. Kalau website **eksplisit melarang** di `robots.txt` atau ToS
3. Kalau data sensitive (private, login required)
4. Kalau website punya proteksi anti-bot kompleks (Cloudflare, captcha) — ROI scraping turun

> **Etika scraping:**
> - Cek `https://website.com/robots.txt` untuk lihat aturan
> - Rate-limit request (jangan flood server — beri delay 1-2 detik per request)
> - Jangan scraping data personal user
> - Identifikasi diri pakai header `User-Agent` yang jujur
> - Cek Terms of Service

---

## 2. Anatomy Halaman Web

Sebelum scraping, kamu harus paham struktur halaman.

### 2.1 HTML Dasar

```html
<html>
<head>
    <title>Toko Kopi Online</title>
</head>
<body>
    <div class="produk">
        <h2 class="nama">Espresso</h2>
        <span class="harga">Rp 18,000</span>
        <p class="deskripsi">Kopi single shot</p>
    </div>
    <div class="produk">
        <h2 class="nama">Latte</h2>
        <span class="harga">Rp 30,000</span>
    </div>
</body>
</html>
```

Setiap data yang mau kamu scrape ada di **HTML element** dengan **tag** (`<div>`, `<h2>`, `<span>`) dan/atau **attribute** (`class="produk"`, `id="..."`).

### 2.2 Inspect Element

Di browser (Chrome/Firefox/Edge):
- Klik kanan element yang mau kamu scrape → **Inspect** (atau F12)
- Browser tampilkan HTML element-nya
- Hover di HTML akan highlight di halaman

> **[GAMBAR DIPERLUKAN — Browser DevTools Inspect]**
> **Apa:** screenshot Chrome DevTools dengan element ter-inspect, panel HTML di kanan, halaman di kiri.
> **Konteks:** referensi visual untuk peserta cara identify selector.

---

## 3. requests — Fetch HTML

### 3.1 Install

```bash
pip install requests beautifulsoup4 lxml
```

### 3.2 Basic Request

```python
import requests

url = "https://example.com"
response = requests.get(url)

print(response.status_code)    # 200 = sukses, 404 = not found, 403 = forbidden
print(response.text[:500])     # HTML content
```

### 3.3 Pakai User-Agent (etis)

```python
headers = {
    "User-Agent": "SavvysEducationBot/1.0 (Learning purposes; contact: yourname@gmail.com)"
}
response = requests.get(url, headers=headers)
```

### 3.4 Handle Error

```python
try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    html = response.text
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {e}")
except requests.exceptions.Timeout:
    print("Timeout — server lama respond")
except Exception as e:
    print(f"Error: {e}")
```

---

## 4. BeautifulSoup — Parse HTML

```python
from bs4 import BeautifulSoup

html = response.text
soup = BeautifulSoup(html, "lxml")  # parser lxml lebih cepat

# Akses element
title = soup.find("title")
print(title.text)

# Find by tag
all_h2 = soup.find_all("h2")
for h2 in all_h2:
    print(h2.text)

# Find by class
produk_divs = soup.find_all("div", class_="produk")
for div in produk_divs:
    nama = div.find("h2", class_="nama").text.strip()
    harga = div.find("span", class_="harga").text.strip()
    print(f"{nama}: {harga}")
```

### 4.1 Common Selectors

```python
# By tag
soup.find("h2")
soup.find_all("a")

# By class
soup.find("div", class_="produk")            # underscore karena class is Python keyword
soup.find_all("span", {"class": "harga"})    # alternative

# By id
soup.find("div", id="header")

# By attribute
soup.find("a", href="/about")
soup.find_all("img", {"src": True})          # img dengan src

# CSS selector (lebih ringkas)
soup.select("div.produk")               # all div with class "produk"
soup.select("div.produk h2.nama")       # nested
soup.select("a[href^='/produk/']")      # href starts with
```

### 4.2 Extract Data

```python
elem = soup.find("div", class_="produk")

# Text
elem.text                          # all text inside
elem.get_text(strip=True)          # cleaner

# Attribute
link = soup.find("a")
link["href"]                       # value of href
link.get("href")                   # safer (return None kalau tidak ada)
```

---

## 5. Skenario Real — Scrape Website Sample

> **Catatan untuk pemula:** scraping situs production (Tokopedia, Lazada, dll) sering di-block. Kita pakai situs latihan: **`books.toscrape.com`** — situs yang sengaja didesain untuk practice scraping, gratis & free.

### Skenario: Scrape Daftar Buku

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com"
headers = {"User-Agent": "SavvysEducationBot/1.0"}

# Fetch halaman utama
response = requests.get(base_url, headers=headers)
soup = BeautifulSoup(response.text, "lxml")

books = []
for article in soup.select("article.product_pod"):
    title = article.h3.a["title"]
    price = article.select_one("p.price_color").text
    rating = article.select_one("p.star-rating")["class"][1]   # "Three", "Four", dll
    available = article.select_one("p.instock.availability").text.strip()

    books.append({
        "title": title,
        "price": price,
        "rating": rating,
        "available": available,
    })

df = pd.DataFrame(books)
print(df.head())
df.to_csv("books.csv", index=False)
```

### Pagination — Scrape Multiple Pages

```python
all_books = []

for page_num in range(1, 6):  # 5 halaman pertama
    url = f"{base_url}/catalogue/page-{page_num}.html"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    for article in soup.select("article.product_pod"):
        all_books.append({
            "title": article.h3.a["title"],
            "price": article.select_one("p.price_color").text,
            "page": page_num,
        })

    time.sleep(1)  # rate limit — jeda 1 detik per page

print(f"Total scraped: {len(all_books)} books")
```

> **Tip:** `time.sleep(1)` adalah **etika** dasar scraping. Jangan flood server.

---

## 6. Selenium — Untuk Website Dinamis (JavaScript)

Sebagian website pakai **JavaScript** untuk load content (single page apps). HTML awal kosong, content load setelah JS jalan. `requests` cuma dapat HTML statis — tidak akan dapat content yang load via JS.

Solusi: **Selenium** (control real browser).

```python
# pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://example.com")

time.sleep(3)  # tunggu JS load

# Akses element
elements = driver.find_elements(By.CSS_SELECTOR, "div.produk")
for elem in elements:
    print(elem.text)

driver.quit()
```

> **Selenium 10x lebih lambat dari requests** — pakai cuma kalau memang perlu (JS-rendered content). Sebisa mungkin **inspect Network tab** browser dulu — kadang content sebenarnya load via API JSON yang bisa kamu hit langsung.

---

## 7. Best Practice & Etika Scraping

### Best Practice

1. **Cek robots.txt dulu** — `https://target.com/robots.txt`
2. **Rate-limit** — `time.sleep(1)` minimum per request
3. **User-Agent jujur** — sebut tools & email kontak kalau ada
4. **Handle error gracefully** — try/except, retry dengan backoff
5. **Cache hasil scrape** — simpan ke file, jangan re-scrape kalau tidak perlu
6. **Schedule kalau recurring** — jangan run manual setiap kali

### Anti-pattern

❌ Scrape concurrent dengan 100 thread (DoS efectively)
❌ Scrape data login-protected
❌ Scrape & repost content (copyright)
❌ Bypass rate limit dengan rotate IP / VPN

---

## 8. Latihan

Lihat `latihan/soal.md`. Tugas: scrape books.toscrape.com 50 buku + analisis.

---

## Apa Selanjutnya?

Lanjut **Day 1 PM — API** — cara yang lebih clean dapat data dari layanan publik.

> **Tip portfolio:** scraping notebook + dataset CSV hasil → push ke `04-data-acquisition/scraping/` portfolio.

---

**Akhir Day 1 AM · Week 3**
*Savvys Education · 2026*

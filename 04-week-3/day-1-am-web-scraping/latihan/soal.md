# Latihan — Web Scraping

> Target: **books.toscrape.com** (situs latihan resmi, scraping-friendly).

## Tugas Utama

Scrape **50 buku** dari halaman utama. Output DataFrame dengan kolom:
- `title` — judul buku
- `price` — harga (parse jadi numeric, hilangkan "£")
- `rating` — bintang (1-5, parse dari class CSS)
- `available` — stok (parse dari text)
- `category` — kategori (klik link buku untuk lihat detail, atau ambil dari sidebar)

Save ke `latihan/books-scraped.csv`.

## Bonus

### Bonus 1 — Scrape 100+ buku (multi-page)
Pagination 5 halaman. Total ~100 buku.

### Bonus 2 — Analisis Hasil
Pakai pandas:
- Distribusi rating
- Avg price per kategori
- Top 5 termurah & termahal

### Bonus 3 — Visualisasi
Bar chart distribusi rating.

## Etika Wajib
- [ ] User-Agent set jujur
- [ ] Rate limit minimal 1 detik per request
- [ ] Cek robots.txt sebelum mulai

## Submission

`latihan/scraping-books.ipynb` + `books-scraped.csv`. Push ke `04-data-acquisition/scraping/` portfolio.

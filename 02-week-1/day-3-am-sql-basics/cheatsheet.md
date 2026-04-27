# Cheatsheet — SQL Basics

## Anatomy Query

```sql
SELECT      kolom1, kolom2, COUNT(*)         -- pilih
FROM        tabel                            -- dari tabel
WHERE       kondisi                          -- filter
GROUP BY    kolom1                           -- (Day 3 PM)
HAVING      kondisi_aggregate                -- (Day 3 PM)
ORDER BY    kolom DESC                       -- sort
LIMIT       N;                               -- batasi
```

> Urutan eksekusi (logical): FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT

## SELECT

```sql
SELECT *                       -- semua kolom (eksplorasi)
SELECT kolom1, kolom2          -- kolom spesifik
SELECT DISTINCT kolom          -- unique values
SELECT (a - b) AS profit       -- calculated column dengan alias
```

## Filter (WHERE)

| Operator | Contoh |
|---|---|
| `=` `!=` `<>` | `WHERE kategori = 'Coffee'` |
| `<` `>` `<=` `>=` | `WHERE harga >= 25000` |
| `BETWEEN ... AND ...` | `WHERE harga BETWEEN 20000 AND 30000` |
| `IN (..., ...)` | `WHERE kategori IN ('Coffee', 'Pastry')` |
| `LIKE 'pattern'` | `WHERE nama LIKE 'Es%'` |
| `IS NULL` / `IS NOT NULL` | `WHERE no_hp IS NULL` |
| `AND` `OR` `NOT` | `WHERE A AND (B OR C)` |

### LIKE Wildcards
- `%` = 0 atau lebih karakter
- `_` = exactly 1 karakter

```sql
LIKE 'Es%'        -- "Es" di awal
LIKE '%Latte%'    -- "Latte" di mana saja
LIKE '%pi'        -- "pi" di akhir
LIKE '_a%'        -- huruf kedua = a
```

## ORDER BY

```sql
ORDER BY harga                    -- ASC default
ORDER BY harga DESC               -- descending
ORDER BY kategori, harga DESC     -- multiple columns
```

## LIMIT

```sql
LIMIT 10              -- ambil 10 pertama
LIMIT 10 OFFSET 20    -- skip 20, ambil 10 (pagination)
```

## Aggregate Functions

| Function | Fungsi |
|---|---|
| `COUNT(*)` | Hitung baris |
| `COUNT(kolom)` | Hitung baris non-NULL |
| `COUNT(DISTINCT kolom)` | Hitung unique values |
| `SUM(kolom)` | Total |
| `AVG(kolom)` | Rata-rata |
| `MIN(kolom)` | Minimum |
| `MAX(kolom)` | Maksimum |

```sql
SELECT
    COUNT(*) AS total,
    SUM(total) AS revenue,
    AVG(total) AS avg_per_trx,
    MIN(total) AS termurah,
    MAX(total) AS termahal
FROM transaksi;
```

## String Functions

```sql
LENGTH(text)          -- panjang
UPPER(text)           -- huruf besar
LOWER(text)           -- huruf kecil
SUBSTR(text, 1, 3)    -- substring (pos 1, 3 char)
TRIM(text)            -- buang whitespace
```

## Date Functions (SQLite)

```sql
strftime('%Y', tanggal)       -- ekstrak tahun
strftime('%m', tanggal)       -- bulan (01-12)
strftime('%Y-%m', tanggal)    -- year-month
strftime('%d', tanggal)       -- hari
strftime('%w', tanggal)       -- day of week (0=Sunday)

DATE('now')                   -- tanggal hari ini
DATE('now', '-7 days')        -- 7 hari lalu
```

## Best Practice

✅ **DO:**
- UPPERCASE untuk SQL keyword (SELECT, FROM, WHERE)
- lowercase + snake_case untuk nama tabel/kolom
- Indentasi konsisten
- Comment dengan `--` untuk multi-step query
- Pakai `LIMIT` saat eksplorasi
- Test query bertahap (SELECT * dulu, baru tambah filter)

❌ **DON'T:**
- `SELECT *` di production query (cuma yang dibutuhkan)
- `WHERE col = NULL` (pakai `IS NULL`)
- String pakai double quote `"..."` (pakai single `'...'`)
- Magic number (jelaskan dengan comment)

## Connect SQLite di VSCode

1. SQLTools extension + SQLTools SQLite Driver
2. Add Connection → SQLite → browse `.db` file
3. Tulis di `.sql` file → `Ctrl+E` untuk run

## Bahan Latihan

- **HackerRank SQL** — gratis, sertifikasi resmi
- **DataLemur** — soal interview FAANG (Day 4-5)
- **Kaggle** — dataset publik untuk SQL practice via BigQuery
- **SQLBolt** — interactive tutorial gratis

## Next Step

✅ SQL Basics → lanjut ke `day-3-pm-sql-dql/` (GROUP BY, HAVING, BigQuery)

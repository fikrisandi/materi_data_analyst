# Week 1 · Day 3 AM
# SQL Basics — Bahasa Universal Data Analyst

> **Tujuan modul:** Setelah membaca dan mengerjakan modul ini, kamu paham konsep database, bisa pakai SQLite di VSCode, dan menulis query dasar untuk filter, sort, dan aggregate data.
>
> **Estimasi waktu:** 3 jam · **Format:** modul step-by-step + query langsung praktik di SQLite.

---

## 1. Mengapa SQL Wajib untuk DA?

Kalau ada **satu skill** yang harus kamu kuasai sebelum apa pun di Data Analytics, itu adalah **SQL**. Ada 4 alasan kuat:

**Pertama**, SQL muncul di **hampir 100% lowongan DA**. Coba buka 10 lowongan DA random di LinkedIn — 10-nya akan menyebut "SQL" sebagai requirement. Beberapa cuma minta "SQL", beberapa spesifik "SQL Intermediate" atau "advanced SQL". Tapi tidak ada yang skip SQL.

**Kedua**, SQL adalah **bahasa universal data**. Mau pakai PostgreSQL, MySQL, BigQuery, Snowflake, Redshift, SQL Server, SQLite — sintaks utamanya **mirip**. Belajar SQL sekali, bisa pakai di mana-mana.

**Ketiga**, SQL **sangat efisien untuk dataset besar**. Pandas Python bisa lambat di dataset 10 juta baris. SQL di database modern (BigQuery, Snowflake) bisa proses miliar baris dalam detik.

**Keempat**, SQL adalah **bahasa deklaratif** — kamu bilang "apa yang kamu mau", bukan "cara mendapatkannya". Database engine yang optimize execution. Ini bikin SQL lebih ringkas & mudah dibaca dibanding code Python untuk operasi yang sama.

> **Pesan utama:** Kalau kamu cuma bisa belajar 1 hal di Week 1, jadikan SQL prioritas. Pandas, statistik, visualisasi — semua bisa nyusul. SQL tidak.

### Excel vs SQL vs Pandas — Kapan Pakai Apa?

| Skenario | Pilih |
|---|---|
| Dataset < 1 juta baris, eksplorasi cepat | **Excel** |
| Dataset di database, query siap-pakai untuk dashboard | **SQL** |
| Dataset 1+ juta baris di file, analisis kompleks | **Python (Pandas)** |
| Reproducible report harian | **SQL + BI tool**, atau **Python script** |
| Statistik inferensial, ML | **Python** |

DA real biasanya pakai **kombinasi**: SQL untuk pull data dari warehouse → Pandas untuk transform & analisis → Tableau/PBI untuk visualisasi.

---

## 2. Database, Table, Schema — Konsep Dasar

Sebelum mulai query, pahami konsep dasar.

### 2.1 Database

**Database** = kumpulan data terstruktur yang disimpan di komputer & bisa diakses lewat query language (SQL).

Analogi: kalau Excel = 1 file workbook, Database = 1 ruang penyimpanan dengan **banyak tabel**, **rules untuk hubungan antar tabel**, dan **akses concurrent** (banyak orang query bersamaan tanpa tabrakan).

Jenis database yang akan kamu temui sebagai DA:
- **SQLite** — file-based, ringan, untuk learning & prototype (yang akan kita pakai hari ini)
- **PostgreSQL / MySQL** — server-based, banyak dipakai aplikasi web
- **BigQuery / Snowflake / Redshift** — cloud data warehouse, untuk analytics skala besar

### 2.2 Table

**Table** (= "tabel") = struktur data berbentuk baris-kolom, mirip Excel sheet — tapi dengan rules:
- Setiap **kolom** punya **tipe data tetap** (integer, text, date, dst)
- Setiap **baris** = 1 record (1 transaksi, 1 pelanggan, 1 produk)
- Bisa punya **primary key** = kolom unique yang identify tiap baris

```
TABLE: transaksi
┌───────────────┬────────────┬───────────┬──────────────┬───────┬───────┬────────┐
│ id_transaksi  │ tanggal    │ id_cabang │ id_pelanggan │ qty   │ total │ ...    │
├───────────────┼────────────┼───────────┼──────────────┼───────┼───────┼────────┤
│ TRX00001      │ 2026-01-02 │ C001      │ P012         │ 2     │ 50000 │ ...    │
│ TRX00002      │ 2026-01-02 │ C001      │ P003         │ 1     │ 28000 │ ...    │
│ ...           │ ...        │ ...       │ ...          │ ...   │ ...   │ ...    │
└───────────────┴────────────┴───────────┴──────────────┴───────┴───────┴────────┘
   ↑ primary key
```

### 2.3 Database Latihan: Kopi Kita

Database `kopi_kita.db` punya 4 tabel:

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│   cabang    │       │  transaksi  │       │    menu     │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id_cabang ★ │ ←──┐  │ id_transaksi★      │ id_menu ★   │
│ nama_cabang │    │  │ tanggal     │   ┌──→ nama_menu  │
│ kota        │    └──│ id_cabang   │   │  │ kategori    │
│ jam_buka    │       │ id_pelanggan│   │  │ harga       │
│ jam_tutup   │       │ id_menu     │←──┘  │ hpp         │
└─────────────┘       │ qty         │      └─────────────┘
                      │ harga_satuan│
                      │ total       │            ┌─────────────┐
                      │ metode_bayar│            │  pelanggan  │
                      └─────────────┘            ├─────────────┤
                            │                    │ id_pelanggan★
                            └────────────────────→ nama        │
                                                 │ no_hp       │
                                                 │ kota_asal   │
                                                 │ membership  │
                                                 └─────────────┘
```

★ = primary key. Garis = foreign key (relasi antar tabel).

---

## 3. Connect SQLite — Pilih SQLTools (VSCode) atau DBeaver

> **Catatan:** SQLite dipilih untuk Week 1 karena **tidak perlu install server** — file `.db` langsung bisa dibuka. Sintaks SQL 95% sama dengan PostgreSQL/MySQL/BigQuery yang akan dipakai Week 2-3. Detail kenapa pakai SQLite vs database lain → lihat `99-resources/platform-guides/database-stack.md`.
>
> Kamu bisa connect lewat **2 tools**: SQLTools di VSCode (untuk yang suka SQL inline dengan code), atau **DBeaver** (untuk yang suka GUI visual). **Rekomendasi: pakai keduanya** — DBeaver untuk eksplor visual, SQLTools untuk nulis query yang akan di-commit ke Git.

### Option A — SQLTools di VSCode

#### A.1 Install SQLTools (Skip kalau sudah)

Sudah dilakukan di Day 1 AM. Kalau belum:
- Extension: **SQLTools** (Matheus Teixeira)
- Extension driver: **SQLTools SQLite Driver**

#### A.2 Connect ke Database

1. Klik icon SQLTools di sidebar kiri (icon database)
2. Klik "Add New Connection"
3. Pilih **SQLite**
4. Connection Name: `Kopi Kita`
5. Database file: klik browse, pilih `data/kopi_kita.db` di folder Day 3 AM
6. Klik "Connect Now"

### Option B — DBeaver (Recommended untuk Visual Exploration)

#### B.1 Buka DBeaver

DBeaver sudah di-install di Day 1 AM. Buka aplikasi.

#### B.2 New Connection

1. Klik icon **plug** di kiri atas, atau menu **Database → New Database Connection**
2. Pilih **SQLite**
3. Path: browse ke `data/kopi_kita.db`
4. **Test Connection** → kalau muncul "Connected", klik **Finish**
5. Database muncul di sidebar **Database Navigator** (kiri)

#### B.3 Eksplor Database

Di sidebar:
- Expand `kopi_kita.db` → Tables → kamu lihat 4 tabel
- Klik kanan tabel `transaksi` → **View Data** → **All Rows** (lihat isi 250 baris)
- Klik kanan tabel → **ER Diagram** (visualisasi schema relasi)
- Klik kanan database → **SQL Editor** → **New SQL Editor** (mulai nulis query)

> **[GAMBAR DIPERLUKAN — DBeaver Connection ke SQLite]**
> **Apa:** screenshot DBeaver dengan database `kopi_kita.db` ter-connect, sidebar expand sampai tabel transaksi terlihat, dan View Data tab terbuka di kanan.
> **Konteks:** referensi visual peserta yang stuck.

> **[GAMBAR DIPERLUKAN — SQLTools Connection Setup]**
> **Apa yang harus di-screenshot:** dialog SQLTools "Add New Connection" dengan field terisi (Connection Name "Kopi Kita", Database file path).
> **Konteks isi nanti:** referensi visual untuk peserta yang stuck setup SQLTools.

### 3.3 Bikin SQL File & Run Query

Bikin file `code/queries.sql` di folder ini.

**Di VSCode (SQLTools):**
- Buka `queries.sql`
- Eksekusi query: pilih query (highlight), lalu `Ctrl+E` (atau klik kanan → "Run on Active Connection")
- Hasil muncul di tab baru di bawah

**Di DBeaver:**
- Klik kanan database → **SQL Editor → New SQL Editor**
- Tulis query di editor
- Tekan **F5** (atau `Ctrl+Enter`) untuk execute
- Hasil muncul di tab Results di bawah

**Tip workflow:** simpan semua query final di file `queries.sql` (Git-tracked), lalu copy-paste ke DBeaver kalau butuh eksplor visual hasil.

---

## 4. Query Pertama — SELECT, FROM, LIMIT

### 4.1 SELECT * — Lihat Semua Kolom

Tulis di `queries.sql`:

```sql
SELECT *
FROM menu;
```

Eksekusi (`Ctrl+E`). Hasil:

```
id_menu  nama_menu       kategori    harga   hpp
M01      Espresso        Coffee      18000   6000
M02      Americano       Coffee      22000   7000
M03      Cappuccino      Coffee      28000   9000
...
```

Penjelasan:
- `SELECT *` = pilih semua kolom (`*` artinya "semua")
- `FROM menu` = dari tabel `menu`
- `;` di akhir = pemisah statement

### 4.2 SELECT Kolom Spesifik

```sql
SELECT nama_menu, harga
FROM menu;
```

Hasil cuma 2 kolom:

```
nama_menu       harga
Espresso        18000
Americano       22000
...
```

> **Best practice:** di production, **hindari `SELECT *`** kalau cuma butuh beberapa kolom. Lebih cepat & lebih jelas intent-nya.

### 4.3 LIMIT — Batasi Jumlah Baris

Saat dataset besar, kamu nggak mau load semua. Pakai `LIMIT`:

```sql
SELECT *
FROM transaksi
LIMIT 10;
```

Hasil: 10 baris pertama.

> **Tip:** selalu mulai dengan `LIMIT 10` saat eksplorasi tabel baru. Cegah download 1 juta baris yang akhirnya cuma kamu lihat 10 baris.

### 4.4 SELECT dengan Alias

```sql
SELECT
    nama_menu AS menu,
    harga AS harga_jual,
    hpp AS cost
FROM menu;
```

Output kolom rename jadi `menu`, `harga_jual`, `cost`. Berguna untuk readability di report.

### 4.5 SELECT dengan Calculated Column

```sql
SELECT
    nama_menu,
    harga,
    hpp,
    (harga - hpp) AS profit
FROM menu;
```

Output baru kolom `profit` = `harga - hpp` per baris.

---

## 5. Filter — WHERE & Operator

### 5.1 WHERE Dasar

Filter baris dengan kondisi. Tampilkan menu kategori "Coffee" saja:

```sql
SELECT *
FROM menu
WHERE kategori = 'Coffee';
```

Penjelasan:
- `WHERE` = mulai filter
- `kategori = 'Coffee'` = kondisi
- String pakai **single quote** `'...'` (jangan double quote `"..."` — itu untuk identifier di beberapa DB)

### 5.2 Operator Comparison

| Operator | Fungsi | Contoh |
|---|---|---|
| `=` | Sama dengan | `WHERE harga = 25000` |
| `!=` atau `<>` | Tidak sama | `WHERE kategori != 'Coffee'` |
| `<` `>` | Kurang dari / lebih dari | `WHERE harga < 25000` |
| `<=` `>=` | Kurang/lebih dari atau sama | `WHERE harga >= 25000` |

Contoh:

```sql
-- Menu dengan harga di atas 25000
SELECT nama_menu, harga
FROM menu
WHERE harga > 25000;

-- Transaksi dengan total di bawah 30000
SELECT *
FROM transaksi
WHERE total < 30000
LIMIT 10;
```

### 5.3 Multi-Condition: AND, OR, NOT

```sql
-- Menu Coffee dengan harga di bawah 25000
SELECT *
FROM menu
WHERE kategori = 'Coffee'
  AND harga < 25000;

-- Menu Coffee atau Pastry
SELECT *
FROM menu
WHERE kategori = 'Coffee'
   OR kategori = 'Pastry';

-- Bukan kategori Coffee
SELECT *
FROM menu
WHERE NOT kategori = 'Coffee';
-- atau:
SELECT *
FROM menu
WHERE kategori != 'Coffee';
```

> **Tip readability:** indentasi multi-condition dengan AND/OR di awal baris baru.

### 5.4 Operator BETWEEN

Range antara 2 nilai:

```sql
-- Menu harga 20000 - 30000
SELECT *
FROM menu
WHERE harga BETWEEN 20000 AND 30000;
```

Sama dengan `harga >= 20000 AND harga <= 30000`. BETWEEN inclusive (kedua ujung termasuk).

### 5.5 Operator IN

Cek apakah nilai ada di list:

```sql
-- Menu kategori Coffee atau Pastry (tanpa OR berulang)
SELECT *
FROM menu
WHERE kategori IN ('Coffee', 'Pastry');
```

Lebih clean dari `kategori = 'Coffee' OR kategori = 'Pastry'`.

### 5.6 Operator LIKE — Pattern Matching String

```sql
-- Menu yang namanya mulai dengan "Es"
SELECT *
FROM menu
WHERE nama_menu LIKE 'Es%';

-- Menu yang ada kata "Latte" di mana saja
SELECT *
FROM menu
WHERE nama_menu LIKE '%Latte%';

-- Menu yang namanya 5 huruf, ditengahnya 'a'
SELECT *
FROM menu
WHERE nama_menu LIKE '__a__';
```

Wildcard:
- `%` = 0 atau lebih karakter
- `_` = exactly 1 karakter

### 5.7 NULL Handling

NULL = "tidak ada nilai" (bukan 0, bukan empty string).

```sql
-- Pelanggan yang tidak ada no HP-nya
SELECT *
FROM pelanggan
WHERE no_hp IS NULL;

-- Pelanggan yang punya no HP
SELECT *
FROM pelanggan
WHERE no_hp IS NOT NULL;
```

> **Penting:** **JANGAN** pakai `= NULL` atau `!= NULL` — itu salah. NULL bukan nilai, jadi tidak bisa "sama dengan" apa pun. **Selalu pakai `IS NULL` / `IS NOT NULL`.**

---

## 6. Sort — ORDER BY

### 6.1 ORDER BY Dasar

```sql
-- Menu diurutkan dari termurah
SELECT *
FROM menu
ORDER BY harga;

-- Default: ASCENDING (kecil ke besar)
-- DESCENDING:
SELECT *
FROM menu
ORDER BY harga DESC;
```

### 6.2 ORDER BY Multiple Columns

```sql
-- Urut berdasarkan kategori dulu, lalu harga (dalam kategori)
SELECT *
FROM menu
ORDER BY kategori ASC, harga DESC;
```

### 6.3 ORDER BY dengan LIMIT — Top N

```sql
-- Top 5 transaksi termahal
SELECT *
FROM transaksi
ORDER BY total DESC
LIMIT 5;
```

Pattern ini sangat sering dipakai di analisis: "Top 10 customer", "Top 5 produk", dll.

---

## 7. Aggregate Functions — COUNT, SUM, AVG, MIN, MAX

Aggregate function = fungsi yang **menggabungkan banyak baris jadi 1 nilai**.

### 7.1 COUNT — Hitung Baris

```sql
-- Total jumlah transaksi
SELECT COUNT(*) FROM transaksi;

-- Total jumlah menu
SELECT COUNT(*) FROM menu;

-- Total transaksi yang pakai QRIS
SELECT COUNT(*)
FROM transaksi
WHERE metode_bayar = 'QRIS';
```

### 7.2 SUM — Jumlahkan

```sql
-- Total revenue Q1 2026
SELECT SUM(total) AS total_revenue
FROM transaksi;

-- Total revenue dari QRIS saja
SELECT SUM(total) AS revenue_qris
FROM transaksi
WHERE metode_bayar = 'QRIS';
```

### 7.3 AVG — Rata-rata

```sql
-- Rata-rata transaksi
SELECT AVG(total) AS avg_transaksi
FROM transaksi;

-- Rata-rata harga menu Coffee
SELECT AVG(harga) AS avg_harga_kopi
FROM menu
WHERE kategori = 'Coffee';
```

### 7.4 MIN, MAX

```sql
-- Transaksi termurah & termahal
SELECT MIN(total) AS min_trx, MAX(total) AS max_trx
FROM transaksi;
```

### 7.5 Multiple Aggregations

```sql
-- Ringkasan transaksi Q1 2026
SELECT
    COUNT(*) AS total_transaksi,
    SUM(total) AS total_revenue,
    AVG(total) AS avg_transaksi,
    MIN(total) AS trx_termurah,
    MAX(total) AS trx_termahal
FROM transaksi;
```

> **Catatan:** kamu bisa kombinasikan aggregate dengan WHERE:
> ```sql
> SELECT COUNT(*), SUM(total)
> FROM transaksi
> WHERE id_cabang = 'C001';
> ```

---

## 8. Operator Lanjutan & DISTINCT

### 8.1 DISTINCT — Unique Values

```sql
-- Daftar metode bayar yang ada (unique)
SELECT DISTINCT metode_bayar
FROM transaksi;
-- Output: Cash, QRIS, Debit, Kredit (4 baris, bukan 250)

-- Berapa pelanggan unique yang transaksi Q1?
SELECT COUNT(DISTINCT id_pelanggan)
FROM transaksi;
```

### 8.2 String Functions Dasar

```sql
-- Length string
SELECT nama_menu, LENGTH(nama_menu) AS panjang
FROM menu;

-- Uppercase / lowercase
SELECT UPPER(nama_menu) FROM menu;
SELECT LOWER(nama_menu) FROM menu;

-- Substring (dari posisi N, ambil M karakter)
SELECT nama_menu, SUBSTR(nama_menu, 1, 3) AS singkat
FROM menu;
```

### 8.3 Date Functions

```sql
-- Filter tanggal
SELECT *
FROM transaksi
WHERE tanggal >= '2026-01-01'
  AND tanggal < '2026-02-01';

-- Extract bagian tanggal (SQLite syntax)
SELECT
    tanggal,
    strftime('%Y', tanggal) AS tahun,
    strftime('%m', tanggal) AS bulan,
    strftime('%d', tanggal) AS hari
FROM transaksi
LIMIT 5;
```

> **Catatan:** date function syntax beda antar database. SQLite pakai `strftime()`, PostgreSQL pakai `EXTRACT()`, BigQuery pakai `EXTRACT()`. Sintaks utama (SELECT, WHERE) sama.

---

## 9. Mini Case Study — Analisis Kopi Kita dengan SQL

Sekarang aplikasikan semua yang kamu pelajari. Jawab 6 pertanyaan berikut **dengan SQL** (tidak boleh Excel/Pandas).

### Q1. Eksplorasi Awal
- Berapa total transaksi Q1 2026?
- Berapa total revenue?
- Berapa rata-rata revenue per transaksi?
- Berapa transaksi termurah & termahal?

### Q2. Kategori Menu
Berapa total revenue per kategori menu? **Tip:** karena `kategori` ada di tabel `menu`, kamu butuh **join** ke tabel `transaksi`. Kita belum belajar JOIN — gunakan workaround: dulu tampilkan `id_menu` saja, nanti Day 4 kita upgrade.

```sql
-- Total revenue per id_menu
SELECT id_menu, SUM(total) AS revenue
FROM transaksi
GROUP BY id_menu
ORDER BY revenue DESC;
```

(Catatan: GROUP BY akan dibahas detail di Week 2 Day 4. Untuk sekarang, jalankan query di atas saja.)

### Q3. Metode Bayar
Tampilkan untuk setiap metode bayar:
- Jumlah transaksi
- Total revenue
- Rata-rata per transaksi

### Q4. Cabang
Bandingkan 2 cabang Tebet vs Dago:
- Jumlah transaksi
- Total revenue
- Pelanggan unique yang pernah transaksi

### Q5. Bulan
Bulan mana paling ramai (transaction count)? Mana paling tinggi revenue?

### Q6. Pelanggan Loyal
Top 5 pelanggan paling sering transaksi (by count). Tampilkan id_pelanggan + jumlah transaksi.

### Output

Save semua query di `code/queries.sql` dengan komentar untuk tiap pertanyaan:

```sql
-- ====================================================
-- Q1: Eksplorasi Awal
-- ====================================================
SELECT
    COUNT(*) AS total_trx,
    SUM(total) AS total_rev,
    ...
FROM transaksi;

-- ====================================================
-- Q2: Kategori Menu
-- ====================================================
...
```

---

## 10. Tips Menulis Query Yang Bersih

1. **UPPERCASE untuk keyword SQL**, lowercase untuk nama tabel/kolom:
   ```sql
   ✅ SELECT * FROM transaksi WHERE id_cabang = 'C001';
   ❌ select * from TRANSAKSI where id_cabang = 'C001';
   ```

2. **Indentasi konsisten** untuk multi-line:
   ```sql
   ✅ SELECT
        id_menu,
        SUM(total) AS revenue
      FROM transaksi
      WHERE metode_bayar = 'QRIS'
      GROUP BY id_menu
      ORDER BY revenue DESC;
   ```

3. **Comment yang clear**:
   ```sql
   -- Top 10 transaksi terbesar Q1 2026 untuk audit
   SELECT * FROM transaksi
   ORDER BY total DESC
   LIMIT 10;
   ```

4. **Selalu LIMIT saat eksplorasi** dataset besar.

5. **Test query bertahap** — mulai SELECT * dengan LIMIT, lalu tambah filter, lalu aggregation. Jangan langsung tulis query 50 baris.

---

## Apa Selanjutnya?

Selamat — kamu sudah selesai materi SQL Basics. Skill yang baru kamu pelajari adalah **fondasi paling krusial** dari semua skill DA.

**Selanjutnya:**

1. **Selesaikan latihan di `latihan/soal.md`** — 12 soal dari mudah ke advanced
2. **Push hasil ke portfolio:**
   ```bash
   cd ~/savvys-da-kursus/portfolio/02-sql-bigquery
   # copy queries.sql + insight.md ke sini
   git add . && git commit -m "Week 1 Day 3 AM: SQL Basics queries"
   git push
   ```
3. **Lanjut ke Day 3 PM — SQL DQL & BigQuery** — folder `02-week-1/day-3-pm-sql-dql/`. Akan belajar:
   - GROUP BY untuk aggregation per kelompok
   - HAVING untuk filter setelah aggregate
   - Setup BigQuery sandbox (gratis Google Cloud)
   - Query dataset publik (NYC Taxi, Indonesia COVID, dll)

> **Tip:** kalau sudah selesai materi & latihan, coba **HackerRank SQL Basic Challenges** (gratis): [hackerrank.com/domains/sql](https://hackerrank.com/domains/sql). Mulai dari "Basic Select" — sebagian besar bisa kamu kerjakan dengan apa yang sudah kamu pelajari.

---

**Akhir Day 3 AM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan Sesi

1. Paham apa itu database & SQL, kenapa wajib untuk DA
2. Bisa connect ke SQLite via VSCode (SQLTools extension)
3. Bisa query dasar: SELECT, FROM, WHERE, ORDER BY, LIMIT
4. Bisa filter dengan operator: =, !=, <, >, BETWEEN, IN, LIKE, IS NULL
5. Bisa pakai function dasar: COUNT, SUM, AVG, MIN, MAX
6. Bisa gabungkan operator dengan AND, OR, NOT

## Durasi

~3 jam

## Prasyarat

- Sudah selesai Day 1 (Setup + Git)
- VSCode extension **SQLTools** dan **SQLTools SQLite Driver** terinstall
- Database latihan ada di `data/kopi_kita.db`

## Format Output

- `materi.md` — modul (~3,000 kata)
- `data/kopi_kita.db` — SQLite database (4 tabel: cabang, menu, pelanggan, transaksi)
- `code/queries.sql` — semua query yang dibahas
- `latihan/soal.md` — 12 soal latihan
- `cheatsheet.md` — SQL cheatsheet

## Struktur Konten

| Section | Topik |
|---|---|
| 1 | Mengapa SQL Wajib untuk DA |
| 2 | Database, Table, Schema — Konsep Dasar |
| 3 | Connect SQLite di VSCode |
| 4 | Query Pertama: SELECT, FROM, LIMIT |
| 5 | Filter: WHERE & Operator |
| 6 | Sort: ORDER BY |
| 7 | Aggregate Functions: COUNT, SUM, AVG, MIN, MAX |
| 8 | Operator Lanjutan: BETWEEN, IN, LIKE, IS NULL |
| 9 | Mini Case Study: Analisis Kopi Kita dengan SQL |
| 10 | Tips Menulis Query yang Bersih |

## Output Portfolio

```
data-analyst-portfolio/02-sql-bigquery/
├── README.md
├── queries.sql            (semua query Week 1 + Week 2)
└── insight.md
```

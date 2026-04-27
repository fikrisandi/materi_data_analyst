# Week 1 · Day 3 PM
# SQL DQL — GROUP BY, HAVING, JOIN & BigQuery Sandbox

> **Tujuan modul:** Setelah modul ini, kamu bisa pakai GROUP BY untuk aggregation per kelompok, HAVING untuk filter aggregate, JOIN untuk gabung tabel, dan punya akun BigQuery untuk query dataset publik berskala besar.
>
> **Estimasi waktu:** 3 jam · **Format:** modul step-by-step + latihan SQLite & BigQuery.

---

## 1. Recap & Apa itu DQL

**DQL = Data Query Language** — subset SQL untuk **mengambil & menganalisis** data (vs DDL untuk schema, DML untuk insert/update). DA hampir 100% bekerja di DQL.

Pagi ini kita sudah pelajari DQL dasar: SELECT, WHERE, ORDER BY, LIMIT, basic aggregate. Sore ini kita masuk **DQL inti yang membedakan DA dari user spreadsheet biasa**: GROUP BY, HAVING, JOIN.

---

## 2. GROUP BY — Aggregation per Group

### 2.1 Skenario

Day 3 AM kita sudah pakai aggregate (`COUNT`, `SUM`, `AVG`). Tapi semua aggregate itu **untuk seluruh tabel**. Sekarang pertanyaan baru: **"berapa total revenue *per cabang*?"**

Tanpa GROUP BY, kamu harus tulis 2 query:

```sql
SELECT SUM(total) FROM transaksi WHERE id_cabang = 'C001';  -- Tebet
SELECT SUM(total) FROM transaksi WHERE id_cabang = 'C002';  -- Dago
```

Repetitif. Kalau ada 50 cabang, kamu nulis 50 query? Pakai GROUP BY:

```sql
SELECT
    id_cabang,
    SUM(total) AS revenue
FROM transaksi
GROUP BY id_cabang;
```

Output:
```
id_cabang  revenue
C001       3,250,000
C002       2,800,000
```

**Yang terjadi:** SQL otomatis bagi data jadi grup per `id_cabang`, lalu hitung `SUM(total)` untuk tiap grup.

### 2.2 GROUP BY Multiple Columns

```sql
SELECT
    id_cabang,
    metode_bayar,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue
FROM transaksi
GROUP BY id_cabang, metode_bayar
ORDER BY id_cabang, revenue DESC;
```

Hasil = cross-tab antara cabang × metode bayar.

### 2.3 Aturan Wajib GROUP BY

> **Rule of thumb:** semua kolom di SELECT harus **(a)** ada di GROUP BY, atau **(b)** berupa aggregate function.

❌ Salah:
```sql
SELECT id_cabang, nama_pelanggan, SUM(total)
FROM transaksi
GROUP BY id_cabang;
-- Error / unexpected: nama_pelanggan tidak di GROUP BY dan bukan aggregate
```

✅ Benar:
```sql
SELECT id_cabang, COUNT(DISTINCT id_pelanggan) AS pelanggan_unique, SUM(total)
FROM transaksi
GROUP BY id_cabang;
```

### 2.4 GROUP BY dengan Function

```sql
SELECT
    strftime('%Y-%m', tanggal) AS bulan,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue
FROM transaksi
GROUP BY bulan
ORDER BY bulan;
```

---

## 3. HAVING — Filter Setelah Aggregate

WHERE filter **sebelum aggregate**. HAVING filter **setelah aggregate**.

Skenario: tampilkan menu yang **revenue total > 500,000** saja.

❌ WHERE tidak bisa:
```sql
SELECT id_menu, SUM(total) AS revenue
FROM transaksi
WHERE SUM(total) > 500000   -- ERROR! Aggregate di WHERE
GROUP BY id_menu;
```

✅ Pakai HAVING:
```sql
SELECT id_menu, SUM(total) AS revenue
FROM transaksi
GROUP BY id_menu
HAVING SUM(total) > 500000
ORDER BY revenue DESC;
```

### Urutan Eksekusi (Logical)

```
FROM    → WHERE   → GROUP BY → HAVING  → SELECT  → ORDER BY → LIMIT
(data)    (filter   (group     (filter   (project   (sort)     (cut)
          rows)     rows)      groups)   columns)
```

> **Tip:** kalau bingung WHERE vs HAVING — kalau filternya pakai aggregate function (SUM, COUNT, AVG), pakai HAVING.

### Contoh Kombinasi

```sql
-- Cabang yang revenue > 1jt, hanya transaksi QRIS, urut by revenue desc
SELECT id_cabang, SUM(total) AS revenue
FROM transaksi
WHERE metode_bayar = 'QRIS'   -- filter dulu hanya QRIS
GROUP BY id_cabang
HAVING SUM(total) > 1000000   -- baru filter group
ORDER BY revenue DESC;
```

---

## 4. JOIN — Gabung Tabel

### 4.1 Skenario

Tabel `transaksi` punya `id_menu`, tapi nama menu ada di tabel `menu`. Kamu mau output yang sudah punya **nama menu** + **kategori**.

Tanpa JOIN, kamu pakai subquery:

```sql
SELECT
    id_transaksi,
    (SELECT nama_menu FROM menu m WHERE m.id_menu = t.id_menu) AS nama_menu,
    total
FROM transaksi t
LIMIT 10;
```

Bisa, tapi tidak efficient & susah dibaca. Pakai JOIN:

```sql
SELECT
    t.id_transaksi,
    m.nama_menu,
    m.kategori,
    t.total
FROM transaksi t
INNER JOIN menu m ON t.id_menu = m.id_menu
LIMIT 10;
```

Output:
```
id_transaksi  nama_menu       kategori    total
TRX00001      Cappuccino      Coffee      28000
TRX00002      Es Kopi Susu    Coffee      25000
...
```

### 4.2 Anatomy JOIN

```sql
FROM transaksi t                         -- tabel kiri (alias t)
INNER JOIN menu m                        -- gabung dengan tabel kanan (alias m)
    ON t.id_menu = m.id_menu             -- kondisi join (key matching)
```

> **Alias** (`t`, `m`) optional tapi sangat membantu readability. Pakai alias singkat (1-2 huruf).

### 4.3 Join 3+ Tabel

```sql
SELECT
    t.id_transaksi,
    t.tanggal,
    c.nama_cabang,
    p.nama AS nama_pelanggan,
    m.nama_menu,
    t.total
FROM transaksi t
INNER JOIN cabang c    ON t.id_cabang = c.id_cabang
INNER JOIN pelanggan p ON t.id_pelanggan = p.id_pelanggan
INNER JOIN menu m      ON t.id_menu = m.id_menu
LIMIT 10;
```

---

## 5. INNER vs LEFT JOIN

### 5.1 Mengapa Banyak Jenis JOIN?

Bayangkan kamu punya warung. Buku pencatatan kamu pisah: 1 buku isi *daftar pelanggan*, 1 buku lagi isi *daftar transaksi*. Kalau bos nanya "siapa pelanggan paling sering jajan bulan ini?", kamu cocokkan baris di kedua buku pakai ID pelanggan.

Tapi pertanyaan beda butuh "kelengkapan data" beda:
- "Pelanggan mana yang transaksi?" → cuma yang ada di **kedua** buku (INNER)
- "Pelanggan dorman (terdaftar tapi belum pernah transaksi)?" → semua pelanggan, walau belum ada transaksi (LEFT)

### 5.2 INNER JOIN

```sql
SELECT p.nama, COUNT(t.id_transaksi) AS jumlah_trx
FROM pelanggan p
INNER JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
GROUP BY p.id_pelanggan
ORDER BY jumlah_trx DESC;
```

INNER JOIN **hanya** keluarkan baris yang **ada di kedua tabel**. Pelanggan yang belum pernah transaksi → tidak muncul.

### 5.3 LEFT JOIN

```sql
SELECT p.nama, COUNT(t.id_transaksi) AS jumlah_trx
FROM pelanggan p
LEFT JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
GROUP BY p.id_pelanggan
ORDER BY jumlah_trx ASC;
```

LEFT JOIN **semua baris dari tabel kiri** (`pelanggan`), tambah info dari tabel kanan kalau cocok. Pelanggan yang belum pernah transaksi → muncul dengan `jumlah_trx = 0`.

### 5.4 Visual Mental Model

```
Tabel A         Tabel B        INNER JOIN A,B    LEFT JOIN A,B
┌────┐          ┌────┐         ┌──┐              ┌──────┐
│ A1 │          │ B1 │         │  │              │ A1   │
│ A2 │   ON     │ B2 │   →     │A2│              │ A2 B2│
│ A3 │  match   │ B3 │   →     │A3│              │ A3 B3│
│ A4 │          │ B4 │         │  │              │ A4   │
└────┘          └────┘         └──┘              └──────┘
                               (cuma yang        (semua A,
                                cocok)            tambah B
                                                   kalau cocok)
```

### 5.5 RIGHT, FULL, CROSS JOIN

- **RIGHT JOIN** = kebalikan LEFT (semua baris dari tabel kanan). Jarang dipakai — biasanya tukar urutan jadi LEFT.
- **FULL OUTER JOIN** = semua baris dari kedua tabel. SQLite tidak support, tapi BigQuery support.
- **CROSS JOIN** = cartesian product (semua kombinasi). Jarang dipakai untuk DA.

---

## 6. Setup BigQuery Sandbox

BigQuery = data warehouse cloud Google. Sandbox = mode gratis (tanpa kartu kredit) untuk learning.

### 6.1 Aktivasi Sandbox

1. Buka [console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery)
2. Login dengan akun Gmail
3. Saat ditanya "Create project" — buat project baru, namanya `savvys-da-learning` (atau bebas)
4. Otomatis masuk ke mode Sandbox (10 GB storage gratis, 1 TB query/bulan)

### 6.2 UI Tour

```
┌──────────────────────────────────────────────────────────────┐
│ Google Cloud Console — BigQuery                              │
├────────────────────┬─────────────────────────────────────────┤
│ EXPLORER           │ QUERY EDITOR                            │
│                    │                                         │
│ ▼ savvys-da-...    │ SELECT * FROM ... LIMIT 10;             │
│   ▶ MyDataset      │                                         │
│                    │ [Run]  [Save]  [Schedule]               │
│ ▼ Public Datasets  │                                         │
│   ▶ bigquery-      │                                         │
│     public-data    │                                         │
│     ▶ usa_names    │                                         │
│     ▶ samples      │                                         │
│     ▶ ...          │                                         │
├────────────────────┴─────────────────────────────────────────┤
│ QUERY RESULTS                                                │
│                                                              │
│ row_id | name | ...                                          │
└──────────────────────────────────────────────────────────────┘
```

> **[GAMBAR DIPERLUKAN — BigQuery Console UI]**
> **Apa yang harus di-screenshot:** halaman BigQuery setelah pertama kali login, sidebar Explorer dengan project & public datasets, query editor di tengah.
> **Konteks:** orientasi visual buat peserta yang baru pertama lihat BigQuery.

---

## 7. Query Dataset Publik di BigQuery

### 7.1 Dataset Publik yang Bagus untuk Latihan

Di sidebar Explorer → expand `bigquery-public-data`. Beberapa dataset menarik:

| Dataset | Deskripsi |
|---|---|
| `usa_names` | Daftar nama bayi USA per tahun |
| `nyc_yellow_taxi_trips` | Perjalanan taxi New York (miliaran baris) |
| `samples.shakespeare` | Karya Shakespeare per kata |
| `noaa_gsod` | Data cuaca global |
| `covid19_open_data` | Data COVID global |
| `chicago_crime` | Data kriminalitas Chicago |
| `google_analytics_sample` | Sample web analytics |

### 7.2 Query Pertama di BigQuery

```sql
-- Top 10 nama bayi laki-laki USA tahun 2020
SELECT
  name,
  number AS jumlah
FROM `bigquery-public-data.usa_names.usa_1910_current`
WHERE year = 2020
  AND gender = 'M'
ORDER BY jumlah DESC
LIMIT 10;
```

> **Catatan syntax BigQuery:**
> - Nama tabel pakai backtick (`` `...` ``) untuk full qualified name
> - Format: `` `project.dataset.table` ``
> - Backtick wajib kalau ada karakter spesial atau pakai full path

### 7.3 Pakai Public Indonesia COVID Dataset

```sql
SELECT
  date,
  cumulative_confirmed,
  cumulative_deceased
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code = 'ID'
  AND date >= '2022-01-01'
ORDER BY date DESC
LIMIT 30;
```

### 7.4 Cost Awareness

Setiap query di BigQuery dihargai **per byte di-scan**. Sandbox kasih 1 TB/bulan gratis. Tips hemat:

1. **JANGAN `SELECT *`** di tabel besar — cuma kolom yang dibutuhkan
2. **Pakai partitioning** kalau ada (filter `_PARTITIONTIME` atau kolom partition)
3. **Pakai LIMIT** saat eksplorasi
4. Lihat estimasi cost di pojok kanan atas sebelum Run

```sql
-- Mahal (full table scan)
SELECT * FROM `bigquery-public-data.nyc_yellow_taxi_trips...`

-- Hemat (partition filter)
SELECT pickup_datetime, total_amount
FROM `bigquery-public-data.nyc_yellow_taxi_trips...`
WHERE _PARTITIONTIME >= '2023-01-01'
LIMIT 1000;
```

---

## 8. Mini Case Study — Analisis Pelanggan dengan JOIN

Pakai database `kopi_kita.db`. Jawab dengan SQL:

### Q1. Top 10 Pelanggan Loyal (dengan Nama & Membership)

```sql
SELECT
    p.nama,
    p.membership,
    COUNT(t.id_transaksi) AS jumlah_kunjungan,
    SUM(t.total) AS total_belanja
FROM pelanggan p
INNER JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
GROUP BY p.id_pelanggan
ORDER BY jumlah_kunjungan DESC
LIMIT 10;
```

### Q2. Kategori Menu Terlaris per Cabang

```sql
SELECT
    c.nama_cabang,
    m.kategori,
    COUNT(*) AS jumlah_trx,
    SUM(t.total) AS revenue
FROM transaksi t
INNER JOIN cabang c ON t.id_cabang = c.id_cabang
INNER JOIN menu m ON t.id_menu = m.id_menu
GROUP BY c.id_cabang, m.kategori
ORDER BY c.nama_cabang, revenue DESC;
```

### Q3. Pelanggan Dorman (Punya Membership tapi Tidak Pernah Transaksi Q1)

```sql
SELECT
    p.id_pelanggan,
    p.nama,
    p.membership
FROM pelanggan p
LEFT JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
WHERE t.id_transaksi IS NULL;
```

> **Pattern populer:** "Item yang ada di Tabel A tapi tidak ada di Tabel B" → LEFT JOIN + WHERE B.key IS NULL.

### Q4. Profit per Menu

```sql
SELECT
    m.nama_menu,
    m.kategori,
    SUM(t.qty) AS qty_terjual,
    SUM(t.total) AS revenue,
    SUM(t.total - (t.qty * m.hpp)) AS profit
FROM menu m
INNER JOIN transaksi t ON m.id_menu = t.id_menu
GROUP BY m.id_menu
ORDER BY profit DESC;
```

---

## Apa Selanjutnya?

Lanjut ke **Day 4 AM — Statistics Descriptive** (`day-4-am-stats-descriptive/`). Fondasi statistik untuk DA: mean/median/std, distribusi, deteksi outlier.

> **Tip:** kalau sudah selesai materi, langsung coba **HackerRank SQL "Aggregations"** dan **"Basic Join"** — kamu sudah punya skill untuk selesaikan sebagian besar.

---

**Akhir Day 3 PM · Week 1**
*Savvys Education · 2026*

# Week 2 · Day 4 AM
# SQL Advanced — Window Function, CTE, Subquery

> **Tujuan:** Setelah modul ini kamu bisa pakai window function (ROW_NUMBER, RANK, LAG), CTE (Common Table Expression), subquery, dan setup PostgreSQL via Docker.
>
> **Estimasi:** 3 jam.

---

## 1. Setup PostgreSQL (One-Time)

Sebelum mulai, setup PostgreSQL local. Pakai Docker (recommended) atau Supabase free.

### Docker (5 menit)

```bash
docker run -d --name savvys-postgres \
  -e POSTGRES_PASSWORD=savvys2026 \
  -e POSTGRES_DB=kopi_kita \
  -p 5432:5432 \
  postgres:15
```

### Migrate Data dari SQLite

```bash
# Install driver
pip install psycopg2-binary

# Run migration
cd ~/savvys-da-kursus/.../day-3-am-sql-basics/
python _migrate_to_postgres.py
```

### Connect via DBeaver

New Connection → PostgreSQL → host `localhost`, port `5432`, db `kopi_kita`, user `postgres`, password `savvys2026`.

> **Detail panduan PostgreSQL:** `99-resources/platform-guides/database-stack.md`

---

## 2. Subquery — Query di Dalam Query

### 2.1 Subquery di WHERE

```sql
-- Transaksi yang nilai-nya di atas rata-rata
SELECT id_transaksi, total
FROM transaksi
WHERE total > (SELECT AVG(total) FROM transaksi);
```

### 2.2 Subquery di SELECT

```sql
SELECT
    nama_cabang,
    (SELECT COUNT(*) FROM transaksi t WHERE t.id_cabang = c.id_cabang) AS jumlah_trx
FROM cabang c;
```

### 2.3 Subquery di FROM (Derived Table)

```sql
SELECT cabang_summary.id_cabang, cabang_summary.total_revenue
FROM (
    SELECT id_cabang, SUM(total) AS total_revenue
    FROM transaksi
    GROUP BY id_cabang
) AS cabang_summary
WHERE cabang_summary.total_revenue > 1000000;
```

### 2.4 EXISTS / NOT EXISTS

```sql
-- Pelanggan yang punya minimal 1 transaksi > 100000
SELECT *
FROM pelanggan p
WHERE EXISTS (
    SELECT 1 FROM transaksi t
    WHERE t.id_pelanggan = p.id_pelanggan
      AND t.total > 100000
);
```

---

## 3. CTE — Common Table Expression (`WITH`)

CTE bikin subquery jadi lebih readable.

### 3.1 Basic CTE

```sql
WITH cabang_summary AS (
    SELECT id_cabang, SUM(total) AS revenue
    FROM transaksi
    GROUP BY id_cabang
)
SELECT * FROM cabang_summary
WHERE revenue > 1000000;
```

Sama hasilnya dengan subquery di FROM, tapi **lebih readable** terutama untuk multi-step.

### 3.2 Multiple CTE

```sql
WITH
cabang_summary AS (
    SELECT id_cabang, SUM(total) AS revenue
    FROM transaksi
    GROUP BY id_cabang
),
pelanggan_summary AS (
    SELECT id_pelanggan, COUNT(*) AS jumlah_trx
    FROM transaksi
    GROUP BY id_pelanggan
    HAVING COUNT(*) >= 5
)
SELECT
    p.nama,
    cs.revenue,
    ps.jumlah_trx
FROM pelanggan p
JOIN pelanggan_summary ps ON p.id_pelanggan = ps.id_pelanggan
JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
JOIN cabang_summary cs ON t.id_cabang = cs.id_cabang
LIMIT 10;
```

### 3.3 Recursive CTE (Advanced)

Untuk hierarchical data (org chart, kategori bertingkat). **Skip dulu — jarang dipakai DA pemula.**

---

## 4. Window Function — Game Changer untuk DA

**Window function** = aggregate yang **tidak grupkan baris**, tapi tambah kolom dengan hasil aggregate kontekstual.

Tools paling impactful sejak SQL standar — wajib kuasai untuk interview FAANG.

### 4.1 Anatomy

```sql
function() OVER (
    PARTITION BY col       -- groupby logical (opsional)
    ORDER BY col           -- urutan dalam partition (opsional, wajib untuk RANK)
    ROWS BETWEEN ... AND ... -- frame (opsional)
)
```

### 4.2 ROW_NUMBER, RANK, DENSE_RANK

```sql
-- Top transaksi per cabang
SELECT
    id_cabang,
    id_transaksi,
    total,
    ROW_NUMBER() OVER (PARTITION BY id_cabang ORDER BY total DESC) AS rn,
    RANK()       OVER (PARTITION BY id_cabang ORDER BY total DESC) AS rnk,
    DENSE_RANK() OVER (PARTITION BY id_cabang ORDER BY total DESC) AS dr
FROM transaksi
ORDER BY id_cabang, rn
LIMIT 10;
```

Beda:
- `ROW_NUMBER`: 1, 2, 3, 4 (no ties, selalu unique)
- `RANK`: 1, 2, 2, 4 (ties get same rank, gap setelahnya)
- `DENSE_RANK`: 1, 2, 2, 3 (ties get same rank, no gap)

### 4.3 Use Case: Top N per Group

Ambil top 3 transaksi per cabang:

```sql
WITH ranked AS (
    SELECT *,
        ROW_NUMBER() OVER (PARTITION BY id_cabang ORDER BY total DESC) AS rn
    FROM transaksi
)
SELECT id_cabang, id_transaksi, total
FROM ranked
WHERE rn <= 3;
```

### 4.4 LAG, LEAD — Compare with Previous/Next Row

```sql
-- Revenue harian + selisih dengan hari sebelumnya
WITH daily AS (
    SELECT
        DATE(tanggal) AS hari,
        SUM(total) AS revenue
    FROM transaksi
    GROUP BY hari
)
SELECT
    hari,
    revenue,
    LAG(revenue) OVER (ORDER BY hari) AS revenue_kemarin,
    revenue - LAG(revenue) OVER (ORDER BY hari) AS selisih
FROM daily
ORDER BY hari;
```

### 4.5 SUM/AVG dengan PARTITION BY (Running Total)

```sql
SELECT
    tanggal,
    total,
    SUM(total) OVER (ORDER BY tanggal) AS running_total,
    SUM(total) OVER (PARTITION BY id_cabang ORDER BY tanggal) AS running_per_cabang
FROM transaksi
ORDER BY tanggal;
```

### 4.6 % of Total

```sql
-- Setiap transaksi: berapa % dari total revenue cabang-nya?
SELECT
    id_transaksi,
    id_cabang,
    total,
    SUM(total) OVER (PARTITION BY id_cabang) AS revenue_cabang,
    total * 100.0 / SUM(total) OVER (PARTITION BY id_cabang) AS pct_of_cabang
FROM transaksi
ORDER BY pct_of_cabang DESC;
```

### 4.7 NTILE — Bagi data jadi N bucket

```sql
-- Bagi transaksi jadi 4 quartile by total
SELECT
    id_transaksi,
    total,
    NTILE(4) OVER (ORDER BY total) AS quartile
FROM transaksi;
```

---

## 5. CASE WHEN — Conditional Logic

```sql
SELECT
    id_transaksi,
    total,
    CASE
        WHEN total >= 100000 THEN 'Besar'
        WHEN total >= 50000 THEN 'Sedang'
        ELSE 'Kecil'
    END AS kategori
FROM transaksi;
```

Kombinasi dengan aggregate:

```sql
-- Hitung jumlah Big/Medium/Small per cabang
SELECT
    id_cabang,
    SUM(CASE WHEN total >= 100000 THEN 1 ELSE 0 END) AS jumlah_besar,
    SUM(CASE WHEN total BETWEEN 50000 AND 99999 THEN 1 ELSE 0 END) AS jumlah_sedang,
    SUM(CASE WHEN total < 50000 THEN 1 ELSE 0 END) AS jumlah_kecil
FROM transaksi
GROUP BY id_cabang;
```

---

## 6. Latihan Wajib — DataLemur Style

DataLemur ([datalemur.com](https://datalemur.com)) punya banyak soal SQL FAANG-style. Pattern-nya:
1. Ambil top N per group
2. Running total / cumulative
3. Pct of total
4. Period-over-period comparison
5. Cohort analysis

Semua bisa diselesaikan dengan window function + CTE.

> **Tip karir:** kalau kamu bisa selesaikan minimal 30 problem DataLemur (Easy + Medium), kamu sudah siap interview SQL DA di unicorn Indonesia.

---

## Apa Selanjutnya?

Lanjut **Day 4 PM — BigQuery Hands-On** untuk pengalaman query dataset publik berskala besar dengan window function yang sudah dipelajari.

---

**Akhir Day 4 AM · Week 2**
*Savvys Education · 2026*

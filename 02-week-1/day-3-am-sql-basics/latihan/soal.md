# Latihan — SQL Basics

> **Database:** `data/kopi_kita.db` (SQLite)
> **Submission:** simpan jawaban di `latihan/jawaban.sql` dengan komentar untuk tiap soal.
> **Bonus:** kerjakan juga di [HackerRank SQL Basic Select](https://hackerrank.com/domains/sql) untuk dapat sertifikasi gratis.

---

## Bagian A — Mudah (5 soal)

### A.1
Tampilkan semua kolom dari tabel `pelanggan`. Limit 10 baris.

### A.2
Tampilkan hanya `nama` dan `kota_asal` dari tabel `pelanggan`.

### A.3
Tampilkan semua transaksi dengan total > 100,000.

### A.4
Berapa total revenue Q1 2026? (Sum dari kolom `total` di tabel `transaksi`.)

### A.5
Berapa banyak menu kategori "Coffee"?

---

## Bagian B — Menengah (5 soal)

### B.1
Tampilkan menu yang harganya antara 20,000 - 30,000 (inclusive). Pakai operator `BETWEEN`.

### B.2
Tampilkan pelanggan dengan membership "Gold" yang berasal dari kota "Jakarta".

### B.3
Tampilkan top 5 transaksi termahal. Sort dari paling tinggi.

### B.4
Hitung rata-rata harga menu per kategori. Output: kategori + avg_harga.

> **Hint:** pakai GROUP BY (akan dibahas Day 3 PM, tapi syntax-nya cuma `GROUP BY kategori`).

### B.5
Berapa pelanggan unique yang pernah pakai metode bayar QRIS?

---

## Bagian C — Lanjut (4 soal)

### C.1
Tampilkan menu yang namanya mengandung kata "Latte" atau "Kopi". Pakai `LIKE`.

### C.2
Tampilkan transaksi yang dilakukan di **bulan Februari 2026** saja. Pakai filter tanggal.

### C.3
Tampilkan top 3 menu (id_menu) dengan **revenue tertinggi**. Pakai aggregate + ORDER BY + LIMIT.

### C.4
Berapa transaksi yang nilainya di **atas rata-rata transaksi**?

> **Hint:** pakai subquery: `WHERE total > (SELECT AVG(total) FROM transaksi)`

---

## Bagian D — Bonus (untuk yang sudah selesai)

### D.1 — Profit per Menu
Tampilkan untuk setiap menu (id_menu): jumlah qty terjual, total revenue, total profit.
- Profit per transaksi = (harga - hpp) × qty
- Tip: kamu butuh `JOIN` ke tabel menu (akan dibahas Day 3 PM). Untuk sekarang, asumsikan harga & hpp ada di tabel transaksi (Day 3 PM kita upgrade dengan JOIN).

Quick approach pakai subquery:
```sql
SELECT
    t.id_menu,
    SUM(t.qty) AS total_qty,
    SUM(t.total) AS revenue,
    SUM(t.total - (t.qty * (SELECT hpp FROM menu m WHERE m.id_menu = t.id_menu))) AS profit
FROM transaksi t
GROUP BY t.id_menu
ORDER BY profit DESC;
```

### D.2 — HackerRank Challenge
Selesaikan minimal 10 problem di [HackerRank SQL "Basic Select"](https://hackerrank.com/domains/sql/select/).

---

## Submission

Save di `latihan/jawaban.sql`:

```sql
-- ====================================================
-- LATIHAN SQL BASICS - [Nama Kamu]
-- Tanggal: YYYY-MM-DD
-- ====================================================

-- A.1: Tampilkan semua kolom dari tabel pelanggan, limit 10
SELECT *
FROM pelanggan
LIMIT 10;

-- A.2: ...
-- (lanjut isi 14 soal)
```

Push ke portfolio:
```bash
cd ~/savvys-da-kursus/portfolio/02-sql-bigquery
# copy jawaban.sql ke sini
git add jawaban.sql
git commit -m "Week 1 Day 3 AM: SQL Basics latihan jawaban"
git push
```

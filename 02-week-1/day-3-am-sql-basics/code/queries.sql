-- ====================================================
-- Week 1 Day 3 AM — SQL Basics Queries
-- Database: kopi_kita.db (SQLite)
-- ====================================================

-- ====================================================
-- 1. SELECT Dasar
-- ====================================================

SELECT * FROM menu;

SELECT nama_menu, harga FROM menu;

SELECT * FROM transaksi LIMIT 10;

-- Calculated column
SELECT
    nama_menu,
    harga,
    hpp,
    (harga - hpp) AS profit
FROM menu;

-- ====================================================
-- 2. WHERE & Operator
-- ====================================================

SELECT * FROM menu
WHERE kategori = 'Coffee';

SELECT nama_menu, harga FROM menu
WHERE harga > 25000;

-- Multi-condition AND
SELECT * FROM menu
WHERE kategori = 'Coffee'
  AND harga < 25000;

-- Multi-condition OR
SELECT * FROM menu
WHERE kategori = 'Coffee'
   OR kategori = 'Pastry';

-- BETWEEN
SELECT * FROM menu
WHERE harga BETWEEN 20000 AND 30000;

-- IN
SELECT * FROM menu
WHERE kategori IN ('Coffee', 'Pastry');

-- LIKE
SELECT * FROM menu
WHERE nama_menu LIKE 'Es%';

SELECT * FROM menu
WHERE nama_menu LIKE '%Latte%';

-- IS NULL
SELECT * FROM pelanggan
WHERE no_hp IS NULL;

-- ====================================================
-- 3. ORDER BY & LIMIT
-- ====================================================

SELECT * FROM menu
ORDER BY harga DESC;

SELECT * FROM menu
ORDER BY kategori ASC, harga DESC;

-- Top 5 transaksi termahal
SELECT * FROM transaksi
ORDER BY total DESC
LIMIT 5;

-- ====================================================
-- 4. Aggregate Functions
-- ====================================================

-- Ringkasan transaksi
SELECT
    COUNT(*) AS total_transaksi,
    SUM(total) AS total_revenue,
    AVG(total) AS avg_transaksi,
    MIN(total) AS trx_termurah,
    MAX(total) AS trx_termahal
FROM transaksi;

-- Per metode bayar
SELECT COUNT(*) AS jumlah_qris
FROM transaksi
WHERE metode_bayar = 'QRIS';

-- Pelanggan unique yang pernah transaksi
SELECT COUNT(DISTINCT id_pelanggan) AS pelanggan_aktif
FROM transaksi;

-- ====================================================
-- 5. Mini Case Study Solutions
-- ====================================================

-- Q1: Eksplorasi
SELECT
    COUNT(*) AS total_trx,
    SUM(total) AS total_revenue,
    ROUND(AVG(total)) AS avg_transaksi,
    MIN(total) AS trx_termurah,
    MAX(total) AS trx_termahal
FROM transaksi;

-- Q2: Revenue per id_menu
SELECT
    id_menu,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue
FROM transaksi
GROUP BY id_menu
ORDER BY revenue DESC;

-- Q3: Metode Bayar
SELECT
    metode_bayar,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue,
    ROUND(AVG(total)) AS avg_per_trx
FROM transaksi
GROUP BY metode_bayar
ORDER BY revenue DESC;

-- Q4: Per Cabang
SELECT
    id_cabang,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue,
    COUNT(DISTINCT id_pelanggan) AS pelanggan_unique
FROM transaksi
GROUP BY id_cabang;

-- Q5: Per Bulan
SELECT
    strftime('%Y-%m', tanggal) AS bulan,
    COUNT(*) AS jumlah_trx,
    SUM(total) AS revenue
FROM transaksi
GROUP BY bulan
ORDER BY bulan;

-- Q6: Top 5 Pelanggan Loyal
SELECT
    id_pelanggan,
    COUNT(*) AS jumlah_kunjungan,
    SUM(total) AS total_belanja
FROM transaksi
GROUP BY id_pelanggan
ORDER BY jumlah_kunjungan DESC
LIMIT 5;

# Latihan — SQL Advanced

> Pakai PostgreSQL (kopi_kita) atau BigQuery. Semua query support window function & CTE.

## A — Subquery (3 soal)

### A.1
Transaksi yang nilai-nya di **atas avg cabang-nya** (bukan avg keseluruhan).

### A.2
Pelanggan yang **belum pernah** transaksi (NOT EXISTS pattern).

### A.3
Cabang yang revenue-nya **lebih tinggi** dari revenue total Bandung. (Pakai subquery untuk total Bandung dulu.)

## B — CTE (3 soal)

### B.1
Pakai CTE: hitung total revenue per cabang, lalu filter cabang dengan revenue > 1jt.

### B.2
Multi-CTE: (1) revenue per cabang, (2) jumlah pelanggan unique per cabang, (3) join keduanya.

### B.3
CTE: pelanggan dengan **min 5 kunjungan**. Tampilkan profile lengkap (nama, membership, dll).

## C — Window Function (5 soal)

### C.1 — Top N per Group
Top 3 transaksi terbesar per cabang. Tampilkan nama_cabang, id_transaksi, total, ranking.

### C.2 — Running Total
Revenue per hari + cumulative running total Q1 2026.

### C.3 — Period Comparison
Pakai LAG: revenue per minggu + selisih (%) dengan minggu sebelumnya.

### C.4 — Pct of Total
Setiap menu: revenue + persentase kontribusi ke revenue total. Sort desc.

### C.5 — Quartile
Bagi pelanggan ke 4 quartile berdasarkan total belanja Q1. Tampilkan jumlah pelanggan per quartile.

## D — Real Interview Question (DataLemur Style)

### D.1
Pakai NYC Taxi (BigQuery `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`):

Hari apa dalam seminggu yang **avg tip percentage**-nya tertinggi? Tampilkan nama hari + avg_tip_pct, sorted desc.

### D.2
Public Holidays Effect — pakai dataset COVID:
Cari tanggal yang **kasus baru di-report**-nya 50% lebih tinggi dari moving avg 7 hari sebelumnya.

## Submission
`latihan/jawaban.sql`. Push ke `02-sql-bigquery/` portfolio.

🎯 **Setelah selesai:** kerjakan minimal 5 soal "Easy" di [DataLemur](https://datalemur.com) untuk solidify skill window function.

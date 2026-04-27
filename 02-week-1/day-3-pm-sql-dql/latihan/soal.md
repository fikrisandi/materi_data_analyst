# Latihan — SQL DQL (GROUP BY, HAVING, JOIN)

> **Database:** `../day-3-am-sql-basics/data/kopi_kita.db`

## Bagian A — GROUP BY (4 soal)

### A.1
Total revenue dan jumlah transaksi per cabang. Sort by revenue desc.

### A.2
Rata-rata harga menu per kategori.

### A.3
Top 5 pelanggan paling sering transaksi (by count). Tampilkan id_pelanggan + jumlah_kunjungan.

### A.4
Total qty terjual per menu (id_menu). Sort descending.

## Bagian B — HAVING (3 soal)

### B.1
Cabang yang revenue total > 1,500,000.

### B.2
Pelanggan yang transaksi ≥ 10 kali.

### B.3
Menu (id_menu) yang qty terjual ≥ 50.

## Bagian C — JOIN (4 soal)

### C.1
Top 10 transaksi terbesar dengan kolom: id_transaksi, tanggal, **nama_cabang**, **nama_menu**, total.

### C.2
Total revenue per **kategori menu** (bukan id_menu) per **cabang**. Output: nama_cabang, kategori, revenue.

### C.3
Top 5 pelanggan dengan **nama** + **membership** + jumlah_kunjungan + total_belanja.

### C.4
Pelanggan yang membership-nya "Gold" tapi **tidak pernah** transaksi Q1 2026.

> Hint: LEFT JOIN + WHERE IS NULL

## Bagian D — BigQuery (3 soal)

### D.1
Top 20 nama bayi laki-laki USA tahun 2020:
```sql
-- buka BigQuery console, query bigquery-public-data.usa_names.usa_1910_current
```

### D.2
Total kasus COVID Indonesia per bulan tahun 2022 (dari `bigquery-public-data.covid19_open_data`).

### D.3
Top 5 line dari Shakespeare yang paling banyak muncul kata "love" (dari `bigquery-public-data.samples.shakespeare`).

## Submission
Save di `latihan/jawaban-dql.sql`. Push ke `02-sql-bigquery/` portfolio.

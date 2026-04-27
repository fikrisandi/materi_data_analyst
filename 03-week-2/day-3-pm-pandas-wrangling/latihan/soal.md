# Latihan — Pandas Wrangling

> Pakai `kopi_kita.db` SQLite. Jawab di `latihan/jawaban.ipynb`.

## Bagian A — GroupBy (3 soal)

### A.1
Total revenue, jumlah transaksi, & rata-rata per **cabang**. Output DataFrame.

### A.2
Per **bulan**, hitung jumlah transaksi & total revenue.

### A.3
Top 5 menu (id_menu) berdasarkan total qty terjual.

## Bagian B — Merge (3 soal)

### B.1
Merge transaksi + menu, tampilkan kolom: id_transaksi, tanggal, **nama_menu**, **kategori**, total.

### B.2
Merge transaksi + cabang + pelanggan + menu jadi satu wide DataFrame `df_full`.

### B.3
Pelanggan yang belum pernah transaksi (left join transaksi ke pelanggan, filter NaN).

## Bagian C — Pivot Table (2 soal)

### C.1
Pivot: `nama_cabang` (rows) × `kategori` menu (columns) × sum of `total` (values).

### C.2
Pivot: `bulan` × `metode_bayar` × jumlah transaksi.

## Bagian D — Transform & Apply (2 soal)

### D.1
Tambah kolom `pct_of_cabang_revenue` = persentase kontribusi tiap transaksi terhadap total revenue cabang-nya. Pakai `transform`.

### D.2
Tambah kolom `kategori_total` (Besar/Sedang/Kecil) pakai `apply`.

## Bagian E — Date & String (2 soal)

### E.1
Tambah kolom `nama_hari` (Monday-Sunday) dari `tanggal`. Hari apa paling ramai?

### E.2
Pelanggan yang nama-nya **diawali huruf "A"**. Berapa orang?

## Bagian F — Mini Case Study

Buat 1 notebook `analysis.ipynb` yang jawab:
1. Total profit per kategori menu (revenue - HPP×qty)
2. Top 10 pelanggan by profit kontribusi
3. Trend revenue per minggu — visualisasi pakai `df.plot()`

Tulis 3 insight markdown cell di akhir notebook.

## Submission
`latihan/jawaban.ipynb` + `analysis.ipynb`. Push ke `03-python-pandas/` portfolio.

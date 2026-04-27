# Latihan — Pandas Intro

> Dataset: `kopi_kita.db` (SQLite, Week 1) atau `penjualan-warung-2026.xlsx`.
> Kerjakan di Jupyter Notebook `latihan/jawaban.ipynb`.

## Soal 1 — Load Data
Load data tabel `transaksi` dari SQLite ke DataFrame `df`. Verifikasi:
- Shape (250, 9)
- Tipe kolom benar (tanggal harus datetime)

Hint untuk parse tanggal:
```python
df["tanggal"] = pd.to_datetime(df["tanggal"])
```

## Soal 2 — Eksplorasi
Tampilkan:
- 10 baris pertama
- 5 baris random
- Info struktur (`df.info()`)
- Describe statistik

## Soal 3 — Filter
1. Tampilkan hanya transaksi dari Cabang Tebet (`C001`)
2. Tampilkan hanya transaksi total > 50000 dan metode QRIS
3. Tampilkan transaksi di bulan Februari 2026

## Soal 4 — Top N
1. Top 10 transaksi terbesar
2. Top 5 transaksi terkecil

## Soal 5 — Tambah Kolom
1. Tambah kolom `bulan` (dari kolom tanggal, ambil bulan saja)
2. Tambah kolom `kategori_total`:
   - >= 100000: "Besar"
   - 50000-99999: "Sedang"
   - < 50000: "Kecil"

## Soal 6 — Aggregation
1. Total revenue, mean, median, std dari kolom `total`
2. Berapa transaksi unique per `id_pelanggan`?
3. Berapa pelanggan unique total?

## Soal 7 — Multi-Source
Load tabel `transaksi`, `menu`, `pelanggan` jadi 3 DataFrame. Tampilkan ringkasan masing-masing (shape, head).

## Bonus
Save hasil filter Soal 3 (transaksi Februari) ke file CSV `output/transaksi-feb-2026.csv`.

## Submission
`latihan/jawaban.ipynb`. Push ke `03-python-pandas/` portfolio.

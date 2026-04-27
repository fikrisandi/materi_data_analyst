# Latihan — Statistics Descriptive

> Dataset: `kopi_kita.db` (SQLite) atau `penjualan-warung-2026.xlsx`. Bebas pakai Excel/SQL.

## Bagian A — Central Tendency (3 soal)

### A.1
Hitung mean, median, mode dari kolom `total` (transaksi). Bandingkan ketiganya — apakah data skewed?

### A.2
Mean harga menu per kategori. Pakai SQL GROUP BY:
```sql
SELECT kategori, AVG(harga) FROM menu GROUP BY kategori;
```

### A.3
Median jumlah kunjungan per pelanggan. **Hint:** dulu hitung kunjungan per pelanggan, baru ambil median dari hasil.

## Bagian B — Dispersion (3 soal)

### B.1
Hitung Std deviation transaksi `total` per cabang. Cabang mana lebih volatile?

### B.2
Hitung Q1, Q3, IQR dari kolom `total`.

### B.3
Pelanggan paling konsisten transaksi (paling kecil std nilai transaksi)? Pelanggan paling volatile?

## Bagian C — Outlier (2 soal)

### C.1
Pakai IQR rule. Berapa transaksi dianggap outlier? Sebut id_transaksi-nya.

### C.2
Pakai Z-score (>3). Berapa transaksi outlier? Bandingkan dengan IQR — apakah hasilnya sama?

## Bagian D — Korelasi (2 soal)

### D.1
Korelasi antara `qty` dan `total` di tabel transaksi. (Trivially tinggi karena total = qty × harga, tapi cek angka eksaknya.)

### D.2
Korelasi antara harga menu dan jumlah qty terjual (data harus di-aggregate dulu). Apakah menu mahal **kurang** laku, atau tetap laku?

## Bagian E — Insight Bisnis

Tulis 3 insight statement dari analisis statistik di atas. Format:

```
1. [Fakta statistik] + [Interpretasi bisnis] + [Rekomendasi]
   Contoh: "Std transaksi Cabang Tebet 35% lebih tinggi dari Dago, padahal mean mirip.
           Ini berarti Tebet punya pelanggan yang lebih beragam (mix big-spender & casual),
           sementara Dago lebih homogen.
           Rekomendasi: Tebet bisa coba program member tier untuk segmentasi target."
```

## Submission
Save di `latihan/jawaban-stats.xlsx` atau `latihan/jawaban-stats.sql`. Push ke `05-statistics-case/` portfolio.

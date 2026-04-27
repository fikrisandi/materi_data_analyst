# Week 1 · Day 4 AM
# Statistics Descriptive — Memahami Data dengan Angka Ringkasan

> **Tujuan modul:** Setelah modul ini, kamu paham statistik deskriptif dasar (mean, median, std, distribusi, outlier, korelasi) dan bisa pakai untuk membaca karakter data sebelum analisis lanjutan.
>
> **Estimasi waktu:** 3 jam.

---

## 1. Mengapa Statistik untuk DA — Bukan Hanya Aggregasi

Banyak DA pemula menganggap statistik = matematika rumit dengan banyak rumus. Padahal untuk **statistik deskriptif** (yang dipelajari hari ini), inti-nya cuma 1 hal: **bagaimana meringkas dataset besar dengan beberapa angka yang bermakna**.

Bayangkan kamu punya 250 transaksi. Atasan tanya: "gimana penjualan Q1?" Kamu nggak mungkin jawab dengan menyebut 250 angka satu per satu. Kamu butuh angka **ringkasan** yang mewakili: rata-rata, sebaran, ekstrim.

> **Pesan utama:** Statistik deskriptif = **kompresi informasi**. Tujuannya bukan menjadi ahli statistik, tapi bisa **menjawab pertanyaan bisnis dengan angka yang tepat**.

### Excel/SQL Pakai Aggregasi, Statistik Pakai Konteks

Day 2-3 kita pakai SUM, AVG, COUNT — itu **aggregasi**. Statistik tambah konteks:
- **AVG = 50000** itu informasi setengah jadi. **AVG = 50000 ± 25000 (1 std)** lebih bermakna — kamu tahu spread-nya.
- **MAX = 200000** bisa misleading kalau itu outlier ekstrim. Statistik kasih kamu cara identify outlier.

---

## 2. Central Tendency — Mean, Median, Mode

Ketiga ini "nilai pusat" dari distribusi data, tapi **definisinya beda** dan **tidak interchangeable**.

### 2.1 Mean (Rata-rata Aritmatika)

```
Mean = (jumlah semua nilai) / (jumlah data)
```

Excel: `=AVERAGE(range)` · SQL: `AVG(col)` · Python: `df['col'].mean()`

Skenario: gaji 5 karyawan: `[10jt, 12jt, 11jt, 13jt, 100jt]` (1 outlier CEO).
- Mean = `(10+12+11+13+100)/5` = **29.2 jt**
- Padahal 4 dari 5 karyawan dapat di bawah 14 jt!

**Mean sensitif outlier.** Kalau ada outlier ekstrim, mean bisa misleading.

### 2.2 Median (Nilai Tengah)

Urutkan data, ambil nilai di tengah.

Untuk data ganjil: nilai persis tengah. Untuk genap: rata-rata 2 nilai tengah.

Excel: `=MEDIAN(range)` · SQL: tidak built-in (pakai workaround atau PERCENTILE_DISC) · Python: `df['col'].median()`

Skenario sama: `[10, 11, 12, 13, 100]` → urut, ambil tengah → **median = 12 jt**

**Median tahan outlier.** Lebih representatif untuk data dengan outlier (gaji, harga rumah, durasi tunggu, dll).

### 2.3 Mode (Nilai Paling Sering Muncul)

```
Mode = nilai yang frekuensi-nya tertinggi
```

Excel: `=MODE(range)` · SQL: pakai `GROUP BY + ORDER BY COUNT DESC LIMIT 1` · Python: `df['col'].mode()`

Skenario: ukuran sepatu pelanggan: `[40, 41, 42, 42, 42, 43, 44, 42]` → **mode = 42**

Mode bagus untuk **data kategorikal** (warna favorit, kategori produk terlaris) atau **data diskrit yang punya nilai yang sering ulang**.

### 2.4 Kapan Pakai Apa?

| Kasus | Pakai |
|---|---|
| Data kontinu, no outlier | Mean |
| Data kontinu, ada outlier | Median |
| Data sangat skewed (income, durasi) | Median |
| Data kategorikal | Mode |
| Symmetric distribution normal | Mean ≈ Median (dua-duanya OK) |

> **Insight DA:** kalau atasan tanya "rata-rata gaji karyawan kita", **kamu wajib clarify**: mean atau median? Beda kesimpulan, beda keputusan.

---

## 3. Dispersion — Sebaran Data

Mean/median = pusat. Tapi seberapa **jauh data tersebar dari pusat**? Itu dispersion.

### 3.1 Range

```
Range = Max - Min
```

Sederhana, tapi sangat sensitif outlier.

Skenario: `[10, 12, 11, 13, 100]` → range = **90**. Padahal 4 dari 5 di range 10-13.

### 3.2 Variance & Standard Deviation

**Variance** = rata-rata kuadrat selisih dari mean.

```
Variance = Σ(x - mean)² / n
```

**Standard Deviation (Std)** = √Variance. Lebih intuitif karena unit sama dengan data asli.

Excel: `=STDEV.S(range)` (sample) · `=STDEV.P(range)` (population)
SQL: `STDDEV(col)` (kebanyakan DB)
Python: `df['col'].std()`

> **Sample vs Population Std:**
> - Sample (`STDEV.S`): bagi dengan `n-1` — pakai kalau data kamu sample dari populasi besar (situasi default DA)
> - Population (`STDEV.P`): bagi dengan `n` — kalau punya seluruh populasi
>
> 99% kasus DA pakai sample. Default Excel SQL Pandas = sample.

### 3.3 Interpretasi Std

Skenario: 2 toko punya AVG penjualan harian sama (50jt), tapi std beda:
- Toko A: AVG = 50jt, **Std = 5jt** → penjualan stabil (45-55jt umumnya)
- Toko B: AVG = 50jt, **Std = 30jt** → penjualan volatile (kadang 20jt, kadang 80jt)

Mana lebih predictable? Toko A. Std bantu kamu **paham reliability data**, bukan hanya angka pusat.

### 3.4 IQR (Interquartile Range)

Quartile = data dibagi 4 grup:
- Q1 (25%) — 25% data di bawah ini
- Q2 (50%) — = median
- Q3 (75%) — 75% data di bawah ini

```
IQR = Q3 - Q1
```

IQR = "spread of middle 50%". **Tahan outlier**, lebih robust dari std untuk data skewed.

Excel: `=QUARTILE(range, 1)` untuk Q1, `=QUARTILE(range, 3)` untuk Q3 · Python: `df['col'].quantile([0.25, 0.75])`.

---

## 4. Distribusi & Bentuk Data

### 4.1 Bentuk Distribusi yang Sering Ditemui

```
NORMAL (bell curve)        SKEWED LEFT (tail kiri)    SKEWED RIGHT (tail kanan)
     ╱╲                        ╲╲                            ╱╱
    ╱  ╲                       ╲ ╲                          ╱ ╱
   ╱    ╲                      ╲  ╲                        ╱  ╱
  ╱      ╲                      ╲  ╲___                ___╱  ╱
─╯        ╰─                     ╲___─                 ─___╱
 mean=median                 mean<median            mean>median


BIMODAL (2 puncak)            UNIFORM (rata)
   ╱╲    ╱╲
  ╱  ╲  ╱  ╲                ─────────
 ╱    ╲╱    ╲              │         │
╯            ╰─             │         │
                            │         │
2 segmen pelanggan         setiap nilai sama freq
```

### 4.2 Kapan Bentuk Distribusi Penting?

- **Normal** → mean & std meaningful, banyak teori statistik berlaku (CI, hypothesis test). Banyak data alami: tinggi badan, IQ, error pengukuran.
- **Right-skewed** → mean lebih tinggi dari median. Common di: gaji, harga rumah, durasi sesi user, jumlah view video. **Pakai median**, bukan mean.
- **Bimodal** → mungkin ada **2 sub-grup** di data. Misal: jam transaksi punya 2 puncak (pagi & sore). Coba **segment data** sebelum analisis lanjut.

### 4.3 Cek Distribusi dengan Histogram

Excel: pilih kolom → Insert → Chart → Histogram.
Python: `df['col'].hist(bins=30)`.

> **[GAMBAR DIPERLUKAN — Contoh Histogram Distribusi]**
> **Apa:** screenshot atau gambar 4 jenis histogram side-by-side: Normal, Skewed Right, Bimodal, Uniform.
> **Konteks:** visual referensi peserta untuk identify bentuk data sendiri.

---

## 5. Outlier Detection

Outlier = data point yang **jauh banget** dari mayoritas. Bisa **error data** atau **fenomena nyata** yang signifikan.

### 5.1 Z-Score Method

```
Z = (x - mean) / std
```

Aturan umum:
- |Z| > 2 → "agak ekstrim", patut diperhatikan
- |Z| > 3 → "ekstrim", kemungkinan outlier

Cocok untuk **distribusi normal**.

### 5.2 IQR Method

```
Lower bound = Q1 - 1.5 * IQR
Upper bound = Q3 + 1.5 * IQR
```

Apa pun di luar range ini = outlier. **Tahan untuk distribusi skewed**.

### 5.3 Apa yang Dilakukan dengan Outlier?

Pilihan:
1. **Investigate dulu** — apakah error pencatatan? (transaksi 1 milyar di warung kopi → kemungkinan typo)
2. **Hapus** — kalau yakin error
3. **Cap/Winsorize** — ganti outlier dengan nilai 95th/99th percentile
4. **Pisahkan analisis** — kalau outlier representasi sub-segmen (pelanggan VIP, dll)
5. **Pakai median & IQR** alih-alih mean & std

> **Anti-pattern:** **JANGAN** otomatis hapus outlier tanpa investigasi. Kadang outlier adalah **sinyal paling penting** dalam data (fraud, anomali, opportunity).

---

## 6. Korelasi Pearson

**Korelasi** = seberapa **terkait** dua variabel.

### 6.1 Pearson Correlation Coefficient (r)

```
r ∈ [-1, +1]
+1 = perfectly positive (naik bareng)
 0 = no linear relationship
-1 = perfectly negative (1 naik, 1 turun)
```

Excel: `=CORREL(range1, range2)` · SQL: kompleks (pakai window) · Python: `df.corr()` atau `df['a'].corr(df['b'])`

### 6.2 Interpretasi Nilai r

| |r| | Strength |
|---|---|
| 0.0 - 0.3 | Weak / no relationship |
| 0.3 - 0.6 | Moderate |
| 0.6 - 0.9 | Strong |
| > 0.9 | Very strong |

### 6.3 Caveat — Korelasi BUKAN Kausalitas!

Klasik example:
- Penjualan ice cream **berkorelasi tinggi** dengan **kasus tenggelam** di pantai
- Tapi ice cream tidak **menyebabkan** tenggelam!
- Variable ketiga: **musim panas** → lebih banyak orang ke pantai + lebih banyak beli ice cream

Selalu tanya: **apakah ada variabel ketiga yang tidak diukur?** (confounding variable).

> **Pesan utama:** "x berkorelasi dengan y" tidak berarti "x menyebabkan y". DA pemula sering salah klaim ini di laporan — hindari dari awal.

---

## 7. Mini Case Study — Profil Statistik Penjualan Kopi Kita

Pakai dataset yang sudah dipakai di Day 2 (Excel) dan Day 3 (SQL). Pertanyaan:

### Q1. Profil Distribusi Total Transaksi
- Mean, Median, Mode dari kolom `total`
- Std deviation
- Q1, Q3, IQR
- Mean - Median: apakah skewed?

### Q2. Outlier
Pakai metode IQR. Berapa banyak transaksi yang termasuk outlier? Apakah valid (transaksi besar real) atau error?

### Q3. Korelasi Qty vs Total
Hitung Pearson correlation antara `qty` dan `total`. Apakah hasilnya masuk akal?

### Q4. Profil per Cabang
Bandingkan mean & std `total` per cabang. Cabang mana lebih volatile?

### Output

Bisa kerjakan di Excel atau SQL. Pakai Excel kalau lebih nyaman.

```excel
Q1.1 Mean       =AVERAGE(Transaksi!H2:H251)
Q1.2 Median     =MEDIAN(Transaksi!H2:H251)
Q1.3 Mode       =MODE(Transaksi!H2:H251)
Q1.4 Std        =STDEV.S(Transaksi!H2:H251)
Q1.5 Q1         =QUARTILE(Transaksi!H2:H251, 1)
Q1.6 Q3         =QUARTILE(Transaksi!H2:H251, 3)
Q1.7 IQR        =Q1.6 - Q1.5
Q1.8 Outlier?   =Q1.5 - 1.5*Q1.7   (lower bound)
                 =Q1.6 + 1.5*Q1.7   (upper bound)
```

Atau di SQL (SQLite):

```sql
SELECT
    AVG(total) AS mean,
    -- median butuh workaround di SQLite, di BigQuery: APPROX_QUANTILES
    MIN(total) AS min,
    MAX(total) AS max
FROM transaksi;
```

Tulis 3 insight statement dari hasil analisis.

---

## Apa Selanjutnya?

Lanjut ke **Day 4 PM — Mini Case Study Week 1** untuk integrasi semua skill (Excel + SQL + Stats).

> **Tip:** statistik deskriptif lebih dalam akan kita pakai lagi di Week 3 (Statistics Inferential — hypothesis testing, confidence interval, A/B testing).

---

**Akhir Day 4 AM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan
1. Paham central tendency: mean, median, mode — kapan pakai apa
2. Paham dispersion: variance, standard deviation, IQR
3. Paham distribusi: normal, skewed, bimodal
4. Bisa deteksi outlier dengan Z-score & IQR rule
5. Bisa korelasi dasar (Pearson)

## Durasi ~3 jam · Prasyarat: Day 3 (SQL)

## Output
- `materi.md` (~2,500 kata)
- `latihan/soal.md` — analisis statistik dataset Kopi Kita
- `cheatsheet.md`

## Struktur
| Section | Topik |
|---|---|
| 1 | Mengapa Statistik untuk DA — Bukan Hanya Aggregasi |
| 2 | Central Tendency: Mean, Median, Mode |
| 3 | Dispersion: Range, Variance, Std, IQR |
| 4 | Distribusi & Bentuk Data |
| 5 | Outlier Detection |
| 6 | Korelasi Pearson |
| 7 | Mini Case: Profil Statistik Penjualan Kopi Kita |

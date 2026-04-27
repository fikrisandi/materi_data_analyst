# Week 1 · Day 2 AM
# Excel Foundation untuk Data Analyst

> **Tujuan modul:** Setelah membaca dan mengerjakan modul ini, kamu paham fungsi Excel di workflow DA, bisa pakai formula essentials, VLOOKUP & INDEX-MATCH, Pivot Table, Conditional Formatting — dan sudah selesai 1 mini case study real.
>
> **Estimasi waktu:** 3 jam · **Format:** modul step-by-step + latihan langsung dengan dataset.

---

## 1. Mengapa Excel Tetap Relevan untuk DA

Mungkin kamu pernah dengar: "DA modern pakai Python, Excel itu jadul". Faktanya tidak begitu.

**Excel masih sangat relevan** karena 3 alasan:

1. **Universal di dunia kerja.** 99% perusahaan punya orang yang pakai Excel. Kalau kamu kasih dashboard Tableau ke manager Finance senior yang tidak biasa, dia tetap minta versi Excel-nya. Excel = lingua franca data di kantor.
2. **Untuk dataset kecil-menengah, lebih cepat dari Python.** Kalau analisis kamu butuh 100 baris × 10 kolom, buka Excel, pivot, selesai 5 menit. Pakai pandas? 30 menit minimum.
3. **Cepat untuk eksplorasi.** Sebelum bikin notebook Python untuk analisis serius, banyak DA pro **eksplor data dulu di Excel** — lihat distribusi cepat, sort manual, pivot kasar.

**Kapan Excel bukan pilihan tepat?** Saat:
- Dataset > 1 juta baris (Excel limit ~1.04 juta baris per sheet)
- Analisis berulang yang harus reproducible (otomatisasi via Python lebih baik)
- Statistik kompleks (Excel tidak cocok untuk hypothesis testing serius)
- Real-time pipeline (Excel tidak ada konsep auto-refresh dari database)

> **Pesan utama:** Excel bukan kompetitor SQL/Python. Excel adalah **tool pertama** yang kamu pegang saat data masuk ke meja. SQL/Python adalah tool yang kamu pakai saat skala atau kompleksitas naik.

---

## 2. Anatomi Workbook & Worksheet

### Vocabulary Dasar

```
WORKBOOK (file .xlsx)
└── WORKSHEET 1 ("Sheet1")     ← satu spreadsheet/tab
│   ├── COLUMN A, B, C, ...    ← kolom (vertikal)
│   ├── ROW 1, 2, 3, ...       ← baris (horizontal)
│   └── CELL A1, B5, C10, ...  ← perpotongan kolom & baris
│
├── WORKSHEET 2 ("Pivot")
└── WORKSHEET 3 ("Summary")
```

### Buka Dataset Latihan

Buka file `data/penjualan-warung-2026.xlsx`. Kamu lihat 5 sheet di bawah:

| Sheet | Isi |
|---|---|
| **README** | Penjelasan dataset |
| **Transaksi** | 250 baris transaksi Q1 2026 |
| **Menu** | 8 menu dengan harga & HPP |
| **Cabang** | 2 cabang (Jakarta & Bandung) |
| **Pelanggan** | 50 pelanggan dengan info membership |

> **[GAMBAR DIPERLUKAN — Workbook dengan 5 Sheet]**
> **Apa yang harus di-screenshot:** file `penjualan-warung-2026.xlsx` terbuka di Excel, tampilkan 5 tab di bawah, kursor di sheet "Transaksi".
> **Konteks isi nanti:** orientasi pertama peserta dengan dataset.

### Konsep Cell Reference

Setiap cell punya alamat unik (contoh: `B5` = kolom B baris 5). Saat kamu pakai formula, kamu bisa:

- **Relative reference** — `B5` (otomatis berubah saat copy ke cell lain)
- **Absolute reference** — `$B$5` (tetap walau di-copy)
- **Mixed** — `$B5` (kolom tetap, baris berubah) atau `B$5` (baris tetap, kolom berubah)

> **Trik:** Tekan `F4` saat menulis formula untuk toggle antara `B5` → `$B$5` → `B$5` → `$B5` → kembali.

---

## 3. Formula Essentials

### 3.1 SUM, AVERAGE, COUNT

Buka sheet **Transaksi**. Di cell kosong (misal di kolom J atau di sheet baru), coba:

```excel
=SUM(H2:H251)              # total revenue Q1 2026
=AVERAGE(H2:H251)          # rata-rata per transaksi
=COUNT(H2:H251)            # jumlah transaksi (cell numeric)
=COUNTA(A2:A251)           # jumlah baris (cell non-empty, termasuk text)
=MAX(H2:H251)              # transaksi terbesar
=MIN(H2:H251)              # transaksi terkecil
```

> **Catatan:** kolom H = Total. Kolom A = ID Transaksi.

### 3.2 IF — Logika Dasar

```excel
=IF(H2>50000, "Besar", "Kecil")
```

Penjelasan: kalau total transaksi > 50000, label "Besar", lainnya "Kecil".

Drag formula ke bawah untuk apply ke semua baris.

### 3.3 COUNTIF, SUMIF — Hitung & Sum dengan Kondisi

```excel
=COUNTIF(I2:I251, "QRIS")         # berapa transaksi pakai QRIS?
=SUMIF(I2:I251, "QRIS", H2:H251)  # total revenue dari QRIS
```

Penjelasan COUNTIF/SUMIF:
- Argument 1: range yang dicek
- Argument 2: kondisi
- (untuk SUMIF) Argument 3: range yang di-sum

### 3.4 COUNTIFS, SUMIFS — Multiple Conditions

Multiple kondisi:

```excel
=COUNTIFS(C2:C251, "C001", I2:I251, "QRIS")
# Berapa transaksi di Cabang Tebet (C001) yang pakai QRIS?

=SUMIFS(H2:H251, C2:C251, "C001", I2:I251, "QRIS")
# Total revenue Cabang Tebet via QRIS
```

> **Tip:** kolom B = Tanggal, C = ID Cabang, E = ID Menu, F = Qty, G = Harga, H = Total, I = Metode Bayar. Pelajari posisi kolom dulu sebelum nulis formula.

### 3.5 ROUND, CONCATENATE, & Operasi Text

```excel
=ROUND(AVERAGE(H2:H251), 0)     # rata-rata dibulatkan ke integer
=CONCAT("Total: Rp ", H2)        # text + number jadi "Total: Rp 50000"
=TEXT(H2, "#,##0")               # format number jadi "50,000"
```

---

## 4. Lookup — VLOOKUP & INDEX-MATCH

Lookup adalah operasi paling sering dipakai DA: **mencari nilai di tabel lain berdasarkan key**.

### 4.1 Skenario

Di sheet **Transaksi**, kamu lihat kolom **ID Menu** (M01, M02, ...). Tapi kamu mau tahu **nama menunya** dan **kategorinya** — yang ada di sheet **Menu**.

Solusi: VLOOKUP atau INDEX-MATCH.

### 4.2 VLOOKUP — Versi Klasik

Syntax:
```
=VLOOKUP(lookup_value, table_array, col_index, exact_match)
```

Di sheet Transaksi, di cell baru (misal kolom J), tulis:

```excel
=VLOOKUP(E2, Menu!$A$2:$E$9, 2, FALSE)
```

Penjelasan:
- `E2` = ID Menu di baris 2 transaksi (misal "M03")
- `Menu!$A$2:$E$9` = range tabel Menu (A2 sampai E9, sheet Menu)
- `2` = kolom ke-2 dari range (= Nama Menu)
- `FALSE` = exact match (TRUE = approximate, jarang dipakai untuk DA)

Drag ke bawah → semua transaksi sekarang punya nama menu.

Sekarang ambil kategori juga:

```excel
=VLOOKUP(E2, Menu!$A$2:$E$9, 3, FALSE)
```

Cuma ganti `2` jadi `3` (kolom ke-3 = Kategori).

### 4.3 Kelemahan VLOOKUP

VLOOKUP punya 2 batasan menjengkelkan:
1. **Cuma bisa lookup ke kanan** dari kolom key. Kalau key di kolom B dan yang dicari di kolom A, tidak bisa.
2. **Kalau urutan kolom di tabel sumber berubah** (misal kolom Nama dipindah dari ke-2 ke ke-3), formula kamu rusak.

Solusi: **INDEX-MATCH** (lebih flexible).

### 4.4 INDEX-MATCH — Versi Modern

Syntax:
```
=INDEX(return_range, MATCH(lookup_value, lookup_range, 0))
```

Sama-sama cari nama menu:

```excel
=INDEX(Menu!$B$2:$B$9, MATCH(E2, Menu!$A$2:$A$9, 0))
```

Penjelasan:
- `Menu!$B$2:$B$9` = kolom yang nilainya akan dikembalikan (Nama Menu)
- `MATCH(E2, Menu!$A$2:$A$9, 0)` = posisi `E2` dicari di kolom A Menu, return number (1, 2, 3, ...)
- `0` di akhir MATCH = exact match
- `INDEX` ambil nilai di posisi tersebut dari range B

Lebih ribet awalnya, tapi:
- Bisa lookup ke kiri & kanan
- Stabil walau struktur tabel berubah

### 4.5 XLOOKUP — Versi Terbaru (Excel 2021+)

Kalau kamu pakai Excel 2021 atau Microsoft 365:

```excel
=XLOOKUP(E2, Menu!$A$2:$A$9, Menu!$B$2:$B$9)
```

Lebih clean dari INDEX-MATCH. Tapi karena banyak perusahaan masih pakai Excel lama, **INDEX-MATCH wajib dikuasai**.

---

## 5. Pivot Table — Tools Paling Powerful

Pivot Table adalah **tool yang paling membedakan DA dari pengguna Excel biasa**. Kalau cuma bisa 1 hal di Excel, kuasai Pivot Table.

### 5.1 Apa itu Pivot Table?

**Definisi:** Pivot Table = tabel ringkasan yang otomatis aggregasi data berdasarkan dimensi yang kamu pilih. Tanpa nulis formula apa pun.

Skenario: kamu punya 250 baris transaksi. Pertanyaan bisnis:
- Berapa total revenue per cabang?
- Menu apa yang paling laku?
- Hari/bulan mana yang paling ramai?
- Metode bayar mana yang dominan?

Tanpa Pivot Table, kamu harus tulis SUMIFS/COUNTIFS satu per satu. **Dengan Pivot Table, semua ini selesai dalam 1 menit.**

### 5.2 Bikin Pivot Table Pertama

1. Klik di sembarang cell di sheet **Transaksi**
2. Menu **Insert** → **PivotTable**
3. Excel akan otomatis pilih range A1:I251. Klik OK.
4. Pivot akan masuk ke sheet baru.

Kamu lihat panel di kanan dengan 4 area:
- **Filters** — saringan global
- **Columns** — dimensi yang jadi kolom pivot
- **Rows** — dimensi yang jadi baris pivot
- **Values** — angka yang di-aggregate

### 5.3 Pivot Pertama: Total Revenue per Cabang

Di panel kanan:
1. Drag **ID Cabang** ke area **Rows**
2. Drag **Total** ke area **Values** (default akan jadi Sum)

Hasil:
```
ID Cabang     Sum of Total
C001          1,xxx,xxx
C002          1,xxx,xxx
Grand Total   3,xxx,xxx
```

Selamat — kamu baru bikin pivot table pertama. **Tanpa formula apa pun.**

### 5.4 Pivot Lebih Kompleks: Revenue per Cabang × Kategori Menu

Tunggu — kategori menu tidak ada di sheet Transaksi (cuma ada ID Menu). Jadi kita perlu **ke kembali tarik kategori dulu via VLOOKUP**, atau bisa juga pakai Pivot dengan multiple sheet.

Cara mudah: di sheet Transaksi, tambah kolom J = Nama Menu, kolom K = Kategori (pakai VLOOKUP yang tadi). Lalu refresh pivot (Klik kanan di pivot → Refresh).

Sekarang di pivot:
1. Drag **ID Cabang** ke Rows
2. Drag **Kategori** ke Columns
3. Drag **Total** ke Values

Hasil (cross-tab):
```
ID Cabang | Coffee | Non-Coffee | Pastry | Snack | Total
C001      | xxx    | xxx        | xxx    | xxx   | xxx
C002      | xxx    | xxx        | xxx    | xxx   | xxx
```

### 5.5 Filtering Pivot

Drag **Metode Bayar** ke area **Filters** di atas pivot. Sekarang ada filter di pivot. Pilih "QRIS" — pivot otomatis filter ke transaksi QRIS saja.

### 5.6 Pivot Chart

Setelah pivot jadi, klik di pivot → menu **PivotTable Analyze** → **PivotChart**. Pilih tipe chart (Bar, Line, Pie). Chart akan bind ke pivot — kalau pivot di-update, chart auto-update.

> **[GAMBAR DIPERLUKAN — Pivot Table dengan PivotChart]**
> **Apa yang harus di-screenshot:** Excel dengan pivot table di kiri (Cabang × Kategori, values Total), pivot chart di kanan (clustered bar chart).
> **Konteks isi nanti:** Visual hasil pivot — peserta lihat seperti apa "selesai".

---

## 6. Conditional Formatting

Conditional Formatting = mengubah warna cell berdasarkan kondisi. Bagus untuk **visual analysis cepat**.

### Skenario

Di sheet Transaksi, kamu mau tandai transaksi besar (>100,000) supaya gampang dilihat.

1. Pilih kolom Total (H2:H251)
2. Menu **Home** → **Conditional Formatting** → **Highlight Cells Rules** → **Greater Than...**
3. Isi `100000`, pilih warna (default merah/orange)
4. OK

Sekarang transaksi >100,000 berwarna mencolok.

### Other Conditional Formatting yang Berguna untuk DA

- **Color Scales** (gradient warna berdasarkan value) — bagus untuk lihat trend di banyak baris
- **Data Bars** (bar chart kecil di dalam cell) — visual proportion tanpa pivot
- **Icon Sets** (panah naik/turun, ⬆️⬇️) — bagus untuk perbandingan

Coba: pilih kolom Total, **Conditional Formatting** → **Color Scales** → pilih merah-hijau. Sekarang transaksi tinggi merah, transaksi rendah hijau (atau sebaliknya).

---

## 7. Mini Case Study — Analisis Penjualan Kopi Kita Q1 2026

Sekarang aplikasikan semua yang sudah dipelajari. Buka dataset, jawab 5 pertanyaan bisnis berikut:

### Pertanyaan Bisnis

**Q1.** Berapa **total revenue** Q1 2026? Berapa **rata-rata revenue per transaksi**?

**Q2.** **Cabang mana** (Tebet vs Dago) yang paling profitable di Q1? (Hint: butuh kolom **Profit** = Total − (HPP × Qty). HPP ada di sheet Menu → pakai VLOOKUP.)

**Q3.** **Menu apa yang paling laku** (by qty)? **Top 3** menu by revenue?

**Q4.** **Bulan mana** (Jan, Feb, Mar) yang paling ramai? (Hint: pakai fungsi `MONTH(B2)` untuk extract bulan dari tanggal.)

**Q5.** Metode bayar mana yang dominan? Apakah ada perbedaan pola antara **2 cabang**?

### Cara Pengerjaan

1. **Buka workbook**, save as `analysis.xlsx` (jangan kerja di file dataset asli)
2. **Tambah kolom kerja** di sheet Transaksi:
   - J: Nama Menu (VLOOKUP)
   - K: Kategori (VLOOKUP)
   - L: HPP (VLOOKUP dari Menu kolom HPP)
   - M: Profit per Transaksi (= H - L*F → Total - HPP×Qty)
   - N: Bulan (= TEXT(B2, "mmm") atau =MONTH(B2))
3. **Bikin 5 pivot table** untuk jawab Q1-Q5 (atau gabung di 1 pivot dengan multiple values)
4. **Pakai Conditional Formatting** untuk tandai pivot dengan color scales
5. **Tulis 3 insight statement** di akhir sheet (1 paragraf, 1-2 kalimat per insight)

### Output yang Diharapkan

File `analysis.xlsx` dengan:
- Sheet "Transaksi" (raw + kolom kerja)
- Sheet "Pivot Q1" sampai "Pivot Q5"
- Sheet "Insight" (dengan 3 insight statement)

> **Insight bukan angka.** "Revenue Q1 = Rp 5jt" itu **fakta**, bukan insight. Insight = interpretasi dari fakta + rekomendasi tindakan. Contoh insight: "Cabang Tebet revenue 60% lebih tinggi dari Dago, padahal jumlah pelanggan unique mirip — ini disebabkan order value rata-rata Tebet (Rp 45rb) lebih tinggi daripada Dago (Rp 28rb). **Rekomendasi:** evaluasi pricing strategy Dago atau push menu kategori higher-margin di sana."

---

## 8. Tips Excel untuk DA Profesional

### Shortcut Wajib

| Shortcut | Fungsi |
|---|---|
| `Ctrl+Shift+L` | Toggle Filter |
| `Ctrl+Shift+End` | Pilih semua sampai akhir data |
| `Ctrl+Arrow` | Lompat ke ujung data ke arah arrow |
| `Ctrl+T` | Convert range jadi Excel Table (auto-format) |
| `Alt+=` | Auto-sum (pintar deteksi range) |
| `F4` | Toggle absolute/relative reference saat nulis formula |
| `Ctrl+;` | Insert tanggal hari ini |
| `Ctrl+Shift+;` | Insert jam sekarang |
| `Ctrl+1` | Format Cells dialog |

### Best Practice untuk DA

1. **Selalu simpan raw data di sheet terpisah & jangan diedit.** Bikin sheet "working" untuk analisis. Kalau ada yang salah, raw masih clean.
2. **Pakai Excel Tables (Ctrl+T)** untuk data yang akan jadi sumber pivot. Auto-expand saat ada baris baru.
3. **Beri nama range** untuk formula yang sering pakai (Tab "Formulas" → "Define Name"). Lebih readable.
4. **Dokumentasikan asumsi & sumber data** di sheet README. Penting untuk audit & handover.
5. **Hindari merge cells** untuk data — merge bikin pivot & filter rusak. Merge OK untuk header/title saja.

### Anti-pattern yang Harus Dihindari

❌ **Banyak sheet untuk hal serupa** — 12 sheet untuk 12 bulan? Pakai 1 sheet + filter bulan.

❌ **Formula raksasa nested 7 IF** — pakai IFS, atau tabel lookup terpisah.

❌ **Format cell sebagai data** — warna cell = data? Bikin kolom dedicated untuk status/kategori.

❌ **Spasi di akhir text untuk align** — pakai cell formatting (alignment), bukan spasi.

❌ **Save as .xls (lama)** — pakai .xlsx atau .xlsb (binary, lebih cepat untuk file besar).

---

## Apa Selanjutnya?

Kamu sudah selesai modul pertama yang substantial. Sekarang Excel bukan misteri lagi.

**Selanjutnya:**

1. **Selesaikan latihan di `latihan/soal.md`** kalau belum (10 soal: 5 mudah, 3 menengah, 2 advanced)
2. **Push hasil analisis ke portfolio:**
   ```bash
   cd ~/savvys-da-kursus/portfolio/01-excel-foundation
   # copy analysis.xlsx ke sini
   git add analysis.xlsx README.md insight.md
   git commit -m "Week 1 Day 2: Excel Foundation — analisis Kopi Kita Q1 2026"
   git push
   ```
3. **Lanjut ke Day 2 PM — Excel Power Query** — folder `02-week-1/day-2-pm-excel-power-query/`. Akan belajar data cleaning advanced di Excel: merge data dari multiple file, transformation, refresh otomatis.

---

**Akhir Day 2 AM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan Sesi

1. Paham fungsi Excel sebagai tools DA (kapan pakai, kapan ganti ke SQL/Python)
2. Bisa formula essentials: SUM, AVERAGE, IF, COUNTIF, SUMIF
3. Bisa lookup: VLOOKUP, INDEX-MATCH (lebih advanced)
4. Bisa Pivot Table: aggregation per dimensi, drill-down
5. Bisa Conditional Formatting untuk visual analysis
6. Selesai 1 mini case study: analisis penjualan warung kopi Q1 2026

## Durasi

~3 jam

## Prasyarat

- Excel atau Google Sheets terinstall
- Sudah selesai Day 1 (Setup + Git)
- Dataset latihan ada di `data/penjualan-warung-2026.xlsx`

## Format Output

- `materi.md` — modul tertulis (~3,000 kata)
- `data/penjualan-warung-2026.xlsx` — dataset latihan (250 transaksi, 5 sheet)
- `latihan/soal.md` — 10 soal latihan dari basic ke advanced
- `cheatsheet.md` — formula & shortcut Excel

## Struktur Konten

| Section | Topik |
|---|---|
| 1 | Mengapa Excel Tetap Relevan untuk DA |
| 2 | Anatomi Workbook & Worksheet |
| 3 | Formula Essentials: SUM, AVERAGE, IF, COUNT family |
| 4 | Lookup: VLOOKUP & INDEX-MATCH |
| 5 | Pivot Table — Tools Paling Powerful |
| 6 | Conditional Formatting |
| 7 | Mini Case: Analisis Penjualan Kopi Kita Q1 2026 |
| 8 | Tips Excel untuk DA Profesional |

## Output Portfolio

```
data-analyst-portfolio/01-excel-foundation/
├── README.md (insight singkat)
├── data/penjualan-warung-2026.xlsx (raw)
├── analysis.xlsx (hasil pivot, lookup, conditional formatting)
└── insight.md (3 insight statement dari analisis)
```

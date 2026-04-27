# Week 1 · Day 2 PM
# Excel Power Query — Data Cleaning & Transformation

> **Tujuan modul:** Setelah modul ini, kamu paham Power Query, bisa gabung & bersihkan data dari multiple file Excel, dan otomatisasi proses data cleaning yang sebelumnya manual & repetitive.
>
> **Estimasi waktu:** 2.5 jam · **Format:** modul step-by-step + latihan langsung.

---

## 1. Mengapa Power Query? — Skenario Real

Bayangkan kamu DA di Kopi Kita yang sudah punya 3 cabang. Setiap awal bulan, manajer cabang kirim laporan penjualan dalam file Excel terpisah:
- `tebet-januari-2026.xlsx`
- `dago-januari-2026.xlsx`
- `kelapa-gading-januari-2026.xlsx`

Masalah:
- Format kolom **berbeda** (Tebet pakai "Total", Dago pakai "Amount", Kelapa Gading pakai "TOTAL_RP")
- Format tanggal **inkonsisten** (DD/MM/YYYY, YYYY-MM-DD, "Jan 1, 2026")
- Cabang Kelapa Gading menulis nilai sebagai text "Rp 50,000" (bukan number)
- Ada **baris kosong** dan **typo** ("Cappucino" alih-alih "Cappuccino")
- Ada **case inkonsisten** ("CASH", "Cash", "cash", "tunai")

Pertanyaan dari atasan: **"Tolong dong gabungkan data 3 cabang Januari, lalu kasih total revenue per cabang."**

Kalau kamu copy-paste manual:
- 30 menit minimum (kalau lancar)
- Tiap bulan harus diulang
- Risiko typo & manual error

**Power Query** bikin proses ini **sekali setup, auto-rerun setiap bulan**. Setelah setup awal, tiap awal bulan kamu cuma **klik Refresh** — laporan auto-update pakai 3 file baru.

> **Pesan utama:** Power Query = **otomatisasi data cleaning di Excel**. Mirip Pandas Python, tapi GUI-based & lebih ramah untuk DA non-coding.

---

## 2. Anatomi Power Query Editor

Power Query muncul di Excel **Tab Data**. Ada beberapa cara akses:

- **Get Data** → pilih sumber (file, folder, database)
- **From Table/Range** → convert range existing jadi query
- **Recent Sources** → akses sumber yang sebelumnya pernah dipakai

Setelah click salah satu, **Power Query Editor** terbuka di window baru. Layout:

```
┌─────────────────────────────────────────────────────────────────┐
│ HOME · TRANSFORM · ADD COLUMN · VIEW                            │
├─────────────────────────────────────────────────────────────────┤
│ [QUERIES]              │ [PREVIEW DATA]              │ [STEPS]  │
│                        │                             │          │
│ - tebet-januari        │  Tanggal | Menu | Qty | ... │ - Source │
│ - dago-januari         │  ...                        │ - Promote│
│ - kelapa-gading        │  ...                        │ - Type   │
│ - GabunganJanuari      │                             │ - Filter │
│                        │                             │ - ...    │
└─────────────────────────────────────────────────────────────────┘
```

Komponen kunci:
- **Queries (kiri)** — list query (1 query = 1 dataset hasil transform)
- **Preview Data (tengah)** — tampilan data setelah step yang lagi dipilih
- **Applied Steps (kanan)** — daftar step transform berurutan. Klik step manapun untuk lihat data di titik tersebut.

Setiap kali kamu klik Transform di toolbar (rename column, change type, dll), **step baru otomatis ditambah** ke list. Kamu bisa undo dengan klik X di step.

Saat selesai, klik **Close & Load** untuk push hasil ke Excel sheet.

---

## 3. Import Data dari File / Folder

### 3.1 Import 1 File

1. Excel → **Data** → **Get Data** → **From File** → **From Excel Workbook**
2. Pilih `tebet-januari-2026.xlsx`
3. Di Navigator: pilih sheet (misal "Penjualan") → klik **Transform Data** (jangan Load — supaya bisa edit dulu)

Power Query Editor terbuka.

### 3.2 Import Folder Sekaligus (Power Query Magic)

Skenario: kamu punya 3 file di folder `data/`. Daripada import satu-satu:

1. **Data** → **Get Data** → **From File** → **From Folder**
2. Pilih folder `data/`
3. Power Query tampilkan list 3 file
4. Klik **Combine** → **Combine & Transform Data**
5. Pilih sheet yang sama di semua file (misal "Penjualan")

Power Query otomatis **gabungkan semua file**. Tambahkan kolom `Source.Name` (nama file) supaya kamu tahu data dari cabang mana.

> **Tip:** kalau format file beda (sheet name berbeda, header berbeda), kamu butuh **manual approach** — import 3 file terpisah, bersihkan satu per satu, lalu **Append**. Lihat Section 5.

---

## 4. Cleaning — Date, Text, Whitespace

### 4.1 Promote First Row to Headers

Saat import, kadang baris pertama bukan dianggap header. Klik:
**Home** → **Use First Row as Headers**

### 4.2 Change Column Type

Klik kanan kolom → **Change Type** → pilih:
- **Date** untuk tanggal
- **Whole Number** untuk integer
- **Decimal Number** untuk float
- **Text** untuk string

> **Power Query auto-detect type** sebagian besar. Tapi format aneh (seperti "Jan 1, 2026") harus manual.

Kalau ada error setelah change type, baris error muncul dengan icon ⚠️. Kamu bisa filter Error rows: klik kanan kolom → **Remove Errors**.

### 4.3 Trim & Clean Whitespace

Skenario: cell berisi `" Espresso "` (ada spasi awal/akhir).

Pilih kolom → **Transform** → **Format** → **Trim** (buang whitespace awal & akhir) atau **Clean** (buang non-printable characters).

### 4.4 Standardize Case

Untuk kolom Metode Bayar yang berisi "CASH", "Cash", "cash", "tunai":

**Transform** → **Format** → **Capitalize Each Word** (atau UPPERCASE/lowercase).

Lalu untuk normalize "tunai" → "Cash":
**Transform** → **Replace Values** → Find "Tunai", Replace dengan "Cash".

### 4.5 Parse Date dari Text

Kolom dengan format "Jan 1, 2026" tidak bisa langsung di-Change Type ke Date. Solusi:

1. **Add Column** → **Custom Column** dengan formula:
   ```
   = Date.From(Text.From([Tanggal]))
   ```
2. Atau: **Transform** → **Parse Date** (kalau format umum)

Kalau format aneh banget, pakai **Add Column → Column from Examples**:
- Power Query tampilkan kolom kosong, kamu ketik **contoh hasil yang kamu mau** untuk 2-3 baris
- Power Query otomatis bikin formula yang match

### 4.6 Buang Baris Kosong

**Home** → **Remove Rows** → **Remove Blank Rows**.

---

## 5. Append vs Merge Queries

**Append** = "tumpuk" 2+ tabel **vertikal** (jumlah kolom mirip, baris bertambah).
**Merge** = "join" 2 tabel **horizontal** berdasarkan key (mirip VLOOKUP).

### 5.1 Append — Skenario Multi-Cabang

Setelah import & cleaning 3 file Tebet, Dago, Kelapa Gading masing-masing jadi query terpisah. Tapi kolom **harus sama nama-nya**:

Pastikan kolom rename jadi:
- `Tanggal` (bukan "Date" / "TANGGAL")
- `Menu` (bukan "Item" / "MENU")
- `Qty` (bukan "Quantity")
- `Total` (bukan "Amount" / "TOTAL_RP")
- `Metode_Bayar` (bukan "Payment" / "BAYAR")

Lalu:
1. **Home** → **Append Queries** → **Append Queries as New**
2. Pilih 3 query (Tebet, Dago, Kelapa Gading)
3. Power Query bikin query baru `Append1` dengan semua baris

Tambahkan kolom `Cabang` di tiap query asli supaya tahu data dari cabang mana setelah append.

### 5.2 Merge — Skenario Lookup

Skenario: kamu punya tabel **Transaksi** (250 baris) dan **Menu** (8 baris). Kamu mau gabung supaya tabel Transaksi punya kolom Kategori dari Menu (mirip VLOOKUP).

1. **Home** → **Merge Queries** (ada juga "Merge as New")
2. Tabel kiri = Transaksi
3. Tabel kanan = Menu
4. Pilih kolom key di kedua tabel: `id_menu` di Transaksi & `id_menu` di Menu
5. Join Kind: **Left Outer** (semua transaksi, tambah info menu kalau cocok)
6. Hasilnya: kolom baru `Menu` (struct) muncul. Klik tombol expand di header → centang `nama_menu` & `kategori`

> **Tip:** Merge di Power Query lebih powerful dari VLOOKUP — bisa **multiple key** & **multiple result columns** sekaligus.

---

## 6. Group By & Pivot di Power Query

### 6.1 Group By

Skenario: total revenue per Cabang × Metode Bayar.

1. **Home** → **Group By**
2. Pilih kolom: Cabang, Metode_Bayar (Advanced — multiple group)
3. Aggregations:
   - New name: `Total Revenue`, Operation: `Sum`, Column: `Total`
   - New name: `Jumlah Transaksi`, Operation: `Count Rows`

Hasil:

```
Cabang        | Metode_Bayar | Total Revenue | Jumlah Transaksi
Tebet         | Cash         | 1,500,000     | 25
Tebet         | QRIS         | 3,200,000     | 50
Dago          | Cash         | 1,100,000     | 18
...
```

### 6.2 Pivot Column

Skenario: hasil di atas mau jadi cross-tab (Cabang sebagai baris, Metode Bayar sebagai kolom).

1. Klik kolom `Metode_Bayar` (yang akan jadi kolom)
2. **Transform** → **Pivot Column**
3. Values column: pilih `Total Revenue`
4. OK

Output:
```
Cabang        | Cash      | QRIS      | Debit     | Kredit
Tebet         | 1,500,000 | 3,200,000 | 800,000   | 400,000
Dago          | 1,100,000 | 2,500,000 | 600,000   | 200,000
...
```

### 6.3 Unpivot Column

Kebalikan dari Pivot — convert "wide" jadi "long". Bagus untuk data yang mau dimasukkan ke Pivot Table Excel.

Pilih kolom yang mau di-unpivot → **Transform** → **Unpivot Columns**.

---

## 7. Conditional Column

Skenario: tambah kolom **Kategori Transaksi** yang kategorisasi:
- Total < 30000 → "Kecil"
- 30000-70000 → "Sedang"
- >= 70000 → "Besar"

1. **Add Column** → **Conditional Column**
2. New column name: `Kategori`
3. Tambah aturan:
   - If `Total` < 30000 → `Kecil`
   - Else If `Total` < 70000 → `Sedang`
   - Else → `Besar`
4. OK

> **Power Query M Language (advanced):** kalau kamu klik View → Formula Bar, kamu lihat formula mentah. Power Query pakai bahasa namanya **M** — mirip F#. Tidak wajib dipelajari awal, tapi makin advanced kamu makin perlu paham M.

---

## 8. Refresh & Maintainability

Setelah Close & Load, hasil masuk Excel sheet sebagai Excel Table.

**Refresh** saat data sumber update:
1. **Data** → **Refresh All** (atau Ctrl+Alt+F5)
2. Power Query auto-rerun semua step dengan data terbaru

**Best practice:**

1. **Beri nama query yang descriptive** (bukan default `Query1`, `Query2`).
2. **Jangan delete step** kalau salah — selalu Edit step dengan icon gear ⚙️.
3. **Dokumentasikan** dengan klik kanan step → "Properties" → tambah comment.
4. **Save query connection only** (bukan Load to Sheet) untuk query intermediate.

> **Tip:** kalau pivot table-mu data source-nya query Power Query, refresh sekali di Data tab → semua pivot otomatis update.

---

## 9. Mini Case Study — Gabung 3 Cabang Januari 2026

Sekarang aplikasikan semua. **Tugas:** gabung file 3 cabang yang ada di `data/` jadi 1 tabel rapi.

**Output yang diharapkan:** Excel Table `Penjualan_Januari_2026` dengan kolom:
- Tanggal (date type)
- Cabang (Tebet / Dago / Kelapa Gading)
- Menu (text, sudah di-trim & corrected typo)
- Qty (whole number)
- Total (whole number)
- Metode_Bayar (text, standardized — Cash/QRIS/Debit/Kredit)
- Kategori_Transaksi (Kecil/Sedang/Besar)

### Langkah Penyelesaian (Outline)

1. Import 3 file Excel separately (Tebet, Dago, Kelapa Gading)
2. Untuk tiap query:
   - Use First Row as Headers
   - Rename kolom jadi standar (Tanggal, Menu, Qty, Total, Metode_Bayar)
   - Change types
   - Trim whitespace di Menu
   - Replace typo: "Cappucino" → "Cappuccino"
   - Standardize Metode_Bayar
   - Untuk Kelapa Gading: parse "Rp 50,000" jadi number 50000
   - Tambah kolom **Cabang** (hardcoded: "Tebet", "Dago", "Kelapa Gading")
3. Append 3 queries jadi 1 (`Penjualan_Januari_2026`)
4. Tambah Conditional Column `Kategori_Transaksi`
5. Close & Load to new sheet

### Validasi

Setelah selesai, output harusnya punya sekitar 100-115 baris (40+38+35 minus baris kosong yang dibuang).

Bikin Pivot Table dari hasil ini:
- Rows: Cabang
- Values: Sum of Total
- Lihat: total revenue per cabang.

Save semua di file `analysis-power-query.xlsx`.

---

## Apa Selanjutnya?

Lanjut ke **Day 3 AM — SQL Basics** (`02-week-1/day-3-am-sql-basics/`). SQL akan kasih cara yang **lebih powerful** untuk operasi serupa, terutama saat data sudah masuk database (bukan file Excel terpisah).

> **Insight:** Power Query untuk DA = sweet spot antara Excel formula (terbatas) dan Python (powerful tapi steep learning curve). Banyak DA pro pakai Power Query untuk 60% pekerjaan harian.

---

**Akhir Day 2 PM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan

1. Paham apa itu Power Query & kapan dipakai (vs formula manual)
2. Bisa import data dari multiple Excel files & gabungkan
3. Bisa data cleaning: ubah format tanggal, trim whitespace, standardize text, hapus baris kosong
4. Bisa transformasi: pivot/unpivot, group by, conditional column
5. Setup auto-refresh saat data sumber berubah

## Durasi
~2.5 jam

## Prasyarat
- Day 2 AM (Excel Foundation) selesai
- Excel 2016+ atau Microsoft 365 (Power Query built-in di Data tab)

## Format Output
- `materi.md` — modul (~2,500 kata)
- `data/` — 3 file Excel "kotor" untuk latihan (`tebet-januari-2026.xlsx`, `dago-januari-2026.xlsx`, `kelapa-gading-januari-2026.xlsx`)
- `latihan/soal.md` — task: gabung 3 file, bersihkan, output 1 tabel rapi
- `cheatsheet.md`

## Struktur Konten
| Section | Topik |
|---|---|
| 1 | Mengapa Power Query? Skenario Real |
| 2 | Anatomi Power Query Editor |
| 3 | Import Data dari File / Folder |
| 4 | Cleaning: Date, Text, Whitespace |
| 5 | Append vs Merge Queries |
| 6 | Group By & Pivot di Power Query |
| 7 | Conditional Column |
| 8 | Refresh & Maintainability |
| 9 | Mini Case: Gabung 3 Cabang Januari 2026 |

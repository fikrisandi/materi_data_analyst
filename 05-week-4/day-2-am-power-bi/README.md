# Week 4 · Day 2 AM
# Power BI Desktop — Build Corporate Dashboard

> **Tujuan:** Setelah modul ini kamu paham UI Power BI, bisa bikin dashboard interactive dengan Power Query + DAX, dan paham kapan pakai Power BI vs Tableau.
>
> **Estimasi:** 3 jam.

---

## 1. Power BI vs Tableau — Kapan Pakai Apa?

| | Power BI | Tableau |
|---|---|---|
| **Harga** | Free Desktop, $10/user/mo Premium | Free Public, $70/user/mo Desktop |
| **Best for** | Microsoft ecosystem (Excel, Azure, Office) | Standalone, advanced visual |
| **Calculation** | DAX (powerful) | Calculated Field + LOD |
| **Mobile** | Power BI Mobile App | Tableau Mobile |
| **Industri Indonesia** | Banking, BUMN, korporat tradisional | Tech, startup, e-commerce |

**Rekomendasi:** kuasai **keduanya**, deepen di salah satu (sesuai target industri). Power BI lebih ramah pemula karena ekosistem Office.

---

## 2. Setup

1. Download **Power BI Desktop** (Windows only, free) dari [powerbi.microsoft.com](https://powerbi.microsoft.com/desktop)
2. Install
3. Buka — sign in dengan akun Microsoft (gratis bikin)

> **Catatan Mac users:** Power BI Desktop **Windows only**. Pakai VM (Parallels) atau skip session ini.

---

## 3. UI Tour

```
┌─────────────────────────────────────────────────────────────────┐
│ HOME · INSERT · MODELING · VIEW · HELP                          │
├──────────────────────┬──────────────────────────────────────────┤
│ VISUALIZATIONS       │  CANVAS                                  │
│ ─────────────────    │                                          │
│ [icon] Bar           │  Drag visual ke sini                     │
│ [icon] Column        │                                          │
│ [icon] Line          │                                          │
│ [icon] Pie           │                                          │
│ [icon] Card          │                                          │
│ [icon] Slicer        │                                          │
│ ...                  │                                          │
├──────────────────────┴──────────────────────────────────────────┤
│ FIELDS PANE (kanan)                                             │
│ ▼ Transaksi                                                     │
│   • id_transaksi                                                │
│   • total                                                       │
│   • cabang                                                      │
└─────────────────────────────────────────────────────────────────┘
```

3 mode di kiri:
- **Report** — bikin visual & dashboard
- **Data** — view & edit table
- **Model** — relationship antar tabel

---

## 4. Get Data

1. **Home → Get Data → Excel**
2. Pilih `kopi_kita.xlsx`
3. Pilih sheet yang mau di-load
4. Klik **Transform Data** (bukan Load) — buka Power Query Editor

Power Query udah dipelajari Week 1 Day 2 PM — sama persis di Power BI. Pakai untuk cleaning sebelum load.

5. Setelah cleaning, klik **Close & Apply** — data masuk ke Power BI

---

## 5. Build Visual

### 5.1 Card — KPI

1. Drag visual **Card** ke canvas
2. Drag field **Total** ke Card
3. Klik dropdown → Sum
4. Format: Format pane → Display units (Thousands / Millions)

### 5.2 Bar Chart — Revenue per Cabang

1. Drag visual **Stacked Bar Chart**
2. Y-axis: `Cabang`
3. X-axis: `Total` (Sum)
4. Format judul: "Revenue per Cabang Q1 2026"

### 5.3 Line Chart — Trend

1. Drag **Line Chart**
2. X-axis: `Tanggal` (group by Month)
3. Y-axis: `Total`

### 5.4 Slicer — Interactive Filter

1. Drag **Slicer** visual
2. Drop field **Cabang**
3. Sekarang user bisa klik untuk filter semua chart

### 5.5 Map — kalau ada kolom geographic

1. **Map** visual
2. Location: `Kota`
3. Bubble size: `Total`

---

## 6. DAX — Data Analysis eXpressions

DAX = formula language Power BI. Mirip Excel formula tapi lebih powerful.

### 6.1 Measure vs Calculated Column

- **Calculated Column** — dihitung per row, store di table (ambil disk space)
- **Measure** — dihitung saat query, dynamic per context

**Best practice DA:** prefer **Measure** untuk metric (total, ratio, %), pakai **Calculated Column** cuma untuk attribute (kategori, flag).

### 6.2 Bikin Measure

Klik kanan tabel → **New Measure**:

```dax
Total Revenue = SUM(transaksi[total])
```

Drag measure ini ke chart.

### 6.3 DAX Functions Sering Dipakai

```dax
-- Aggregation
Total Revenue = SUM(transaksi[total])
Avg Order Value = AVERAGE(transaksi[total])
Customer Count = DISTINCTCOUNT(transaksi[id_pelanggan])

-- Conditional
Big Customer = COUNTROWS(FILTER(transaksi, transaksi[total] > 100000))

-- Time intelligence
Sales YTD = TOTALYTD([Total Revenue], transaksi[tanggal])
Sales MoM = [Total Revenue] - CALCULATE([Total Revenue], DATEADD(transaksi[tanggal], -1, MONTH))

-- % of total
% of Total = DIVIDE([Total Revenue], CALCULATE([Total Revenue], ALL(transaksi)))
```

### 6.4 DAX Common Patterns

```dax
-- Top N
Rank Sales = RANKX(ALL(transaksi[id_menu]), [Total Revenue], , DESC)

-- Conditional measure
High Value Customer = IF([Customer Total Revenue] > 1000000, "Yes", "No")

-- Year-over-year
YoY Growth = DIVIDE([Total Revenue] - [Total Revenue Last Year], [Total Revenue Last Year])
```

---

## 7. Relationship — Multiple Tables

Skenario: `transaksi`, `menu`, `cabang`, `pelanggan` dimuat sebagai 4 table. Kamu mau bisa filter chart `transaksi` by `kategori` (yang ada di `menu`).

1. View → **Model**
2. Drag `id_menu` di `transaksi` → ke `id_menu` di `menu` — bikin garis relationship
3. Tipe: Many-to-One (transaksi → menu)
4. Sekarang field di `menu` (kategori, harga) bisa dipakai filter chart `transaksi`

> **Catatan:** Power BI default auto-detect relationship. Tapi sering perlu di-fix manual untuk akurasi.

---

## 8. Publish

1. **File → Publish → Publish to Power BI Service** (butuh akun Power BI Pro untuk public sharing)
2. Atau: **Save** sebagai `.pbix` file → kirim manual

> **Power BI Service free** punya limitation untuk public sharing. Untuk portfolio, **screenshot dashboard** lebih praktis daripada link.

---

## 9. Latihan

Bikin 1 dashboard di Power BI dengan dataset Kopi Kita atau Olist. Detail di `latihan/soal.md`.

🎯 **Sertifikasi target:** [Microsoft PL-300 (Power BI Data Analyst Associate)](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/) — kalau target karir di banking/korporat tradisional Indonesia.

---

## Apa Selanjutnya?

Lanjut **Day 2 PM — Looker Studio** (third BI tool, gratis selamanya).

---

**Akhir Day 2 AM · Week 4**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Power BI vs Tableau (kapan pakai apa)
- UI tour (Report, Data, Model views)
- Get Data + Power Query
- Build visuals (Card, Bar, Line, Slicer, Map)
- DAX (measure vs calculated column, common functions)
- Relationships antar table

~3 jam · materi.md + latihan

🎯 Sertifikasi target: Microsoft PL-300

⚠️ Windows only. Mac users skip atau pakai VM.

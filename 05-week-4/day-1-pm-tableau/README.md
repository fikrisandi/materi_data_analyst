# Week 4 · Day 1 PM
# Tableau Public — Build Your First Dashboard

> **Tujuan:** Setelah modul ini kamu punya akun Tableau Public, paham UI Tableau Desktop, dan sudah bikin 1 dashboard interactive yang di-publish public.
>
> **Estimasi:** 3 jam.

---

## 1. Tableau — Apa & Kenapa Belajar?

**Tableau** = BI tool paling populer untuk **data storytelling visual**. Dipakai di banyak unicorn Indonesia (Tokopedia, GoTo, Traveloka).

**Strength Tableau:**
- Drag-and-drop interface, tidak perlu coding
- Visualization stunning out of the box
- Tableau Public = free hosting dashboard publik (bagus untuk portfolio)
- Tableau Desktop Specialist = sertifikasi resmi yang diakui industri

**Weakness:**
- Tableau Desktop full version berbayar (~70 USD/month)
- Tableau Public dashboard **public** (semua orang bisa lihat) — tidak cocok untuk data confidential
- Calculation kompleks butuh learn LOD expression

---

## 2. Setup Tableau Public

1. Sign up di [public.tableau.com](https://public.tableau.com) — gratis selamanya
2. Download **Tableau Public Desktop** (gratis, OS Windows/Mac)
3. Install & buka

> **[GAMBAR DIPERLUKAN — Tableau Public Welcome Screen]**
> **Apa:** screenshot Tableau Public Desktop pertama kali kebuka — Connect panel di kiri.
> **Konteks:** orientasi peserta sebelum mulai.

---

## 3. UI Tour — 30 Detik

```
┌─────────────────────────────────────────────────────────────────┐
│ FILE  DATA  ANALYSIS  MAP  FORMAT  SERVER  WINDOW  HELP         │
├──────────────────────┬──────────────────────────────────────────┤
│ DATA PANE (kiri)     │  CANVAS (tengah)                         │
│ ─────────────────    │                                          │
│ ▼ Dimensions          │  Drop Field Here                          │
│   • Cabang           │  [chart akan render di sini]            │
│   • Tanggal          │                                          │
│ ▼ Measures           │                                          │
│   • Total            │                                          │
│   • Qty              │                                          │
│                      │                                          │
├──────────────────────┴──────────────────────────────────────────┤
│ MARKS CARD (kiri-bawah)                                         │
│ Color | Size | Label | Detail | Tooltip                         │
└─────────────────────────────────────────────────────────────────┘
```

Konsep kunci:
- **Dimensions** (kategori) → biasanya jadi sumbu / color
- **Measures** (numeric) → biasanya jadi value / size
- **Marks** = visual element (bar, line, dot)

---

## 4. Connect ke Data

Tableau Public bisa connect ke:
- **Excel** (.xlsx) — paling sering untuk learning
- **CSV**
- **Google Sheets**
- **PDF tables**

> **Tableau Public TIDAK BISA** connect ke database server (PostgreSQL, MySQL). Hanya Tableau Desktop (paid) yang bisa.

### Workflow

1. Klik **Connect** → **Microsoft Excel**
2. Pilih `data/kopi_kita.xlsx` (export dari SQLite kita ke xlsx dulu, atau export Pandas DataFrame)
3. Tableau load dataset, tampilkan preview di tab Data Source

---

## 5. Bikin Chart Pertama — Bar Chart Revenue per Cabang

1. Klik tab **Sheet 1** di bawah
2. Drag **Cabang** (dimension) ke **Columns** shelf di atas
3. Drag **Total** (measure) ke **Rows** shelf
4. Tableau auto-bikin bar chart

Tweak:
- Drag **Cabang** ke **Color** card (warna per cabang)
- Klik **Total** di Rows → klik dropdown → **Format** → ganti format ke "Currency Custom"
- Klik **Sort** icon di toolbar → sort descending

Rename sheet jadi `01-Revenue per Cabang`.

---

## 6. Bikin 5 Chart Lebih untuk Dashboard

Bikin 5 sheet:

### Sheet 2 — Trend Revenue per Bulan
- Columns: `Tanggal` → ubah ke MONTH (klik dropdown → Month)
- Rows: `Total`
- Tipe chart: Line

### Sheet 3 — Top Menu by Revenue
- Columns: `Total`
- Rows: `Nama Menu`
- Sort descending
- Show top 10 saja

### Sheet 4 — Cabang × Kategori
- Columns: `Cabang`
- Rows: `Kategori`
- Marks: Square + Color = SUM(Total)
- Tipe chart: heatmap

### Sheet 5 — Distribusi Total Transaksi
- Columns: `Total` (binned — klik dropdown → Create Bins → size 25000)
- Rows: `Number of Records`
- Tipe chart: Histogram

### Sheet 6 — KPI Summary
- Drag `Total` ke center (auto SUM)
- Format jadi big number: "Rp 5,800,000 — Total Revenue Q1"

---

## 7. Combine ke Dashboard

1. Klik tab **New Dashboard** (icon di bawah)
2. Set size: pilih size yang sesuai (Desktop, Phone, atau Custom)
3. Drag sheet-sheet ke canvas
4. Atur layout (drag border untuk resize)
5. Tambah **Title** (Object → Text)
6. Tambah **Filter** (klik sheet → dropdown → Filter)

> **[GAMBAR DIPERLUKAN — Tableau Dashboard Final]**
> **Apa:** screenshot dashboard final dengan 6 sheet ter-arrange + title + filter.
> **Konteks:** bukti visual peserta bisa bikin dashboard.

---

## 8. Calculated Field

Untuk metric yang tidak ada di data raw:

1. Klik **Analysis → Create Calculated Field**
2. Nama: `Profit`
3. Formula: `[Total] - ([Qty] * [HPP])`
4. OK → field baru muncul di Measures

Sekarang kamu bisa drag `Profit` ke chart.

### Calculated Field Common Examples

```
// Profit margin %
([Total] - [HPP]*[Qty]) / [Total] * 100

// Year-over-Year growth
ZN(SUM([Total])) - LOOKUP(ZN(SUM([Total])), -1)

// Top N filter
RANK_DENSE(SUM([Total])) <= 10
```

---

## 9. Publish ke Tableau Public

1. **File → Save to Tableau Public As...**
2. Login dengan akun Tableau Public kamu
3. Workbook akan upload ke `public.tableau.com/profile/<username>`
4. URL bisa di-share publik

> **Tip portfolio:** copy URL Tableau Public ke `06-visualization/tableau-dashboard-link.md` di portfolio. Ini akan jadi salah satu link paling impressive di CV kamu.

---

## 10. Latihan

`latihan/soal.md` — bikin 1 dashboard 6-chart dengan dataset Kopi Kita atau Olist.

---

## Apa Selanjutnya?

Lanjut **Day 2 AM — Power BI Desktop**.

---

**Akhir Day 1 PM · Week 4**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Tableau Public sign up + Desktop install
- Connect ke Excel/CSV
- Build 6 charts: bar, line, top N, heatmap, histogram, KPI
- Combine ke Dashboard
- Calculated Fields
- Publish ke Tableau Public (gratis hosting)

~3 jam · materi.md + latihan

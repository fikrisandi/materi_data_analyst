# Week 4 · Day 2 PM
# Looker Studio — Dashboard Cloud Gratis

> **Tujuan:** Setelah modul ini kamu paham Looker Studio (formerly Google Data Studio), bisa bikin dashboard cloud gratis dari Google Sheets / BigQuery, dan paham kapan pakai Looker vs Tableau/PBI.
>
> **Estimasi:** 2.5 jam.

---

## 1. Looker Studio — Apa & Kenapa?

**Looker Studio** = BI tool cloud Google, **gratis selamanya**. Dulu namanya "Google Data Studio".

**Strength:**
- **Gratis 100%** — tidak ada paid tier
- **Cloud-native** — dashboard live online, tidak perlu desktop install
- **Native integration** dengan Google ecosystem (Sheets, BigQuery, Analytics, Ads)
- **Easy sharing** — link & embed

**Weakness:**
- Visual lebih simple dari Tableau (kurang advanced chart)
- Calculation kalah dari Power BI DAX
- Best untuk Google-centric workflow

**Kapan pakai Looker:**
- Data sumber sudah di Google (Sheets, BigQuery, GA)
- Butuh dashboard publik yang gratis & easy share
- Tim non-teknis (lebih friendly untuk pemula)

---

## 2. Setup

1. Buka [lookerstudio.google.com](https://lookerstudio.google.com)
2. Login dengan Gmail (sudah aktif otomatis)
3. Klik **Create → Report**

Selesai — tidak perlu install apa pun.

> **[GAMBAR DIPERLUKAN — Looker Studio Welcome]**
> **Apa:** screenshot home Looker Studio dengan tombol Create Report.
> **Konteks:** orientasi awal.

---

## 3. Connect Data

Looker support banyak data source:
- **Google Sheets** — paling sering untuk simple data
- **BigQuery** — untuk dataset besar
- **Google Analytics** — web analytics
- **Google Ads** — marketing performance
- **CSV upload**
- **MySQL / PostgreSQL** (via partner connector)

### Workflow

1. Add data → pilih source (misal Google Sheets)
2. Pilih spreadsheet & sheet
3. Looker auto-detect schema

---

## 4. Build Dashboard

### 4.1 Add Chart

1. Toolbar atas → klik **Add a chart**
2. Pilih tipe (Bar, Line, Scorecard, Table, dll)
3. Drag ke canvas
4. Di panel kanan, set:
   - **Dimension** (kategori/dimensi)
   - **Metric** (numeric, akan di-aggregate)
   - **Sort, filter, breakdown**

### 4.2 Common Charts di Looker

- **Scorecard** — single big number (KPI)
- **Bar / Column** — comparison
- **Line / Area** — trend
- **Pie / Donut** — composition (HATI-HATI)
- **Table** — detail view
- **Geo Map** — geographic
- **Pivot Table** — cross-tab

### 4.3 Calculated Field

Right panel → **Add a Field**:

```
// Profit
total - (qty * hpp)

// Profit Margin %
(total - qty * hpp) / total * 100

// Conditional
CASE
    WHEN total >= 100000 THEN "Besar"
    WHEN total >= 50000 THEN "Sedang"
    ELSE "Kecil"
END
```

Syntax mirip SQL CASE.

---

## 5. Interactivity

### 5.1 Date Range Control

Drag **Date Range Control** ke canvas. User bisa pilih periode → semua chart auto-filter.

### 5.2 Filter Control

Drag **Filter Control** → pilih dimension (misal Cabang). User bisa multi-select untuk filter dashboard.

### 5.3 Drill Down

Set hierarchy di chart settings: misal `Tahun → Kuartal → Bulan → Minggu`. User bisa drill down dengan klik.

---

## 6. Sharing

1. Klik **Share** di pojok kanan atas
2. Set permission:
   - **Anyone with link** — public
   - **Anyone in your organization** — internal
   - **Specific people** — by email
3. Copy link → paste di portfolio

> **Tip portfolio:** dashboard Looker punya URL `lookerstudio.google.com/reporting/<ID>`. Copy ke `06-visualization/looker-dashboard-link.md` di portfolio repo.

---

## 7. Embedding

Looker dashboard bisa di-embed di portofolio website kamu (kalau punya):

```html
<iframe
  src="https://lookerstudio.google.com/embed/reporting/<ID>"
  width="100%"
  height="600"
  frameborder="0">
</iframe>
```

---

## 8. Latihan

`latihan/soal.md` — bikin 1 dashboard Looker dari Google Sheets export Kopi Kita.

---

## Apa Selanjutnya?

Lanjut **Day 3 AM — Data Storytelling**.

---

**Akhir Day 2 PM · Week 4**
*Savvys Education · 2026*

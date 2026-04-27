# Week 4 · Day 1 AM
# Data Visualization Principles

> **Tujuan:** Setelah modul ini kamu paham prinsip dasar visualization (kapan pakai chart apa), bisa identify chart yang misleading, dan paham 5 prinsip Tufte/Cleveland untuk visualisasi efektif.
>
> **Estimasi:** 2.5 jam.

---

## 1. Mengapa Visualization Penting?

DA bisa punya analisis paling akurat di dunia, tapi kalau tidak bisa **komunikasikan ke stakeholder** — analisis itu tidak akan jadi keputusan.

Visualization yang baik:
- **Reduce time-to-insight** — stakeholder paham dalam 5 detik, bukan 5 menit
- **Highlight pattern** yang sulit terlihat di tabel
- **Reduce ambiguity** — angka 50,000 + 60,000 vs bar chart yang langsung visual
- **Memorable** — manusia ingat gambar lebih lama dari angka

> **Pesan utama:** Visualization bukan dekorasi. Visualization = **alat untuk reasoning** & **alat untuk persuade**.

---

## 2. Anatomi Chart yang Baik

Setiap chart punya:
1. **Title** — pertanyaan yang dijawab atau insight yang disampaikan
2. **Axes** — labeled clear (apa unit, apa range)
3. **Data marks** — bar, line, dot, dll yang represent data
4. **Annotations** — label atau highlight area penting
5. **Source** — dari mana data, kapan periode

### Title Pattern

❌ "Sales Q1 2026" (deskriptif, ambigu)
✅ "Sales Q1 2026 down 12% from Q4 2025, dipicu drop di kategori snack"

Title yang baik = **mini insight statement**, bukan caption neutral.

---

## 3. Chart Selection Guide

### 3.1 Comparison

| Use Case | Chart |
|---|---|
| Bandingkan kategori (5-10 item) | **Bar / Column chart** |
| Bandingkan kategori (banyak item) | **Horizontal bar** (label muat) |
| Bandingkan 2 kategori dimensions | **Grouped / Stacked bar** |
| Bandingkan progress vs target | **Bullet chart** |

### 3.2 Trend over Time

| Use Case | Chart |
|---|---|
| Trend 1 metric | **Line chart** |
| Trend 2-5 metric | **Multi-line** |
| Volume + trend | **Combo (bar + line)** |
| Distribusi over time | **Stacked area** |

### 3.3 Composition / Part-to-Whole

| Use Case | Chart |
|---|---|
| 2-5 kategori, simple | **Pie chart** (HATI-HATI — sering misleading) |
| 5+ kategori | **Bar (sorted desc)** atau **Treemap** |
| Detail breakdown | **Stacked bar / Stacked area** |

> ⚠️ **Pie chart**: hindari kalau >5 kategori atau angka mirip — manusia susah bandingkan luas.

### 3.4 Distribution

| Use Case | Chart |
|---|---|
| Distribusi 1 variabel kontinu | **Histogram** |
| Distribusi + outlier | **Box plot** |
| Distribusi 2 variabel | **Scatter plot** |
| Distribusi banyak grup | **Violin plot** |

### 3.5 Relationship

| Use Case | Chart |
|---|---|
| 2 numeric variables | **Scatter plot** |
| 2 numeric + 1 categorical | **Scatter dengan color** |
| Correlation matrix | **Heatmap** |

### 3.6 Geographic

| Use Case | Chart |
|---|---|
| Distribusi per region | **Choropleth map** |
| Density / point | **Bubble map** |

---

## 4. Chart Anti-pattern

### 4.1 Pie Chart with Many Slices
❌ 12 slice pie chart — manusia nggak bisa bandingkan 12 sudut.
✅ Bar chart sorted descending.

### 4.2 3D Chart Tanpa Alasan
❌ 3D bar chart yang bikin distorsi visual.
✅ 2D flat bar chart.

### 4.3 Y-axis Yang Terpotong (Truncated)
Bar chart dengan Y-axis mulai dari 80% (bukan 0) bikin perbedaan kecil tampak besar. Kadang ini disengaja untuk **manipulasi**.
✅ Kalau pakai truncated axis, **highlight di label** bahwa axis tidak start dari 0.

### 4.4 Dual Y-axis Tanpa Kejelasan
2 line chart dengan 2 Y-axis berbeda — bingung mana berhubungan dengan mana.
✅ Kalau perlu compare, pakai **secondary chart** terpisah.

### 4.5 Rainbow Color
Warna pelangi tanpa makna — bikin chart sulit dibaca.
✅ Pakai **categorical palette** (warna distinct) atau **sequential palette** (gradient untuk ordered data).

---

## 5. Prinsip Tufte / Cleveland

### Edward Tufte — "Data-Ink Ratio"
**Tingkatkan data-ink, kurangi non-data-ink.**

- Buang gridlines yang tidak perlu
- Buang border yang heavy
- Buang ornament 3D
- Hilangkan legend kalau bisa pakai direct label

### William Cleveland — "Perception Hierarchy"
Dari paling **akurat** dipersepsi mata manusia ke paling **buruk**:

```
1. Position on common scale          (bar, scatter)  ← paling akurat
2. Position on same scale (different X)
3. Length
4. Angle / slope
5. Area
6. Volume / curvature
7. Color hue / saturation             ← paling buruk
```

**Implikasi:** bar chart > pie chart (length > angle). Scatter > heatmap (position > color).

---

## 6. Color Strategy

### 6.1 Categorical (kategori distinct)
Pakai **ColorBrewer Set2** atau **Viridis discrete**: warna berbeda untuk kategori berbeda. Hindari pakai >7 warna — orang tidak bisa membedakan.

### 6.2 Sequential (ordered, low to high)
Pakai **gradient single-hue**: light → dark biru, atau light → dark hijau.

### 6.3 Diverging (negative → 0 → positive)
Pakai **2 hue dengan netral di tengah**: red → white → blue.

### 6.4 Accessibility
~5% pria buta warna. Hindari pakai **merah & hijau** sebagai kontras utama. Pakai colorbrewer "colorblind safe" palette.

> **Tools:** [colorbrewer2.org](https://colorbrewer2.org) — pilih palette yang colorblind safe + print friendly.

---

## 7. Visualisasi di Python (Quick Recap)

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Style
sns.set_theme(style="whitegrid")

# Bar chart
df.groupby("kategori")["revenue"].sum().plot(kind="bar", title="Revenue per Kategori")

# Line chart
df.groupby("bulan")["revenue"].sum().plot(kind="line", marker="o")

# Histogram
df["total"].hist(bins=30)

# Scatter
df.plot.scatter(x="qty", y="total")

# Box plot
df.boxplot(column="total", by="cabang")

# Heatmap (correlation)
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

plt.tight_layout()
plt.savefig("chart.png", dpi=150)
plt.show()
```

---

## 8. Latihan

`latihan/soal.md` — analisis dataset Kopi Kita, bikin 6 chart proper dengan title yang **insight-driven** + 1 chart yang **misleading** (untuk practice identify).

---

## Apa Selanjutnya?

Lanjut **Day 1 PM — Tableau Public hands-on**.

> **Tip:** sebelum sesi PM, sign up [Tableau Public](https://public.tableau.com) (gratis) — install desktop app sekalian.

---

**Akhir Day 1 AM · Week 4**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Anatomi chart yang baik
- Chart selection (comparison, trend, composition, distribution, relationship, geographic)
- Anti-pattern (pie 12-slice, truncated Y, dual axis, rainbow)
- Prinsip Tufte (data-ink ratio) & Cleveland (perception hierarchy)
- Color strategy (categorical, sequential, diverging, accessibility)

~2.5 jam · materi.md + latihan

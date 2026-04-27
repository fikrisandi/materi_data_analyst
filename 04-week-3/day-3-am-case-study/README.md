# Week 3 · Day 3 AM
# Case Study — End-to-End Analytics Project

> **Tujuan:** Aplikasi semua skill Week 1-3 ke 1 case bisnis besar. Output: notebook + insight + rekomendasi.
>
> **Estimasi:** 3 jam (kerja mandiri).

---

## 1. Brief Case

### Konteks
Kamu data analyst di **Tokopedia (fiktif)** — divisi **Marketplace Analytics**. Director Marketplace minta analisis sales data 2024 untuk persiapan strategy 2025.

### Dataset

Pakai **Kaggle dataset** publik: ["Brazilian E-Commerce Public Dataset by Olist"](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (atau dataset e-commerce serupa).

Download dan extract ke `data/`. Dataset berisi 9 file CSV:
- orders, order_items, products, customers, sellers, payments, reviews, geolocation, category translation

### Pertanyaan

Director ingin tahu:
1. **Sales Performance** — total revenue, jumlah order, AOV (Average Order Value) per kategori produk per kuartal
2. **Customer Geography** — region mana yang paling kontribusi? Ada perbedaan behavior per region?
3. **Payment Behavior** — distribusi metode bayar; apakah ada pengaruh ke order value?
4. **Product Quality** — kategori mana yang **rating-nya rendah** padahal volume tinggi (red flag)?
5. **Delivery Performance** — average delivery time per region; pengaruh ke rating?
6. **Recommendations** — 3 actionable initiative untuk 2025

---

## 2. Workflow yang Disarankan

### Step 1 — Data Loading & Cleaning (45 min)
- Load 9 CSV ke pandas
- Cek shape, dtypes, missing values
- Convert date columns
- Handle missing data
- Bikin master DataFrame dengan join yang relevan

### Step 2 — Exploratory Data Analysis (60 min)
- Deskriptif per variabel kunci
- Distribusi order_value, rating, delivery_time
- Identify outlier

### Step 3 — Answer 6 Pertanyaan (75 min)
- Jawab tiap pertanyaan dengan SQL/Pandas
- Visualisasi untuk pertanyaan 1, 2, 5

### Step 4 — Statistical Test (30 min)
- Apakah perbedaan delivery time per region significant?
- Apakah rating berkorelasi dengan delivery time?

### Step 5 — Recommendations (30 min)
- Tulis 3 inisiatif actionable
- Setiap initiative: insight pendukung + expected impact

---

## 3. Output yang Diharapkan

```
05-statistics-case/case-study-w3/
├── README.md           ← brief case + ringkasan finding
├── notebook.ipynb      ← analisis lengkap
├── data/               ← CSV files (kalau kecil) atau link Kaggle
├── images/             ← plots di-export
└── recommendations.md  ← 3 inisiatif konkret
```

## 4. Rubrik Penilaian

- **Data Cleaning** — handle missing & outlier dengan justifikasi (15%)
- **EDA** — kedalaman eksplorasi (15%)
- **Insight Quality** — bukan cuma report, ada interpretasi bisnis (30%)
- **Visualisasi** — proper chart (10%)
- **Statistical Rigor** — pakai test yang tepat (15%)
- **Recommendations** — actionable, ada expected impact (15%)

## 5. Submission

Push ke `05-statistics-case/case-study-w3/` portfolio dengan `git push`.

---

**Akhir Day 3 AM · Week 3**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- End-to-end analytics project
- Dataset: Olist Brazilian E-Commerce (Kaggle)
- 6 business questions + 3 recommendations
- Workflow: clean → EDA → analyze → test → recommend

~3 jam kerja mandiri · materi.md (brief)

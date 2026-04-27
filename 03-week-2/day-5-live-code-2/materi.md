# Week 2 · Day 5
# Live Code 2 & Recap Week 2

> **Tujuan:** Konsolidasi Week 2 dengan live coding integrasi Python + Pandas + SQL Advanced. Persiapan Week 3 (Scraping/API).
>
> **Durasi:** ~3 jam.

---

## 1. Recap Week 2

```
Day 1 AM   Python Basics (var, types, list, dict)        ✓
Day 1 PM   Conditions & Loops                            ✓
Day 2 AM   Functions & Modules                           ✓
Day 2 PM   OOP intro & Debugging                         ✓
Day 3 AM   Pandas Intro (DataFrame, Series, basic)       ✓
Day 3 PM   Pandas Wrangling (groupby, merge, pivot)      ✓
Day 4 AM   SQL Advanced (Window, CTE, Subquery, PG)      ✓
Day 4 PM   BigQuery Hands-On (NYC Taxi, COVID, GA)       ✓
Day 5      → Live Code & Recap (kamu di sini)
```

Skill yang sudah kamu kuasai sekarang:
- Apply Junior DA → Mid DA junior level
- Selesaikan **HackerRank SQL Intermediate Skills Certification**
- Jawab sebagian soal interview SQL (DataLemur Easy & Medium)
- Pull data dari multiple source (file, SQL, API simple) dan analisis end-to-end

---

## 2. Live Code Challenge — Customer Lifetime Value (CLV) Analysis

Skenario business yang umum di e-commerce: **Customer Lifetime Value** = total value yang diperkirakan dari 1 pelanggan selama hidupnya sebagai customer kita.

### Setup

Pakai PostgreSQL (atau SQLite) `kopi_kita`. Mentor demo step-by-step.

### Step 1 — Pull Data via SQL

```sql
WITH customer_metrics AS (
    SELECT
        p.id_pelanggan,
        p.nama,
        p.membership,
        p.tanggal_join,
        COUNT(t.id_transaksi) AS frequency,
        SUM(t.total) AS total_revenue,
        AVG(t.total) AS avg_order,
        MAX(t.tanggal) AS last_visit,
        MIN(t.tanggal) AS first_visit
    FROM pelanggan p
    LEFT JOIN transaksi t ON p.id_pelanggan = t.id_pelanggan
    GROUP BY p.id_pelanggan, p.nama, p.membership, p.tanggal_join
)
SELECT * FROM customer_metrics
ORDER BY total_revenue DESC NULLS LAST;
```

### Step 2 — Pindah ke Python untuk Analisis Lebih Dalam

```python
import pandas as pd
import sqlite3
from datetime import datetime

conn = sqlite3.connect("data/kopi_kita.db")
df = pd.read_sql("""
    -- query CTE di atas
""", conn)
conn.close()

# Convert dates
df["tanggal_join"] = pd.to_datetime(df["tanggal_join"])
df["last_visit"] = pd.to_datetime(df["last_visit"])
df["first_visit"] = pd.to_datetime(df["first_visit"])

# Compute recency (days since last visit)
df["recency_days"] = (pd.Timestamp("2026-04-01") - df["last_visit"]).dt.days

# Customer tenure
df["tenure_days"] = (pd.Timestamp("2026-04-01") - df["tanggal_join"]).dt.days
```

### Step 3 — RFM Segmentation

**RFM** = Recency (kapan terakhir transaksi), Frequency (berapa sering), Monetary (total spend). Framework klasik untuk customer segmentation.

```python
# Score 1-5 per dimensi (5 = best)
df["R_score"] = pd.qcut(df["recency_days"], 5, labels=[5, 4, 3, 2, 1])  # smaller days = better
df["F_score"] = pd.qcut(df["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
df["M_score"] = pd.qcut(df["total_revenue"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])

# Combine
df["RFM_score"] = df["R_score"].astype(str) + df["F_score"].astype(str) + df["M_score"].astype(str)

# Segment
def segment(row):
    if row["R_score"] >= 4 and row["F_score"] >= 4:
        return "Champion"
    elif row["R_score"] >= 3 and row["F_score"] >= 3:
        return "Loyal"
    elif row["R_score"] >= 4:
        return "New Customer"
    elif row["R_score"] <= 2 and row["F_score"] >= 3:
        return "At Risk"
    else:
        return "Hibernating"

df["segment"] = df.apply(segment, axis=1)
```

### Step 4 — Insight & Visualisasi

```python
# Distribusi segment
seg_summary = df.groupby("segment").agg(
    jumlah=("id_pelanggan", "count"),
    total_revenue=("total_revenue", "sum"),
    avg_revenue=("total_revenue", "mean"),
).reset_index()

print(seg_summary)

# Plot
import matplotlib.pyplot as plt
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
seg_summary.plot(x="segment", y="jumlah", kind="bar", ax=axes[0], title="Customer Count per Segment")
seg_summary.plot(x="segment", y="total_revenue", kind="bar", ax=axes[1], title="Revenue per Segment")
plt.tight_layout()
plt.show()
```

---

## 3. Drill 30 Menit (Mandiri)

5 challenge dengan dataset Kopi Kita. Selesaikan satu yang paling resonate:

1. **Cohort Analysis** — pelanggan yang join Januari 2026, retention rate-nya gimana di Februari & Maret?
2. **Menu Pareto** — 20% menu kontribusi berapa % revenue?
3. **Predict Top Spender** — pelanggan dengan ciri apa yang biasanya jadi top spender?
4. **Churn Risk** — pelanggan yang **tidak transaksi 30 hari terakhir** padahal sebelumnya aktif → tag sebagai "Risk Churn"
5. **Cabang Comparison Deep Dive** — apa yang bikin Cabang Tebet beda secara metric dengan Dago?

---

## 4. Persiapan Week 3

Week 3 mulai topik baru:
- **Web Scraping** — fetch data dari website yang tidak punya API
- **API** — fetch data dari REST API (BPS, Twitter, OpenWeather, dll)
- **Statistics Inferential** — hypothesis testing, A/B testing
- **Business Knowledge** — funnel, cohort, North Star Metric

Cek setup:

```bash
conda activate savvys-da
python -c "import requests, bs4; print('OK')"
# kalau error: pip install requests beautifulsoup4
```

---

## Apa Selanjutnya?

✅ **Week 2 selesai.** Selamat — kamu sekarang punya skill Python + Pandas + SQL Advanced + BigQuery yang setara DA Junior level.

```bash
cd ~/savvys-da-kursus/portfolio
git add . && git commit -m "Week 2 complete" && git push
```

Buka folder `04-week-3/day-1-am-web-scraping/` — sampai jumpa Senin pagi!

---

**Akhir Week 2**
*Savvys Education · 2026*

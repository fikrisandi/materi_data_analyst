# Week 3 · Day 4 — Live Code 3 & Recap Week 3

> **Tujuan:** Konsolidasi Week 3 + persiapan Week 4 Capstone.
>
> **Durasi:** 3 jam.

---

## 1. Recap Week 3

```
Day 1 AM   Web Scraping (BeautifulSoup, etika)              ✓
Day 1 PM   API (REST, auth, BPS, OpenWeather)               ✓
Day 2 AM   Business Knowledge (KPI, funnel, cohort, NSM)    ✓
Day 2 PM   Statistics Inferential (hypothesis, A/B test)    ✓
Day 3 AM   Case Study (E-commerce dataset)                  ✓
Day 3 PM   Mentoring                                        ✓
Day 4      → Live Code & Recap (kamu di sini)
```

Skill complete sekarang:
- Apply Mid-level DA (untuk fresh graduate / transisi karir entry-mid)
- Selesaikan **Forage Virtual Internship** (BCG / Accenture / KPMG)
- Selesaikan **DataLemur Easy + 50% Medium**
- Pull data dari multiple source (DB, API, scraping) → analyze → recommend

---

## 2. Live Code Challenge — Mini Marketing Funnel Analysis

### Skenario

Bayangkan startup edutech "Belajar Bareng" — punya funnel:
```
1. Visit homepage      → 50,000 unique visitors/bulan
2. Sign up free trial  → 5,000
3. Activate (pakai 1x) → 2,000
4. Convert to paid     → 400
```

### Step 1 — Generate Synthetic Data

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

n_users = 50000
users = pd.DataFrame({
    "user_id": range(1, n_users + 1),
    "signup_date": [datetime(2026, 1, 1) + timedelta(days=int(d)) for d in np.random.randint(0, 90, n_users)],
    "channel": np.random.choice(["Organic", "Paid Social", "Email", "Referral"], n_users, p=[0.4, 0.3, 0.2, 0.1]),
})

# Simulate funnel
users["signed_up"] = np.random.binomial(1, 0.10, n_users).astype(bool)
users["activated"] = users["signed_up"] & np.random.binomial(1, 0.40, n_users).astype(bool)
users["converted"] = users["activated"] & np.random.binomial(1, 0.20, n_users).astype(bool)
```

### Step 2 — Funnel Visualization

```python
funnel = pd.Series({
    "Visit": len(users),
    "Sign up": users["signed_up"].sum(),
    "Activate": users["activated"].sum(),
    "Convert": users["converted"].sum(),
})

import matplotlib.pyplot as plt
funnel.plot(kind="bar", title="Conversion Funnel — Belajar Bareng Q1 2026")
plt.ylabel("Users")
plt.show()
```

### Step 3 — Funnel per Channel

```python
funnel_per_channel = users.groupby("channel").agg(
    total_visit=("user_id", "count"),
    sign_up=("signed_up", "sum"),
    activate=("activated", "sum"),
    convert=("converted", "sum"),
)

# Pct conversion
funnel_per_channel["pct_signup"] = funnel_per_channel["sign_up"] / funnel_per_channel["total_visit"] * 100
funnel_per_channel["pct_convert"] = funnel_per_channel["convert"] / funnel_per_channel["total_visit"] * 100

print(funnel_per_channel)
```

**Insight yang muncul:**
- Channel mana yang **acquisition tinggi** tapi **conversion rendah**? (waste budget)
- Channel mana yang **conversion tinggi**? (double down)

### Step 4 — A/B Test Sintetik

```python
from statsmodels.stats.proportion import proportions_ztest

# Imagine: layout B vs A
# A (control): 5000 visit, 250 convert (5%)
# B (treatment): 5000 visit, 320 convert (6.4%)

count = [250, 320]
nobs = [5000, 5000]

z, p = proportions_ztest(count, nobs)
print(f"z={z:.3f}, p={p:.4f}")

if p < 0.05:
    print("Significant lift! Ship layout B.")
```

---

## 3. Drill 30 Menit (Mandiri)

Pakai dataset Olist (atau Kopi Kita), pilih 1 challenge:

1. **Cohort retention curve** — plot retention curve untuk pelanggan yang first transaksi Jan vs Feb vs Mar
2. **A/B test simulasi** — bagi pelanggan 50/50, hitung apakah lift "fake" >5% would be detectable
3. **Customer segmentation** — pakai RFM, identify "Champion" segment, hitung % dari total customer & % dari total revenue

---

## 4. Persiapan Week 4 — Capstone

Week 4 = **capstone project final**. Yang dibutuhkan:

- Tableau Public account (gratis)
- Power BI Desktop installed (gratis untuk Windows)
- Looker Studio aktif (sudah ada Gmail = otomatis aktif)
- 1 dataset capstone (akan dikasih day 1)

```bash
conda activate savvys-da
python -c "import matplotlib, seaborn; print('OK')"
```

---

## Apa Selanjutnya?

✅ **Week 3 selesai.**

```bash
cd ~/savvys-da-kursus/portfolio
git add . && git commit -m "Week 3 complete" && git push
```

Buka folder `05-week-4/day-1-am-data-viz/` — minggu terakhir, capstone time!

---

**Akhir Week 3**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Recap Week 3
- Live demo: Marketing Funnel Analysis + A/B test sintetik
- Drill mandiri: cohort, A/B, RFM segmentation
- Persiapan Week 4 (Capstone)

~3 jam · materi.md

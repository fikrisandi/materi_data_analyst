# Week 3 · Day 2 AM
# Business Knowledge — KPI, Funnel, Cohort, North Star Metric

> **Tujuan:** Setelah modul ini kamu paham framework bisnis yang umum di DA: KPI design, conversion funnel, cohort analysis, dan North Star Metric. Skill ini yang **membedakan DA biasa dari DA strategic**.
>
> **Estimasi:** 3 jam.

---

## 1. Mengapa Business Knowledge Penting?

DA pemula sering jago **teknikal** (SQL, Python) tapi lemah di **konteks bisnis**. Hasilnya: laporan akurat tapi **tidak actionable**.

Contoh:
- DA junior: "Revenue Q1 = 5 juta, naik 12% dari Q4."
- DA strategic: "Revenue naik 12% **dari Q4** — angka bagus di permukaan, tapi acquisition cost juga naik 18%, jadi **Customer Acquisition Cost (CAC) sebenarnya naik faster than revenue per user**. Implikasi: pertumbuhan tidak sustainable kalau pola ini lanjut."

Bedanya: **business knowledge**.

---

## 2. KPI — Key Performance Indicator

### 2.1 Apa itu KPI?

**KPI** = metric yang **mengukur seberapa baik bisnis berjalan**. Dipilih sengaja, bukan random.

### 2.2 SMART Framework untuk Pilih KPI

KPI yang baik harus **SMART**:
- **S**pecific — jelas apa yang diukur (bukan "engagement", tapi "DAU = Daily Active User")
- **M**easurable — bisa dihitung dari data
- **A**ctionable — kalau angka turun, tim tahu apa yang harus dilakukan
- **R**elevant — terkait dengan tujuan bisnis
- **T**ime-bound — periode jelas (harian/mingguan/bulanan)

### 2.3 Vanity Metric vs Actionable Metric

❌ **Vanity metric** — nice to look at, tapi tidak actionable:
- "Total signup"
- "Total page view"
- "Follower social media"

✅ **Actionable metric** — drive decision:
- "Activation rate" (% signup yang complete onboarding)
- "Retention D7" (% user yang masih aktif 7 hari setelah signup)
- "Conversion rate signup → paid"

### 2.4 KPI Hierarchy — Output, Outcome, Impact

```
INPUT (effort)        →    OUTPUT (immediate)    →    OUTCOME (behavior)    →    IMPACT (business value)
─────────────────         ────────────────────         ─────────────────         ──────────────────────
Marketing budget          Total ad impression          Click-through            Revenue from new user
Engineering hours         Features shipped             Daily active user        Retention rate
Customer support cost     Tickets resolved             NPS score                Renewal rate
```

> **Tip:** kalau perusahaan kamu fokus ke **input/output**, kamu mungkin track effort. Kalau fokus ke **outcome/impact**, kamu mengarah ke business value. Yang ke-2 lebih strategic.

---

## 3. Conversion Funnel

**Funnel** = serangkaian step yang user lewati dari awal sampai konversi (purchase, signup, dll).

### Skenario E-commerce

```
1. Visit homepage          100,000 user
2. Browse product            40,000 user (40%)
3. Add to cart               12,000 user (30% dari step 2)
4. Checkout start             4,800 user (40% dari step 3)
5. Complete purchase          3,000 user (62.5% dari step 4)

Final conversion rate: 3,000 / 100,000 = 3%
```

### Cara Analisis Funnel di SQL

```sql
WITH funnel AS (
    SELECT
        user_id,
        MAX(CASE WHEN event = 'visit_homepage' THEN 1 ELSE 0 END) AS step1,
        MAX(CASE WHEN event = 'browse_product' THEN 1 ELSE 0 END) AS step2,
        MAX(CASE WHEN event = 'add_to_cart' THEN 1 ELSE 0 END) AS step3,
        MAX(CASE WHEN event = 'checkout_start' THEN 1 ELSE 0 END) AS step4,
        MAX(CASE WHEN event = 'purchase_complete' THEN 1 ELSE 0 END) AS step5
    FROM events
    WHERE date BETWEEN '2026-01-01' AND '2026-01-31'
    GROUP BY user_id
)
SELECT
    SUM(step1) AS total_visit,
    SUM(step2) AS total_browse,
    SUM(step3) AS total_cart,
    SUM(step4) AS total_checkout,
    SUM(step5) AS total_purchase
FROM funnel;
```

### Insight dari Funnel

**Drop-off paling besar** = bottleneck. Fokus optimasi di sana.

Di contoh atas: drop-off terbesar di step 1→2 (60% drop). Mungkin homepage tidak menarik. **Fix homepage = highest leverage**.

---

## 4. Cohort Analysis

**Cohort** = grup user yang punya karakteristik sama (biasanya **kapan signup/first purchase**).

**Cohort Analysis** = lihat behavior cohort over time — apakah cohort baru lebih retain dari cohort lama? Apakah feature yang launched bulan ini bantu retention?

### Skenario: Retention Cohort

| Cohort signup | Month 0 | Month 1 | Month 2 | Month 3 |
|---|---|---|---|---|
| Jan 2026  | 100% | 60%  | 45%  | 38%  |
| Feb 2026  | 100% | 65%  | 50%  | 42%  |
| Mar 2026  | 100% | 70%  | 55%  | -    |
| Apr 2026  | 100% | 72%  | -    | -    |

**Reading:**
- Month 1 retention naik dari 60% (Jan) → 72% (Apr) → improvement!
- Apa yang berubah? Mungkin feature baru, onboarding redesign, atau marketing channel yang lebih qualified.

### SQL Pattern

```sql
WITH first_purchase AS (
    SELECT user_id, DATE_TRUNC(MIN(date), MONTH) AS cohort_month
    FROM transactions
    GROUP BY user_id
),
activity AS (
    SELECT
        fp.cohort_month,
        DATE_DIFF(t.date, fp.cohort_month, MONTH) AS months_since,
        COUNT(DISTINCT t.user_id) AS active_users
    FROM transactions t
    JOIN first_purchase fp ON t.user_id = fp.user_id
    GROUP BY 1, 2
)
SELECT * FROM activity ORDER BY cohort_month, months_since;
```

---

## 5. North Star Metric

**North Star Metric** = **1 metric tunggal** yang representasi **value yang perusahaan deliver ke customer**. Semua tim align ke metric ini.

### Contoh

| Perusahaan | North Star |
|---|---|
| Spotify | Total music listening time |
| Airbnb | Nights booked |
| Netflix | Hours watched |
| Uber | Rides completed |
| Tokopedia | GMV (Gross Merchandise Value) |

### Karakteristik North Star yang Baik

- **Reflect customer value** — bukan "revenue", tapi "value yang customer dapat" yang akhirnya jadi revenue
- **Leading indicator** — bukan lagging (revenue itu lagging)
- **Measurable & trackable** — bisa di-update harian
- **Universal** — tim apa pun bisa kontribusi naikin metric ini

### North Star vs KPI Tim

North Star = company-level. Tim individual punya **input metric** yang kontribusi ke North Star.

```
NORTH STAR: Total music listening time (Spotify)
                │
        ┌───────┼────────┬──────────┐
   New users   Time/    Days/      Songs
   acquired    session  week       played
   (Acq team) (Eng)    (Engagement) (ML)
```

---

## 6. Common DA Frameworks Lain

### 6.1 AARRR — Pirate Metrics

Acronym untuk e-commerce / SaaS:
- **A**cquisition — dapat user (signup)
- **A**ctivation — first value moment
- **R**etention — pakai lagi
- **R**eferral — invite friend
- **R**evenue — bayar / convert

### 6.2 RFM Segmentation

(Sudah dibahas Week 2 Day 5)

### 6.3 LTV / CAC Ratio

```
LTV = Lifetime Value (total revenue dari 1 customer selama jadi customer)
CAC = Customer Acquisition Cost (biaya dapat 1 customer)

LTV / CAC > 3 → bisnis sustainable
LTV / CAC < 1 → bisnis bleeding money
```

### 6.4 Churn Rate

```
Churn Rate = (Pelanggan yang lost di periode X) / (Total pelanggan di awal periode X)
```

Untuk SaaS bagus: < 5% monthly. Untuk e-commerce: tergantung produk.

---

## 7. Latihan

`latihan/soal.md` — terapkan framework ke dataset Kopi Kita.

---

## Apa Selanjutnya?

Lanjut **Day 2 PM — Statistics Inferential** (hypothesis testing & A/B testing).

---

**Akhir Day 2 AM · Week 3**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- KPI design (SMART, vanity vs actionable)
- Conversion Funnel
- Cohort Analysis
- North Star Metric
- Frameworks: AARRR, RFM, LTV/CAC, Churn Rate

~3 jam · materi.md + latihan

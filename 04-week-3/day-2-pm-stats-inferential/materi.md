# Week 3 · Day 2 PM
# Statistics Inferential — Hypothesis Testing & A/B Testing

> **Tujuan:** Setelah modul ini kamu paham hypothesis testing (null/alternative, p-value, confidence interval), bisa baca hasil A/B test, dan paham trap statistik yang umum (multiple comparison, Simpson's paradox).
>
> **Estimasi:** 3 jam.

---

## 1. Mengapa Statistik Inferential?

Day 4 AM Week 1 kita bahas **descriptive statistics** (mean, median, std). Inferential statistics lebih jauh: **menarik kesimpulan tentang populasi dari sample**, dengan **measurement of uncertainty**.

Skenario:
- Marketing run A/B test: layout A vs B. Konversi A = 3.0%, B = 3.2%.
- Pertanyaan: B beneran lebih baik, atau **kebetulan random**?
- Stats inferential = jawab pertanyaan ini dengan **confidence level**.

---

## 2. Sample vs Population

- **Population** = semua data yang relevan (semua user, semua transaksi)
- **Sample** = subset yang kamu ukur

Kamu jarang akses 100% populasi (terlalu mahal/lambat). Kamu **sample**, lalu **infer** ke population.

```
Population: 1 juta user
   ↓ sample
Sample: 1,000 user → measure
   ↑ infer (with uncertainty)
Conclusion about population
```

---

## 3. Hypothesis Testing

### 3.1 Setup

Untuk tiap claim, definisikan 2 hypothesis:

- **Null hypothesis (H₀)** — "tidak ada efek / tidak ada beda"
- **Alternative hypothesis (H₁)** — "ada efek / ada beda"

Default kita **assume null benar** sampai bukti cukup kuat untuk reject.

### 3.2 Skenario A/B Test

Klaim: "Layout B lebih baik dari A"

- H₀: rate konversi A = rate konversi B (no difference)
- H₁: rate konversi A ≠ rate konversi B (ada difference)

### 3.3 P-Value

**P-value** = probability dari hasil yang diobservasi (atau lebih ekstrim) **kalau H₀ benar**.

- P-value **kecil** (< 0.05 biasanya) = hasil sangat tidak mungkin kalau H₀ benar → reject H₀
- P-value **besar** (> 0.05) = hasil masih mungkin kalau H₀ benar → fail to reject H₀

> **Significance level (α)** = threshold untuk reject. Standard: 0.05 (5%). Lebih ketat: 0.01 (1%).

### 3.4 Common Misinterpretation

❌ "P-value 0.03 berarti ada 3% probability bahwa H₀ benar."
✅ "P-value 0.03 berarti **kalau H₀ benar**, kita akan dapat hasil seperti ini (atau lebih ekstrim) hanya 3% dari waktu."

Beda halus, tapi **penting**. Jangan klaim sebab-akibat dari p-value.

---

## 4. Common Tests

### 4.1 Z-Test / T-Test (Compare 2 Means)

Skenario: rata-rata transaksi cabang A vs B beda?

```python
from scipy import stats

cabang_a = [50000, 75000, 60000, ...]   # data cabang A
cabang_b = [55000, 80000, 65000, ...]

# Independent t-test
t_stat, p_value = stats.ttest_ind(cabang_a, cabang_b)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value: {p_value:.4f}")

if p_value < 0.05:
    print("Reject H0 — beda significant")
else:
    print("Fail to reject H0 — beda tidak significant")
```

### 4.2 Chi-Square Test (Categorical)

Skenario: distribusi metode bayar berbeda antara cabang?

```python
from scipy.stats import chi2_contingency

# Contingency table
data = [
    [50, 100, 30, 20],   # Tebet: Cash, QRIS, Debit, Kredit
    [40, 80, 25, 15],    # Dago
]

chi2, p, dof, expected = chi2_contingency(data)
print(f"chi2: {chi2:.4f}, p: {p:.4f}")
```

### 4.3 Proportion Z-Test (untuk A/B Test Konversi)

```python
from statsmodels.stats.proportion import proportions_ztest

# Group A: 1500 conversion dari 50000
# Group B: 1600 conversion dari 50000
counts = [1500, 1600]
nobs = [50000, 50000]

z_stat, p_value = proportions_ztest(counts, nobs)
print(f"p-value: {p_value:.4f}")
```

---

## 5. Confidence Interval (CI)

CI = range estimasi nilai populasi dengan confidence level (biasanya 95%).

```
"Rate konversi B = 3.2%, 95% CI [3.0%, 3.4%]"
```

Artinya: kalau eksperimen di-rerun banyak kali, 95% interval seperti ini akan capture true value.

```python
from scipy import stats
import numpy as np

data = [50000, 75000, 60000, ...]
mean = np.mean(data)
sem = stats.sem(data)
ci = stats.t.interval(0.95, len(data) - 1, loc=mean, scale=sem)

print(f"Mean: {mean}, 95% CI: {ci}")
```

> **Reporting tip:** sertakan **CI**, bukan cuma point estimate. Lebih informative.

---

## 6. A/B Testing — Workflow Lengkap

### Step 1: Define Hypothesis & Metric

- "Layout B akan menaikkan conversion rate dibanding A by minimum 5%"
- Metric: conversion rate (purchase / visit)

### Step 2: Power Analysis — Berapa Sample yang Dibutuhkan?

```python
from statsmodels.stats.power import zt_ind_solve_power

effect_size = 0.05         # 5% relative effect
power = 0.80               # 80% chance detect (standard)
alpha = 0.05

n = zt_ind_solve_power(
    effect_size=effect_size,
    power=power,
    alpha=alpha,
    alternative='two-sided',
)
print(f"Sample size per group: {n:.0f}")
```

### Step 3: Run Experiment

Random assign user ke grup A & B. **Jangan stop early** kalau tidak signifikan — tunggu sample size tercapai.

### Step 4: Analyze

Pakai proportion z-test.

### Step 5: Decide

Kalau p < 0.05 dan effect direction positive → ship variant. Kalau tidak → keep current / iterate.

---

## 7. Common Trap untuk DA

### 7.1 Multiple Comparison Problem

Kalau test 20 hipotesis dengan α = 0.05, **expect 1 false positive** by chance.

Solusi: **Bonferroni correction** — kalau test N hipotesis, pakai α/N per test.

### 7.2 Simpson's Paradox

Pattern berbalik saat di-aggregate vs di-segment.

Contoh: secara aggregate, layout A lebih baik. Tapi kalau di-segment per device (mobile/desktop), layout B menang di **kedua** device. Ini bisa terjadi karena distribusi traffic beda.

> **Selalu segment data sebelum kesimpulan akhir.**

### 7.3 P-hacking

Test berbagai variant sampai dapat p < 0.05. **Tidak valid** scientifically. Pre-register hypothesis sebelum lihat data.

### 7.4 Correlation ≠ Causation

(Sudah dibahas Week 1 Day 4 AM) — tetap berlaku.

---

## 8. Latihan

`latihan/soal.md` — analisis A/B test simulated data.

---

## Apa Selanjutnya?

Lanjut **Day 3 — Case Study Week 3**.

> **Tip portfolio:** notebook A/B test analysis dengan recommendation → push ke `05-statistics-case/ab-test-analysis.ipynb`.

---

**Akhir Day 2 PM · Week 3**
*Savvys Education · 2026*

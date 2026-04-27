# Latihan — Statistics Inferential

## Setup

```python
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
```

## Soal 1 — Hypothesis Test
Cabang Tebet vs Dago — apakah rata-rata transaksi beda significant? Pakai t-test pada kolom `total` dataset Kopi Kita.

State H0, H1, p-value, kesimpulan.

## Soal 2 — A/B Test Konversi
Simulasi A/B test:
```python
# Group A (control)
n_a = 5000
conv_a = 250    # 5.0%

# Group B (treatment)
n_b = 5000
conv_b = 280    # 5.6%
```

Pakai `proportions_ztest`. Apakah lift dari A ke B significant?

## Soal 3 — Confidence Interval
Hitung 95% CI untuk:
- Mean total transaksi semua data
- Mean total transaksi cabang Tebet
- Mean total transaksi cabang Dago

Bandingkan CI — apakah overlap?

## Soal 4 — Power Analysis
Kamu mau detect 5% lift di conversion rate. Baseline rate 5%. α=0.05, power=80%.

Berapa sample size yang dibutuhkan per grup?

## Soal 5 — Chi-Square
Apakah distribusi `metode_bayar` beda significant antara 2 cabang? Pakai chi-square test.

## Bonus — Simpson's Paradox
Bikin contoh sintetik di mana:
- Aggregate: Layout A lebih baik dari B
- Per segment (mobile, desktop): Layout B lebih baik di kedua

Visualisasikan untuk show pattern.

## Submission
`latihan/stats-inferential.ipynb`. Push ke `05-statistics-case/` portfolio.

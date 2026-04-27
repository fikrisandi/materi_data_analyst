# Cheatsheet — Statistics Descriptive

## Central Tendency

| Stat | Excel | SQL | Python | Kapan |
|---|---|---|---|---|
| Mean | `=AVERAGE(r)` | `AVG(c)` | `df.col.mean()` | Data simetris no outlier |
| Median | `=MEDIAN(r)` | (workaround) | `df.col.median()` | Data dengan outlier |
| Mode | `=MODE(r)` | `GROUP BY...COUNT...` | `df.col.mode()` | Data kategorikal/diskrit |

## Dispersion

| Stat | Excel | SQL | Python |
|---|---|---|---|
| Range | `=MAX-MIN` | `MAX-MIN` | `df.col.max()-df.col.min()` |
| Variance | `=VAR.S(r)` | `VARIANCE` | `df.col.var()` |
| Std (sample) | `=STDEV.S(r)` | `STDDEV` | `df.col.std()` |
| Std (pop) | `=STDEV.P(r)` | - | `df.col.std(ddof=0)` |
| Q1 | `=QUARTILE(r,1)` | (PERCENTILE) | `df.col.quantile(0.25)` |
| Q3 | `=QUARTILE(r,3)` | (PERCENTILE) | `df.col.quantile(0.75)` |
| IQR | `=Q3-Q1` | - | `q3-q1` |

## Bentuk Distribusi

- **Normal** → mean ≈ median, bell curve
- **Right-skewed** → mean > median (income, harga rumah)
- **Left-skewed** → mean < median (jarang)
- **Bimodal** → 2 puncak, mungkin ada sub-grup
- **Uniform** → flat

Visual: pakai histogram (Excel: Insert > Chart > Histogram; Python: `df.col.hist()`)

## Outlier Detection

### Z-Score
```
z = (x - mean) / std
|z| > 3 → outlier
```
(Cocok untuk normal distribution)

### IQR Rule
```
lower = Q1 - 1.5 × IQR
upper = Q3 + 1.5 × IQR
outside [lower, upper] = outlier
```
(Robust untuk skewed)

## Korelasi Pearson

```
r ∈ [-1, +1]
```

| |r| | Strength |
|---|---|
| 0–0.3 | Weak |
| 0.3–0.6 | Moderate |
| 0.6–0.9 | Strong |
| >0.9 | Very strong |

Excel: `=CORREL(r1, r2)` · Python: `df.corr()`

## Aturan Emas

⚠️ **Korelasi ≠ Kausalitas.** Selalu tanya: ada variabel ketiga?

⚠️ **Outlier jangan langsung dibuang.** Investigate dulu — sinyal atau noise?

⚠️ **Mean menyesatkan untuk skewed data.** Pakai median.

## Quick Profile Pattern

```python
df.describe()
# Output: count, mean, std, min, 25%, 50% (median), 75%, max
```

Excel quick: `=AVERAGE`, `=MEDIAN`, `=STDEV.S`, `=QUARTILE(...,1)`, `=QUARTILE(...,3)` di kolom rapi.

## Next
✅ Stats Descriptive → lanjut `day-4-pm-case-study-w1/`

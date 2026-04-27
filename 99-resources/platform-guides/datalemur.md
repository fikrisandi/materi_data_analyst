# DataLemur — Panduan untuk Peserta DA

## Apa Itu DataLemur?

[datalemur.com](https://datalemur.com) — bank soal SQL **interview-style** dari perusahaan FAANG (Meta, Google, Amazon, dll). 

**Bedanya dengan HackerRank:**
- HackerRank: skill verification & certification
- DataLemur: simulasi soal interview real

## Tier Soal

| Tier | Karakteristik | Cocok Untuk |
|---|---|---|
| **Easy** | 1-2 step query, basic SELECT/JOIN/GROUP BY | Pemula post-Week 1 |
| **Medium** | Window function, multi-step CTE, edge case | Post-Week 2 |
| **Hard** | Complex business logic, performance optimization | Senior DA prep |

## Goal per Level

| Level | Target |
|---|---|
| Pemula DA (post Week 1) | 5-10 Easy solved |
| Mid level (post Week 2) | 15+ Easy + 10 Medium solved |
| Siap apply senior | 50+ Medium + 5 Hard solved |
| Siap interview FAANG | 100+ all tier solved |

## Pattern Soal yang Sering Muncul

### 1. Top N per Group
"Top 3 product per category by sales" → ROW_NUMBER + PARTITION BY.

### 2. Running Total / Cumulative
"Daily revenue with cumulative running total" → SUM() OVER (ORDER BY).

### 3. Period-over-Period
"Month-over-month growth" → LAG / LEAD.

### 4. Pct of Total / Pct of Group
"% contribution of each product to total" → SUM() OVER ().

### 5. Find Pattern (LIKE / Regex)
"Email yang dari domain Yahoo" → LIKE atau REGEXP.

### 6. Median / Percentile
"Median salary per department" → PERCENTILE_DISC atau workaround.

### 7. Sequential Events
"User yang login 3 hari berturut-turut" → window function untuk gap & islands.

### 8. Cohort Analysis
"Retention rate per signup cohort" → multi-CTE dengan date arithmetic.

## Tips Tackle Soal

1. **Pahami schema dulu** sebelum tulis query — DataLemur kasih sample data
2. **Start from inside-out** — write inner query dulu, baru wrap dengan logic luar
3. **Test edge cases** — ties, NULL, empty result
4. **Optimize kalau hint says** — kadang soal minta efficient query

## Free Tier

- 50+ free questions termasuk Easy & Medium
- Unlimited submissions
- Discussion forum gratis
- Premium ($16/bulan) → akses hard problems + video solutions

## Tips Practice Schedule

- 15-30 menit per hari = 1 problem
- Setelah solved, baca **discussion forum** untuk lihat alternative approach
- Re-attempt setelah 1 minggu untuk check retention

## Untuk Persiapan Interview

3 minggu sebelum interview:
1. Solved minimum 30 Medium problems
2. Time yourself: 10-15 min per problem average
3. Practice **explain your thinking** out loud — banyak interview minta verbal walkthrough

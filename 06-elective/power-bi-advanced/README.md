# Elective — Power BI Advanced

> **Tujuan:** Mendalami Power BI di area DAX advanced, time intelligence, dan custom visual. Cocok untuk target industri korporat.
>
> **Estimasi:** 4-5 jam self-paced.

---

## 1. DAX Advanced

### 1.1 CALCULATE — Heart of DAX

```dax
-- Conditional sum (mirip SUMIF Excel)
QRIS Revenue = CALCULATE(
    SUM(transaksi[total]),
    transaksi[metode_bayar] = "QRIS"
)

-- Multi-condition
Big QRIS Tebet = CALCULATE(
    SUM(transaksi[total]),
    transaksi[metode_bayar] = "QRIS",
    transaksi[id_cabang] = "C001",
    transaksi[total] > 100000
)
```

### 1.2 FILTER & ALL

```dax
-- ALL = remove filter context
% of Total = DIVIDE(
    SUM(transaksi[total]),
    CALCULATE(SUM(transaksi[total]), ALL(transaksi))
)

-- FILTER untuk complex condition
Top Customer Revenue = CALCULATE(
    SUM(transaksi[total]),
    FILTER(
        VALUES(pelanggan[id_pelanggan]),
        [Customer Revenue] > 500000
    )
)
```

---

## 2. Time Intelligence

```dax
-- YTD
Sales YTD = TOTALYTD([Total Sales], transaksi[tanggal])

-- Previous Period
Sales Last Month = CALCULATE(
    [Total Sales],
    DATEADD(transaksi[tanggal], -1, MONTH)
)

-- Same Period Last Year
Sales SPLY = CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(transaksi[tanggal])
)

-- Growth %
YoY Growth = DIVIDE([Total Sales] - [Sales SPLY], [Sales SPLY])
```

> **Wajib ada Date Table** untuk time intelligence yang benar. Bikin via `CALENDAR(MIN(tanggal), MAX(tanggal))`.

---

## 3. Variables in DAX

```dax
Profit Margin = 
VAR TotalRev = SUM(transaksi[total])
VAR TotalCost = SUMX(transaksi, transaksi[qty] * RELATED(menu[hpp]))
VAR Profit = TotalRev - TotalCost
RETURN
    DIVIDE(Profit, TotalRev)
```

VAR bikin DAX **lebih readable** & **performant** (compute sekali, pakai banyak).

---

## 4. Iterators — SUMX, AVERAGEX, FILTER

```dax
-- Mirip SUM tapi iterate per row
Total Profit = SUMX(
    transaksi,
    transaksi[total] - (transaksi[qty] * RELATED(menu[hpp]))
)

-- Average ber-row
Avg Profit per Order = AVERAGEX(transaksi, [Profit per Row])
```

---

## 5. Custom Visual

Power BI marketplace (visual.microsoft.com) punya banyak custom visual:
- Sankey Chart
- Bullet Chart
- Funnel Plot
- Decomposition Tree (built-in di PBI)

Install: **Get more visuals** di pane Visualizations.

---

## 6. Latihan & Sertifikasi

1. Bikin dashboard dengan 5 measure DAX advanced (CALCULATE, time intelligence, %, conditional)
2. Mulai prep **Microsoft PL-300** — official cert PBI Data Analyst Associate

> **Resource:** [Microsoft Learn — PL-300](https://learn.microsoft.com/en-us/credentials/certifications/data-analyst-associate/) (gratis, ~30 jam total)

---

**Akhir Elective Power BI Advanced**
*Savvys Education · 2026*

# SQL Master Cheatsheet — Semua Level

## Basic Query (Week 1 Day 3 AM)

```sql
SELECT col1, col2 FROM tabel WHERE cond ORDER BY col DESC LIMIT 10;
SELECT DISTINCT col FROM tabel;
SELECT (a - b) AS profit FROM tabel;
```

## Filter Operators

```sql
=, !=, <, >, <=, >=
BETWEEN x AND y
IN (a, b, c)
LIKE 'pattern%'         -- % = any chars, _ = 1 char
IS NULL, IS NOT NULL
AND, OR, NOT
```

## Aggregate (Week 1 Day 3 PM)

```sql
COUNT(*), COUNT(DISTINCT col), SUM(col), AVG(col), MIN(col), MAX(col)
```

## GROUP BY & HAVING

```sql
SELECT cabang, SUM(total) AS rev
FROM transaksi
WHERE metode = 'QRIS'
GROUP BY cabang
HAVING SUM(total) > 1000000
ORDER BY rev DESC;
```

## JOIN

```sql
INNER JOIN  -- intersection
LEFT JOIN   -- semua A, match B
RIGHT JOIN  -- semua B, match A
FULL JOIN   -- semua kedua

FROM transaksi t
INNER JOIN menu m ON t.id_menu = m.id_menu;
```

## Window Function (Week 2 Day 4)

```sql
ROW_NUMBER() OVER (PARTITION BY cabang ORDER BY total DESC) AS rn
RANK() OVER (...)
DENSE_RANK() OVER (...)

SUM(total) OVER (PARTITION BY cabang) AS revenue_cabang
SUM(total) OVER (ORDER BY tanggal) AS running_total

LAG(total, 1) OVER (ORDER BY tanggal) AS prev_value
LEAD(total, 1) OVER (ORDER BY tanggal) AS next_value

NTILE(4) OVER (ORDER BY total) AS quartile
```

## CTE — `WITH`

```sql
WITH summary AS (
    SELECT cabang, SUM(total) AS rev FROM transaksi GROUP BY cabang
),
filtered AS (
    SELECT * FROM summary WHERE rev > 1000000
)
SELECT * FROM filtered;
```

## Subquery

```sql
WHERE total > (SELECT AVG(total) FROM transaksi)
WHERE EXISTS (SELECT 1 FROM ... WHERE ...)
```

## CASE WHEN

```sql
CASE
    WHEN total >= 100000 THEN 'Besar'
    WHEN total >= 50000 THEN 'Sedang'
    ELSE 'Kecil'
END AS kategori
```

## Date Functions

### SQLite
```sql
strftime('%Y-%m', tanggal)  -- year-month
strftime('%w', tanggal)     -- day of week
DATE('now', '-7 days')
```

### PostgreSQL
```sql
DATE_TRUNC('month', tanggal)
EXTRACT(MONTH FROM tanggal)
NOW(), CURRENT_DATE
```

### BigQuery
```sql
EXTRACT(YEAR FROM date_col)
DATE_ADD('2026-01-01', INTERVAL 7 DAY)
DATE_DIFF(end, start, DAY)
DATE_TRUNC(tanggal, MONTH)
```

## String Functions

```sql
LENGTH(text), UPPER, LOWER, TRIM
SUBSTR(text, 1, 3)
CONCAT(a, b)
REPLACE(text, 'old', 'new')
```

## Best Practice

- UPPERCASE keyword, lowercase nama tabel/kolom
- Indentasi konsisten
- Comment dengan `-- ...`
- Test query bertahap
- LIMIT saat eksplor

## Anti-pattern

- `WHERE col = NULL` → pakai `IS NULL`
- `WHERE SUM(col) > x` → pakai `HAVING`
- String `"..."` → pakai `'...'`
- `SELECT *` di production query

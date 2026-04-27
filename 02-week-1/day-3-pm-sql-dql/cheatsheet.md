# Cheatsheet — SQL DQL & BigQuery

## GROUP BY & HAVING

```sql
SELECT id_cabang, SUM(total) AS revenue
FROM transaksi
WHERE metode_bayar = 'QRIS'
GROUP BY id_cabang
HAVING SUM(total) > 1000000
ORDER BY revenue DESC;
```

**Urutan eksekusi:**
```
FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

**Aturan emas:** kolom di SELECT harus di GROUP BY ATAU di-aggregate.

## JOIN Types

| JOIN | Hasil |
|---|---|
| `INNER JOIN` | Cuma yang cocok di KEDUA tabel |
| `LEFT JOIN` | Semua dari tabel kiri + yang cocok di kanan |
| `RIGHT JOIN` | Semua dari tabel kanan + yang cocok di kiri |
| `FULL OUTER JOIN` | Semua dari kedua tabel |
| `CROSS JOIN` | Cartesian product (semua kombinasi) |

## JOIN Pattern

```sql
SELECT t.col1, m.col2
FROM transaksi t
INNER JOIN menu m ON t.id_menu = m.id_menu;

-- Multi-table
FROM transaksi t
INNER JOIN cabang c ON t.id_cabang = c.id_cabang
INNER JOIN menu m   ON t.id_menu = m.id_menu;
```

## "Anti-Join" (item di A tapi tidak di B)

```sql
SELECT a.*
FROM table_a a
LEFT JOIN table_b b ON a.key = b.key
WHERE b.key IS NULL;
```

## BigQuery Sandbox

- 10 GB storage gratis · 1 TB query/bulan gratis
- Tabel pakai full path: `` `project.dataset.table` ``
- JANGAN `SELECT *` (mahal)
- Lihat cost estimate sebelum Run

## Public Datasets Bagus

| Dataset | Topik |
|---|---|
| `bigquery-public-data.usa_names` | Nama bayi USA |
| `bigquery-public-data.covid19_open_data` | COVID global |
| `bigquery-public-data.nyc_yellow_taxi_trips` | NYC taxi |
| `bigquery-public-data.google_analytics_sample` | Web analytics |
| `bigquery-public-data.chicago_crime` | Kriminalitas Chicago |
| `bigquery-public-data.samples.shakespeare` | Shakespeare |

## Common Gotcha

❌ `WHERE SUM(total) > 1000` → ERROR (aggregate di WHERE)
✅ `HAVING SUM(total) > 1000`

❌ `SELECT col1, SUM(col2) FROM t` (tanpa GROUP BY)
✅ `SELECT col1, SUM(col2) FROM t GROUP BY col1`

❌ JOIN tanpa ON → cartesian product (data eksplosi)
✅ Selalu `ON` dengan key yang valid

## Latihan Lanjutan

- HackerRank SQL: **Basic Join**, **Advanced Join**
- DataLemur: filter "Easy" dan "Medium"
- LeetCode: filter "Easy" SQL problems

## Next
✅ DQL → lanjut `day-4-am-stats-descriptive/`

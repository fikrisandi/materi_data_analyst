# Elective — Looker Studio Advanced

> **Tujuan:** Mendalami Looker Studio dengan BigQuery integration, calculated metrics, parameter, dan embedding.
>
> **Estimasi:** 3-4 jam self-paced.

---

## 1. Connect Looker ke BigQuery

Yang biasa dipakai DA enterprise:

1. Looker → Add data → **BigQuery**
2. Pilih project & dataset
3. Pilih tabel atau **custom query** (untuk pre-aggregate)
4. Looker auto-detect schema

> **Tip:** untuk dashboard real-time, set BigQuery view sebagai data source. Looker auto-refresh saat user buka dashboard.

---

## 2. Custom Query

```sql
-- Custom query langsung di Looker
SELECT
    DATE(pickup_datetime) AS date,
    COUNT(*) AS trips,
    SUM(total_amount) AS revenue,
    AVG(tip_amount / NULLIF(fare_amount, 0)) AS tip_rate
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'
GROUP BY date
```

---

## 3. Calculated Field & Calculated Metric

### Calculated Field

```
// Profit
total - (qty * hpp)

// Conditional
CASE
    WHEN total >= 100000 THEN "Besar"
    WHEN total >= 50000 THEN "Sedang"
    ELSE "Kecil"
END

// String operations
CONCAT(nama, " — ", kota)
REGEXP_EXTRACT(email, "@(.+)\\.")
```

### Aggregate Function

```
-- Summing in calc
SUM(total) - SUM(qty * hpp)

-- Distinct count
COUNT_DISTINCT(id_pelanggan)
```

---

## 4. Parameter — Dynamic Input

Bikin **parameter** untuk user input dynamic:

1. Add a parameter → numeric
2. Default value: 100000
3. Pakai di calculated field:

```
CASE
    WHEN total >= @threshold THEN "Big"
    ELSE "Small"
END
```

User di dashboard bisa adjust threshold via slider.

---

## 5. Blending Data — Multiple Sources

Looker bisa blend data dari 2+ source (mirip JOIN):

1. Resource → Manage blends
2. Add blend
3. Pilih join key
4. Tipe: Left join (default)

Use case: blend **revenue from BigQuery** dengan **target from Sheets**.

---

## 6. Embedding di Web

```html
<iframe
  src="https://lookerstudio.google.com/embed/reporting/<REPORT_ID>"
  width="100%"
  height="800"
  frameborder="0">
</iframe>
```

Atau embed di Notion, Confluence, internal wiki — Looker support embed di hampir semua platform.

---

## 7. Latihan

1. Connect Looker ke BigQuery public dataset (NYC Taxi atau COVID)
2. Bikin dashboard 4-chart dengan 2 calculated field & 1 parameter
3. Share publicly + simpan link di portfolio

---

**Akhir Elective Looker Studio Advanced**
*Savvys Education · 2026*

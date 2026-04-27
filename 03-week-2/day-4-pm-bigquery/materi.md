# Week 2 · Day 4 PM
# BigQuery Hands-On — Query Dataset Publik Skala Besar

> **Tujuan:** Setelah modul ini kamu bisa pakai BigQuery sandbox untuk analisis dataset publik berskala besar (miliar baris), paham syntax BigQuery-specific (date function, array, struct), dan tahu cara optimize cost.
>
> **Estimasi:** 3 jam.

---

## 1. Recap & Setup

BigQuery sudah dibahas Week 1 Day 3 PM. Recap:

- Sandbox: gratis, tanpa kartu kredit, 10 GB storage + 1 TB query/bulan
- Akses: [console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery) dengan akun Gmail
- Dataset publik: `bigquery-public-data.<dataset>.<table>`

Hari ini kita praktik mendalam dengan **3 dataset menarik**:

1. **NYC Yellow Taxi 2022** — analisis transportation
2. **COVID Open Data** — analisis time series Indonesia
3. **Google Analytics Sample** — analisis web behavior

---

## 2. BigQuery Syntax — Yang Beda dari Standard SQL

BigQuery 95% sama dengan PostgreSQL, tapi ada beberapa perbedaan:

### 2.1 Tabel Reference

```sql
-- Pakai backtick untuk full path
SELECT * FROM `bigquery-public-data.usa_names.usa_1910_current` LIMIT 10;
```

### 2.2 Date Functions

```sql
EXTRACT(YEAR FROM date_col)
EXTRACT(MONTH FROM date_col)
EXTRACT(DAYOFWEEK FROM date_col)    -- 1 = Sunday
EXTRACT(DAYOFYEAR FROM date_col)

DATE_ADD('2026-01-01', INTERVAL 7 DAY)
DATE_SUB('2026-01-01', INTERVAL 1 MONTH)
DATE_DIFF('2026-12-31', '2026-01-01', DAY)
DATE_TRUNC(date_col, MONTH)         -- truncate ke awal bulan
```

### 2.3 String Functions

```sql
LOWER(text), UPPER(text), TRIM(text)
LENGTH(text), CONCAT(a, b), SPLIT(text, ',')
REGEXP_CONTAINS(text, r'pattern')
SUBSTR(text, 1, 5)
```

### 2.4 Array & Struct (Advanced)

BigQuery support nested data — array & struct.

```sql
-- Array
SELECT [1, 2, 3] AS arr;

-- Struct
SELECT STRUCT('Andi' AS nama, 28 AS umur) AS user;

-- Unnest array
SELECT name, score
FROM UNNEST(ARRAY<STRUCT<name STRING, score INT64>>[
    ('Andi', 90),
    ('Budi', 85)
]);
```

> **Untuk DA pemula, fokus query basic dulu. Array/struct lebih advanced — relevan untuk dataset BigQuery yang nested seperti Google Analytics.**

---

## 3. Case 1: NYC Yellow Taxi 2022

Dataset: `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`

> ⚠️ **Cost awareness:** dataset ini punya ratusan juta baris. Selalu pakai filter & LIMIT.

### Q1. Total Trip & Revenue 2022

```sql
SELECT
    COUNT(*) AS total_trip,
    ROUND(SUM(total_amount), 2) AS total_revenue,
    ROUND(AVG(total_amount), 2) AS avg_per_trip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-01-01' AND '2022-12-31';
```

### Q2. Trip per Hari dalam Seminggu

```sql
SELECT
    EXTRACT(DAYOFWEEK FROM pickup_datetime) AS day_num,
    FORMAT_DATE('%A', DATE(pickup_datetime)) AS day_name,
    COUNT(*) AS jumlah_trip,
    ROUND(AVG(total_amount), 2) AS avg_amount
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'
GROUP BY day_num, day_name
ORDER BY day_num;
```

### Q3. Tip Behavior — Cash vs Card

```sql
SELECT
    payment_type,
    COUNT(*) AS jumlah,
    ROUND(AVG(tip_amount), 2) AS avg_tip,
    ROUND(SUM(CASE WHEN tip_amount > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS pct_with_tip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-07'
GROUP BY payment_type
ORDER BY jumlah DESC;
```

### Q4. Trend Hourly Demand

```sql
SELECT
    EXTRACT(HOUR FROM pickup_datetime) AS jam,
    COUNT(*) AS jumlah_trip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-07'
GROUP BY jam
ORDER BY jam;
```

> Plot hasil di Excel atau pandas → akan terlihat 2 puncak (rush hour pagi & sore).

---

## 4. Case 2: COVID Indonesia

Dataset: `bigquery-public-data.covid19_open_data.covid19_open_data`

### Q1. Cumulative Confirmed Indonesia 2020-2023

```sql
SELECT
    EXTRACT(YEAR FROM date) AS tahun,
    EXTRACT(MONTH FROM date) AS bulan,
    MAX(cumulative_confirmed) AS max_confirmed,
    MAX(cumulative_deceased) AS max_deceased
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code = 'ID'
  AND aggregation_level = 0
GROUP BY tahun, bulan
ORDER BY tahun, bulan;
```

### Q2. Per Provinsi (kalau aggregation_level = 1)

```sql
SELECT
    subregion1_name AS provinsi,
    MAX(cumulative_confirmed) AS confirmed,
    MAX(cumulative_deceased) AS deceased
FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
WHERE country_code = 'ID'
  AND aggregation_level = 1
  AND date <= '2022-12-31'
GROUP BY provinsi
ORDER BY confirmed DESC
LIMIT 10;
```

### Q3. Wave Detection — Daily New Cases

```sql
WITH daily AS (
    SELECT
        date,
        new_confirmed
    FROM `bigquery-public-data.covid19_open_data.covid19_open_data`
    WHERE country_code = 'ID'
      AND aggregation_level = 0
      AND new_confirmed > 0
)
SELECT
    date,
    new_confirmed,
    AVG(new_confirmed) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma_7d
FROM daily
WHERE date BETWEEN '2021-06-01' AND '2021-09-30'
ORDER BY date;
```

Window function `ROWS BETWEEN 6 PRECEDING AND CURRENT ROW` = moving average 7 hari.

---

## 5. Case 3: Google Analytics Sample

Dataset: `bigquery-public-data.google_analytics_sample.ga_sessions_*`

> Dataset ini **partitioned** per tanggal. Pakai `_TABLE_SUFFIX` untuk filter.

### Q1. Sessions per Country

```sql
SELECT
    geoNetwork.country AS country,
    COUNT(*) AS sessions,
    SUM(totals.transactions) AS transactions
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE _TABLE_SUFFIX BETWEEN '20170701' AND '20170731'
GROUP BY country
ORDER BY sessions DESC
LIMIT 10;
```

### Q2. Top Pages

```sql
SELECT
    hits.page.pagePath AS page,
    COUNT(*) AS pageviews
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`,
    UNNEST(hits) AS hits
WHERE _TABLE_SUFFIX BETWEEN '20170701' AND '20170707'
  AND hits.type = 'PAGE'
GROUP BY page
ORDER BY pageviews DESC
LIMIT 10;
```

> **Catatan:** GA dataset pakai struktur nested/array — butuh `UNNEST` untuk flatten. Ini contoh bagus advanced BigQuery feature.

---

## 6. Cost Optimization

BigQuery dihitung **per byte yang di-scan**. 1 TB free per bulan, tapi mudah habis kalau salah query.

### 6.1 Cek Sebelum Run

Sebelum klik "Run", BigQuery tampilkan estimasi di kanan atas — "This query will process X.X GB". Kalau terlalu besar, optimize dulu.

### 6.2 Pakai Partition Filter

Tabel besar biasanya **partitioned** (dibagi per tanggal). Filter partition column = scan jauh lebih sedikit.

```sql
-- Mahal (scan semua partition)
SELECT * FROM big_table WHERE name = 'X';

-- Hemat (scan 1 partition saja)
SELECT * FROM big_table
WHERE _PARTITIONTIME = TIMESTAMP('2023-01-01')
  AND name = 'X';
```

### 6.3 SELECT Only Needed Columns

BigQuery columnar storage — `SELECT *` baca semua kolom. `SELECT a, b` cuma 2 kolom = jauh lebih murah.

### 6.4 Preview Sample Dulu

```sql
-- Preview 100 row dulu
SELECT * FROM big_table LIMIT 100;
```

LIMIT di BigQuery **tidak otomatis hemat scan** — masih scan semua. Tapi LIMIT bantu kamu test query dulu sebelum scan full.

---

## 7. Latihan & Praktik

Buka BigQuery console kamu, kerjakan 8 query latihan di `latihan/soal.md`.

---

## Apa Selanjutnya?

Lanjut **Day 5 — Live Code 2 + persiapan Week 3** (Web Scraping & API).

> **Tip portfolio:** ekspor 2-3 query terbaik kamu ke `queries-bigquery.sql` di `02-sql-bigquery/` portfolio. Dokumentasikan apa yang dianalisis.

---

**Akhir Day 4 PM · Week 2**
*Savvys Education · 2026*

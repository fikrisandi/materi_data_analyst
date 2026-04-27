# Latihan — BigQuery

> Pakai BigQuery sandbox. Save query di `latihan/jawaban-bigquery.sql`.

## A — NYC Taxi (3 soal)

### A.1
Top 5 zona pickup dengan revenue tertinggi (June 2022).

### A.2
Distribusi `passenger_count` — berapa % trip 1 penumpang vs 2+ (June 2022)?

### A.3
Pakai window function: trip yang **fare_amount** > 90th percentile dari semua trip (Juli 2022).

## B — COVID Indonesia (2 soal)

### B.1
Per provinsi Indonesia: max cumulative_confirmed di akhir 2022. Top 10.

### B.2
Daily new cases Indonesia + 7-day moving average untuk Q3 2021 (puncak Delta wave).

## C — Custom Dataset (3 soal)

Pilih 1 public dataset menarik dari `bigquery-public-data` (ada banyak: Chicago crime, Stack Overflow, Shakespeare, dll). Jawab 3 pertanyaan analytical yang kamu tentukan sendiri.

Tulis di notebook markdown:
1. Pertanyaan & dataset
2. SQL query
3. Hasil
4. 1 insight statement

## Submission
`latihan/jawaban-bigquery.sql` + `analysis-bigquery.md` dengan 3 query custom + insight. Push ke `02-sql-bigquery/` portfolio.

🎯 **Cost check:** semua query kamu total scan-nya berapa GB? Catat di akhir file. Goal: < 5 GB total untuk semua latihan.

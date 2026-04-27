# Week 1 · Day 5
# Live Code 1 & Recap Week 1

> **Tujuan modul:** Konsolidasi Week 1 dengan live coding pada dataset baru. Siap masuk Week 2 (Python).
>
> **Durasi:** ~3 jam (90 min live code + 30 min Q&A + 60 min Python prep).

---

## 1. Recap Week 1 — Apa yang Sudah Kamu Pelajari

```
Day 1 AM   Setup VSCode + Miniconda + Git ✓
Day 1 PM   Git workflow + GitHub portfolio ✓
Day 2 AM   Excel Foundation: pivot, VLOOKUP, INDEX-MATCH ✓
Day 2 PM   Power Query: ETL ringan di Excel ✓
Day 3 AM   SQL Basics: SELECT, WHERE, ORDER BY ✓
Day 3 PM   SQL DQL: GROUP BY, HAVING, JOIN, BigQuery ✓
Day 4 AM   Statistics Descriptive: mean/median/std/IQR/outlier ✓
Day 4 PM   Mini Case Study: Kopi Kita Q1 2026 ✓
Day 5      → Live Code & Recap (kamu di sini)
```

Skill yang sudah kamu kuasai cukup untuk:
- Apply Junior Data Analyst entry level (~6-12jt Jakarta)
- Selesaikan **HackerRank SQL Basic Skills Certification**
- Bantu tim non-DA dengan analytics ringan via Excel/SQL

---

## 2. Live Code Challenge — NYC Taxi Trips di BigQuery

### Setup

Buka BigQuery sandbox kamu. Dataset: `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`.

### Pertanyaan Live (Mentor demo)

**Q1.** Total trip & revenue NYC Yellow Taxi tahun 2022.

```sql
SELECT
    COUNT(*) AS total_trip,
    SUM(total_amount) AS total_revenue,
    AVG(total_amount) AS avg_per_trip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-01-01' AND '2022-12-31';
```

**Q2.** Top 10 zona pickup paling ramai.

```sql
SELECT
    pickup_location_id,
    COUNT(*) AS jumlah_trip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-30'
GROUP BY pickup_location_id
ORDER BY jumlah_trip DESC
LIMIT 10;
```

**Q3.** Distribusi tip — apakah orang tip di NYC?

```sql
SELECT
    payment_type,
    COUNT(*) AS jumlah,
    AVG(tip_amount) AS avg_tip,
    SUM(CASE WHEN tip_amount > 0 THEN 1 ELSE 0 END) AS trip_dengan_tip,
    SUM(CASE WHEN tip_amount > 0 THEN 1 ELSE 0 END) * 100.0 / COUNT(*) AS pct_with_tip
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-07'
GROUP BY payment_type
ORDER BY jumlah DESC;
```

**Q4.** Korelasi distance vs fare.

```sql
SELECT
    CORR(trip_distance, fare_amount) AS corr_distance_fare
FROM `bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2022`
WHERE pickup_datetime BETWEEN '2022-06-01' AND '2022-06-07'
  AND trip_distance > 0
  AND fare_amount > 0;
```

(Hampir pasti tinggi — wajar karena tarif berdasarkan jarak.)

---

## 3. Drill Challenge (untuk peserta)

5 soal mandiri 30 menit. Pakai dataset NYC Taxi atau Kopi Kita.

1. Hari apa dalam seminggu paling ramai NYC taxi? (`EXTRACT(DAYOFWEEK FROM pickup_datetime)`)
2. Top 5 trip terbesar (by total_amount).
3. Average tip per zona pickup. Top 10.
4. Trip yang **payment_type = Cash** vs **Credit** — beda tip rate?
5. Distribusi `passenger_count` — berapa % trip 1 penumpang vs 2+?

---

## 4. Persiapan Week 2 — Python

Week 2 mulai Python. Cek setup:

```bash
conda activate savvys-da
python --version       # 3.12.x
python -c "import pandas, numpy, matplotlib; print('OK')"
```

Kalau setup belum lengkap, **fix sekarang**, jangan tunggu Week 2 Day 1. Hubungi mentor kalau stuck.

### Bacaan Persiapan (Opsional)

- [Real Python — Python Basics](https://realpython.com/python-basics/)
- [LearnPython.org Interactive Tutorial](https://www.learnpython.org)
- [Khan Academy — Algebra & Statistics Refresh](https://www.khanacademy.org)

---

## Apa Selanjutnya?

✅ **Week 1 selesai.** Selamat — fondasi sudah solid.

**Week 2 fokus:** Python + Pandas + SQL Advanced + BigQuery hands-on.

```bash
cd ~/savvys-da-kursus/portfolio
git add . && git commit -m "Week 1 complete" && git push
```

Buka folder `03-week-2/day-1-am-python-basics/` — sampai jumpa Senin pagi!

---

**Akhir Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan
- Recap & konsolidasi Week 1
- Latihan live coding dengan dataset baru (di luar Kopi Kita)
- Persiapan ke Week 2 (Python)

## Format
- 90 menit live code (mentor demo + peserta ikut)
- 30 menit Q&A
- 60 menit persiapan setup Python (recap Day 1 AM)

## Output
- `materi.md` — outline live code + recap Week 1
- `code/livecode-1.sql` — query yang akan didemonstrasikan
- `latihan/soal.md` — drill challenge

# Latihan — Excel Foundation

> **Dataset:** `data/penjualan-warung-2026.xlsx` (250 transaksi Q1 2026)
> **Tujuan:** latih formula, lookup, pivot, conditional formatting.
> **Submission:** simpan hasil di `latihan/jawaban.xlsx`. Solusi lengkap di `latihan/solusi.md`.

---

## Bagian A — Soal Mudah (5 soal)

### Soal A.1 — Total Revenue Q1
Hitung **total revenue Q1 2026** (Jan-Mar). Pakai formula SUM.

### Soal A.2 — Rata-rata per Transaksi
Hitung **rata-rata Total per transaksi**. Bulatkan ke integer.

### Soal A.3 — Hitung Transaksi QRIS
Berapa transaksi yang pakai metode bayar **QRIS**? Pakai COUNTIF.

### Soal A.4 — Total Revenue Cabang Tebet
Berapa total revenue Cabang Tebet (`C001`)? Pakai SUMIF.

### Soal A.5 — Transaksi Terbesar
Berapa nominal **transaksi terbesar** Q1 2026? Pakai MAX. Bonus: transaksi ID berapa? (Pakai INDEX-MATCH untuk cari ID.)

---

## Bagian B — Soal Menengah (3 soal)

### Soal B.1 — VLOOKUP Nama Menu
Tambah kolom **Nama Menu** di sheet Transaksi pakai VLOOKUP ke sheet Menu. Drag formula ke seluruh 250 baris.

### Soal B.2 — Pivot: Revenue per Cabang × Metode Bayar
Bikin pivot table:
- Rows: ID Cabang
- Columns: Metode Bayar
- Values: Sum of Total

Cabang mana yang QRIS-nya paling dominan?

### Soal B.3 — Conditional Formatting Color Scale
Pakai conditional formatting **Color Scales** pada kolom Total. Identifikasi visual: di mana cluster transaksi besar terkonsentrasi (cabang mana, bulan mana, metode bayar apa)?

---

## Bagian C — Soal Advanced (2 soal)

### Soal C.1 — Profit per Transaksi
Tambah kolom **HPP per Transaksi** pakai VLOOKUP ke sheet Menu (kolom HPP × Qty). Lalu kolom **Profit** = Total − HPP per Transaksi.

Bikin pivot:
- Rows: ID Cabang
- Values: Sum of Profit

Cabang mana yang **profit-nya** lebih tinggi (bukan revenue, tapi profit)?

### Soal C.2 — Pelanggan Loyal
Pakai pivot dengan:
- Rows: ID Pelanggan
- Values: Count of ID Transaksi (jumlah kunjungan)

Sort descending. **Top 5 pelanggan paling sering datang** siapa? Bonus: pakai VLOOKUP ke sheet Pelanggan untuk dapat nama mereka.

---

## Submission

Simpan hasil di `latihan/jawaban.xlsx`:
- Sheet "A1-A5" untuk Bagian A (cell formula + hasil)
- Sheet "B1" untuk pivot Soal B.1 (VLOOKUP applied)
- Sheet "B2" untuk pivot Soal B.2
- Sheet "C1" untuk pivot Soal C.1
- Sheet "C2" untuk pivot Soal C.2
- Sheet "Insight" — tulis 3 insight bisnis dari analisis di atas

Push ke portfolio repo:
```bash
cd ~/savvys-da-kursus/portfolio/01-excel-foundation
# copy jawaban.xlsx ke sini, rename jadi analysis.xlsx
git add analysis.xlsx
git commit -m "Week 1 Day 2 AM: Excel Foundation latihan"
git push
```

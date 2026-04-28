# Latihan — Excel Foundation

> **Dataset:** `data/penjualan-warung-2026.xlsx` (250 transaksi Q1 2026)
> **Tujuan:** latih formula, lookup, pivot, conditional formatting.
> **Submission:** Save As → `latihan/jawaban.xlsx`. Kunci jawaban dipegang mentor.

---

## ⚠️ Cara Kerja (baca dulu sebelum mulai!)

Buka file dataset → kamu akan lihat **11 sheet**:

**Sheet data (jangan diubah)** — ini sumber data, treat sebagai read-only:
- `Transaksi`, `Menu`, `Cabang`, `Pelanggan`

**Sheet kerja (kerjakan di sini)** — sudah disediakan dengan header siap:
- `A — Mudah` — untuk soal Bagian A (5 soal + bonus)
- `B1 — VLOOKUP Menu` — copy 250 baris transaksi, kolom Nama Menu kosong
- `B2 — Pivot Cabang x Bayar` — area kosong + instruksi
- `C1 — Profit` — copy 250 baris transaksi, kolom HPP & Profit kosong
- `C2 — Loyal` — area pivot + tabel Top-5 kosong
- `Insight` — template 3 insight bisnis

**Aturan penting:**
1. **JANGAN** kerjain di sheet `Transaksi` (data sumber). Selalu di sheet kerja.
2. Wajib pakai **formula**, bukan ngetik nilai manual. Mentor akan cek formula bar.
3. Pakai absolute reference (`$A$2:$E$9`) untuk lookup yang di-drag.

---

## Bagian A — Soal Mudah (5 soal) → kerjakan di sheet `A — Mudah`

### Soal A.1 — Total Revenue Q1
Hitung **total revenue Q1 2026** (Jan-Mar). Pakai formula SUM.

### Soal A.2 — Rata-rata per Transaksi
Hitung **rata-rata Total per transaksi**. Bulatkan ke integer pakai ROUND.

### Soal A.3 — Hitung Transaksi QRIS
Berapa transaksi yang pakai metode bayar **QRIS**? Pakai COUNTIF.

### Soal A.4 — Total Revenue Cabang Tebet
Berapa total revenue Cabang Tebet (`C001`)? Pakai SUMIF.

### Soal A.5 — Transaksi Terbesar
Berapa nominal **transaksi terbesar** Q1 2026? Pakai MAX.
**Bonus:** ID transaksi-nya berapa? Pakai INDEX-MATCH (bukan VLOOKUP — kenapa? Karena ID Transaksi di kolom kiri, sedangkan Total di kolom kanan. VLOOKUP cuma bisa ke kanan.)

---

## Bagian B — Soal Menengah (3 soal)

### Soal B.1 — VLOOKUP Nama Menu → kerjakan di sheet `B1 — VLOOKUP Menu`
Isi kolom **Nama Menu** (kolom J) pakai VLOOKUP ke sheet Menu. Drag formula dari J5 sampai J254 (250 baris).

### Soal B.2 — Pivot: Revenue per Cabang × Metode Bayar → kerjakan di sheet `B2 — Pivot Cabang x Bayar`
Bikin pivot table:
- Rows: ID Cabang
- Columns: Metode Bayar
- Values: Sum of Total

Cabang mana yang QRIS-nya paling dominan? Tulis jawaban di sel yang disediakan.

### Soal B.3 — Conditional Formatting Color Scale → kerjakan di sheet `Transaksi` (visual)
Pakai conditional formatting **Color Scales** pada kolom Total (H2:H251). Identifikasi visual: di mana cluster transaksi besar terkonsentrasi (cabang mana, bulan mana, metode bayar apa)? Tulis 1-2 kalimat observasi di sheet `Insight`.

> Catatan: untuk soal B.3 kamu **boleh** pakai conditional formatting di sheet `Transaksi` karena ini overlay visual, bukan modifikasi data.

---

## Bagian C — Soal Advanced (2 soal)

### Soal C.1 — Profit per Transaksi → kerjakan di sheet `C1 — Profit`
Tambah kolom **HPP per Transaksi** (kolom J) pakai VLOOKUP ke sheet Menu (kolom HPP × Qty).
Lalu kolom **Profit** (kolom K) = Total − HPP per Transaksi.

Bikin pivot dari sheet ini:
- Rows: ID Cabang
- Values: Sum of Profit

Cabang mana yang **profit-nya** lebih tinggi (bukan revenue, tapi profit)?

### Soal C.2 — Pelanggan Loyal → kerjakan di sheet `C2 — Loyal`
Pakai pivot dengan:
- Rows: ID Pelanggan
- Values: Count of ID Transaksi (jumlah kunjungan)

Sort descending. Salin **Top 5 pelanggan paling sering datang** ke tabel di bawah pivot. Pakai VLOOKUP untuk dapat Nama dan Kota Asal mereka dari sheet Pelanggan.

---

## Insight — kerjakan di sheet `Insight`

Tulis **3 insight bisnis** dari hasil analisis di atas. Setiap insight WAJIB punya:
- Data pendukung (angka konkret hasil pengerjaan kamu)
- Saran bisnis yang actionable

Lihat contoh "Insight contoh" di bagian bawah sheet untuk referensi format.

---

## Submission

1. Save As file dataset → `latihan/jawaban.xlsx`
2. Copy ke portfolio repo:
   ```bash
   cd ~/savvys-da-kursus/portfolio/01-excel-foundation
   # copy jawaban.xlsx ke sini, rename jadi analysis.xlsx
   git add analysis.xlsx
   git commit -m "Week 1 Day 2 AM: Excel Foundation latihan"
   git push
   ```

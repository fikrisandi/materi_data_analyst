# Latihan — Excel Power Query

## Tugas Utama

Gabung 3 file di `data/` (Tebet, Dago, Kelapa Gading) jadi 1 tabel rapi pakai Power Query. Detail kolom output di `materi.md` Section 9.

## Checklist
- [ ] Import 3 file separately
- [ ] Standardize column names
- [ ] Change types (Date, Number, Text)
- [ ] Trim whitespace di Menu
- [ ] Fix typo "Cappucino" → "Cappuccino"
- [ ] Standardize Metode_Bayar (Cash, QRIS, Debit, Kredit)
- [ ] Parse "Rp 50,000" → 50000 (Kelapa Gading)
- [ ] Tambah kolom Cabang
- [ ] Append 3 queries
- [ ] Conditional Column Kategori_Transaksi
- [ ] Close & Load → output 100-115 baris

## Bonus
1. Bikin Pivot Table dari hasil: Cabang × Metode_Bayar (sum of Total)
2. Refresh test: edit 1 file source (tambah baris), refresh — apakah tabel auto-update?

## Submission
File `analysis-power-query.xlsx` di `latihan/`. Push ke `01-excel-foundation/` di portfolio.

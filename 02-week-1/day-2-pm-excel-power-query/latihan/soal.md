# Latihan — Excel Power Query

## Setup

1. Buka **`latihan/template-jawaban.xlsx`** (template yang sudah disediakan)
2. **Save As** → `latihan/jawaban.xlsx` sebelum mulai kerja
3. Lihat sheet `README` di file untuk gambaran sheet target

> **Catatan:** sheet `Combined_Clean` di template adalah **target output** — Power Query akan auto-fill ke sheet ini saat Close & Load. Header sudah disiapkan; rows kosong, akan terisi otomatis.

## Tugas Utama

Gabung 3 file di `data/` (Tebet, Dago, Kelapa Gading) jadi 1 tabel rapi pakai Power Query. Output target: ~115 baris dengan kolom `Tanggal | Menu | Qty | Total | Metode_Bayar | Cabang | Kategori_Transaksi`.

## Checklist (kerjakan urut)
- [ ] Import 3 file separately (Data → Get Data → From Workbook, 1 per file)
- [ ] Standardize column names ke target output
- [ ] Change types (Tanggal=Date, Qty/Total=Number, Menu/Bayar/Cabang=Text)
- [ ] Trim whitespace di kolom Menu (Kelapa Gading punya leading/trailing space)
- [ ] Fix typo "Cappucino" → "Cappuccino"
- [ ] Standardize Metode_Bayar jadi 4 nilai: `Cash`, `QRIS`, `Debit`, `Kredit`
  - **Penting:** map "Tunai" → "Cash" (alias)
- [ ] Parse "Rp 50,000" → 50000 (Kelapa Gading kolom TOTAL_RP text)
- [ ] Tambah kolom `Cabang` per query (literal: "Tebet" / "Dago" / "Kelapa Gading")
- [ ] Append 3 queries jadi 1 query `Combined`
- [ ] Tambah Conditional Column `Kategori_Transaksi`:
  - `Total < 30.000` → "Kecil"
  - `30.000 ≤ Total < 60.000` → "Sedang"
  - `Total ≥ 60.000` → "Besar"
- [ ] Close & Load → output ke sheet `Combined_Clean` (~115 baris)

## Bonus

### Bonus 1 — Verifikasi per Cabang
Bikin Pivot Table dari `Combined_Clean`: Rows=Cabang, Values=Sum of Total + Count + Average. Tempel hasilnya di sheet `Per_Cabang` di tabel yang sudah disediakan.

### Bonus 2 — Refresh Test (untuk verifikasi pakai Power Query, bukan copy-paste)
Edit salah satu file source (mis. tambah 1 baris di `tebet-januari-2026.xlsx`) → save → balik ke file kerja → Data → Refresh All. Apakah `Combined_Clean` auto-update?

## Submission

Save file final sebagai `latihan/jawaban.xlsx`. Push ke `01-excel-foundation/` di portfolio.

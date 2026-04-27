# Cheatsheet — Excel Foundation

## Formula Wajib Hafal

| Formula | Contoh | Fungsi |
|---|---|---|
| `=SUM(range)` | `=SUM(H2:H251)` | Total |
| `=AVERAGE(range)` | `=AVERAGE(H2:H251)` | Rata-rata |
| `=COUNT(range)` | `=COUNT(H2:H251)` | Hitung sel berisi angka |
| `=COUNTA(range)` | `=COUNTA(A2:A251)` | Hitung sel non-empty |
| `=MAX(range)` / `=MIN(range)` | `=MAX(H2:H251)` | Maks / Min |
| `=IF(cond, true, false)` | `=IF(H2>50000, "Besar", "Kecil")` | Logika |
| `=COUNTIF(range, cond)` | `=COUNTIF(I:I, "QRIS")` | Hitung dengan kondisi |
| `=SUMIF(crit_range, cond, sum_range)` | `=SUMIF(I:I, "QRIS", H:H)` | Sum dengan kondisi |
| `=COUNTIFS(...)` | `=COUNTIFS(C:C, "C001", I:I, "QRIS")` | Multiple conditions |
| `=SUMIFS(...)` | `=SUMIFS(H:H, C:C, "C001", I:I, "QRIS")` | Sum multi conditions |
| `=ROUND(num, digits)` | `=ROUND(AVG(H2:H251), 0)` | Bulatkan |
| `=TEXT(val, format)` | `=TEXT(H2, "#,##0")` | Format jadi teks |
| `=MONTH(date)` / `=YEAR(date)` | `=MONTH(B2)` | Extract bulan/tahun |

## Lookup

| Formula | Use case |
|---|---|
| `=VLOOKUP(key, table, col, FALSE)` | Cari nilai di kolom kanan key |
| `=INDEX(return, MATCH(key, lookup, 0))` | Lookup flexible (kanan & kiri) |
| `=XLOOKUP(key, lookup, return)` | Excel 2021+, paling bersih |

## Cell Reference

| Format | Behavior saat copy |
|---|---|
| `B5` | Kolom & baris berubah (relative) |
| `$B$5` | Kolom & baris tetap (absolute) |
| `$B5` | Kolom tetap, baris berubah |
| `B$5` | Baris tetap, kolom berubah |

Tekan `F4` untuk toggle saat nulis formula.

## Pivot Table — Cycle 30 Detik

1. Klik di data → **Insert** → **PivotTable** → OK
2. Drag ke area:
   - **Rows** = dimensi vertikal (cabang, bulan, kategori)
   - **Columns** = dimensi horizontal
   - **Values** = angka (Sum, Average, Count)
   - **Filters** = saringan global

## Conditional Formatting — Top 4 Pakai

| Rule | Use case |
|---|---|
| **Highlight Cells > X** | Tandai outlier |
| **Color Scales** (gradient) | Lihat trend visual |
| **Data Bars** | Bar chart in-cell |
| **Top/Bottom 10** | Highlight extreme |

## Shortcut Wajib

| Shortcut | Fungsi |
|---|---|
| `Ctrl+T` | Convert to Excel Table |
| `Ctrl+Shift+L` | Toggle Filter |
| `Ctrl+Arrow` | Lompat ke ujung data |
| `Ctrl+Shift+End` | Pilih sampai akhir data |
| `Alt+=` | Auto-sum |
| `F4` | Toggle absolute reference |
| `Ctrl+;` | Insert tanggal hari ini |
| `Ctrl+1` | Format Cells dialog |
| `Alt+H+B+A` | All borders |

## Best Practice DA

1. **Raw data sheet terpisah** — jangan diedit langsung
2. **Excel Tables (Ctrl+T)** untuk auto-expand
3. **Named Ranges** untuk formula readable
4. **README sheet** untuk dokumentasi
5. **Tidak merge cells** untuk data (OK untuk title)

## Anti-pattern

- ❌ 12 sheet untuk 12 bulan → pakai 1 sheet + filter
- ❌ Nested 7 IF → pakai IFS atau lookup table
- ❌ Warna cell sebagai data → pakai kolom dedicated
- ❌ Save as .xls → pakai .xlsx atau .xlsb

## Kapan Excel Bukan Pilihan?

- Dataset > 1 juta baris → SQL/Python
- Reproducible report harian → Python/BI tool
- Statistik kompleks → Python (scipy, statsmodels)
- Real-time data → BI dashboard

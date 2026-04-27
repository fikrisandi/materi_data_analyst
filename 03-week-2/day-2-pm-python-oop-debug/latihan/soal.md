# Latihan — Python OOP & Debugging

## Bagian A — Debug 5 Buggy Code

Code starter di `code/buggy.py` — fix 5 bug:

1. `NameError` — variable typo
2. `TypeError` — concat string + int
3. `KeyError` — dict key tidak ada (handle dengan `.get()`)
4. `IndexError` — out of range list
5. `ZeroDivisionError` — handle dengan if check

## Bagian B — Bikin Class

### B.1
Bikin class `Cabang` dengan:
- attribute: nama, kota, transaksi (list)
- method: `total_revenue()`, `avg_per_trx()`, `top_n_transaksi(n=5)`

### B.2
Bikin subclass `CabangPremium(Cabang)` yang tambah:
- attribute: target_revenue
- method: `apakah_target_tercapai()` return True/False

## Bagian C — Try/Except

### C.1
Bikin function `read_csv_safe(path)` yang baca file CSV pakai `csv` module. Handle:
- FileNotFoundError → return list kosong dengan warning print
- PermissionError → raise dengan pesan customized
- Exception lain → catch, print error message, return None

## Submission
Save di `latihan/jawaban.py` atau `.ipynb`.

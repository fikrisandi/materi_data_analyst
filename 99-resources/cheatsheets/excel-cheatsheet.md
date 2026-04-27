# Excel Master Cheatsheet untuk DA

## Formula Wajib

| Formula | Contoh |
|---|---|
| `=SUM(A1:A10)` | Total |
| `=AVERAGE(A1:A10)` | Rata-rata |
| `=MEDIAN(A1:A10)` | Median |
| `=COUNT(A1:A10)` | Hitung numeric |
| `=COUNTA(A1:A10)` | Hitung non-empty |
| `=MAX(...)`, `=MIN(...)` | Maks / Min |
| `=ROUND(num, digits)` | Pembulatan |

## Conditional

```excel
=IF(A1>100, "Besar", "Kecil")
=COUNTIF(A:A, "QRIS")
=SUMIF(I:I, "QRIS", H:H)
=COUNTIFS(C:C, "C001", I:I, "QRIS")
=SUMIFS(H:H, C:C, "C001", I:I, "QRIS")
=AVERAGEIFS(...)
```

## Lookup

```excel
=VLOOKUP(key, range, col_idx, FALSE)
=INDEX(return_range, MATCH(key, lookup_range, 0))
=XLOOKUP(key, lookup_range, return_range)    -- Excel 2021+
```

## Date/Time

```excel
=TODAY(), =NOW()
=YEAR(A1), =MONTH(A1), =DAY(A1)
=WEEKDAY(A1, 2)        -- 1=Mon, 7=Sun
=EOMONTH(A1, 0)        -- end of month
=NETWORKDAYS(start, end)
=DATEDIF(start, end, "d")      -- days between
```

## Text

```excel
=LEN(A1)
=UPPER(A1), =LOWER(A1), =PROPER(A1)
=TRIM(A1)
=LEFT(A1, 5), =RIGHT(A1, 3), =MID(A1, 2, 3)
=CONCATENATE(A1, " ", B1)         -- atau A1 & " " & B1
=TEXT(123456, "#,##0")            -- "123,456"
=SUBSTITUTE(A1, "old", "new")
```

## Stat

```excel
=STDEV.S(A1:A10)            -- sample
=STDEV.P(A1:A10)            -- population
=VAR.S(A1:A10)
=QUARTILE(A1:A10, 1)        -- Q1
=QUARTILE(A1:A10, 3)        -- Q3
=PERCENTILE(A1:A10, 0.9)    -- 90th percentile
=CORREL(A1:A10, B1:B10)
```

## Cell Reference

| Format | Behavior copy |
|---|---|
| `A1` | Relative (kolom & baris berubah) |
| `$A$1` | Absolute (tetap) |
| `$A1` | Kolom tetap |
| `A$1` | Baris tetap |

`F4` saat nulis formula → toggle.

## Pivot Table

`Insert → PivotTable`

- **Rows** — dimensi vertikal
- **Columns** — dimensi horizontal
- **Values** — angka aggregate
- **Filters** — saringan global

## Conditional Formatting

`Home → Conditional Formatting`

- Highlight Cells > X
- Color Scales (gradient)
- Data Bars (in-cell bar)
- Top/Bottom 10
- Custom formula

## Power Query (Data tab)

- Get Data → import
- Append Queries (stack vertikal)
- Merge Queries (join horizontal)
- Group By, Pivot, Unpivot
- Conditional Column

## Shortcut

| Shortcut | Fungsi |
|---|---|
| `Ctrl+T` | Convert to Excel Table |
| `Ctrl+Shift+L` | Toggle Filter |
| `Ctrl+Arrow` | Jump to ujung data |
| `Ctrl+Shift+End` | Pilih sampai akhir |
| `Alt+=` | Auto-sum |
| `F4` | Toggle absolute reference |
| `Ctrl+1` | Format Cells |
| `Ctrl+;` | Insert today |
| `Ctrl+Shift+;` | Insert now (jam) |

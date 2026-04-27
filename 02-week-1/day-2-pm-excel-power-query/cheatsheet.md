# Cheatsheet — Excel Power Query

## Akses Power Query
- **Data tab** → **Get Data** / **From Table/Range**
- Import file: From File → From Excel Workbook
- Import folder: From File → From Folder

## Operasi Wajib Hafal

| Operasi | Cara | Use case |
|---|---|---|
| First row as header | Home → Use First Row as Headers | Saat header tidak ke-detect |
| Change type | Klik kanan kolom → Change Type | Date, Number, Text |
| Trim whitespace | Transform → Format → Trim | Bersihkan space awal/akhir |
| Replace value | Transform → Replace Values | Fix typo / standardize |
| Remove blank rows | Home → Remove Rows → Remove Blank | Hapus baris kosong |
| Filter rows | Filter dropdown di header | Same as Excel filter |
| Group By | Home → Group By | Aggregation |
| Pivot | Transform → Pivot Column | Long → Wide |
| Unpivot | Transform → Unpivot Columns | Wide → Long |

## Combine Queries

| Operasi | Cara | Use case |
|---|---|---|
| **Append** | Home → Append Queries | Stack vertikal (kolom sama) |
| **Merge** | Home → Merge Queries | Join horizontal pakai key (mirip VLOOKUP) |

## Add Column Patterns

| Operasi | Cara |
|---|---|
| Custom column | Add Column → Custom Column (formula M) |
| Conditional column | Add Column → Conditional Column |
| Column from examples | Add Column → Column from Examples |
| Index column | Add Column → Index Column |

## Formula M Useful

```m
= Date.From([col])               // text → date
= Number.FromText([col])         // text → number
= Text.From([col])               // any → text
= Text.Trim([col])               // trim
= Text.Lower([col])              // lowercase
= Text.Upper([col])              // uppercase
= Text.Replace([col],"old","new")// replace
= if [Total] >= 70000 then "Besar" else if [Total] >= 30000 then "Sedang" else "Kecil"
```

## Best Practice

✅ **DO:**
- Beri nama query descriptive
- Edit step dengan icon ⚙️ (jangan delete)
- Save intermediate query as "Connection Only"
- Refresh saat data update

❌ **DON'T:**
- Manual copy-paste data lagi (point of Power Query!)
- Hard-code path file (gunakan parameter)
- Delete step kalau salah (edit aja)

## Refresh

- Single query: klik kanan query → Refresh
- All: Data → Refresh All (`Ctrl+Alt+F5`)
- Schedule auto-refresh: Data → Connection Properties

## Kapan Pakai Power Query?

✅ Cocok untuk:
- Gabung multiple file Excel format mirip
- Bersihkan data dari sumber yang konsisten polanya
- ETL ringan untuk dashboard Excel
- Setup laporan repetitif (monthly report)

❌ Tidak cocok untuk:
- Statistik kompleks (pakai Python)
- Real-time data dari API (pakai Power Automate / Python)
- Dataset > 10 juta baris (pakai database/SQL)

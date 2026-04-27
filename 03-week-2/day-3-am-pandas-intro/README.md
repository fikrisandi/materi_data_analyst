# Week 2 · Day 3 AM
# Pandas Intro — DataFrame & Series

> **Tujuan:** Setelah modul ini kamu paham konsep DataFrame & Series, bisa baca/tulis CSV/Excel, dan operasi dasar (filter, sort, select column, basic aggregation).
>
> **Estimasi:** 3 jam.

---

## 1. Apa itu Pandas?

**Pandas** = library Python untuk **manipulasi & analisis data tabular**. Sering disebut "Excel di Python", tapi 100x lebih powerful.

```python
import pandas as pd                # convention alias
import numpy as np
```

Pandas dibangun di atas NumPy, jadi performance bagus untuk dataset medium (sampai ~10 juta baris di laptop normal).

---

## 2. Series — 1D Labeled Array

Series = list dengan label.

```python
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
# a    10
# b    20
# c    30
# d    40
# dtype: int64

print(s["a"])    # 10
print(s.mean())  # 25.0
```

Mirip dict atau column di Excel. Sebagian besar waktu kamu kerja dengan **DataFrame**, bukan Series.

---

## 3. DataFrame — 2D Tabular Data

DataFrame = tabel dengan baris & kolom (mirip Excel sheet atau SQL table).

```python
import pandas as pd

data = {
    "nama": ["Andi", "Budi", "Citra"],
    "umur": [28, 25, 30],
    "kota": ["Jakarta", "Bandung", "Surabaya"],
}

df = pd.DataFrame(data)
print(df)

#     nama  umur      kota
# 0   Andi    28   Jakarta
# 1   Budi    25   Bandung
# 2  Citra    30  Surabaya
```

Anatomi:
- **Rows** punya **index** (default 0, 1, 2, ...)
- **Columns** punya **name** (header)
- Setiap kolom = 1 Series

---

## 4. Read & Write Data

### 4.1 Read CSV

```python
df = pd.read_csv("data/transaksi.csv")
print(df.head())            # 5 baris pertama
print(df.tail())            # 5 baris terakhir
print(df.shape)             # (jumlah_baris, jumlah_kolom)
```

### 4.2 Read Excel

```python
df = pd.read_excel("data/penjualan.xlsx", sheet_name="Transaksi")

# Read multiple sheets sekaligus
all_sheets = pd.read_excel("data/penjualan.xlsx", sheet_name=None)
df_trx = all_sheets["Transaksi"]
df_menu = all_sheets["Menu"]
```

### 4.3 Read SQL

```python
import sqlite3

conn = sqlite3.connect("data/kopi_kita.db")
df = pd.read_sql("SELECT * FROM transaksi", conn)
conn.close()
```

### 4.4 Read Other Formats

```python
df = pd.read_json("data.json")
df = pd.read_parquet("data.parquet")    # format efficient
df = pd.read_clipboard()                # langsung paste dari Excel!
```

### 4.5 Write

```python
df.to_csv("output.csv", index=False)        # index=False supaya tidak nulis kolom index
df.to_excel("output.xlsx", index=False, sheet_name="Hasil")
df.to_parquet("output.parquet")
```

---

## 5. Eksplorasi DataFrame

### 5.1 Cek Struktur

```python
df.head()           # 5 baris pertama
df.head(10)         # 10 baris pertama
df.tail()           # 5 baris terakhir
df.sample(5)        # 5 baris random

df.shape            # (n_rows, n_cols)
df.columns          # list nama kolom
df.dtypes           # tipe data per kolom
df.info()           # ringkasan: types, non-null count
df.describe()       # stat ringkas: count, mean, std, min, max, percentiles
```

### 5.2 Pilih Kolom

```python
df["nama"]                       # 1 kolom (return Series)
df[["nama", "umur"]]             # multiple kolom (return DataFrame)

# Akses kolom dgn dot notation (kalau nama valid Python identifier)
df.nama                          # sama dengan df["nama"]
```

### 5.3 Pilih Baris

```python
# .iloc — by position (integer)
df.iloc[0]            # baris pertama
df.iloc[0:3]          # baris 0, 1, 2 (exclusive end)
df.iloc[-1]           # baris terakhir

# .loc — by label
df.loc[0]             # baris dengan index label 0

# Pilih baris + kolom sekaligus
df.iloc[0:3, 0:2]     # 3 baris pertama, 2 kolom pertama
df.loc[0:3, ["nama", "umur"]]    # baris 0-3 (inclusive di .loc!), kolom nama+umur
```

> **Common gotcha:** `.iloc[0:3]` exclusive end (3 baris: 0, 1, 2). `.loc[0:3]` inclusive end (4 baris: 0, 1, 2, 3).

---

## 6. Filter Baris (Boolean Indexing)

```python
# Filter umur > 27
df[df["umur"] > 27]

# Multi condition (gunakan & atau |, JANGAN and/or)
df[(df["umur"] > 25) & (df["kota"] == "Jakarta")]

# isin() — match list of values
df[df["kota"].isin(["Jakarta", "Bandung"])]

# String filter — startswith
df[df["nama"].str.startswith("A")]

# String filter — contains
df[df["nama"].str.contains("an", case=False)]
```

> **Important:** pakai **`&` `|` `~`** (bitwise) untuk multi-condition di pandas, bukan `and` `or` `not`. Bracketing wajib karena precedence.

---

## 7. Tambah / Modifikasi Kolom

```python
# Kolom baru hasil kalkulasi
df["umur_dalam_bulan"] = df["umur"] * 12

# Kondisional — np.where
df["kategori_umur"] = np.where(df["umur"] >= 30, "Senior", "Muda")

# Pakai apply (untuk logic complex)
df["kategori"] = df["umur"].apply(
    lambda x: "Senior" if x >= 30 else ("Muda" if x >= 25 else "Junior")
)

# String operations
df["nama_upper"] = df["nama"].str.upper()
df["nama_panjang"] = df["nama"].str.len()
```

---

## 8. Sort & Rename

```python
# Sort
df_sorted = df.sort_values("umur", ascending=False)
df_sorted = df.sort_values(["kota", "umur"], ascending=[True, False])

# Rename kolom
df = df.rename(columns={"nama": "name", "umur": "age"})

# Reset index (setelah filter biasanya jadi non-sequential)
df = df.reset_index(drop=True)
```

---

## 9. Aggregation Dasar

```python
df["total"].sum()                  # total
df["total"].mean()                 # rata-rata
df["total"].median()               # median
df["total"].std()                  # std deviation
df["total"].min(), df["total"].max()
df["total"].count()                # non-null count
df["total"].nunique()              # unique count

# Multiple stats sekaligus
df["total"].describe()
df.describe()                      # untuk semua kolom numeric
```

---

## 10. Praktik dengan Dataset Kopi Kita

```python
import pandas as pd
import sqlite3

# Read dari SQLite
conn = sqlite3.connect("../day-3-am-sql-basics/data/kopi_kita.db")
df = pd.read_sql("SELECT * FROM transaksi", conn)
conn.close()

# Eksplorasi
print(df.shape)              # (250, 9)
print(df.head())
print(df.dtypes)

# Filter
df_qris = df[df["metode_bayar"] == "QRIS"]
print(f"Jumlah QRIS: {len(df_qris)}")

# Aggregation
print(f"Total revenue: Rp {df['total'].sum():,}")
print(f"Avg per trx: Rp {df['total'].mean():,.0f}")

# Top 5 transaksi
top5 = df.nlargest(5, "total")
print(top5[["id_transaksi", "tanggal", "total"]])

# Save
df_qris.to_csv("output/qris-only.csv", index=False)
```

---

## 11. Pandas vs SQL — Cheat Reference

| Operasi | SQL | Pandas |
|---|---|---|
| Pilih kolom | `SELECT col1, col2` | `df[["col1", "col2"]]` |
| Filter | `WHERE col > 5` | `df[df["col"] > 5]` |
| Sort | `ORDER BY col DESC` | `df.sort_values("col", ascending=False)` |
| Limit | `LIMIT 10` | `df.head(10)` |
| Distinct | `SELECT DISTINCT col` | `df["col"].unique()` |
| Count | `COUNT(*)` | `len(df)` |
| Sum | `SUM(col)` | `df["col"].sum()` |
| Group by | `GROUP BY col` | `df.groupby("col")` (Day 3 PM) |

---

## Apa Selanjutnya?

Lanjut **Day 3 PM — Pandas Wrangling** — yang akan kasih kamu groupby, merge, pivot, dan operasi lanjutan untuk DA sebenarnya.

---

**Akhir Day 3 AM · Week 2**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- DataFrame & Series concept
- Read/Write CSV, Excel, SQL
- Eksplorasi: head, info, describe
- Select, filter (boolean indexing)
- Sort, rename, reset_index
- Aggregation dasar
- Pandas vs SQL comparison

~3 jam · materi.md + latihan/soal.md

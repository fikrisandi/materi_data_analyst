# Week 2 · Day 3 PM
# Pandas Wrangling — Merge, GroupBy, Pivot, Transform

> **Tujuan:** Setelah modul ini kamu bisa pakai pandas untuk operasi DA inti: merge tabel (mirip SQL JOIN), groupby aggregation, pivot table, dan transform/apply.
>
> **Estimasi:** 3 jam.

---

## 1. groupby — Aggregation per Group

Equivalent SQL `GROUP BY`. Tools paling sering dipakai DA setelah filter.

### 1.1 Basic groupby

```python
import pandas as pd
df = pd.read_sql("SELECT * FROM transaksi", conn)

# Total revenue per cabang
df.groupby("id_cabang")["total"].sum()

# Multiple aggregations
df.groupby("id_cabang")["total"].agg(["sum", "mean", "count"])

# Multiple kolom + multiple aggs
df.groupby(["id_cabang", "metode_bayar"]).agg({
    "total": ["sum", "mean", "count"],
    "qty": "sum",
})
```

### 1.2 Reset Index Setelah groupby

```python
result = df.groupby("id_cabang")["total"].sum()
print(type(result))   # Series

# Convert ke DataFrame untuk easier handling
result_df = df.groupby("id_cabang")["total"].sum().reset_index()
```

### 1.3 Custom Aggregation Function

```python
df.groupby("id_cabang")["total"].agg(
    total_revenue="sum",
    avg_per_trx="mean",
    jumlah_trx="count",
    pelanggan_unique=lambda x: df.loc[x.index, "id_pelanggan"].nunique(),
).reset_index()
```

---

## 2. merge — Gabung DataFrame (SQL JOIN)

```python
df_trx = pd.read_sql("SELECT * FROM transaksi", conn)
df_menu = pd.read_sql("SELECT * FROM menu", conn)

# INNER JOIN equivalent
result = df_trx.merge(df_menu, on="id_menu", how="inner")
```

Parameter `how`:
- `inner` — default, hanya yang cocok di kedua sisi
- `left` — semua dari df kiri
- `right` — semua dari df kanan
- `outer` — semua dari kedua

```python
# Kalau key beda nama
result = df_trx.merge(df_menu,
                     left_on="id_menu",
                     right_on="menu_id",
                     how="inner")
```

### Multi-merge

```python
df_full = (
    df_trx
    .merge(df_menu, on="id_menu")
    .merge(df_cabang, on="id_cabang")
    .merge(df_pelanggan, on="id_pelanggan")
)
```

---

## 3. pivot_table — Cross-Tab

Pandas pivot mirip Excel pivot.

```python
# Cross-tab cabang × kategori
pivot = df_full.pivot_table(
    index="nama_cabang",
    columns="kategori",
    values="total",
    aggfunc="sum",
    fill_value=0,
)
```

Output:
```
kategori        Coffee    Non-Coffee   Pastry   Snack
nama_cabang
Tebet         2,000,000   500,000     400,000  300,000
Dago          1,800,000   400,000     350,000  250,000
```

### Pivot vs Groupby

| | groupby | pivot_table |
|---|---|---|
| Output shape | Long (1 row per group) | Wide (cross-tab) |
| Multiple agg | `.agg([...])` | `aggfunc=[...]` |
| Best for | Detail analysis | Visual cross-comparison |

---

## 4. apply & transform

### 4.1 apply — Custom Logic per Row/Column

```python
# Apply function per row
def kategorikan(row):
    if row["total"] >= 100000:
        return "Besar"
    elif row["total"] >= 50000:
        return "Sedang"
    return "Kecil"

df["kategori"] = df.apply(kategorikan, axis=1)
```

### 4.2 transform — Group-aware Transformation

```python
# Pct of cabang's total
df["pct_of_cabang"] = df["total"] / df.groupby("id_cabang")["total"].transform("sum") * 100
```

`transform` keep result panjang sama dengan input (untuk fitting back to df).

---

## 5. Handling Missing Data (NaN)

```python
# Cek missing
df.isna().sum()              # count NaN per kolom

# Drop rows dengan NaN
df.dropna()                  # drop semua row dengan NaN
df.dropna(subset=["nama"])   # drop hanya kalau "nama" NaN

# Fill missing
df["umur"].fillna(df["umur"].median())   # fill dengan median
df.fillna({"umur": 0, "nama": "Unknown"})

# Replace
df.replace({"yes": True, "no": False})
```

---

## 6. String Operations

```python
df["nama"].str.upper()
df["nama"].str.lower()
df["nama"].str.strip()                    # buang whitespace
df["nama"].str.replace(" ", "_")
df["nama"].str.contains("Andi", case=False)
df["nama"].str.startswith("A")
df["nama"].str.split(" ")                 # split jadi list
df["nama"].str.split(" ").str[0]          # ambil first word
df["nama"].str.len()
```

---

## 7. Date Operations

```python
df["tanggal"] = pd.to_datetime(df["tanggal"])

df["bulan"] = df["tanggal"].dt.month       # 1-12
df["tahun"] = df["tanggal"].dt.year
df["nama_hari"] = df["tanggal"].dt.day_name()    # Monday, Tuesday, ...
df["nama_bulan"] = df["tanggal"].dt.month_name()
df["minggu_ke"] = df["tanggal"].dt.isocalendar().week

# Date diff
df["umur_hari"] = (pd.Timestamp("today") - df["tanggal_join"]).dt.days
```

---

## 8. Concatenate & Append

```python
df_total = pd.concat([df_jakarta, df_bandung, df_surabaya], ignore_index=True)

# Tambah baris (rare untuk DA)
df_new = df.append({"nama": "X", "umur": 30}, ignore_index=True)
```

---

## 9. Mini Case — Analisis Profit Kopi Kita dengan Pandas

```python
import pandas as pd
import sqlite3

conn = sqlite3.connect("../day-3-am-sql-basics/data/kopi_kita.db")
df_trx = pd.read_sql("SELECT * FROM transaksi", conn)
df_menu = pd.read_sql("SELECT * FROM menu", conn)
df_cabang = pd.read_sql("SELECT * FROM cabang", conn)
df_pel = pd.read_sql("SELECT * FROM pelanggan", conn)
conn.close()

# Convert tanggal
df_trx["tanggal"] = pd.to_datetime(df_trx["tanggal"])

# Merge semua
df = (df_trx
      .merge(df_menu, on="id_menu")
      .merge(df_cabang, on="id_cabang")
      .merge(df_pel, on="id_pelanggan", suffixes=("_trx", "_pel")))

# Kalkulasi profit per transaksi
df["profit"] = df["total"] - (df["qty"] * df["hpp"])

# Insight 1: Profit per Cabang × Kategori
profit_summary = (df
    .groupby(["nama_cabang", "kategori"])
    .agg(revenue=("total", "sum"),
         profit=("profit", "sum"),
         qty=("qty", "sum"),
         margin=("profit", lambda x: x.sum() / df.loc[x.index, "total"].sum() * 100))
    .reset_index())
print(profit_summary)

# Insight 2: Top 10 pelanggan by profit contribution
top_pelanggan = (df
    .groupby(["id_pelanggan", "nama"])
    .agg(jumlah_trx=("id_transaksi", "count"),
         total_belanja=("total", "sum"),
         profit_kontribusi=("profit", "sum"))
    .reset_index()
    .nlargest(10, "profit_kontribusi"))
print(top_pelanggan)

# Insight 3: Trend per minggu
df["minggu"] = df["tanggal"].dt.isocalendar().week
trend = df.groupby("minggu")["total"].sum()
trend.plot(kind="line", title="Revenue per Minggu")
```

---

## Apa Selanjutnya?

Lanjut **Day 4 AM — SQL Advanced** (Window Function, CTE) dan **Day 4 PM — BigQuery hands-on**.

> **Tip portfolio:** save mini case study di atas sebagai `analysis-pandas.ipynb` di portfolio `03-python-pandas/`. Plus 3 insight statement di markdown cell.

---

**Akhir Day 3 PM · Week 2**
*Savvys Education · 2026*

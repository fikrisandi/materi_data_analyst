# Pandas Master Cheatsheet

```python
import pandas as pd
import numpy as np
```

## Read / Write

```python
df = pd.read_csv("file.csv")
df = pd.read_excel("file.xlsx", sheet_name="Sheet1")
df = pd.read_sql("SELECT * FROM tabel", conn)
df = pd.read_json("file.json")

df.to_csv("out.csv", index=False)
df.to_excel("out.xlsx", index=False)
```

## Inspect

```python
df.head(), df.tail(), df.sample(5)
df.shape         # (rows, cols)
df.columns
df.dtypes
df.info()
df.describe()    # stat summary
df.isna().sum()  # missing count
```

## Select

```python
df["col"]                # 1 col → Series
df[["col1", "col2"]]      # multi col → DataFrame

df.iloc[0:3]              # by position
df.iloc[0:3, 0:2]         # rows + cols
df.loc[0:3]               # by label (inclusive end!)
df.loc[0:3, ["col1"]]
```

## Filter

```python
df[df["umur"] > 25]
df[(df["umur"] > 25) & (df["kota"] == "Jakarta")]
df[df["kota"].isin(["Jakarta", "Bandung"])]
df[df["nama"].str.startswith("A")]
df[df["nama"].str.contains("an", case=False)]
df.query("umur > 25 and kota == 'Jakarta'")    # alternative syntax
```

## Sort

```python
df.sort_values("col", ascending=False)
df.sort_values(["col1", "col2"], ascending=[True, False])
df.nlargest(5, "total")
df.nsmallest(5, "total")
```

## Add / Modify Column

```python
df["new_col"] = df["a"] + df["b"]
df["category"] = np.where(df["x"] > 5, "A", "B")
df["category"] = df["x"].apply(lambda v: "A" if v > 5 else "B")
df = df.rename(columns={"old": "new"})
```

## Aggregate

```python
df["col"].sum(), .mean(), .median(), .std(), .min(), .max()
df["col"].count(), .nunique()
df["col"].value_counts()        # frequency
df.describe()                    # all numeric
```

## GroupBy

```python
df.groupby("cabang")["total"].sum()
df.groupby("cabang").agg({"total": "sum", "qty": "mean"})
df.groupby(["cabang", "metode"]).agg(
    revenue=("total", "sum"),
    avg_order=("total", "mean"),
    customer_count=("id_pelanggan", "nunique"),
).reset_index()
```

## Merge / Join (mirip SQL)

```python
df.merge(df2, on="id", how="inner")     # inner, left, right, outer
df.merge(df2, left_on="a", right_on="b", how="left")
```

## Pivot / Unpivot

```python
pivot = df.pivot_table(
    index="cabang",
    columns="kategori",
    values="total",
    aggfunc="sum",
    fill_value=0,
)

unpivot = df.melt(id_vars=["id"], value_vars=["a", "b", "c"])
```

## Apply / Transform

```python
df["x"].apply(lambda v: v * 2)           # element-wise
df.apply(func, axis=1)                    # per row
df.groupby("cabang")["total"].transform("sum")   # broadcast aggregate
```

## Missing Data

```python
df.isna(), df.isna().sum()
df.dropna()
df.dropna(subset=["col"])
df.fillna(0)
df.fillna(df.mean())
df.fillna({"col1": 0, "col2": "Unknown"})
```

## Date

```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day_name"] = df["date"].dt.day_name()
df["week"] = df["date"].dt.isocalendar().week

(pd.Timestamp("today") - df["date"]).dt.days
```

## String

```python
df["s"].str.upper(), .lower(), .strip(), .len()
df["s"].str.replace("a", "b")
df["s"].str.split(" ").str[0]
df["s"].str.contains("pattern")
```

## Concat

```python
pd.concat([df1, df2], ignore_index=True)
```

## Common Patterns DA

```python
# Top N per group
df.groupby("cabang").apply(lambda x: x.nlargest(3, "total"))

# Pct of total
df["pct"] = df["total"] / df["total"].sum() * 100

# Pct of group
df["pct_group"] = df["total"] / df.groupby("cabang")["total"].transform("sum") * 100

# Cumulative
df["cumsum"] = df.sort_values("date")["value"].cumsum()
```

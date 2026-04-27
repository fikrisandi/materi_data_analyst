# Week 2 · Day 1 PM
# Python Conditions & Loops

> **Tujuan:** Setelah modul ini kamu paham control flow (if/else, for, while, list comprehension) dan bisa menulis logika program.
>
> **Estimasi:** 2.5 jam.

---

## 1. Mengapa Conditions & Loops?

Python sebagai DA tidak banyak butuh OOP atau design pattern. Tapi **conditions & loops** muncul di **hampir semua workflow**:
- Filter data berdasarkan kriteria → conditions
- Iterate per row dataset → loops
- Apply logic per pelanggan / per transaksi → kombinasi keduanya

Setelah Day 1 AM (variables & data types), modul ini membuat kamu bisa **menulis logika** — bukan cuma store data.

---

## 2. Conditions — if / elif / else

### 2.1 Basic if

```python
umur = 18
if umur >= 18:
    print("Dewasa")
```

> **Indentasi WAJIB.** Python pakai 4 spasi (atau Tab — VSCode auto convert ke spaces). Salah indent = error.

### 2.2 if / else

```python
nilai = 75
if nilai >= 80:
    print("Lulus dengan baik")
else:
    print("Lulus standar")
```

### 2.3 if / elif / else

```python
total_belanja = 750000

if total_belanja >= 1000000:
    diskon = 0.15
elif total_belanja >= 500000:
    diskon = 0.10
elif total_belanja >= 200000:
    diskon = 0.05
else:
    diskon = 0

bayar = total_belanja * (1 - diskon)
print(f"Bayar: Rp {bayar:,.0f}")
```

### 2.4 Nested Conditions

```python
membership = "Gold"
total_belanja = 600000

if membership == "Gold":
    if total_belanja >= 500000:
        diskon = 0.15
    else:
        diskon = 0.10
elif membership == "Silver":
    diskon = 0.05
else:
    diskon = 0
```

### 2.5 Ternary (Inline Conditional)

```python
# panjang
if total >= 100000:
    kategori = "Besar"
else:
    kategori = "Kecil"

# pendek (ternary)
kategori = "Besar" if total >= 100000 else "Kecil"
```

### 2.6 Truthy & Falsy Values

Python anggap nilai berikut **falsy** (dianggap `False` di if):
- `0`, `0.0`
- `""` (empty string)
- `[]`, `{}`, `()` (empty collections)
- `None`
- `False`

Lainnya = **truthy**.

```python
nama = ""
if nama:
    print("Ada nama")
else:
    print("Nama kosong")  # ini yang jalan

# Pattern umum cek list non-empty
items = []
if items:
    print(f"Ada {len(items)} items")
else:
    print("List kosong")
```

---

## 3. For Loop

### 3.1 Iterate List

```python
menu = ["Espresso", "Latte", "Cappuccino"]

for item in menu:
    print(f"- {item}")
```

### 3.2 Iterate Range

```python
# range(start, stop, step)
for i in range(5):           # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):       # 1 sampai 10
    print(i)

for i in range(0, 100, 10):  # 0, 10, 20, ..., 90
    print(i)
```

### 3.3 Iterate dengan Index — enumerate

```python
menu = ["Espresso", "Latte", "Cappuccino"]

for i, item in enumerate(menu):
    print(f"{i+1}. {item}")

# Output:
# 1. Espresso
# 2. Latte
# 3. Cappuccino
```

### 3.4 Iterate Dictionary

```python
pelanggan = {"nama": "Andi", "umur": 28, "kota": "Jakarta"}

# Iterate keys
for key in pelanggan:
    print(key)

# Iterate values
for value in pelanggan.values():
    print(value)

# Iterate keys + values (most common)
for key, value in pelanggan.items():
    print(f"{key}: {value}")
```

### 3.5 Iterate 2 List Bareng — zip

```python
menus = ["Espresso", "Latte"]
harga = [18000, 30000]

for menu, hrg in zip(menus, harga):
    print(f"{menu}: Rp {hrg:,}")
```

### 3.6 Loop Pattern untuk DA

Pattern paling sering: **iterate baris data, hitung sesuatu, simpan hasil**.

```python
transaksi = [
    {"id": "TRX1", "total": 50000, "metode": "QRIS"},
    {"id": "TRX2", "total": 75000, "metode": "Cash"},
    {"id": "TRX3", "total": 30000, "metode": "QRIS"},
]

# Hitung total revenue dari QRIS
total_qris = 0
for t in transaksi:
    if t["metode"] == "QRIS":
        total_qris += t["total"]

print(f"Total revenue QRIS: Rp {total_qris:,}")  # 80,000
```

> **Catatan:** untuk DA real, kamu akan pakai **Pandas** (Day 3) yang punya cara lebih elegant. Loop manual dipakai saat data kecil atau logika yang complex.

---

## 4. While Loop

```python
saldo = 100000
hari = 0

while saldo > 0:
    saldo -= 15000  # konsumsi harian
    hari += 1

print(f"Habis di hari ke-{hari}")
```

While dipakai saat **kondisi berhenti dinamis** (bukan jumlah iterasi tetap).

> **Hati-hati infinite loop:** pastikan kondisi akan jadi False di suatu titik. Kalau kebablasan, `Ctrl+C` di terminal untuk stop.

---

## 5. Loop Control — break, continue

```python
# break = hentikan loop
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# continue = skip iterasi ini, lanjut next
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1, 3, 5, 7, 9 (hanya ganjil)
```

---

## 6. List Comprehension — Pythonic Loop

Cara compact bikin list dari iterasi.

### 6.1 Basic

```python
# Dengan loop biasa
squares = []
for i in range(10):
    squares.append(i ** 2)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Dengan list comprehension (1 baris)
squares = [i ** 2 for i in range(10)]
```

### 6.2 dengan Filter

```python
# Hanya angka genap dari 0-19
genap = [i for i in range(20) if i % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Total tiap transaksi (transform)
totals = [t["total"] for t in transaksi]
# [50000, 75000, 30000]

# Total transaksi QRIS (transform + filter)
totals_qris = [t["total"] for t in transaksi if t["metode"] == "QRIS"]
# [50000, 30000]
```

### 6.3 Dict & Set Comprehension

```python
# Dict comprehension
kuadrat_dict = {i: i ** 2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Set comprehension
unique_kota = {p["kota"] for p in pelanggans}
```

> **Best practice:** comprehension OK kalau short (1 line readable). Kalau logic kompleks, pakai loop biasa untuk readability.

---

## 7. Pattern DA dengan Conditions + Loops

### 7.1 Categorize Data

```python
def kategorikan(total):
    if total >= 100000:
        return "Besar"
    elif total >= 50000:
        return "Sedang"
    else:
        return "Kecil"

transaksi_dengan_kategori = [
    {**t, "kategori": kategorikan(t["total"])}
    for t in transaksi
]
```

### 7.2 Filter & Transform

```python
qris_only = [
    {"id": t["id"], "amount": t["total"]}
    for t in transaksi
    if t["metode"] == "QRIS"
]
```

### 7.3 Aggregate per Group

```python
revenue_per_metode = {}

for t in transaksi:
    metode = t["metode"]
    if metode not in revenue_per_metode:
        revenue_per_metode[metode] = 0
    revenue_per_metode[metode] += t["total"]

print(revenue_per_metode)
# {'QRIS': 80000, 'Cash': 75000}
```

> **Catatan:** Pandas Day 3 punya `df.groupby()` yang lebih elegant untuk ini. Tapi pattern manual ini wajib paham fundamental.

---

## 8. Latihan

Buka `code/latihan-starter.ipynb`. 7 soal di `latihan/soal.md`.

---

## Apa Selanjutnya?

Lanjut **Day 2 AM — Python Functions & Modules**.

---

**Akhir Day 1 PM · Week 2**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan
1. Paham if/elif/else
2. Bisa for loop, while loop, break/continue
3. Bisa list/dict comprehension
4. Pattern: categorize, filter, transform, aggregate manual

## Durasi ~2.5 jam · Prasyarat: Day 1 AM Python Basics

## Output
- `materi.md` (~2,000 kata)
- `code/latihan-starter.ipynb` — Jupyter starter
- `latihan/soal.md` — 7 soal

## Sertifikasi Target
🎯 HackerRank Python Basic Skills (gratis, ~30 menit)

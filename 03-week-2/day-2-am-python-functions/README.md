# Week 2 · Day 2 AM
# Python Functions & Modules

> **Tujuan:** Setelah modul ini kamu bisa nulis function dengan parameter, return value, default args, *args/**kwargs, dan paham cara organisasi code dengan modules + import.
>
> **Estimasi:** 2.5 jam.

---

## 1. Mengapa Functions?

**Function = blok code reusable.** Tanpa function, kamu copy-paste logic yang sama berulang-ulang.

```python
# TANPA function (jelek)
total_jakarta = 0
for t in transaksi:
    if t["cabang"] == "Jakarta":
        total_jakarta += t["total"]

total_bandung = 0
for t in transaksi:
    if t["cabang"] == "Bandung":
        total_bandung += t["total"]

total_surabaya = 0
# ... dst, copy-paste 10x ...

# DENGAN function (rapi)
def total_per_cabang(transaksi, cabang):
    return sum(t["total"] for t in transaksi if t["cabang"] == cabang)

total_jakarta = total_per_cabang(transaksi, "Jakarta")
total_bandung = total_per_cabang(transaksi, "Bandung")
```

**Aturan emas:** kalau kamu tulis logic yang sama 2+ kali, **bikin function**.

---

## 2. Anatomy Function

```python
def nama_function(parameter1, parameter2):
    """Docstring — penjelasan apa fungsi function ini."""
    # body
    hasil = parameter1 + parameter2
    return hasil

# Pemakaian (call function)
output = nama_function(5, 10)
print(output)  # 15
```

Komponen:
- `def` — keyword bikin function
- `nama_function` — nama (snake_case, deskriptif)
- `(...)` — parameter (input function)
- `"""docstring"""` — dokumentasi (opsional tapi recommended)
- `return` — output function (opsional, kalau tidak ada → return `None`)

---

## 3. Parameters & Arguments

### 3.1 Positional Arguments

```python
def hitung_diskon(total, persen):
    return total * persen / 100

# Parameter sesuai urutan
diskon = hitung_diskon(100000, 10)   # 10000
```

### 3.2 Keyword Arguments

```python
diskon = hitung_diskon(total=100000, persen=10)
diskon = hitung_diskon(persen=10, total=100000)  # urutan boleh tukar
```

### 3.3 Default Values

```python
def hitung_diskon(total, persen=10):  # persen default 10
    return total * persen / 100

diskon1 = hitung_diskon(100000)        # pakai default 10% → 10000
diskon2 = hitung_diskon(100000, 15)    # override → 15000
```

> **Aturan:** parameter dengan default di belakang yang tanpa default.

### 3.4 *args — Variable Number of Args

```python
def total_dari_banyak(*nilai):
    return sum(nilai)

print(total_dari_banyak(10, 20, 30))         # 60
print(total_dari_banyak(5, 5, 5, 5, 5))      # 25
```

### 3.5 **kwargs — Variable Keyword Args

```python
def buat_pelanggan(**info):
    print(info)

buat_pelanggan(nama="Andi", umur=25, kota="Jakarta")
# {'nama': 'Andi', 'umur': 25, 'kota': 'Jakarta'}
```

### 3.6 Kombinasi

```python
def function_lengkap(positional1, positional2, default=10, *args, **kwargs):
    print(f"P1: {positional1}, P2: {positional2}")
    print(f"Default: {default}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

function_lengkap("a", "b", 20, "extra1", "extra2", x=1, y=2)
# P1: a, P2: b
# Default: 20
# Args: ('extra1', 'extra2')
# Kwargs: {'x': 1, 'y': 2}
```

> **Untuk DA pemula, fokus dulu di positional + default. *args/**kwargs masuk advanced.**

---

## 4. Return Values

### 4.1 Single Return

```python
def kuadrat(x):
    return x ** 2

print(kuadrat(5))   # 25
```

### 4.2 Multiple Return (sebenarnya tuple)

```python
def stat_basic(numbers):
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

low, high, avg = stat_basic([10, 20, 30, 40])
print(low, high, avg)   # 10 40 25.0
```

### 4.3 Early Return

```python
def hitung_diskon(total, membership):
    if total <= 0:
        return 0    # early return, skip logika di bawah

    if membership == "Gold":
        return total * 0.15
    elif membership == "Silver":
        return total * 0.10
    else:
        return 0
```

---

## 5. Scope — Local vs Global

```python
nama_global = "Savvys"   # global

def hello():
    nama_local = "Andi"   # local
    print(f"Halo {nama_local}, dari {nama_global}")

hello()
print(nama_global)        # OK — global accessible
# print(nama_local)       # ERROR — local tidak accessible di luar function
```

> **Best practice:** **hindari global mutable** (ubah variable global dari dalam function). Pass via parameter & return.

```python
# BURUK
total = 0
def tambah(x):
    global total
    total += x

# BAIK
def tambah(total, x):
    return total + x

total = tambah(total, 5)
```

---

## 6. Lambda — Anonymous Function

Lambda = function tanpa nama, untuk hal kecil.

```python
# Function biasa
def kuadrat(x):
    return x ** 2

# Lambda equivalent
kuadrat = lambda x: x ** 2

# Common usage: sort dengan custom key
pelanggan = [
    {"nama": "Andi", "umur": 28},
    {"nama": "Budi", "umur": 25},
    {"nama": "Citra", "umur": 30},
]

# Sort by umur
pelanggan_sorted = sorted(pelanggan, key=lambda p: p["umur"])
# Result: Budi (25), Andi (28), Citra (30)
```

> **Catatan:** lambda OK untuk inline (1 expression). Kalau logic complex, pakai `def` biasa.

---

## 7. Higher-Order Functions — map, filter

### 7.1 map — Transform

```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
# [1, 4, 9, 16]

# List comprehension equivalent (lebih Pythonic)
squared = [x ** 2 for x in numbers]
```

### 7.2 filter — Filter

```python
numbers = [1, 2, 3, 4, 5, 6]
genap = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4, 6]

# List comprehension
genap = [x for x in numbers if x % 2 == 0]
```

> **Banyak Python expert prefer list comprehension** atas map/filter — lebih readable. Tapi tahu map/filter berguna untuk baca code orang lain.

---

## 8. Modules & Import

### 8.1 Standard Library — Built-in Modules

```python
import math

print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.14159...

# Import specific
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Alias
import math as m
print(m.sqrt(16))
```

### 8.2 Useful Standard Modules untuk DA

```python
import datetime
hari_ini = datetime.date.today()

import random
random.choice(["Coffee", "Tea"])

import json
data = json.loads('{"name": "Andi"}')
print(json.dumps(data))

import os
print(os.getcwd())  # current directory

import csv
# read/write CSV (pandas more powerful)
```

### 8.3 Third-party Modules

```python
import pandas as pd      # Day 3
import numpy as np       # angka & array
import matplotlib.pyplot as plt   # visualisasi

# Convention alias di komunitas DA:
# pandas → pd
# numpy → np
# matplotlib.pyplot → plt
# seaborn → sns
```

### 8.4 Bikin Module Sendiri

File `utils.py`:

```python
# utils.py
def kuadrat(x):
    return x ** 2

def kategorikan(total):
    if total >= 100000:
        return "Besar"
    elif total >= 50000:
        return "Sedang"
    return "Kecil"
```

File `main.py`:

```python
# main.py
from utils import kuadrat, kategorikan

print(kuadrat(5))
print(kategorikan(75000))
```

> **Pattern:** function reusable di file `utils.py`, code utama di `main.py` atau notebook. Bagus untuk projek DA yang punya banyak helper.

---

## 9. Pattern Best Practice

### 9.1 Function Naming

```python
# ✅ Baik — verb + noun, snake_case
def calculate_total_revenue(transaksi):
    ...

def filter_qris_only(transaksi):
    ...

# ❌ Buruk
def doStuff():
    ...

def x(a, b):
    ...
```

### 9.2 Single Responsibility

Satu function = satu tanggung jawab.

```python
# ❌ Buruk — terlalu banyak responsibility
def process_transaksi(transaksi):
    # filter
    # calculate
    # write to file
    # send email
    ...

# ✅ Baik — pisah responsibility
def filter_qris(transaksi):
    return [t for t in transaksi if t["metode"] == "QRIS"]

def calculate_total(transaksi):
    return sum(t["total"] for t in transaksi)

def save_to_csv(data, filename):
    ...
```

### 9.3 Type Hints (Python 3.5+)

```python
def hitung_diskon(total: float, persen: float = 10) -> float:
    """Hitung nominal diskon."""
    return total * persen / 100
```

Tidak wajib, tapi membantu readability + IDE autocomplete.

---

## 10. Latihan

Buka `code/latihan-starter.ipynb`. 8 soal di `latihan/soal.md`.

---

## Apa Selanjutnya?

Lanjut **Day 2 PM — Python OOP & Debugging**.

---

**Akhir Day 2 AM · Week 2**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan
- Function dengan params, return, default, *args/**kwargs
- Lambda untuk inline
- Import standard library + third-party
- Bikin module sendiri (utils.py)
- Pattern: single responsibility, naming convention

## Durasi ~2.5 jam · Prasyarat: Day 1 PM Conditions/Loops

## Output: materi.md, latihan/soal.md

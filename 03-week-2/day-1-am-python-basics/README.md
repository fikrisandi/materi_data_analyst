# Week 2 · Day 1 AM
# Python Basics — Syntax, Variables, Data Types

> **Tujuan:** Setelah modul ini kamu paham syntax Python, bisa pakai variable & data types dasar (int, float, string, list, tuple, dict, set), tahu operator, dan bisa jalankan script Python sederhana.
>
> **Estimasi:** 2.5 jam · **Format:** modul + Jupyter notebook latihan.

---

## 1. Mengapa Python untuk DA?

Setelah Week 1 (Excel + SQL), kamu mungkin bertanya: kenapa belajar Python?

**Jawaban singkat:**
1. **Pandas** — library data manipulation paling powerful, jauh melebihi Excel
2. **Reproducibility** — script Python bisa di-rerun otomatis (vs Excel manual)
3. **Skalabilitas** — Python bisa proses jutaan baris yang Excel pun susah
4. **Otomatisasi** — fetch data dari API, scraping, schedule analysis
5. **Karir** — hampir semua lowongan DA mention Python sebagai requirement

Python untuk DA **berbeda** dari Python untuk software engineer:
- DA cuma butuh **subset Python** — tidak perlu deep OOP, design patterns, async
- Fokus ke pandas, numpy, matplotlib, kadang scikit-learn
- Workflow: **Jupyter Notebook** untuk eksplor, `.py` script untuk produksi

> **Pesan:** Python di kursus ini akan praktis & DA-focused. Tidak perlu khawatir tentang kompleksitas teori CS.

---

## 2. Hello World & First Script

Buka VSCode, aktifkan environment:

```bash
conda activate savvys-da
```

Bikin file `hello.py`:

```python
print("Halo Data Analyst!")
print("Saya siap belajar Python di Savvys Education.")

nama = "Andi"
umur = 25
print(f"Nama: {nama}, umur: {umur} tahun")
```

Jalankan:

```bash
python hello.py
```

Output:
```
Halo Data Analyst!
Saya siap belajar Python di Savvys Education.
Nama: Andi, umur: 25 tahun
```

### Konsep Pertama

- `print()` = function untuk output ke layar
- `nama = "Andi"` = assign nilai ke variable
- `f"...{var}..."` = f-string untuk format string dengan variable

---

## 3. Variable & Data Types

### 3.1 Numeric

```python
umur = 25                # int
tinggi = 1.75            # float
kompleks = 2 + 3j        # complex (rare)

print(type(umur))        # <class 'int'>
print(type(tinggi))      # <class 'float'>
```

### 3.2 String

```python
nama = "Budi"
alamat = 'Jl. Merdeka No. 1'
multiline = """Baris 1
Baris 2
Baris 3"""

# String operations
print(len(nama))                     # 4
print(nama.upper())                  # BUDI
print(nama.lower())                  # budi
print(nama + " Santoso")             # Budi Santoso (concatenation)
print(nama * 3)                      # BudiBudiBudi (repetition)

# F-string
gaji = 8500000
print(f"Gaji {nama}: Rp {gaji:,}")   # Rp 8,500,000
```

### 3.3 Boolean

```python
sudah_lulus = True
masih_aktif = False

print(sudah_lulus and masih_aktif)   # False
print(sudah_lulus or masih_aktif)    # True
print(not sudah_lulus)               # False
```

### 3.4 List — Sequence Mutable

List = collection ordered, bisa berubah, bisa duplikat.

```python
menu = ["Espresso", "Americano", "Cappuccino"]

# Access
print(menu[0])         # Espresso (index 0)
print(menu[-1])        # Cappuccino (index dari belakang)
print(menu[0:2])       # ['Espresso', 'Americano'] (slicing)

# Modify
menu.append("Latte")
print(menu)            # ['Espresso', 'Americano', 'Cappuccino', 'Latte']

menu[0] = "Espresso Doppio"
print(menu)            # ['Espresso Doppio', ...]

# Length
print(len(menu))       # 4
```

### 3.5 Tuple — Sequence Immutable

Tuple = list yang tidak bisa diubah setelah dibuat.

```python
koordinat = (-6.2, 106.8)   # latitude, longitude Jakarta
print(koordinat[0])         # -6.2

# koordinat[0] = -7.0       # Error! Tuple immutable
```

Cocok untuk: data yang **tidak boleh berubah** (koordinat, RGB color, fixed pair).

### 3.6 Dictionary — Key-Value Pair

Dict = collection key-value. Mirip JSON object atau Excel row dengan header.

```python
pelanggan = {
    "id": "P001",
    "nama": "Andi",
    "umur": 28,
    "kota": "Jakarta",
    "membership": "Gold"
}

# Access
print(pelanggan["nama"])              # Andi
print(pelanggan.get("nama"))          # Andi (safer — return None kalau key tidak ada)
print(pelanggan.get("hobi", "n/a"))   # n/a (default value kalau key tidak ada)

# Modify
pelanggan["umur"] = 29
pelanggan["email"] = "andi@example.com"

# Iterate
for key, value in pelanggan.items():
    print(f"{key}: {value}")
```

Dict adalah struktur data **paling sering dipakai** untuk represent record di DA.

### 3.7 Set — Unique Collection

Set = collection unique values, no order.

```python
kota_pelanggan = {"Jakarta", "Bandung", "Jakarta", "Surabaya", "Bandung"}
print(kota_pelanggan)        # {'Jakarta', 'Bandung', 'Surabaya'}

# Operasi set
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)        # {2, 3} — intersection
print(a | b)        # {1, 2, 3, 4} — union
print(a - b)        # {1} — difference
```

Bagus untuk: deduplicate list, cek membership cepat.

### 3.8 None

```python
hasil = None
print(hasil is None)   # True
```

`None` = "tidak ada nilai". Mirip NULL di SQL.

---

## 4. Operator

### 4.1 Arithmetic

```python
a, b = 10, 3
print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.333...
print(a // b)   # 3 (floor division)
print(a % b)    # 1 (modulo)
print(a ** b)   # 1000 (power)
```

### 4.2 Comparison

```python
print(5 == 5)    # True
print(5 != 5)    # False
print(5 < 10)    # True
print(5 >= 5)    # True

# String comparison
print("Andi" == "andi")   # False (case-sensitive)
print("Andi" == "Andi")   # True
```

### 4.3 Logical

```python
umur = 25
income = 8000000

# AND, OR, NOT
print(umur >= 18 and income >= 5000000)   # True
print(umur >= 30 or income >= 5000000)    # True
print(not umur >= 30)                      # True
```

### 4.4 Assignment

```python
x = 10
x += 5    # x = x + 5 → 15
x -= 3    # x = x - 3 → 12
x *= 2    # x = x * 2 → 24
```

### 4.5 Membership: in / not in

```python
menu = ["Espresso", "Latte"]
print("Espresso" in menu)        # True
print("Cappuccino" not in menu)  # True

# Untuk dict, default-nya cek keys
pelanggan = {"nama": "Andi", "kota": "Jakarta"}
print("nama" in pelanggan)       # True
```

---

## 5. Type Casting & Convert

```python
# String → number
umur_str = "25"
umur_int = int(umur_str)
print(umur_int + 5)   # 30

# Number → string
total = 8500000
total_str = str(total)
print(f"Total: Rp {total_str}")

# Float → int (truncate)
print(int(3.7))    # 3 (NOT 4!)
print(round(3.7))  # 4 (proper rounding)

# Bool → int
print(int(True))   # 1
print(int(False))  # 0
```

> **Common gotcha:** `int()` truncate (potong desimal), bukan round. Pakai `round()` kalau mau round proper.

---

## 6. Input dari User (Interactive)

```python
nama = input("Siapa nama kamu? ")
print(f"Halo, {nama}!")

# Numeric input perlu casting
umur_str = input("Umur kamu: ")
umur = int(umur_str)
print(f"Tahun depan kamu {umur + 1} tahun.")
```

Untuk DA, `input()` jarang dipakai (kebanyakan baca dari file/database). Tapi berguna untuk script interactive.

---

## 7. Comments & Docstrings

```python
# Ini comment 1 baris

"""
Ini comment multi-baris (technically string,
tapi sering dipakai sebagai dokumentasi).
"""

# Comment yang baik:
# Hitung total revenue setelah diskon untuk member Gold
total_after_discount = total * 0.9 if is_gold_member else total

# Comment yang buruk (state the obvious):
# Tambah a dengan b
c = a + b
```

---

## 8. Python di Jupyter Notebook

Jupyter Notebook = environment populer untuk DA — combination code + visualization + markdown narration.

### 8.1 Buka Notebook

Di terminal:

```bash
conda activate savvys-da
jupyter notebook
```

Atau langsung di VSCode: bikin file `.ipynb`.

### 8.2 Cell Types

- **Code cell** — Python code
- **Markdown cell** — text dengan format

Run cell: `Shift+Enter`.

### 8.3 Mengapa Jupyter untuk DA?

- Bisa run code per cell (eksperimen cepat)
- Output langsung di bawah cell
- Bisa selipi narasi markdown
- Output (chart, tabel) tersimpan di file
- Bagus untuk **share analisis** dengan stakeholder

> **Catatan:** untuk **production code** (yang dijalankan di scheduler, bukan eksperimen), pakai `.py` file biasa, bukan notebook.

---

## 9. Latihan Praktis

Buka `code/latihan-starter.ipynb`. Selesaikan 8 latihan dasar di soal.md.

---

## Apa Selanjutnya?

Lanjut ke **Day 1 PM — Python Conditions & Loops**. Kamu akan belajar control flow (if/else, for, while) — fondasi semua program.

---

**Akhir Day 1 AM · Week 2**
*Savvys Education · 2026*

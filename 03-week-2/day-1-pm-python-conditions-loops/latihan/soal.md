# Latihan — Python Conditions & Loops

## Bagian A — Conditions (3 soal)

### A.1 — Grading
Bikin function `nilai_ke_grade(nilai)` yang return:
- nilai >= 80 → "A"
- nilai >= 70 → "B"
- nilai >= 60 → "C"
- nilai >= 50 → "D"
- < 50 → "E"

### A.2 — Diskon Member
```python
def hitung_diskon(total, membership):
    # Aturan:
    # Gold + total >=500k → 15% diskon
    # Gold + total <500k → 10% diskon
    # Silver → 5% diskon
    # Regular → 0%
    pass
```

### A.3 — Cek Hari Operasional Warung
Cabang Tebet buka 07:00-22:00. Buat function `apakah_buka(jam)` yang return True/False.

## Bagian B — Loops (3 soal)

### B.1 — Total Revenue
List transaksi dict, hitung total revenue:
```python
transaksi = [
    {"id": "T1", "total": 50000},
    {"id": "T2", "total": 75000},
    {"id": "T3", "total": 30000},
]
# Hasil: 155000
```

### B.2 — Top 3 Pelanggan by Total Belanja
```python
pelanggan_belanja = {
    "P001": 250000,
    "P002": 800000,
    "P003": 150000,
    "P004": 600000,
    "P005": 350000,
}
# Output: list of tuple [(id, total)] urut desc, ambil 3 teratas
```

Hint: pakai `sorted()` dengan `key=lambda x: x[1]`.

### B.3 — Hitung Jumlah Per Kategori
```python
menus = [
    {"id": "M1", "kategori": "Coffee"},
    {"id": "M2", "kategori": "Coffee"},
    {"id": "M3", "kategori": "Pastry"},
    {"id": "M4", "kategori": "Snack"},
]
# Hasil: {"Coffee": 2, "Pastry": 1, "Snack": 1}
```

## Bagian C — Comprehension (1 soal)

### C.1 — Combo Comprehension
Dari list transaksi, dengan list comprehension:
1. Filter hanya transaksi QRIS
2. Buat list `[(id, total)]` dengan total > 50000

```python
transaksi = [
    {"id": "T1", "total": 50000, "metode": "QRIS"},
    {"id": "T2", "total": 75000, "metode": "Cash"},
    {"id": "T3", "total": 80000, "metode": "QRIS"},
    {"id": "T4", "total": 30000, "metode": "QRIS"},
]
# Hasil: [("T3", 80000)]
```

## Submission
Save di `latihan/jawaban.py` atau `.ipynb`. Push ke `03-python-pandas/exercises/` portfolio.

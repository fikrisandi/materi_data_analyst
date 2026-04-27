# Week 2 · Day 2 PM
# Python OOP (Intro) & Debugging

> **Tujuan:** Setelah modul ini kamu paham konsep dasar OOP (class, object, attribute, method) dan bisa pakai debugging tools (print, assert, pdb, VSCode debugger).
>
> **Estimasi:** 2.5 jam.
>
> **Note:** Sebagai DA, kamu **tidak butuh OOP advanced** — yang penting bisa baca code orang lain yang pakai class (misal scikit-learn, custom DA libraries).

---

## 1. Mengapa OOP untuk DA (sedikit, tapi penting)?

Sebagian besar workflow DA dilakukan dengan **function** (Day 2 AM) — bukan class. Tapi kamu tetap perlu paham OOP karena:

1. **Library yang kamu pakai pakai class.** `pd.DataFrame`, `sklearn.linear_model.LinearRegression`, dll — semua class. Memanggil `.fit()`, `.predict()` = method dari class.
2. **Beberapa kasus DA cocok pakai class.** Misal: pipeline analysis yang punya state, custom report generator.
3. **Job interview kadang nanya konsep OOP.** Cukup tahu fundamental — tidak perlu mendalam.

---

## 2. Class & Object

**Class** = template / blueprint.
**Object** = instance dari class (1 contoh konkret).

```python
class Pelanggan:
    def __init__(self, nama, umur, kota):
        self.nama = nama
        self.umur = umur
        self.kota = kota

    def perkenalkan(self):
        print(f"Halo, saya {self.nama} dari {self.kota}")

# Buat object (instance)
andi = Pelanggan("Andi", 28, "Jakarta")
budi = Pelanggan("Budi", 25, "Bandung")

andi.perkenalkan()   # Halo, saya Andi dari Jakarta
budi.perkenalkan()   # Halo, saya Budi dari Bandung

print(andi.nama)     # Andi (akses attribute)
```

Komponen:
- `class Pelanggan:` — bikin class
- `__init__` — constructor (jalan saat bikin object)
- `self` — referensi ke object (mandatory parameter pertama)
- `self.nama` — attribute
- `def perkenalkan(self):` — method (function di dalam class)

---

## 3. Class untuk DA — Contoh Praktis

```python
class AnalisisCabang:
    def __init__(self, nama_cabang, transaksi):
        self.nama_cabang = nama_cabang
        self.transaksi = transaksi

    def total_revenue(self):
        return sum(t["total"] for t in self.transaksi)

    def avg_per_transaksi(self):
        if not self.transaksi:
            return 0
        return self.total_revenue() / len(self.transaksi)

    def summary(self):
        return {
            "cabang": self.nama_cabang,
            "jumlah_trx": len(self.transaksi),
            "total_revenue": self.total_revenue(),
            "avg_per_trx": self.avg_per_transaksi(),
        }


# Pemakaian
trx_tebet = [{"total": 50000}, {"total": 75000}, {"total": 30000}]
tebet = AnalisisCabang("Tebet", trx_tebet)
print(tebet.summary())
```

---

## 4. Inheritance (Pewarisan)

Class bisa "mewarisi" dari class lain.

```python
class PelangganVIP(Pelanggan):
    def __init__(self, nama, umur, kota, level):
        super().__init__(nama, umur, kota)   # panggil constructor parent
        self.level = level
        self.diskon_rate = 0.15 if level == "Gold" else 0.10

    def hitung_diskon(self, total):
        return total * self.diskon_rate

vip = PelangganVIP("Citra", 30, "Surabaya", "Gold")
vip.perkenalkan()                # method dari parent — masih bisa
print(vip.hitung_diskon(100000)) # 15000.0
```

> **Cukup paham fundamental.** OOP advanced (polymorphism, abstract class, multiple inheritance) lebih relevan untuk software engineer, bukan DA.

---

## 5. Special Method (Dunder Methods)

```python
class Transaksi:
    def __init__(self, id_trx, total):
        self.id_trx = id_trx
        self.total = total

    def __repr__(self):
        return f"Transaksi({self.id_trx}, Rp {self.total:,})"

    def __eq__(self, other):
        return self.id_trx == other.id_trx


t1 = Transaksi("TRX001", 50000)
t2 = Transaksi("TRX001", 60000)

print(t1)              # Transaksi(TRX001, Rp 50,000)  — pakai __repr__
print(t1 == t2)        # True (id sama) — pakai __eq__
```

Special method (__init__, __repr__, __eq__, __len__, dll) bikin object kamu integrate dengan Python operations.

---

## 6. Debugging — Find & Fix Bugs

### 6.1 Strategi Debug Pemula: Print Statement

```python
def hitung_total(transaksi):
    print(f"DEBUG: jumlah transaksi = {len(transaksi)}")
    total = 0
    for t in transaksi:
        print(f"DEBUG: processing {t}")
        total += t["total"]
    print(f"DEBUG: total = {total}")
    return total
```

> **Hapus print debug sebelum commit ke Git.**

### 6.2 assert — Validasi Asumsi

```python
def hitung_average(numbers):
    assert len(numbers) > 0, "List tidak boleh kosong"
    return sum(numbers) / len(numbers)

print(hitung_average([10, 20, 30]))   # 20.0
print(hitung_average([]))              # AssertionError: List tidak boleh kosong
```

`assert` cek asumsi. Kalau salah → langsung error dengan pesan jelas.

### 6.3 try / except — Handle Error Gracefully

```python
try:
    total = int(input("Masukkan total: "))
    print(f"Total: Rp {total:,}")
except ValueError:
    print("Input tidak valid — harus angka.")
except Exception as e:
    print(f"Error tidak terduga: {e}")
finally:
    print("Selesai.")
```

Pattern:
- `try` — code yang mungkin error
- `except SpecificError` — handle error tertentu
- `except Exception as e` — catch-all (last resort)
- `finally` — selalu jalan, error atau tidak

### 6.4 VSCode Debugger

Built-in di VSCode. Lebih powerful dari print.

**Cara pakai:**

1. Buka file Python di VSCode
2. Click di gutter (kiri nomor baris) untuk set **breakpoint** (titik merah)
3. F5 → pilih "Python File" → debugger jalan, berhenti di breakpoint
4. Saat berhenti, lihat panel kiri: **Variables** (semua variable scope), **Call Stack**, **Watch**
5. Tombol kontrol:
   - **Continue (F5)** — lanjut sampai breakpoint berikutnya
   - **Step Over (F10)** — eksekusi 1 baris, skip masuk ke function
   - **Step Into (F11)** — masuk ke function call
   - **Step Out (Shift+F11)** — keluar dari function

> **[GAMBAR DIPERLUKAN — VSCode Debugger Active]**
> **Apa:** screenshot VSCode dengan debugger aktif — breakpoint merah, panel Variables di kiri, kontrol Continue/Step di atas.
> **Konteks:** referensi visual untuk peserta yang baru pertama kali pakai debugger.

### 6.5 pdb — Python Debugger (CLI)

```python
import pdb

def hitung_total(transaksi):
    total = 0
    for t in transaksi:
        pdb.set_trace()   # debugger berhenti di sini
        total += t["total"]
    return total

hitung_total([{"total": 50000}, {"total": 75000}])
```

Saat debugger aktif, ketik command:
- `n` — next line
- `s` — step into function
- `c` — continue
- `p variable_name` — print value
- `q` — quit

VSCode Debugger lebih nyaman dari pdb untuk visual. Pdb berguna saat di server tanpa VSCode.

---

## 7. Common Errors & Cara Baca Traceback

```python
def main():
    transaksi = [
        {"id": "T1", "total": 50000},
        {"id": "T2"},   # ⚠️ tidak ada "total"
    ]
    return sum(t["total"] for t in transaksi)

main()
```

Output error:
```
Traceback (most recent call last):
  File "main.py", line 6, in <module>
    main()
  File "main.py", line 5, in main
    return sum(t["total"] for t in transaksi)
  File "main.py", line 5, in <genexpr>
    return sum(t["total"] for t in transaksi)
KeyError: 'total'
```

Cara baca:
1. **Bottom-up** — baris paling bawah = error sebenarnya (`KeyError: 'total'`)
2. **File path & line** — di mana error terjadi
3. Cek context — biasanya value yang missing.

### Common Error untuk DA Pemula

| Error | Penyebab Biasa |
|---|---|
| `NameError: name 'x' not defined` | Typo nama variable, atau belum di-define |
| `TypeError: unsupported operand` | Operasi pada tipe yang tidak compatible (string + int) |
| `KeyError: 'xyz'` | Akses dict key yang tidak ada |
| `IndexError: list out of range` | Akses list index yang tidak ada |
| `ValueError: invalid literal for int()` | int() pada string yang bukan angka |
| `AttributeError: 'NoneType' has no attribute 'x'` | Variable bernilai None tapi diakses .x |
| `ZeroDivisionError` | Divide by zero |
| `FileNotFoundError` | Path file salah |

---

## 8. Latihan

Buka `code/latihan-starter.ipynb`. Ada 5 buggy code untuk fix dengan debugger, plus 1 OOP exercise.

---

## Apa Selanjutnya?

Lanjut ke **Day 3 AM — Pandas Intro** — yang akan jadi kerja inti DA sehari-hari. OOP yang kita pelajari hari ini cukup untuk memanggil `pd.DataFrame`, `df.groupby()`, dll dengan paham.

---

**Akhir Day 2 PM · Week 2**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- OOP intro: class, object, attribute, method, inheritance dasar
- Debugging: print, assert, try/except, VSCode debugger, pdb
- Common errors & cara baca traceback
~2.5 jam · materi.md + latihan/soal.md

"""Generate 3 file Excel kotor untuk latihan Power Query.

Skenario: 3 cabang Kopi Kita kirim laporan dengan format berbeda-beda.
Tujuan latihan: peserta gabung 3 file pakai Power Query dan bersihkan.
"""

import random
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook

random.seed(7)
OUT = Path(__file__).parent / "data"
OUT.mkdir(parents=True, exist_ok=True)

# ====== Cabang Tebet — format rapi tapi inkonsisten format tanggal ======
wb1 = Workbook()
ws = wb1.active
ws.title = "Penjualan"
ws.append(["Tanggal", "Menu", "Qty", "Total", "Metode Bayar"])
for i in range(40):
    ws.append([
        f"{random.randint(1,30):02d}/01/2026",  # DD/MM/YYYY
        random.choice(["Espresso","Americano","Cappuccino","Latte","Es Kopi Susu"]),
        random.randint(1,3),
        random.randint(20000,80000),
        random.choice(["CASH","qris","Debit","kredit"]),  # case inconsistent
    ])
wb1.save(OUT / "tebet-januari-2026.xlsx")

# ====== Cabang Dago — format beda + ada baris kosong ======
wb2 = Workbook()
ws = wb2.active
ws.title = "Sheet1"
ws.append(["Date", "Item", "Quantity", "Amount", "Payment"])
for i in range(40):
    if random.random() < 0.05:
        ws.append([None, None, None, None, None])  # baris kosong
        continue
    ws.append([
        f"2026-01-{random.randint(1,30):02d}",  # YYYY-MM-DD
        random.choice(["Espresso","Americano","Cappuccino","Latte","Matcha Latte","Croissant"]),
        random.randint(1,3),
        random.randint(20000,80000),
        random.choice(["Cash","QRIS","Debit","Kredit"]),
    ])
wb2.save(OUT / "dago-januari-2026.xlsx")

# ====== Bandung Cabang Baru — format CSV-like, ada typo ======
wb3 = Workbook()
ws = wb3.active
ws.title = "data"
ws.append(["TANGGAL", "MENU", "QTY", "TOTAL_RP", "BAYAR"])
for i in range(35):
    ws.append([
        f"Jan {random.randint(1,30)}, 2026",  # text format
        random.choice([" Espresso ", "americano", "Cappucino", "Latte"]),  # typo + leading/trailing space
        random.randint(1,3),
        f"Rp {random.randint(20000,80000):,}",  # format text dengan Rp
        random.choice(["Cash","QRIS","DEBIT","KREDIT","Tunai"]),  # ada "Tunai" alias Cash
    ])
wb3.save(OUT / "kelapa-gading-januari-2026.xlsx")

print("Generated 3 dirty Excel files:")
for f in OUT.glob("*.xlsx"):
    print(f"  {f.name} ({f.stat().st_size} bytes)")

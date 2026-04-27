"""Generate dataset latihan Excel untuk Day 2 AM — Excel Foundation.

Dataset: Penjualan Warung Kopi "Kopi Kita" — fiktif, 200+ baris transaksi
Q1 2026 (Jan-Mar), 2 cabang, 8 menu, 50 pelanggan unique.

Output: data/penjualan-warung-2026.xlsx dengan multiple sheets.
"""

import random
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment

random.seed(42)

OUT_PATH = Path(__file__).parent / "data" / "penjualan-warung-2026.xlsx"
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# ===== Master data =====
CABANG = [
    {"id": "C001", "nama": "Kopi Kita Tebet",   "kota": "Jakarta",  "buka": "07:00", "tutup": "22:00"},
    {"id": "C002", "nama": "Kopi Kita Dago",    "kota": "Bandung",  "buka": "08:00", "tutup": "23:00"},
]

MENU = [
    {"id": "M01", "nama": "Espresso",          "kategori": "Coffee", "harga": 18000, "hpp": 6000},
    {"id": "M02", "nama": "Americano",         "kategori": "Coffee", "harga": 22000, "hpp": 7000},
    {"id": "M03", "nama": "Cappuccino",        "kategori": "Coffee", "harga": 28000, "hpp": 9000},
    {"id": "M04", "nama": "Es Kopi Susu",      "kategori": "Coffee", "harga": 25000, "hpp": 8000},
    {"id": "M05", "nama": "Latte",             "kategori": "Coffee", "harga": 30000, "hpp": 10000},
    {"id": "M06", "nama": "Matcha Latte",      "kategori": "Non-Coffee", "harga": 32000, "hpp": 11000},
    {"id": "M07", "nama": "Croissant",         "kategori": "Pastry", "harga": 25000, "hpp": 10000},
    {"id": "M08", "nama": "Pisang Goreng",     "kategori": "Snack",  "harga": 18000, "hpp": 5000},
]

NAMA_PELANGGAN = [
    "Andi Pratama","Bunga Larasati","Citra Dewi","Dimas Saputra","Eka Wulandari",
    "Fajar Nugroho","Gita Permata","Hari Susanto","Indah Sari","Joko Widodo",
    "Kartika Sari","Lina Marlina","Mahmud Hasan","Nia Ramadhani","Oki Setiana",
    "Putra Wijaya","Qori Astuti","Rini Kusuma","Sandi Pratama","Tina Aulia",
    "Umar Said","Vina Panduwinata","Wati Susanti","Xena Anggraeni","Yanto Saputra",
    "Zahra Salsabila","Adi Nugroho","Bella Saphira","Cinta Laura","Doddy Soekarno",
    "Erlangga Putra","Faridah Hanim","Galih Andika","Hesti Purwadinata","Ivan Gunawan",
    "Jihan Aulia","Kemal Pasha","Laila Munaf","Maman Surya","Nadia Zulkifli",
    "Oka Antara","Prilly Latuconsina","Qonita Rizki","Rahmat Hidayat","Salma Salsabila",
    "Tio Pakusadewo","Umi Pipik","Vino Bastian","Wenda Tan","Xerxes Anggara",
]


def gen_pelanggan_data():
    rows = []
    for i, nama in enumerate(NAMA_PELANGGAN, start=1):
        cabang = random.choice(CABANG)
        rows.append({
            "id_pelanggan": f"P{i:03d}",
            "nama": nama,
            "no_hp": f"08{random.randint(10000000, 99999999)}",
            "kota_asal": cabang["kota"] if random.random() > 0.3 else random.choice(["Jakarta","Bandung","Bekasi","Tangerang","Depok","Bogor"]),
            "tanggal_join": date(2025, 6, 1) + timedelta(days=random.randint(0, 240)),
            "membership": random.choices(["Regular","Silver","Gold"], weights=[60,30,10])[0],
        })
    return rows


def gen_transaksi(n_total=250):
    rows = []
    start_date = date(2026, 1, 1)
    end_date = date(2026, 3, 31)

    for i in range(1, n_total + 1):
        tanggal = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
        cabang = random.choice(CABANG)
        # weight item populer
        menu_weights = [10, 15, 20, 30, 18, 12, 8, 17]
        menu = random.choices(MENU, weights=menu_weights)[0]
        qty = random.choices([1, 2, 3, 4], weights=[60, 25, 10, 5])[0]
        pelanggan_idx = random.randint(0, len(NAMA_PELANGGAN) - 1)

        rows.append({
            "id_transaksi": f"TRX{i:05d}",
            "tanggal": tanggal,
            "id_cabang": cabang["id"],
            "id_pelanggan": f"P{pelanggan_idx+1:03d}",
            "id_menu": menu["id"],
            "qty": qty,
            "harga_satuan": menu["harga"],
            "total": qty * menu["harga"],
            "metode_bayar": random.choices(["Cash","QRIS","Debit","Kredit"], weights=[20, 50, 20, 10])[0],
        })
    rows.sort(key=lambda x: x["tanggal"])
    return rows


def write_sheet(ws, header_fill, rows, columns):
    # header
    for col_idx, (key, label) in enumerate(columns, start=1):
        cell = ws.cell(row=1, column=col_idx, value=label)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")

    for row_idx, row in enumerate(rows, start=2):
        for col_idx, (key, _) in enumerate(columns, start=1):
            ws.cell(row=row_idx, column=col_idx, value=row[key])

    # column width
    for col_idx in range(1, len(columns) + 1):
        ws.column_dimensions[ws.cell(row=1, column=col_idx).column_letter].width = 18


def build_workbook():
    wb = Workbook()
    header_fill = PatternFill("solid", fgColor="1E3A8A")

    # Sheet 1 — Transaksi
    ws_trx = wb.active
    ws_trx.title = "Transaksi"
    transaksi = gen_transaksi(250)
    write_sheet(ws_trx, header_fill, transaksi, [
        ("id_transaksi", "ID Transaksi"),
        ("tanggal", "Tanggal"),
        ("id_cabang", "ID Cabang"),
        ("id_pelanggan", "ID Pelanggan"),
        ("id_menu", "ID Menu"),
        ("qty", "Qty"),
        ("harga_satuan", "Harga Satuan"),
        ("total", "Total"),
        ("metode_bayar", "Metode Bayar"),
    ])

    # Sheet 2 — Menu
    ws_menu = wb.create_sheet("Menu")
    write_sheet(ws_menu, header_fill, MENU, [
        ("id", "ID Menu"),
        ("nama", "Nama Menu"),
        ("kategori", "Kategori"),
        ("harga", "Harga"),
        ("hpp", "HPP (Cost)"),
    ])

    # Sheet 3 — Cabang
    ws_cabang = wb.create_sheet("Cabang")
    write_sheet(ws_cabang, header_fill, CABANG, [
        ("id", "ID Cabang"),
        ("nama", "Nama Cabang"),
        ("kota", "Kota"),
        ("buka", "Jam Buka"),
        ("tutup", "Jam Tutup"),
    ])

    # Sheet 4 — Pelanggan
    ws_pel = wb.create_sheet("Pelanggan")
    pelanggan = gen_pelanggan_data()
    write_sheet(ws_pel, header_fill, pelanggan, [
        ("id_pelanggan", "ID Pelanggan"),
        ("nama", "Nama"),
        ("no_hp", "No HP"),
        ("kota_asal", "Kota Asal"),
        ("tanggal_join", "Tanggal Join"),
        ("membership", "Membership"),
    ])

    # Sheet 5 — Petunjuk
    ws_info = wb.create_sheet("README", 0)
    info_rows = [
        ["DATASET LATIHAN — Kopi Kita (Q1 2026)", ""],
        ["", ""],
        ["Sheet", "Isi"],
        ["Transaksi", "250 baris transaksi Q1 2026 (Jan-Mar) di 2 cabang"],
        ["Menu", "8 menu dengan harga & HPP (cost)"],
        ["Cabang", "2 cabang: Tebet (Jakarta) & Dago (Bandung)"],
        ["Pelanggan", "50 pelanggan dengan info membership"],
        ["", ""],
        ["Asumsi", "Data fiktif untuk latihan. Bukan data perusahaan real."],
        ["Versi", "v1.0 — Savvys Education"],
    ]
    for row_idx, row in enumerate(info_rows, start=1):
        for col_idx, val in enumerate(row, start=1):
            cell = ws_info.cell(row=row_idx, column=col_idx, value=val)
            if row_idx == 1:
                cell.font = Font(bold=True, size=14, color="1E3A8A")
            elif row_idx == 3:
                cell.font = Font(bold=True)
                cell.fill = header_fill
                cell.font = Font(bold=True, color="FFFFFF")
    ws_info.column_dimensions["A"].width = 22
    ws_info.column_dimensions["B"].width = 60

    wb.save(OUT_PATH)
    print(f"Dataset saved: {OUT_PATH}")
    print(f"  Transaksi: {len(transaksi)} rows")
    print(f"  Menu: {len(MENU)} rows")
    print(f"  Cabang: {len(CABANG)} rows")
    print(f"  Pelanggan: {len(pelanggan)} rows")


if __name__ == "__main__":
    build_workbook()

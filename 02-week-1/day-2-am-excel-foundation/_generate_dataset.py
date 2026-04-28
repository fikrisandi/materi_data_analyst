"""Generate dataset latihan Excel untuk Day 2 AM — Excel Foundation.

Dataset: Penjualan Warung Kopi "Kopi Kita" — fiktif, 250 baris transaksi
Q1 2026 (Jan-Mar), 2 cabang, 8 menu, 50 pelanggan unique.

Output: data/penjualan-warung-2026.xlsx
- Sheet data (read-only): Transaksi, Menu, Cabang, Pelanggan
- Sheet kerja stub (siswa isi): A — Mudah, B1 — VLOOKUP Menu,
  B2 — Pivot Cabang x Bayar, C1 — Profit, C2 — Loyal, Insight
"""

import random
from datetime import date, timedelta
from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

random.seed(42)

OUT_PATH = Path(__file__).parent / "data" / "penjualan-warung-2026.xlsx"
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

# ===== Brand colors =====
BRAND_NAVY = "1E3A8A"
BRAND_AMBER = "F59E0B"
BRAND_LIGHT = "FEF3C7"
BRAND_GREY = "F3F4F6"
BRAND_BORDER = "9CA3AF"

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


# ===== Styling helpers =====

def _fill(color):
    return PatternFill("solid", fgColor=color)


def _thin_border():
    side = Side(style="thin", color=BRAND_BORDER)
    return Border(left=side, right=side, top=side, bottom=side)


def write_data_sheet(ws, rows, columns):
    header_fill = _fill(BRAND_NAVY)
    for col_idx, (key, label) in enumerate(columns, start=1):
        cell = ws.cell(row=1, column=col_idx, value=label)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = header_fill
        cell.alignment = Alignment(horizontal="center")

    for row_idx, row in enumerate(rows, start=2):
        for col_idx, (key, _) in enumerate(columns, start=1):
            ws.cell(row=row_idx, column=col_idx, value=row[key])

    for col_idx in range(1, len(columns) + 1):
        ws.column_dimensions[get_column_letter(col_idx)].width = 18

    ws.freeze_panes = "A2"


def write_banner(ws, title, subtitle, span_cols):
    """Banner judul + subtitle di top sheet."""
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=span_cols)
    cell = ws.cell(row=1, column=1, value=title)
    cell.font = Font(bold=True, size=14, color="FFFFFF")
    cell.fill = _fill(BRAND_NAVY)
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.row_dimensions[1].height = 28

    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=span_cols)
    cell = ws.cell(row=2, column=1, value=subtitle)
    cell.font = Font(italic=True, color="374151")
    cell.fill = _fill(BRAND_LIGHT)
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1, wrap_text=True)
    ws.row_dimensions[2].height = 36


def write_table_header(ws, row, headers, widths=None):
    fill = _fill(BRAND_AMBER)
    for col_idx, label in enumerate(headers, start=1):
        cell = ws.cell(row=row, column=col_idx, value=label)
        cell.font = Font(bold=True, color="1F2937")
        cell.fill = fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = _thin_border()
    if widths:
        for col_idx, w in enumerate(widths, start=1):
            ws.column_dimensions[get_column_letter(col_idx)].width = w
    ws.row_dimensions[row].height = 30


def write_empty_cell(ws, row, col, hint=""):
    cell = ws.cell(row=row, column=col, value=hint or None)
    cell.border = _thin_border()
    cell.fill = _fill("FFFFFF")
    cell.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    return cell


# ===== Sheet builders =====

def build_sheet_readme(wb):
    ws = wb.create_sheet("README", 0)
    write_banner(
        ws,
        "DATASET LATIHAN — Kopi Kita (Q1 2026)",
        "Dataset fiktif untuk latihan Excel Foundation. Bukan data perusahaan real. v2.0 — Savvys Education",
        span_cols=2,
    )

    write_table_header(ws, row=4, headers=["Sheet", "Isi"], widths=[28, 78])

    info_rows = [
        ("--- DATASET (jangan diubah) ---", ""),
        ("Transaksi", "250 baris transaksi Q1 2026 (Jan-Mar) di 2 cabang"),
        ("Menu", "8 menu dengan harga & HPP (cost)"),
        ("Cabang", "2 cabang: Tebet (Jakarta) & Dago (Bandung)"),
        ("Pelanggan", "50 pelanggan dengan info membership"),
        ("--- SHEET KERJA (kerjakan di sini) ---", ""),
        ("A — Mudah", "Bagian A.1–A.5: SUM, AVERAGE, COUNTIF, SUMIF, MAX/INDEX-MATCH"),
        ("B1 — VLOOKUP Menu", "Bagian B.1: tambah kolom Nama Menu pakai VLOOKUP"),
        ("B2 — Pivot Cabang x Bayar", "Bagian B.2: Pivot Table Revenue per Cabang × Metode Bayar"),
        ("C1 — Profit", "Bagian C.1: hitung HPP per Transaksi & Profit, lalu pivot"),
        ("C2 — Loyal", "Bagian C.2: pivot pelanggan loyal, ambil Top-5"),
        ("Insight", "Tulis 3 insight bisnis dari hasil analisis"),
    ]
    for i, (sheet, desc) in enumerate(info_rows, start=5):
        is_section = sheet.startswith("---")
        c1 = ws.cell(row=i, column=1, value=sheet)
        c2 = ws.cell(row=i, column=2, value=desc)
        if is_section:
            c1.font = Font(bold=True, color=BRAND_NAVY)
            c1.fill = _fill(BRAND_GREY)
            c2.fill = _fill(BRAND_GREY)
        else:
            c1.font = Font(bold=True)
            c1.alignment = Alignment(indent=1)
            c2.alignment = Alignment(indent=1, wrap_text=True)
        c1.border = _thin_border()
        c2.border = _thin_border()

    notes_row = len(info_rows) + 6
    ws.cell(row=notes_row, column=1, value="ATURAN").font = Font(bold=True, color=BRAND_NAVY)
    notes = [
        "1. JANGAN edit sheet Transaksi/Menu/Cabang/Pelanggan — itu data sumber.",
        "2. Kerjakan setiap soal di sheet kerja yang sudah disediakan (A — Mudah, B1, B2, C1, C2, Insight).",
        "3. Setelah selesai, Save As → latihan/jawaban.xlsx, lalu push ke portfolio repo.",
    ]
    for j, note in enumerate(notes, start=notes_row + 1):
        ws.cell(row=j, column=1, value=note).alignment = Alignment(wrap_text=True, vertical="center")
        ws.merge_cells(start_row=j, start_column=1, end_row=j, end_column=2)


def build_sheet_a_mudah(wb):
    ws = wb.create_sheet("A — Mudah")
    write_banner(
        ws,
        "Bagian A — Soal Mudah (5 soal + 1 bonus)",
        "Tulis FORMULA di kolom 'Hasil'. Excel akan tampilkan nilainya. JANGAN tulis nilai manual — wajib pakai formula.",
        span_cols=4,
    )

    write_table_header(
        ws, row=4,
        headers=["Soal", "Petunjuk Formula", "Hasil (tulis formula di sini)", "Catatan"],
        widths=[42, 48, 32, 32],
    )

    soal = [
        ("A.1 — Total revenue Q1 2026 (Jan–Mar)",
         "=SUM(Transaksi!H2:H251)", "", ""),
        ("A.2 — Rata-rata Total per transaksi (bulatkan ke integer)",
         "=ROUND(AVERAGE(Transaksi!H2:H251), 0)", "", ""),
        ("A.3 — Jumlah transaksi yang pakai QRIS",
         "=COUNTIF(Transaksi!I2:I251, \"QRIS\")", "", ""),
        ("A.4 — Total revenue Cabang Tebet (C001)",
         "=SUMIF(Transaksi!C2:C251, \"C001\", Transaksi!H2:H251)", "", ""),
        ("A.5 — Nominal transaksi terbesar Q1 2026",
         "=MAX(Transaksi!H2:H251)", "", ""),
        ("A.5 (Bonus) — ID Transaksi terbesar (pakai INDEX-MATCH)",
         "=INDEX(Transaksi!A2:A251, MATCH(MAX(Transaksi!H2:H251), Transaksi!H2:H251, 0))", "", ""),
    ]
    for i, (s, p, h, c) in enumerate(soal, start=5):
        ws.cell(row=i, column=1, value=s).alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.cell(row=i, column=2, value=p).alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        ws.cell(row=i, column=2).font = Font(name="Consolas", size=10, color="6B7280")
        write_empty_cell(ws, i, 3)
        write_empty_cell(ws, i, 4)
        ws.cell(row=i, column=1).border = _thin_border()
        ws.cell(row=i, column=2).border = _thin_border()
        ws.row_dimensions[i].height = 38

    ws.freeze_panes = "A4"


def _copy_transaksi_block(ws, start_row, transaksi, extra_headers):
    """Copy seluruh transaksi (kolom A–I) + tambah kolom kosong ber-header."""
    base_headers = [
        "ID Transaksi", "Tanggal", "ID Cabang", "ID Pelanggan",
        "ID Menu", "Qty", "Harga Satuan", "Total", "Metode Bayar",
    ]
    all_headers = base_headers + extra_headers
    write_table_header(
        ws, row=start_row,
        headers=all_headers,
        widths=[14, 13, 11, 13, 10, 7, 14, 14, 14] + [22] * len(extra_headers),
    )

    for r, trx in enumerate(transaksi, start=start_row + 1):
        ws.cell(row=r, column=1, value=trx["id_transaksi"])
        ws.cell(row=r, column=2, value=trx["tanggal"]).number_format = "yyyy-mm-dd"
        ws.cell(row=r, column=3, value=trx["id_cabang"])
        ws.cell(row=r, column=4, value=trx["id_pelanggan"])
        ws.cell(row=r, column=5, value=trx["id_menu"])
        ws.cell(row=r, column=6, value=trx["qty"])
        ws.cell(row=r, column=7, value=trx["harga_satuan"]).number_format = "#,##0"
        ws.cell(row=r, column=8, value=trx["total"]).number_format = "#,##0"
        ws.cell(row=r, column=9, value=trx["metode_bayar"])

        for j in range(len(extra_headers)):
            write_empty_cell(ws, r, 10 + j)

    return start_row + 1, start_row + len(transaksi)  # data range


def build_sheet_b1(wb, transaksi):
    ws = wb.create_sheet("B1 — VLOOKUP Menu")
    write_banner(
        ws,
        "Bagian B.1 — VLOOKUP Nama Menu",
        "Isi kolom 'Nama Menu' (kolom J) pakai VLOOKUP ke sheet Menu. Drag formula dari J5 sampai J254.",
        span_cols=10,
    )
    ws.cell(row=3, column=1,
            value="HINT: =VLOOKUP(E5, Menu!$A$2:$E$9, 2, FALSE)"
            ).font = Font(name="Consolas", size=10, italic=True, color="6B7280")
    ws.merge_cells("A3:J3")

    _copy_transaksi_block(ws, start_row=4, transaksi=transaksi, extra_headers=["Nama Menu"])
    ws.freeze_panes = "A5"


def build_sheet_b2(wb):
    ws = wb.create_sheet("B2 — Pivot Cabang x Bayar")
    write_banner(
        ws,
        "Bagian B.2 — Pivot Table Revenue per Cabang × Metode Bayar",
        "Bikin Pivot Table dari sheet Transaksi. Tempel hasilnya di area di bawah.",
        span_cols=6,
    )

    instruksi = [
        "Langkah:",
        "1. Klik sheet 'Transaksi' → blok A1:I251 → Insert → PivotTable → New Worksheet (atau Existing: pilih sel A12 di sheet ini).",
        "2. Drag 'ID Cabang' ke Rows.",
        "3. Drag 'Metode Bayar' ke Columns.",
        "4. Drag 'Total' ke Values (pastikan Sum of Total).",
        "5. Format angka: kanan-klik → Value Field Settings → Number Format → Number, separator ribuan.",
        "6. Pertanyaan: Cabang mana yang QRIS-nya paling dominan? Tulis jawabanmu di sel A22.",
    ]
    for i, t in enumerate(instruksi, start=3):
        cell = ws.cell(row=i, column=1, value=t)
        cell.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        if i == 3:
            cell.font = Font(bold=True, color=BRAND_NAVY)
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=6)

    ws.cell(row=11, column=1, value="↓ TEMPEL PIVOT TABLE DI SINI ↓").font = Font(bold=True, color=BRAND_AMBER)

    ws.cell(row=21, column=1, value="Jawaban analisis:").font = Font(bold=True)
    write_empty_cell(ws, 22, 1, hint="Tulis cabang mana yang QRIS-nya dominan + alasan singkat...")
    ws.merge_cells("A22:F22")
    ws.row_dimensions[22].height = 40

    for col, w in enumerate([18, 18, 18, 18, 18, 18], start=1):
        ws.column_dimensions[get_column_letter(col)].width = w


def build_sheet_c1(wb, transaksi):
    ws = wb.create_sheet("C1 — Profit")
    write_banner(
        ws,
        "Bagian C.1 — Profit per Transaksi",
        "Isi kolom J 'HPP per Transaksi' (= HPP menu × Qty) dan kolom K 'Profit' (= Total − HPP per Transaksi). Lalu jawab pertanyaan di bawah.",
        span_cols=11,
    )

    hint = "HINT — J5: =VLOOKUP(E5, Menu!$A$2:$E$9, 5, FALSE) * F5    |    K5: =H5 - J5"
    ws.cell(row=3, column=1, value=hint).font = Font(name="Consolas", size=10, italic=True, color="6B7280")
    ws.merge_cells("A3:K3")

    _copy_transaksi_block(ws, start_row=4, transaksi=transaksi, extra_headers=["HPP per Transaksi", "Profit"])

    pivot_row = 4 + len(transaksi) + 3
    ws.cell(row=pivot_row, column=1, value="Pivot Profit per Cabang").font = Font(bold=True, size=12, color=BRAND_NAVY)
    ws.cell(row=pivot_row + 1, column=1,
            value="Bikin Pivot Table dari sheet ini (kolom A–K), Rows: ID Cabang, Values: Sum of Profit. Tempel di bawah."
            ).alignment = Alignment(wrap_text=True)
    ws.merge_cells(start_row=pivot_row + 1, start_column=1, end_row=pivot_row + 1, end_column=11)

    q_row = pivot_row + 4
    ws.cell(row=q_row, column=1, value="Pertanyaan: cabang mana yang PROFIT-nya lebih tinggi (bukan revenue)?").font = Font(bold=True)
    ws.merge_cells(start_row=q_row, start_column=1, end_row=q_row, end_column=11)
    write_empty_cell(ws, q_row + 1, 1, hint="Jawaban + alasan singkat...")
    ws.merge_cells(start_row=q_row + 1, start_column=1, end_row=q_row + 1, end_column=11)
    ws.row_dimensions[q_row + 1].height = 40

    ws.freeze_panes = "A5"


def build_sheet_c2(wb):
    ws = wb.create_sheet("C2 — Loyal")
    write_banner(
        ws,
        "Bagian C.2 — Pelanggan Loyal (Top 5)",
        "Bikin pivot di area kosong, sort descending, lalu rangkum Top-5 ke tabel di bawah dengan VLOOKUP nama.",
        span_cols=5,
    )

    instruksi = [
        "Langkah:",
        "1. Insert → PivotTable dari sheet Transaksi (A1:I251). Letakkan di sel A12 sheet ini.",
        "2. Rows: ID Pelanggan. Values: Count of ID Transaksi (otomatis Count).",
        "3. Sort descending pada Count of ID Transaksi.",
        "4. Salin 5 ID Pelanggan teratas ke tabel 'Top 5' di bawah, lalu pakai VLOOKUP untuk dapat Nama-nya.",
    ]
    for i, t in enumerate(instruksi, start=3):
        cell = ws.cell(row=i, column=1, value=t)
        cell.alignment = Alignment(wrap_text=True, vertical="center", indent=1)
        if i == 3:
            cell.font = Font(bold=True, color=BRAND_NAVY)
        ws.merge_cells(start_row=i, start_column=1, end_row=i, end_column=5)

    ws.cell(row=11, column=1, value="↓ TEMPEL PIVOT TABLE DI SINI (mulai A12) ↓").font = Font(bold=True, color=BRAND_AMBER)

    top5_row = 25
    ws.cell(row=top5_row, column=1, value="Tabel Top 5 Pelanggan Loyal").font = Font(bold=True, size=12, color=BRAND_NAVY)
    ws.merge_cells(start_row=top5_row, start_column=1, end_row=top5_row, end_column=5)

    write_table_header(
        ws, row=top5_row + 1,
        headers=["Rank", "ID Pelanggan", "Jumlah Kunjungan", "Nama (VLOOKUP)", "Kota Asal"],
        widths=[8, 16, 18, 26, 16],
    )
    for rank in range(1, 6):
        write_empty_cell(ws, top5_row + 1 + rank, 1, hint=str(rank))
        for col in range(2, 6):
            write_empty_cell(ws, top5_row + 1 + rank, col)

    hint_row = top5_row + 9
    ws.cell(row=hint_row, column=1,
            value="HINT — Nama: =VLOOKUP(B27, Pelanggan!$A$2:$F$51, 2, FALSE)    |    Kota Asal: ganti index 2 jadi 4"
            ).font = Font(name="Consolas", size=10, italic=True, color="6B7280")
    ws.merge_cells(start_row=hint_row, start_column=1, end_row=hint_row, end_column=5)


def build_sheet_insight(wb):
    ws = wb.create_sheet("Insight")
    write_banner(
        ws,
        "Tugas — 3 Insight Bisnis dari Analisis",
        "Tulis 3 temuan bisnis berbasis data hasil pengerjaan Bagian A, B, dan C. Setiap insight WAJIB punya data pendukung (angka konkret).",
        span_cols=2,
    )

    write_table_header(ws, row=4, headers=["Insight", "Isi"], widths=[28, 80])

    rows = [
        ("Insight #1", ""),
        ("  ↳ Data pendukung", ""),
        ("  ↳ Saran bisnis", ""),
        ("Insight #2", ""),
        ("  ↳ Data pendukung", ""),
        ("  ↳ Saran bisnis", ""),
        ("Insight #3", ""),
        ("  ↳ Data pendukung", ""),
        ("  ↳ Saran bisnis", ""),
    ]
    for i, (label, _) in enumerate(rows, start=5):
        c1 = ws.cell(row=i, column=1, value=label)
        c1.font = Font(bold=label.strip().startswith("Insight"))
        c1.alignment = Alignment(indent=1, vertical="center")
        c1.border = _thin_border()
        write_empty_cell(ws, i, 2)
        ws.row_dimensions[i].height = 28

    contoh_row = len(rows) + 6
    ws.cell(row=contoh_row, column=1, value="CONTOH (jangan disalin persis)").font = Font(bold=True, color=BRAND_NAVY)
    ws.merge_cells(start_row=contoh_row, start_column=1, end_row=contoh_row, end_column=2)
    contoh = [
        ("Insight contoh", "Cabang Dago lebih unggul di profitabilitas walau revenue cuma sedikit lebih tinggi."),
        ("  ↳ Data pendukung", "Profit C002 = Rp 3.774.000 vs C001 = Rp 3.259.000 (gap Rp 515.000, 16% lebih tinggi)."),
        ("  ↳ Saran bisnis", "Replikasi mix menu Dago ke Tebet — kemungkinan ada item margin tinggi yang lebih sering laku di Dago."),
    ]
    for i, (label, isi) in enumerate(contoh, start=contoh_row + 1):
        ws.cell(row=i, column=1, value=label).font = Font(italic=True, color="6B7280")
        ws.cell(row=i, column=2, value=isi).alignment = Alignment(wrap_text=True, vertical="center")
        ws.cell(row=i, column=2).font = Font(italic=True, color="6B7280")
        ws.row_dimensions[i].height = 30


def build_workbook():
    wb = Workbook()
    wb.remove(wb.active)

    transaksi = gen_transaksi(250)
    pelanggan = gen_pelanggan_data()

    # ===== Data sheets (read-only by convention) =====
    ws_trx = wb.create_sheet("Transaksi")
    write_data_sheet(ws_trx, transaksi, [
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

    ws_menu = wb.create_sheet("Menu")
    write_data_sheet(ws_menu, MENU, [
        ("id", "ID Menu"),
        ("nama", "Nama Menu"),
        ("kategori", "Kategori"),
        ("harga", "Harga"),
        ("hpp", "HPP (Cost)"),
    ])

    ws_cabang = wb.create_sheet("Cabang")
    write_data_sheet(ws_cabang, CABANG, [
        ("id", "ID Cabang"),
        ("nama", "Nama Cabang"),
        ("kota", "Kota"),
        ("buka", "Jam Buka"),
        ("tutup", "Jam Tutup"),
    ])

    ws_pel = wb.create_sheet("Pelanggan")
    write_data_sheet(ws_pel, pelanggan, [
        ("id_pelanggan", "ID Pelanggan"),
        ("nama", "Nama"),
        ("no_hp", "No HP"),
        ("kota_asal", "Kota Asal"),
        ("tanggal_join", "Tanggal Join"),
        ("membership", "Membership"),
    ])

    # ===== Sheet kerja stub =====
    build_sheet_a_mudah(wb)
    build_sheet_b1(wb, transaksi)
    build_sheet_b2(wb)
    build_sheet_c1(wb, transaksi)
    build_sheet_c2(wb)
    build_sheet_insight(wb)

    # ===== README di posisi pertama =====
    build_sheet_readme(wb)

    wb.save(OUT_PATH)
    print(f"Dataset saved: {OUT_PATH}")
    print(f"  Transaksi: {len(transaksi)} rows")
    print(f"  Menu: {len(MENU)} rows")
    print(f"  Cabang: {len(CABANG)} rows")
    print(f"  Pelanggan: {len(pelanggan)} rows")
    print(f"  Sheet kerja stub: A — Mudah, B1, B2, C1, C2, Insight")


if __name__ == "__main__":
    build_workbook()

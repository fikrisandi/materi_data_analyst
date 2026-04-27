# Design Template PPT — Detail

> **Status:** Disepakati 2026-04-26. Template ini dipakai konsisten untuk semua deck (Pre-Week, Week 1–4, Elective).

Dokumen ini turunan dari `konsep-utama.md` Section 12. Berisi spesifikasi visual + sample layout untuk tiap jenis slide.

---

## 1. Brand Identity

**Nama brand:** **Savvys Education** ✅
**Tone:** Modern, friendly-professional, anti-intimidating untuk pemula
**Vibe referensi:** mid antara Stripe docs (clean) + Notion (warm) + Linear (modern minimalist)
**Footer signature:** `Savvys Education · 2026`

---

## 2. Color Palette (sumber tunggal)

```
PRIMARY      #1E3A8A    Deep Blue       header, judul, accent utama
PRIMARY-50   #EFF6FF    Very light blue background tint
ACCENT       #14B8A6    Teal            highlight, link, callout positif
WARNING      #F59E0B    Amber           catatan penting, "perhatian"
DANGER       #EF4444    Coral           common mistakes, "jangan dilakukan"
SUCCESS      #22C55E    Green           checkmark, "berhasil"

BG-LIGHT     #FAFAFA    Off-white       BG default
BG-DARK      #0F172A    Deep navy       BG slide code & section divider
TEXT         #1F2937    Charcoal        body di BG terang
TEXT-INV     #F8FAFC    Off-white       body di BG gelap
MUTED        #6B7280    Gray            caption, footnote, secondary
BORDER       #E5E7EB    Light gray      garis pembatas, divider
```

**Aturan:**
- Primary + Accent boleh muncul bersamaan, tapi salah satu harus dominan dalam 1 slide
- Warning & Danger hanya untuk callout — jangan jadi BG penuh
- Tidak boleh ada warna lain di luar palette ini kecuali untuk screenshot/foto asli

---

## 3. Typography

| Role | Font | Size (16:9 PPT std) | Weight | Catatan |
|---|---|---|---|---|
| H1 (judul cover) | Poppins | 54pt | Bold | Hanya di slide cover & section divider |
| H1 (judul slide) | Inter | 36pt | Bold | Default judul setiap slide |
| H2 (sub judul) | Inter | 28pt | SemiBold | |
| H3 (label) | Inter | 22pt | SemiBold | All-caps untuk emphasis |
| Body | Inter | 20pt | Regular | Default body text |
| Body small | Inter | 18pt | Regular | Untuk slide padat |
| Caption / footer | Inter | 14pt | Regular | Footer, timestamp, source |
| Code | JetBrains Mono | 18pt | Regular | Bg gelap recommended |
| Code inline | JetBrains Mono | 18pt | Regular | Bg `#EFF6FF` tipis, padding 2px |

**Line height:** 1.4 untuk body, 1.2 untuk heading.
**Letter spacing:** 0 untuk body, -0.02em untuk heading besar.

---

## 4. Grid & Spacing

- **Aspect ratio:** 16:9 (1920×1080 atau 13.33×7.5 inci)
- **Margin slide:** 80px kiri/kanan, 60px atas/bawah (di canvas 1920×1080)
- **Grid:** 12 kolom dengan gutter 24px
- **Spacing scale:** 8 / 16 / 24 / 32 / 48 / 64 (kelipatan 8)

---

## 5. 12 Layout Templates

### L1 — Cover (slide pertama tiap sesi)
```
┌───────────────────────────────────────────────────┐
│  [BG: PRIMARY gradient or image overlay]          │
│                                                   │
│  Week 1 / Day 2 PM                  ← H3, MUTED   │
│                                                   │
│  Pandas untuk Data Analysis         ← H1 54pt     │
│  Mengolah Data Tabular dengan Python ← H2 inverse │
│                                                   │
│  [icon ilustrasi besar di kanan]                  │
│                                                   │
│                                                   │
│  Savvys Education · 2026                 ← caption     │
└───────────────────────────────────────────────────┘
```

### L2 — Section Divider (antar bagian besar)
```
┌───────────────────────────────────────────────────┐
│  [BG: BG-DARK]                                    │
│                                                   │
│  PART 02                            ← H3 ACCENT   │
│                                                   │
│  Filtering & Slicing Data           ← H1 inverse  │
│                                                   │
│  [garis horizontal ACCENT 200px]                  │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L3 — Agenda / TOC
```
┌───────────────────────────────────────────────────┐
│  Agenda Sesi                        ← H1          │
│                                                   │
│  ① Konsep dasar pandas              [icon]        │
│  ② Membuat & membaca DataFrame      [icon]        │
│  ③ Filtering dengan .loc dan .iloc  [icon]        │
│  ④ Latihan langsung                 [icon]        │
│  ⑤ Insight & next step              [icon]        │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L4 — Concept "Why" (signature layout — 5 Pilar #1)
```
┌───────────────────────────────────────────────────┐
│                                                   │
│  [icon  │  Kenapa JOIN ada?         ← H1          │
│   64px] │                                         │
│         │  Bayangkan kamu punya warung. Buku      │
│         │  pencatatan kamu pisah: 1 buku isi      │
│         │  daftar pelanggan, 1 buku lagi isi      │
│         │  daftar transaksi...                    │
│         │                                         │
│         │  [callout ACCENT box]                   │
│         │  → JOIN = menyambungkan dua tabel       │
│         │    lewat kolom yang nilainya cocok.     │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L5 — Content (text + image split 50/50)
```
┌───────────────────────────────────────────────────┐
│  Anatomi DataFrame                  ← H1          │
│                                                   │
│  ┌──────────────────┐  ┌────────────────────┐    │
│  │  Body text       │  │  [Image / diagram] │    │
│  │  • point 1       │  │                    │    │
│  │  • point 2       │  │                    │    │
│  │  • point 3       │  │                    │    │
│  └──────────────────┘  └────────────────────┘    │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L6 — Bullet List (icon + text per row)
```
┌───────────────────────────────────────────────────┐
│  Kapan Pakai LEFT JOIN?             ← H1          │
│                                                   │
│  [✓]  Cari pelanggan yang dorman                 │
│  [✓]  Audit data yang missing di tabel kanan     │
│  [✓]  Laporan completeness                       │
│  [✗]  BUKAN untuk performance optimization       │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L7 — Code Block (BG gelap)
```
┌───────────────────────────────────────────────────┐
│  Demo: Filter pakai .loc            ← H1          │
│                                                   │
│  ┌─────────────────────────────────────────────┐ │
│  │ [BG-DARK, code dgn syntax highlight]        │ │
│  │                                             │ │
│  │  import pandas as pd                        │ │
│  │                                             │ │
│  │  df = pd.read_csv("penjualan.csv")          │ │
│  │  hasil = df.loc[df["kota"] == "Jakarta"]    │ │
│  │  print(hasil.head())                        │ │
│  │                                             │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  💡 Output: 124 baris dengan kota Jakarta        │
└───────────────────────────────────────────────────┘
```

### L8 — Comparison Table
```
┌───────────────────────────────────────────────────┐
│  Excel vs SQL vs Pandas             ← H1          │
│                                                   │
│  ┌──────────┬──────────┬──────────┬───────────┐  │
│  │ Operasi  │ Excel    │ SQL      │ Pandas    │  │
│  ├──────────┼──────────┼──────────┼───────────┤  │
│  │ Filter   │ Filter   │ WHERE    │ .loc      │  │
│  │ Group    │ Pivot    │ GROUP BY │ .groupby  │  │
│  │ Join     │ VLOOKUP  │ JOIN     │ .merge    │  │
│  └──────────┴──────────┴──────────┴───────────┘  │
└───────────────────────────────────────────────────┘
```

### L9 — Diagram / Flow
```
┌───────────────────────────────────────────────────┐
│  Alur ETL Sederhana                 ← H1          │
│                                                   │
│  ┌──────┐  →  ┌──────┐  →  ┌────────┐ → ┌──────┐ │
│  │ CSV  │     │Python│     │ Clean  │   │Excel │ │
│  │ raw  │     │script│     │ data   │   │viz   │ │
│  └──────┘     └──────┘     └────────┘   └──────┘ │
│   Extract     Transform     Output      Visualize│
│                                                   │
└───────────────────────────────────────────────────┘
```

### L10 — Insight / Key Takeaway (signature — Pilar #5)
```
┌───────────────────────────────────────────────────┐
│  [BG: ACCENT tipis #14B8A6 + 10% opacity]         │
│                                                   │
│  💡 INSIGHT                         ← H3 ACCENT   │
│                                                   │
│  Pelanggan dari kota Tier-2 kontribusi 38%        │
│  revenue tapi hanya 12% effort marketing.         │
│                                                   │
│  → Reallocate budget Q2.            ← action      │
│                                                   │
└───────────────────────────────────────────────────┘
```

### L11 — Exercise / Practice
```
┌───────────────────────────────────────────────────┐
│  [BG: WARNING tipis #F59E0B + 8% opacity]         │
│                                                   │
│  🎯 LATIHAN 2.3                     ← H3 WARNING  │
│                                                   │
│  Dari dataset penjualan.csv, tampilkan:           │
│  1. Top 5 produk dengan revenue tertinggi         │
│  2. Total transaksi per bulan                     │
│  3. Rata-rata order value per kota                │
│                                                   │
│  Estimasi: 15 menit · Output: notebook            │
└───────────────────────────────────────────────────┘
```

### L12 — Resources / Next Step
```
┌───────────────────────────────────────────────────┐
│  Praktik Lanjutan                   ← H1          │
│                                                   │
│  [HackerRank logo] Basic Select                   │
│   → hackerrank.com/.../basic-select               │
│                                                   │
│  [DataLemur logo] Top Cities by Sales             │
│   → datalemur.com/questions/top-cities            │
│                                                   │
│  [Forage logo] BCG Data Analytics Job Sim         │
│   → theforage.com/.../bcg-data-analytics          │
│                                                   │
└───────────────────────────────────────────────────┘
```

---

## 6. Komponen Konsisten Tiap Slide

### Footer (semua slide kecuali Cover & Section Divider)
```
┌───────────────────────────────────────────────────┐
│ ...                                               │
│                                                   │
│                                                   │
├───────────────────────────────────────────────────┤
│ Week 1 · Day 2 PM      [LOGO]            12 / 38  │
│ ↑ section path          ↑ brand          ↑ pages  │
└───────────────────────────────────────────────────┘
```
Font: 14pt MUTED. Tinggi footer: 40px.

### Header (subtle, opsional)
Di slide content padat, header bisa dipakai untuk breadcrumb mini:
```
Week 1 > Day 2 PM > Filtering Data
```
Font 12pt MUTED, di atas judul slide.

---

## 7. Iconography

- **Library:** Lucide Icons (lucide.dev) — modern, free, MIT, lengkap
- **Style:** Outline 2px, ukuran konsisten (24px / 32px / 64px)
- **Warna:** sama dengan TEXT atau MUTED, kecuali kalau highlighted (PRIMARY/ACCENT)
- **Hindari:** mix emoji + flat icon + 3D icon dalam 1 slide

Icon set yang sering dipakai:
- 💡 → `lightbulb` (insight)
- 🎯 → `target` (latihan)
- ⚠️ → `alert-triangle` (warning)
- ❌ → `x-circle` (mistake)
- ✅ → `check-circle` (success)
- 📊 → `bar-chart-3` (data viz)
- 🗃️ → `database` (SQL/db)
- 🐼 → `panda` icon kustom (pandas — cari dari kit)

---

## 8. Animasi & Transisi

**Aturan keras:**
- Tidak ada efek transisi mencolok antar slide. Default = **None** atau **Fade** (200ms)
- Tidak ada animasi text masuk huruf-per-huruf, bouncing, spinning
- Animasi pengungkap bertahap (bullet point muncul satu-satu) **boleh**, tapi cuma di slide kompleks (max 1 layer animasi)
- Code block muncul utuh — jangan animasi line-by-line saat presentasi (mengganggu fokus)

---

## 9. Workflow Implementasi

### 9.1 Untuk pembuatan baru (per sesi)

1. **Tulis draft Markdown** di `<sesi>/materi.md` dengan slide separator `---`
2. **Sisipkan placeholder screenshot** dengan `📸 [SS NEEDED]` (lihat Section 13 konsep-utama)
3. **Render ke PPT** — pakai salah satu:
   - Gamma (import markdown) — paling cepat untuk eyecatching
   - Pandoc + reference doc PPT (kustom template) — paling otomatis
   - Manual di PowerPoint pakai master template `template-master.pptx`
4. **Apply template** — pastikan semua slide pakai master layout dari L1–L12
5. **Polish manual di PPT** — perbaiki gambar, animasi, alignment

### 9.2 File master template ✅

Master template disimpan di `00-konsep/template-master.pptx` (akan di-generate setelah konten Pre-Week siap).

**Aturan pemakaian master:**
- Sebelum mengedit untuk sesi baru, **selalu duplikasi dulu** (`Save As` ke folder sesi yang dituju)
- Jangan edit `template-master.pptx` langsung — ini master, perubahan di sini berlaku ke semua deck baru
- Kalau ada update template (warna, font, layout), update master, lalu propagate manual ke deck yang sudah ada (catat di changelog)

---

## 10. Checklist Quality (sebelum slide dianggap final)

- [ ] Semua warna pakai palette Section 2 (cek tidak ada warna liar)
- [ ] Semua font pakai Inter / Poppins / JetBrains Mono saja
- [ ] Footer + nomor halaman muncul (kecuali Cover/Section Divider)
- [ ] Setiap konsep teknis baru pakai layout L4 (Why + analogi)
- [ ] Setiap section ada minimal 1 layout L10 (Insight) di akhir
- [ ] Code block pakai L7 (BG gelap)
- [ ] Latihan pakai L11 (BG amber)
- [ ] Tidak ada animasi mencolok
- [ ] Placeholder `📸 [SS NEEDED]` belum diganti? — list-kan untuk di-capture nanti
- [ ] Spell-check + istilah English konsisten capitalization

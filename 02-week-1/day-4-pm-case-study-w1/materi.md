# Week 1 · Day 4 PM
# Mini Case Study — Analisis Quarterly Kopi Kita

> **Tujuan modul:** Integrasi semua skill Week 1 untuk jawab 1 case bisnis nyata. Output: deck analisis 3-5 slide siap presentasi.
>
> **Estimasi waktu:** 3 jam · **Format:** kerja mandiri / berpasangan.

---

## 1. Brief

### Konteks

Kamu adalah Junior Data Analyst yang baru bergabung di **Kopi Kita** — chain warung kopi specialty dengan 2 cabang (Tebet di Jakarta, Dago di Bandung). Founder ingin **review kinerja Q1 2026** sebelum keputusan ekspansi cabang ke-3.

### Pertanyaan Founder

> "Saya butuh tahu: (a) cabang mana yang **lebih sehat secara bisnis**, (b) apa **sumber utama revenue** kita, (c) ada **opportunity yang belum dieksplorasi** nggak. Saya mau presentasi 10 menit, deck 3-5 slide saja, fokus ke insight + rekomendasi konkret."

### Dataset

`data/kopi_kita.db` (SQLite) — 4 tabel: cabang, menu, pelanggan, transaksi (250 transaksi Q1 2026).

---

## 2. Framework Analisis

Pakai struktur **PSQ** (Problem → Solution → Question) yang umum di consulting:

### Step 1: Decompose Problem

Pertanyaan founder vague. Pecah jadi sub-questions yang bisa diukur:

**Cabang lebih sehat:**
- Revenue total per cabang
- Jumlah transaksi & average order value
- Profit margin (revenue - HPP×qty)
- Pelanggan unique & repeat rate

**Sumber utama revenue:**
- Top menu by revenue & qty
- Top kategori menu
- Distribusi metode bayar
- Pareto: 20% pelanggan kontribusi berapa % revenue?

**Opportunity:**
- Hari/bulan rendah → bisa di-promote
- Menu profit tinggi tapi qty rendah → push marketing
- Pelanggan dorman (tidak transaksi)
- Cabang dengan growth slowest

### Step 2: Pilih Metric

Untuk tiap sub-question, pilih 1-2 metric KEY. Hindari "tampilkan semua" — fokus pada yang akan **mengubah keputusan founder**.

### Step 3: Compute & Visualize

Pakai SQL untuk query, Excel untuk visualize (bar chart, pivot table). Bisa juga:
- Power Query untuk gabung data
- Excel pivot untuk explore
- SQL untuk query specific

### Step 4: Synthesize Insight

**Setiap insight = fakta + interpretasi + rekomendasi.** Hindari sekedar tampilkan angka.

❌ "Revenue Tebet Rp 3.2 juta, Dago Rp 2.8 juta."
✅ "Revenue Tebet 14% lebih tinggi dari Dago, **terutama karena AOV (average order value) Tebet 30% lebih tinggi** — sinyal segment pelanggan Jakarta lebih premium. **Rekomendasi:** test menu premium di Dago untuk lift AOV."

### Step 5: Present

Deck 3-5 slide:
- **Slide 1** — Title + Executive Summary (1 sentence per finding)
- **Slide 2** — Cabang Performance (revenue, AOV, repeat customer)
- **Slide 3** — Revenue Breakdown (kategori, menu, payment method)
- **Slide 4** — Opportunity (1-2 area)
- **Slide 5** — Rekomendasi Konkret (action 1-2-3)

---

## 3. Tips Pengerjaan

1. **Mulai dari high-level, drill-down.** Jangan langsung loncat ke pertanyaan detail.
2. **Selalu sertakan baseline / benchmark.** Angka sendiri tidak bermakna; perbandingan yang bermakna.
3. **Pakai % perubahan, bukan angka absolut.** "Naik 30%" lebih impactful dari "naik 1.2 juta".
4. **Insight terbatas 3-5.** Semua insight berarti tidak ada insight.
5. **Rekomendasi harus ACTIONABLE.** "Improve marketing" ≠ rekomendasi. "Push menu kategori X di Cabang Y dengan target +10% qty 30 hari" = rekomendasi.

---

## 4. Output yang Diharapkan

File-file di portfolio:

```
data-analyst-portfolio/05-statistics-case/
├── README.md            ← brief case + ringkasan finding
├── analysis.xlsx        ← Excel hasil pivot, lookup, stats
├── queries.sql          ← SQL query yang dipakai
├── deck-q1-2026.pdf     ← Deck 3-5 slide (atau .pptx, atau gambar export)
└── insight.md           ← 3 insight statement detail
```

## 5. Submission

Push ke GitHub:

```bash
cd ~/savvys-da-kursus/portfolio
git add 05-statistics-case/
git commit -m "Week 1 Capstone: Kopi Kita Q1 2026 analysis"
git push
```

Mentor / peer akan review. Akhir Day 5 ada session presentasi singkat (10 menit per peserta).

---

**Akhir Day 4 PM · Week 1**
*Savvys Education · 2026*

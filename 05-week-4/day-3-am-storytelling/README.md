# Week 4 · Day 3 AM
# Data Storytelling — Convert Insight Jadi Narasi

> **Tujuan:** Setelah modul ini kamu paham framework storytelling untuk DA, bisa structure deck yang persuasive, dan paham anti-pattern yang bikin presentation flop.
>
> **Estimasi:** 2.5 jam.

---

## 1. Mengapa Storytelling?

DA punya analisis akurat, dashboard bagus, model statistik valid — **tapi kalau tidak bisa cerita ke stakeholder, semua effort sia-sia**. Director tidak baca notebook 20 cell. CEO tidak buka Power BI dashboard.

Yang mereka lihat: **deck 5 slide** atau **email 1 paragraf**. Kemampuan **convert insight kompleks jadi narasi simple** = pembeda DA biasa vs DA yang dipromosi.

> **Pesan utama:** **Insight tanpa storytelling = insight yang tidak diaksi.**

---

## 2. Framework Storytelling — STAR

**STAR** = **S**ituation, **T**ask, **A**ction, **R**esult.

Aslinya untuk interview behavioral question, tapi **sangat applicable untuk DA storytelling**.

```
S - Situation:  Konteks saat ini, kenapa analisis ini relevan
T - Task:       Pertanyaan bisnis yang dijawab
A - Action:     Analisis yang dilakukan + insight yang ditemukan
R - Result:     Rekomendasi konkret + expected impact
```

### Contoh

**S:** Q1 2026 revenue Kopi Kita Tebet 60% lebih tinggi dari Dago, padahal jumlah pelanggan unique mirip.

**T:** Cari tahu **kenapa** revenue beda.

**A:** Analisis order value per cabang × kategori menu. Temuan: AOV Tebet (Rp 45rb) 30% lebih tinggi dari Dago (Rp 28rb), terutama karena **kategori Coffee Premium** lebih sering dibeli di Tebet.

**R:** Rekomendasi: launch menu Coffee Premium di Dago dengan harga sama. Expected impact: +20% revenue Dago dalam 3 bulan.

> Setiap insight kamu di Capstone Project akan ada framework STAR.

---

## 3. Pyramid Principle (Barbara Minto)

Konsep: **start with conclusion, then back up dengan reasons & data**.

```
                    SLIDE 1: KEY INSIGHT (jawaban)
                              │
              ┌───────────────┼───────────────┐
              │               │               │
        REASON 1         REASON 2         REASON 3
        (slide 2)       (slide 3)        (slide 4)
              │               │               │
        DATA/EVIDENCE   DATA/EVIDENCE    DATA/EVIDENCE
        (chart, num)    (chart, num)     (chart, num)
```

**Anti-pattern:** detail dulu, baru kesimpulan di akhir. Stakeholder eksekutif **drop attention** sebelum kamu sampai ke point.

### Pattern Slide DA

1. **Slide 1** — Conclusion / Key Insight (1 sentence)
2. **Slide 2-4** — 3 reasons / supporting evidence
3. **Slide 5** — Recommendations (3 actions)

5 slide = sweet spot untuk presentation 10 menit. Lebih dari 7 slide = lose attention.

---

## 4. Slide Anatomy — Less is More

### 4.1 Title Sebagai Insight

❌ "Sales Q1 2026" (deskriptif)
✅ "Revenue Tebet 60% lebih tinggi dari Dago — driven oleh AOV gap di Coffee Premium"

Title yang baik = **insight statement langsung**. Stakeholder paham message hanya dari baca title.

### 4.2 1 Slide = 1 Idea

Pattern banyak DA pemula: cram 5 chart + 3 paragraph di 1 slide. **Stakeholder bingung, tidak ada satu pun message yang stick.**

✅ 1 slide = 1 chart + 1 caption (max 2 sentences) + 1 implication (kalau ada).

### 4.3 Annotate Chart

Chart raw tanpa annotation = stakeholder cari sendiri insight-nya. **Spoon-feed insight dengan annotation arrow + text di chart.**

```
       ┌─────────────────────┐
       │                     │
       │      ╱╲             │  ← annotation: "puncak Februari, +35% dari Jan"
       │     ╱  ╲___         │
       │    ╱       ╲___     │
       │___╱             ╲___│
       └─────────────────────┘
        Jan   Feb   Mar  Apr
```

### 4.4 Color untuk Highlight

Default: semua bar abu-abu. Highlight 1 yang penting dengan **warna kontras**.

```
abu-abu  abu-abu  ████   abu-abu
                  Tebet
                  ▲
                  Highlight insight di sini
```

---

## 5. Audience Adaptation

### 5.1 Eksekutif (CEO, Director)
- **5 slide max**
- Insight di slide 1
- No technical detail (no SQL, no model formula)
- Fokus: **bisnis impact, recommendation, risk**

### 5.2 Mid-management (Manager)
- 8-12 slide OK
- Insight di slide 1, detail di slide 2-N
- Some technical OK kalau relevant
- Fokus: **operationalization** (bagaimana implement)

### 5.3 Tim Teknis (Engineers, DA peers)
- 15-20 slide OK
- Detail technical reasoning
- Show code/query
- Fokus: **methodology, reproducibility**

> **Selalu tanya audience-nya siapa sebelum bikin deck.**

---

## 6. Anti-pattern Storytelling

### ❌ "Data Vomit"
Tampilkan **semua angka & chart** tanpa filtering. Stakeholder bingung apa yang penting.

### ❌ Chart Junk
Animasi 3D, bar dengan gradient warna, gridlines tebal — bikin chart susah dibaca.

### ❌ "Conclusion: more data needed"
Akhir presentasi: "kita butuh data lebih banyak". **Tidak actionable.** Always end with **rekomendasi konkret** atau **explicit decision request**.

### ❌ Pakai Jargon Teknis
"P-value 0.03 di chi-square test menunjukkan..." — eksekutif tidak peduli.
✅ "Perbedaan ini significant secara statistik (95% confidence)."

### ❌ Bercerita Linear (kronologis)
"Pertama saya import data... lalu saya bersihkan... lalu saya analisis..." — boring.
✅ Mulai dengan **insight**, baru jelaskan **how** kalau ditanya.

---

## 7. Latihan: Convert Notebook ke 5-slide Deck

`latihan/soal.md` — convert notebook Case Study Week 3 (Olist) jadi 5-slide deck.

---

## Apa Selanjutnya?

Lanjut **Day 3 PM — Capstone Build** (kerja mandiri).

---

**Akhir Day 3 AM · Week 4**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Framework STAR (Situation, Task, Action, Result)
- Pyramid Principle (start with conclusion)
- Slide anatomy (insight as title, 1 slide = 1 idea, annotate)
- Audience adaptation (eksekutif vs manager vs tim teknis)
- Anti-pattern (data vomit, jargon, linear story)

~2.5 jam · materi.md + latihan

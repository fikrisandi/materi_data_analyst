# Week 4 · Day 3 PM
# Capstone Project — Build (Hari 1)

> **Tujuan:** Mulai capstone project end-to-end. Output minggu ini: portfolio piece terbesar yang akan kamu pajang di CV.
>
> **Estimasi:** 4-6 jam (Day 3 PM kerja, Day 4 finalize + present).

---

## 1. Brief Capstone Project

### Format Project

End-to-end analytics dengan **dataset publik** atau **custom**. Output:
1. Notebook analisis (Python + SQL)
2. 1 dashboard interactive (pilih: Tableau / Power BI / Looker)
3. Deck 5-slide insight (pakai framework STAR)
4. README documentation

### Pilih Project

**Opsi 1 — Tracked Path (Recommended)**

Lanjutkan analisis Olist E-commerce dari Week 3. Tambah:
- Customer Lifetime Value calculation
- RFM Segmentation
- Recommendation untuk fitur baru / strategi marketing

**Opsi 2 — Domain-Specific**

Pilih domain sesuai target karir kamu. Cari dataset di Kaggle:
- **HR analytics** — IBM HR Attrition dataset
- **Finance** — Lending Club Loan Data
- **Marketing** — Marketing Campaign dataset
- **Healthcare** — MIMIC-III (butuh approval, atau pakai sample)
- **Telco** — Customer Churn dataset
- **Indonesia-specific** — data.go.id atau BPS

**Opsi 3 — Custom Dataset**

Punya dataset dari kerja saat ini (anonymized OK)? Pakai dataset itu — jadi capstone yang **sangat unique** untuk portfolio.

### Scope yang Disarankan

- **Min 3 business questions** yang dijawab
- **Min 3 visualizations** di dashboard
- **Min 2 statistical tests** (correlation, hypothesis test, A/B test)
- **3 actionable recommendations** dengan expected impact

---

## 2. Project Timeline (Day 3 PM + Day 4)

| Waktu | Aktivitas |
|---|---|
| Day 3 PM 0-30 min | Pilih dataset & define 3 business questions |
| Day 3 PM 30-90 min | Data acquisition + cleaning (notebook step 1-2) |
| Day 3 PM 90-180 min | EDA + analysis answer 3 questions |
| Day 4 0-90 min | Build dashboard (1 tools) + statistical tests |
| Day 4 90-120 min | Bikin deck 5-slide |
| Day 4 120-180 min | Polish notebook + README + push ke GitHub |
| Day 4 180-240 min | Presentation (10 min/peserta) |

---

## 3. Output Folder Structure

```
data-analyst-portfolio/08-capstone/
├── README.md                       ← deskripsi project + finding
├── notebook.ipynb                  ← analisis lengkap
├── data/
│   └── (dataset atau link Kaggle)
├── dashboard/
│   ├── dashboard-link.md           ← URL Tableau/Looker, atau .pbix file
│   └── screenshot.png
├── deck/
│   └── insight-deck.pdf
└── recommendations.md
```

## 4. Tips Eksekusi

### Tips 1 — Don't Boil the Ocean
Pemula sering ambisi terlalu tinggi: "saya mau analisis 10 angle". Hasilnya: tidak satu pun selesai dengan kualitas baik.

✅ **Pick 3 questions, do them excellent.**

### Tips 2 — Polish Communication
Deck & README **wajib polished**. Recruiter lihat README sebelum lihat code.

### Tips 3 — Push as You Go
**Jangan tunggu selesai 100% baru push.** Push setelah tiap milestone — supaya kalau kompi crash, kerjaan tidak hilang.

### Tips 4 — README Profesional
README capstone harus include:
- 1-paragraph executive summary
- Problem statement
- Dataset description + source
- 3 questions answered
- 3 key insights
- 3 recommendations
- Stack: tools yang dipakai
- Author info + LinkedIn link

### Tips 5 — Showcase Range of Skill
Kalau bisa, show:
- SQL query (snippet di notebook)
- Pandas advanced (groupby, merge, transform)
- Statistical test (t-test atau A/B test)
- Visualization (3+ chart types)
- Dashboard interactive

### Tips 6 — Embed Insights, Bukan Code
Notebook section pakai markdown untuk **explain insight**, bukan cuma show output.

```markdown
## Insight 1: Pelanggan Tier-2 Kontribusi 38% Revenue, padahal Hanya 12% Marketing Budget

[chart]

**Implikasi bisnis:** budget marketing tidak align dengan ROI. Reallocate 20% budget dari Tier-1 ke Tier-2.

**Expected impact:** kalau Tier-2 conversion lift 5%, revenue Q3 +Rp 1.2 miliar.
```

---

## 5. Checklist Sebelum Submit

- [ ] Notebook clean, run end-to-end tanpa error
- [ ] Markdown cell untuk tiap section explain insight
- [ ] Dashboard published (link aktif kalau Tableau/Looker)
- [ ] Deck PDF di repo
- [ ] README profesional
- [ ] LinkedIn / Twitter post tentang capstone (opsional, tapi bagus untuk visibility)

---

## 6. Persiapan Presentation Day 4

10 menit per peserta:
- 7 menit present (5 slide)
- 3 menit Q&A

Slide structure:
1. **Title + Problem** — apa yang dianalisis & kenapa penting
2. **Methodology** — dataset + 3 questions + tools
3. **Insight 1** (pakai STAR) — 1 paragraph + 1 chart
4. **Insight 2 + 3** — 1 slide combined atau 2 slide
5. **Recommendations + Next Step** — 3 action items

Practice 1-2x sebelum present.

---

## Apa Selanjutnya?

Day 4 — finalize + present.

**Selamat — kamu hampir selesai 4 minggu kursus!** Capstone ini akan jadi portfolio piece yang paling impressive di CV kamu.

---

**Akhir Day 3 PM · Week 4**
*Savvys Education · 2026*

---

## Tentang Modul Ini

- Pilih dataset & define 3 business questions
- Data acquisition + cleaning
- EDA + analysis
- Mulai build dashboard

~4-6 jam · materi.md (brief)

Output Day 3 PM: notebook 50%+ done + dashboard mulai dibuat.
Output Day 4: notebook polished + dashboard final + deck + present.

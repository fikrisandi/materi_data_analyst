# Savvys Education — Kurikulum Data Analyst

> Materi lengkap kursus Data Analyst 4 minggu — dari pemula sampai siap kerja & sertifikasi.

## Peta Folder

```
Materi Data Analyst/
│
├── 00-konsep/                    📘 Spesifikasi kurikulum & design system
│   ├── konsep-utama.md           ← Single source of truth filosofi & arsitektur
│   ├── design-template.md        ← 12 layout slide, palette, typography
│   └── template-master.pptx      ← (akan di-generate) Master template PPT
│
├── 01-pre-week/                  🎯 Onboarding — Potensi & Profesi Data
│   ├── 01-welcome-potensi-da/
│   ├── 02-diferensiasi-profesi/
│   └── 03-career-statement/
│
├── 02-week-1/                    🛠️ Setup + Excel + SQL Basics + Stats Descriptive
│   ├── day-1-am-setup-env/
│   ├── day-1-pm-git-github/
│   ├── day-2-am-excel-foundation/
│   ├── day-2-pm-excel-power-query/
│   ├── day-3-am-sql-basics/
│   ├── day-3-pm-sql-dql/
│   ├── day-4-am-stats-descriptive/
│   ├── day-4-pm-case-study-w1/
│   └── day-5-live-code-1/
│
├── 03-week-2/                    🐍 Python + Pandas + SQL Advanced + BigQuery
├── 04-week-3/                    🌐 Scraping + API + Stats Inferential + Business
├── 05-week-4/                    📊 Visualization + Storytelling + Capstone
├── 06-elective/                  ➕ Power BI Advanced, Looker Studio
│
└── 99-resources/                 📚 Cross-cutting resources
    ├── datasets/                 ← Capstone spine + dataset latihan
    ├── cheatsheets/              ← Cheat sheet semua tools
    ├── rubrik/                   ← Rubrik penilaian
    ├── mentor-playbook/          ← Panduan untuk mentor
    └── platform-guides/          ← Panduan HackerRank, DataLemur, Forage
```

## Anatomi Folder Sesi

Setiap folder sesi (`day-X-am-Y/` atau `0X-nama-deck/`) selalu berisi:

```
folder-sesi/
├── README.md          ← Tujuan, durasi, prasyarat, output
├── materi.md          ← Draft slide (Markdown source, dengan separator `---`)
├── materi.pptx        ← Hasil render PPT (final delivery)
├── data/              ← File .xlsx, .csv yang dipakai di sesi
├── images/            ← Screenshot, diagram, ilustrasi
├── code/              ← Notebook Jupyter untuk demo (kalau sesi coding)
├── latihan/
│   ├── soal.md
│   └── solusi.md
├── cheatsheet.md      ← Ringkasan 1 halaman
└── mentor-notes.md    ← Briefing khusus mentor (kalau sesi mentoring)
```

## Cara Memulai Mengajar

1. **Baca dulu** `00-konsep/konsep-utama.md` — pahami filosofi & arsitektur
2. **Baca** `00-konsep/design-template.md` — pahami sistem visual
3. **Per sesi**: buka folder sesi → baca `README.md` → buka `materi.pptx` → review `latihan/` & `mentor-notes.md`
4. **Saat butuh dataset**: dataset spine 4 minggu di `99-resources/datasets/capstone-spine/`

## Status Materi

| Modul | Status | Catatan |
|---|---|---|
| 00-konsep | ✅ Final | Konsep + style guide markdown |
| 01-pre-week | ✅ Final | 3 modul (Welcome+Potensi, Diferensiasi Profesi, Career Statement) |
| 02-week-1 | ✅ Final | 9 sesi: Setup, Git, Excel x2, SQL x2, Stats, Case Study, Live Code |
| 03-week-2 | ✅ Final | 9 sesi: Python x4, Pandas x2, SQL Advanced, BigQuery, Live Code |
| 04-week-3 | ✅ Final | 7 sesi: Scraping, API, Business, Stats Inferential, Case, Mentoring, Live Code |
| 05-week-4 | ✅ Final | 7 sesi: Data Viz, Tableau, PBI, Looker, Storytelling, Capstone x2 |
| 06-elective | ✅ Final | Power BI Advanced + Looker Studio Advanced |
| 99-resources | ✅ Final | Cheatsheets, Rubrik, Mentor Playbook, Platform Guides |

**Total konten:** ~77,000+ kata di 127 markdown files. Plus dataset .xlsx + SQLite .db + Python generator scripts.

## Brand & Format

- **Brand:** Savvys Education
- **Format master:** PowerPoint (`.pptx`) — workflow: Markdown draft → render → finalize manual
- **Bahasa:** Indonesia, istilah teknis tetap English
- **Audience:** Pemula + transisi karir + profesional lintas bidang

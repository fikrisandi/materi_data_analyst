# Konsep Utama — Kurikulum Data Analyst

> **Status dokumen:** Living document. Diupdate setiap kali ada keputusan baru.
> **Terakhir diupdate:** 2026-04-26 (revisi: format master = PPT, tambah diferensiasi profesi data, integrasi HackerRank/DataLemur/Forage)

Dokumen ini berisi prinsip-prinsip kurikulum yang sudah disepakati dan yang masih perlu diputuskan. Sebelum pindah ke implementasi (silabus per-hari, isi materi, slide), kerangka di sini harus solid dulu.

---

## 1. Visi Kurikulum

Membangun ulang materi kursus Data Analyst dari 0 dengan kualitas yang **lebih dalam di teori**, **lebih luas di tools**, dan **menghasilkan portofolio nyata** — dirancang untuk bisa dipakai self-paced maupun dengan mentor.

## 2. Target Audience

- **Pemula total** — belum pernah ngoding, belum kenal data
- **Transisi karir** — sudah bekerja di bidang lain, mau pivot ke DA atau butuh data literacy
- **Profesional lintas bidang** — HR, marketing, finance, ops, dll yang butuh DA skill di pekerjaan mereka

Implikasi: bahasa harus tidak intimidating, asumsi prior knowledge = nol, banyak analogi non-teknis.

## 3. Spesifikasi Kursus

| Item | Keputusan |
|---|---|
| Durasi | 4 minggu inti + Pre-Week (Welcome) + Elective |
| Bahasa | Indonesia (istilah teknis tetap English) |
| Format | Campuran — slide PDF + Jupyter Notebook + dataset + worksheet |
| Mode | Self-paced + sebagian sesi mentoring (porsi mentor sedikit) |
| Output peserta | Technical skill, sertifikasi, portofolio GitHub, latihan-latihan tools |

---

## 4. Filosofi Pedagogi — 5 Pilar

### Pilar 1: Theory-first dengan Analogi
Setiap konsep teknis (SQL JOIN, normalisasi, distribusi statistik, OOP, dsb) wajib diawali:
1. **Why** — kenapa konsep ini ada, problem apa yang diselesaikan
2. **Analogi sehari-hari konteks Indonesia** — warung, kos, ojol, marketplace lokal
3. **Baru** masuk syntax/cara pakai

> **Anti-pattern yang dihindari:** "Ini cara pakai pandas `.groupby()`: df.groupby('col').sum()". Tanpa "kenapa groupby ada".

### Pilar 2: Portfolio-driven (Continuous, bukan Capstone-only)
Setiap sesi punya **Portfolio Output** eksplisit. Tidak ada latihan disposable. Akhir kursus, peserta punya 8+ artefak siap CV/LinkedIn.

### Pilar 3: Naik Tangga (Low-code → No-code BI → SQL → Python)
Pemula tidak diterjunkan langsung ke Python. Mulai dari Excel (familiar), lalu BI tools (visual), SQL (deklaratif), Python (programmatic). Confidence dibangun bertahap.

### Pilar 4: Spiral Learning
Konsep yang sama di-revisit dengan kedalaman bertambah lintas tools. Contoh: konsep "filtering data" muncul di Excel filter → SQL WHERE → Pandas `.loc` → Tableau filter. Peserta lihat *pola*, bukan hapal sintaks.

### Pilar 5: Outcome-based per Session
Setiap sesi punya 1 deliverable konkret + 1 **insight statement** (1 kalimat: "dari analisis ini saya menemukan ..."). Storytelling dilatih sejak hari 1, bukan menunggu Week 4.

---

## 5. Modul Wajib: Pre-Week — Potensi Data Analyst

**Sebelum masuk teknikal, peserta harus paham *kenapa* mereka belajar ini.** Modul pembuka berisi:

### 5.1 Apa itu Data Analyst & Data Literacy
- Definisi DA dalam konteks dunia kerja Indonesia 2026
- Apa bedanya "data literacy" (skill umum) vs "Data Analyst" (profesi)

### 5.2 Diferensiasi Profesi Data — Siapa Mengerjakan Apa
Tabel komparatif lengkap:

| Profesi | Fokus Utama | Tools Khas | Output | Analogi (Restoran) |
|---|---|---|---|---|
| **Data Analyst (DA)** | Cari insight dari data yang sudah ada untuk decision making | SQL, Excel, Tableau/PBI, Python dasar | Dashboard, report, insight | Chef yang baca permintaan tamu & racik menu spesial dari bahan yang ada |
| **Data Engineer (DE)** | Bangun & maintain pipeline data (ETL/ELT), infrastructure | SQL, Python, Spark, Airflow, dbt, cloud | Pipeline, data warehouse | Supplier + tukang masak prep yang antar & racik bahan baku ke dapur |
| **Analytics Engineer (AE)** | Modeling data di warehouse, jembatan DE & DA | dbt, SQL, Git, warehouse (Snowflake/BQ) | Tabel siap-pakai, semantic layer | Sous chef yang nyiapin mise en place rapi |
| **Data Scientist (DS)** | Eksperimen, statistical modeling, predictive analytics | Python (sklearn, statsmodels), SQL, R | Model prediktif, hasil eksperimen | Food scientist yang riset rasa baru, A/B test menu |
| **ML Engineer (MLE)** | Productionize model ML, serving infrastructure | Python, MLOps tools, Docker, K8s, cloud | ML system di production | Manajer pabrik makanan masal: scale produksi resep DS |
| **AI Engineer (AIE)** | Bangun aplikasi AI (LLM, RAG, agent) | Python, LangChain, vector DB, API LLM | Aplikasi AI / chatbot / agent | Chef yang pakai robot AI untuk masak otomatis sesuai pesanan |
| **BI Developer** | Spesialis dashboard & reporting | Power BI, Tableau, DAX, SQL | Dashboard enterprise | Food stylist yang plating makanan biar menarik |

**Insight kunci:**
- DA adalah pintu masuk paling ramah → bisa naik ke DS/AE/MLE/AIE seiring skill
- Tidak harus jadi DS/MLE — banyak DA senior bergaji kompetitif & impactful
- Skill DA adalah fondasi semua profesi data lain

### 5.3 Use Case Lintas Profesi (kenapa skill DA berguna di mana-mana)
- HR (people analytics, attrition prediction, salary benchmarking)
- Marketing (funnel, retention, A/B test, campaign ROI)
- Finance (forecasting, risk, fraud detection)
- Operations (supply chain, capacity planning, OEE)
- Product (user behavior, experiment, retention cohort)
- Healthcare, Edukasi, Government, NGO

### 5.4 Pasar Kerja Indonesia
- Data konkret dari LinkedIn / JobStreet / Kalibrr / Glints (jumlah lowongan, perusahaan top hire)
- Jenjang karir: Junior → Mid → Senior → Lead/Principal → Manager
- Lateral move: DA → AE → DS → MLE → AIE
- Range gaji per level (Indonesia, 2026)
- Hybrid role — kapan profesional non-DA (HR, marketing, finance, dll) tetap perlu skill DA

### 5.5 Output Pre-Week
- **Career Statement** — peserta tulis 1 paragraf alasan personal kenapa belajar DA + target role spesifik (full DA atau hybrid). Self-anchor saat motivasi turun di Week 3 (biasanya titik terberat).
- **Mapping skill** — peserta isi self-assessment: dari skill DA yang akan diajarkan, mana yang relevan dengan target career-nya.

---

## 6. Arsitektur Kurikulum ✅ — Opsi B (Lifecycle-first)

| Minggu | Fokus Utama |
|---|---|
| **Pre-Week** | Welcome + Potensi DA + Diferensiasi Profesi Data + Career Statement |
| **Week 1** | Setup environment + Excel (1 hari penuh + Power Query) + SQL Basics + Statistics Descriptive |
| **Week 2** | Python + Pandas + SQL Advanced (window function, CTE, BigQuery) |
| **Week 3** | Web Scraping + API + Statistics Inferential + Business Knowledge + Case Study |
| **Week 4** | Data Visualization (Tableau / Power BI / Looker) + Data Storytelling + Capstone Project |
| **Elective** | Power BI Advanced (DAX), Looker Studio, opsional materi tambahan |

**Alasan dipilih:**
- Pemula butuh *quick win* di W1 — Excel + SQL basic + descriptive stats = "ngerti data" tanpa harus paham Python
- Python masuk W2 setelah confidence sudah ada → pemahaman pandas jadi lebih kuat karena sudah tahu konsep tabular dari Excel & SQL
- Visualisasi & storytelling di W4 jadi puncak — semua hasil olahan W1–W3 dibungkus jadi narasi

**Catatan opsi alternatif (referensi historis):**
- ~~Opsi A (Tools-first, mirip Hacktiv8): Python W1, Pandas+SQL W2~~ — ditolak karena Python di hari 1 berisiko burnout untuk pemula
- ~~Opsi C (Tool-deep-dive): Excel+PBI W1, SQL W2, Python W3, Tableau W4~~ — ditolak karena Python terlalu mundur, Stats kurang ruang

---

## 7. Tools Stack

| Kategori | Tools | Alasan |
|---|---|---|
| Editor | VSCode | Ringan, banyak extension, gratis |
| Python | Miniconda + venv | Lebih ringan dari Anaconda |
| Spreadsheet | Excel + Google Sheets | Excel = dunia kerja, Sheets = kolaborasi |
| Database client | SQLTools (VSCode) + **DBeaver** | Coding-friendly + GUI universal (recommended) |
| Database tier | **SQLite (W1) → PostgreSQL (W2) → BigQuery (W2-3)** | Detail di `99-resources/platform-guides/database-stack.md` |
| BI Tools | Tableau Public + Power BI Desktop + Looker Studio | Ketiganya gratis, masing-masing dapat porsi |
| Versioning | Git + GitHub | Standar industri, dipakai sejak hari 1 |
| Notebook | Jupyter (via VSCode) | Default DA workflow |
| Scraping | requests + BeautifulSoup + Selenium intro | Cukup untuk DA-level |
| Visualisasi Python | Matplotlib + Seaborn + Plotly | Dari basic ke interactive |

**Setup detail (extensions VSCode, env, dst.) → ditulis terpisah di Week 1 Day 1.**

---

## 8. Format & Delivery ✅ (Disepakati: Markdown ebook)

**Master format materi = Markdown (`.md`) per sesi — format ebook chapter, naratif & detail.**

Sebelumnya pernah dipertimbangkan: Quarto (ditolak — kompleks), PDF dari Markdown (ditolak — extra step), PPT/.pptx (dicoba, ditolak — generator Python susah dapat hasil eyecatching, banyak iterasi bug).

**Keputusan final:**
- Tulis langsung di Markdown standar — H1/H2/H3, paragraph, list, table, code block, blockquote
- Naratif dan detail (~3,000–5,000 kata per sesi), bukan slide bullets pendek
- Kalau peserta butuh PPT untuk presentasi, mereka convert sendiri via Gamma / Pandoc / VSCode

### Struktur folder per-sesi

```
01-pre-week/
├── 01-welcome-potensi-da/
│   ├── README.md              ← overview sesi (tujuan, durasi, struktur)
│   ├── materi.md              ← KONTEN UTAMA (ebook chapter, ~3-5k kata)
│   ├── data/                  ← .xlsx, .csv, dataset Kaggle download
│   ├── images/                ← gambar yg sudah di-screenshot (di-link dari materi.md)
│   ├── code/                  ← script .py, .sql, notebook .ipynb (kalau topik coding)
│   ├── latihan/
│   │   ├── soal.md
│   │   └── solusi.md
│   ├── cheatsheet.md          ← ringkasan 1 halaman
│   └── mentor-notes.md        ← briefing untuk mentor (kalau live class)
```

### Konvensi konten:

1. **Gambar / screenshot** — tulis placeholder `[GAMBAR DIPERLUKAN]: <apa yg di-screenshot> · <isi yang dibahas>` di lokasi yang relevan. Detail spesifik supaya user bisa capture nanti tanpa bingung.
2. **Diagram sederhana** (flow, hierarki, relasi) — buat langsung dengan ASCII art di code block. Tidak perlu gambar terpisah.
3. **Tabel** — pakai markdown table standar.
4. **Code Python/SQL/Excel formula** — embed langsung sebagai code block (` ```python ` / ` ```sql `).
5. **Dataset latihan** — pakai data publik gratis: Kaggle, BPS, data.go.id, UCI ML Repository, Mockaroo.
6. **Latihan Excel** — file `.xlsx` beneran di folder `data/`, soal di `latihan/soal.md` reference ke file.
7. **Bahasa** — Indonesia. Istilah teknis tetap English (Data Analyst, query, dashboard, dll).

### Per-sesi terdiri dari:
1. **`materi.md`** — KONTEN UTAMA, master deliverable
2. **`README.md`** — overview & metadata sesi
3. **`latihan/soal.md`** + dataset/file pendukung
4. **`cheatsheet.md`** — ringkasan 1 halaman
5. **`mentor-notes.md`** — briefing mentor (kalau perlu)
6. (Opsional) `data/`, `images/`, `code/` sesuai kebutuhan topik

---

## 9. Strategi Portofolio

Repo `data-analyst-portfolio/` peserta:

```
data-analyst-portfolio/
├── 00-career-statement/        ← Pre-Week (Career Statement + skill mapping)
├── 01-excel-foundation/        ← W1: dashboard penjualan / mini case
├── 02-sql-bigquery/            ← W2: query & analisis dataset publik
├── 03-python-pandas/           ← W2-3: notebook data wrangling
├── 04-data-acquisition/        ← W3: scraping + API project
├── 05-statistics-case/         ← W3: A/B test atau hypothesis test
├── 06-visualization/           ← W4: 3 dashboard (Tableau, PBI, Looker)
├── 07-storytelling-deck/       ← W4: deck insight presentation
├── 08-forage-virtual-internship/ ← Paralel W3-4: sertifikat Forage (BCG/Accenture/dll)
└── 09-capstone/                ← W4: end-to-end project
```

Output publik tambahan:
- 1–2 dashboard di Tableau Public
- 1 dashboard di Looker Studio
- README.md profesional di tiap folder
- Profile README di GitHub
- Badge sertifikasi (HackerRank, Google Cloud, Forage) ditampilkan di GitHub profile + LinkedIn

---

## 10. Strategi Sertifikasi & Latihan ✅

**Pendekatan:** Integrated — tiap minggu punya target platform spesifik untuk latihan & sertifikasi.

### 10.1 Platform Sertifikasi

| Platform | Tipe | Kapan Dipakai |
|---|---|---|
| **HackerRank** | Sertifikasi resmi (gratis) — SQL, Python, Problem Solving | End of W1 (Python Basic), End of W2 (SQL Intermediate) |
| **Google Cloud Skill Badge** | BigQuery for Data Warehousing | Akhir W2 (setelah materi BigQuery) |
| **Tableau Desktop Specialist** | Sertifikasi Tableau resmi | Setelah W4 (post-course) |
| **Microsoft PL-300** | Power BI sertifikasi resmi | Setelah W4 (post-course) — alternatif Tableau |
| **Google Data Analytics Professional** | Coursera (free audit) | Pendamping Pre-Week — opsional |

### 10.2 Platform Latihan Soal (drill expert level)

| Platform | Fokus | Kapan Dipakai |
|---|---|---|
| **HackerRank** | SQL/Python challenges leveled | Mulai W1 untuk Python, W2 untuk SQL |
| **DataLemur.com** | SQL interview FAANG-style (window function, CTE, advanced) | W2 (intermediate) → W3 (expert/window function) |
| **StrataScratch** | SQL + Python case studies real | Opsional, paralel W3 |
| **LeetCode SQL** | SQL problem solving | Opsional, drill speed |

### 10.3 Platform Project & Virtual Internship

| Platform | Output | Kapan Dipakai |
|---|---|---|
| **Forage.com** | Virtual internship simulation (BCG, Accenture, KPMG, JP Morgan, dll) — sertifikat project bisa dipasang LinkedIn | Paralel W3–W4. Wajib minimal 1 program sebagai bukti pengalaman case-based |
| **Kaggle** | Notebook publik + dataset competition | Opsional, capstone alternatif |

**Catatan implementasi:** Tiap minggu materi PPT punya slide khusus "Praktik Lanjutan" yang link ke soal spesifik di platform-platform di atas — bukan generik "buka HackerRank ya".

---

## 11. Decision Points — Final ✅

Semua decision points sudah dikunci pakai rekomendasi default per 2026-04-26.

| # | Topik | Keputusan Final |
|---|---|---|
| D1 | Urutan kurikulum | **Opsi B — Lifecycle-first** (Excel/SQL/Stats Descriptive → Python/Pandas → Acquisition/Inferential → Viz/Storytelling) |
| D2 | Porsi Excel | **1 hari penuh + Power Query** (gabung W1) |
| D3 | Strategi BI Tools | **Spesialisasi**: Tableau (storytelling), Power BI (corporate/DAX), Looker Studio (Google ecosystem). Dijelaskan kapan pakai yang mana |
| D4 | Format Capstone | **Cumulative** — 1 dataset jadi spine 4 minggu, tiap minggu nambah layer (load → clean/query → enrich → visualize/story) |
| D5 | Format master output | **PPT (.pptx)** — workflow: draft Markdown → render via Gamma/Pandoc/Marp → finalize di PowerPoint |
| D6 | Sertifikasi | **Integrated** per minggu — HackerRank, DataLemur, Forage, Google Cloud Skill Badge, Tableau Specialist/PL-300 |
| D7 | Storytelling | **Continuous thread** sejak W1 — tiap deliverable wajib insight statement (1 kalimat) |

---

## 12. Style Guide Konten Markdown ✅

(Sebelumnya Section 12 berisi Design Template PPT, sudah deprecated. File `00-konsep/design-template.md` tetap disimpan sebagai referensi visual kalau peserta convert ke PPT manual.)

**Style guide konten markdown ebook:**
- Heading hierarchy: H1 (judul modul), H2 (Section utama 1, 2, 3), H3 (subtopik dalam section)
- Paragraph naratif yang mengalir, bukan bullet pendek-pendek
- Bullet hanya kalau memang ada list spesifik (misal: list tools, list tugas, list opsi)
- Blockquote (`>`) untuk callout & insight statement
- Tabel markdown untuk komparasi
- Code block dengan language tag (` ```python `, ` ```sql `, ` ```bash `)
- ASCII diagram di code block untuk flow & hierarchy sederhana
- Placeholder gambar: `[GAMBAR DIPERLUKAN]: <deskripsi spesifik>`

Detail lengkap → `00-konsep/markdown-conventions.md`

**Prinsip:** Template tetap, konsisten di semua minggu/sesi. Peserta lihat 1x langsung ngerti pola visual. Disimpan di `00-konsep/design-template.md` (detail lengkap).

### 13.1 Color Palette
| Token | Hex | Pakai untuk |
|---|---|---|
| Primary (Deep Blue) | `#1E3A8A` | Header, judul slide, accent utama |
| Accent (Teal) | `#14B8A6` | Highlight, link, callout positif |
| Warning (Amber) | `#F59E0B` | Catatan penting, "perhatian" |
| Danger (Coral) | `#EF4444` | Common mistakes, "jangan dilakukan" |
| Background | `#FAFAFA` | BG terang default |
| Background Dark | `#0F172A` | BG gelap untuk slide code |
| Text Primary | `#1F2937` | Body text di BG terang |
| Text Inverse | `#F8FAFC` | Body text di BG gelap |
| Muted | `#6B7280` | Caption, footnote, side info |

### 13.2 Typography
| Role | Font | Size | Weight |
|---|---|---|---|
| Heading H1 (judul slide) | Inter / Poppins | 36–44pt | Bold |
| Heading H2 | Inter | 28pt | SemiBold |
| Body | Inter | 18–20pt | Regular |
| Caption / footnote | Inter | 14pt | Regular |
| Code | JetBrains Mono / Fira Code | 16–18pt | Regular |

### 13.3 Slide Templates (12 jenis layout)
1. **Cover** — judul sesi + nomor + ilustrasi besar
2. **Section Divider** — pembatas antar bagian (bg primary, judul putih besar)
3. **Agenda / TOC** — daftar isi sesi
4. **Concept "Why"** — kotak besar pertanyaan + jawaban analogi (icon di kiri)
5. **Content (text-image split)** — 60/40 atau 50/50
6. **Bullet List** — list item dengan icon konsisten
7. **Code Block** — bg gelap (`#0F172A`), font JetBrains Mono, syntax highlight
8. **Comparison Table** — header primary, zebra striping
9. **Diagram / Flow** — process visual (boxes + arrows pakai accent color)
10. **Insight / Key Takeaway** — callout besar dengan icon lampu, bg accent
11. **Exercise / Practice** — bg amber tipis, ada icon target
12. **Resources / Next Step** — link platforms (HackerRank, DataLemur, Forage), badge

### 13.4 Komponen Konsisten Tiap Slide
- **Footer**: nomor slide (kanan) + nama sesi (kiri) + logo brand (tengah/kiri)
- **Header**: nama section / week (subtle, di atas)
- **Page transition**: tanpa efek transisi mencolok — simple fade

### 13.5 Iconography
Pakai 1 icon library konsisten — **Lucide Icons** (modern, free, clean) atau **Phosphor Icons**. Hindari mix-match emoji + flat icon + 3D icon.

---

## 13. Konvensi Catatan Screenshot ✅

Saat materi butuh screenshot tutorial (misal "begini cara install extension VSCode") tapi belum sempat di-capture, gunakan **placeholder note** di slide PPT supaya jelas mana yang perlu ditambah nanti.

**Format placeholder di slide:**

```
┌─────────────────────────────────────────┐
│  📸 [SS NEEDED]                         │
│                                         │
│  Apa yang harus di-screenshot:          │
│  → VSCode → Extensions tab → search     │
│    "Python" → Microsoft official        │
│                                         │
│  Konteks: bagian Setup Day 1, slide #8 │
└─────────────────────────────────────────┘
```

**Aturan:**
1. Selalu pakai prefix `📸 [SS NEEDED]` agar mudah di-grep / di-cari di file PPT
2. Tulis **deskripsi spesifik** apa yang harus di-capture (bukan "screenshot VSCode" doang)
3. Sebut **konteks slide** supaya mudah cross-reference
4. Setelah screenshot diambil, hapus placeholder → ganti dengan gambar
5. Jika beberapa screenshot satu rangkaian (misal install Anaconda 5 langkah), nomor-kan: `📸 [SS NEEDED 1/5]`, `📸 [SS NEEDED 2/5]`, dst.

**Source draft Markdown** pakai sintaks yang sama supaya saat render ke PPT placeholder-nya muncul:

```markdown
> 📸 **[SS NEEDED]** Apa: VSCode > Extensions > "Python" Microsoft. Konteks: Setup Day 1.
```

---

## 14. Yang Sudah Disepakati ✅ (rekap)

- 5 Pilar Pedagogi (Section 4)
- Pre-Week wajib: Potensi DA + Diferensiasi Profesi (Section 5)
- Arsitektur Lifecycle-first (Opsi B), Section 6
- Tools Stack (Section 7)
- Format master = **PPT (.pptx)** + companion files (Section 8)
- Strategi Portofolio continuous (Section 9)
- Sertifikasi Integrated dgn HackerRank/DataLemur/Forage/Google Cloud (Section 10)
- Decision Points D1–D7 final (Section 11)
- Design Template tetap & konsisten (Section 13)
- Konvensi catatan screenshot (Section 14)

## 15. Roadmap Implementasi

1. ✅ Sepakati konsep utama (Section 1–13)
2. ✅ Tulis `00-konsep/design-template.md` detail (12 layout L1–L12, palette, typography)
3. ⏳ **NEXT** — Tulis isi Pre-Week (Potensi DA + Diferensiasi Profesi + Career Statement) → draft Markdown → render PPT
4. ⏳ Generate `00-konsep/template-master.pptx` (master PowerPoint untuk reuse)
5. ⏳ Silabus per-hari Week 1 (Setup VSCode + Excel + SQL Basics + Stats Descriptive)
6. ⏳ Silabus per-hari Week 2 (Python + Pandas + SQL Advanced)
7. ⏳ Silabus per-hari Week 3 (Scraping/API + Stats Inferential + Business Knowledge)
8. ⏳ Silabus per-hari Week 4 (Visualization + Storytelling + Capstone)
9. ⏳ Pemilihan dataset capstone (1 dataset spine 4 minggu)
10. ⏳ Rubrik penilaian latihan & portofolio
11. ⏳ Mentor playbook (untuk sesi yang butuh mentor)
12. ⏳ Materi Elective (Power BI Advanced, Looker Studio)

**Branding & format finalized:**
- Brand name: **Savvys Education**
- Master template: `template-master.pptx`

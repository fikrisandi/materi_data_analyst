# Pre-Week · Modul 2
# Diferensiasi Profesi Data — Siapa Mengerjakan Apa

> **Tujuan modul:** Setelah membaca modul ini, kamu bisa membedakan 7 profesi di ranah data dengan jelas, paham di mana posisi Data Analyst di "peta besar" data, dan tahu jalur pivot karir lateral kalau di masa depan ingin pindah role.
>
> **Estimasi waktu baca:** 40–50 menit · **Format:** modul tertulis untuk dipelajari mandiri.

---

## 1. Mengapa Penting Membedakan Profesi Data?

Saat kamu mulai cari informasi tentang karir di ranah data, kamu akan bertemu banyak istilah yang sekilas mirip: **Data Analyst, Data Engineer, Data Scientist, Machine Learning Engineer, AI Engineer, Analytics Engineer, BI Developer**. Belum termasuk variasi spesifik per perusahaan seperti "Product Analyst", "Growth Analyst", "Quantitative Analyst".

Di Twitter dan LinkedIn, perdebatan tentang "siapa yang lebih hebat" atau "siapa yang lebih dibayar" sering muncul. Ini menyesatkan, karena 3 alasan:

**Pertama**, batasan antar profesi ini **tidak baku & berbeda-beda per perusahaan**. Di startup kecil, satu orang bisa kerjakan tugas DA, DE, dan DS sekaligus (sering disebut "full-stack data person"). Di perusahaan besar (BCA, Tokopedia, Telkomsel), tugas dipecah ke role-role spesialis.

**Kedua**, **gaji bukan urusan profesi**, tapi urusan **value yang kamu deliver**. Senior Data Analyst di fintech bisa dibayar lebih dari Junior Machine Learning Engineer di startup kecil. Pilihan profesi seharusnya berdasarkan **minat & cocok dengan caramu kerja**, bukan rumor "yang paling laku".

**Ketiga**, **DA adalah fondasi** untuk semua profesi lain. Ada banyak DA yang setelah 2–3 tahun pivot ke Analytics Engineer, Data Scientist, atau bahkan AI Engineer — karena skill DA (SQL, statistics, business knowledge) overlap besar dengan profesi-profesi itu. Jadi kalau kamu mulai dari DA, kamu **tidak terkunci** di DA — kamu punya pintu ke banyak arah.

Modul ini tujuannya bukan untuk meyakinkan kamu jadi DA. Tujuannya adalah supaya kamu **paham peta besar profesi data**, biar bisa membuat keputusan karir yang sadar — bukan ikut-ikutan tren.

---

## 2. Bedah 7 Profesi Data

Berikut 7 profesi yang akan kita bahas, urutkan dari yang paling **dekat dengan business decision** sampai yang paling **dekat dengan infrastruktur teknis**:

```
DEKAT BISNIS                                              DEKAT INFRASTRUKTUR
┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
│ BI Dev    │  │ Data      │  │ Data      │  │ Analytics │  │ Data      │
│           │  │ Analyst   │  │ Scientist │  │ Engineer  │  │ Engineer  │
└───────────┘  └───────────┘  └───────────┘  └───────────┘  └───────────┘
                              ┌───────────┐  ┌───────────┐
                              │ ML        │  │ AI        │
                              │ Engineer  │  │ Engineer  │
                              └───────────┘  └───────────┘
```

### 2.1 Data Analyst (DA) — Pencari Insight

**Apa yang dikerjakan:** Mencari insight dari data yang sudah ada untuk membantu pengambilan keputusan bisnis. DA fokus ke pertanyaan-pertanyaan seperti: "Kenapa penjualan turun bulan ini?", "Pelanggan mana yang paling profitable?", "A/B test fitur baru hasilnya gimana?".

**Tools utama:** SQL, Excel, Tableau / Power BI / Looker, Python (Pandas) untuk analisis lebih dalam.

**Output:** Dashboard, report, presentasi insight, hasil A/B test, segmentasi pelanggan.

**Latar belakang umum:** Statistik, ekonomi, manajemen, teknik industri, akuntansi. Tidak harus IT.

**Karakteristik orang yang cocok:** Suka pertanyaan "kenapa", senang bercerita lewat angka, sabar dengan detail, nyaman berkomunikasi dengan tim non-teknis.

**Gaji indikatif (Indonesia 2026):** Junior 6–12 jt → Senior 22–40 jt → Manager 50–100+ jt.

### 2.2 Data Engineer (DE) — Pembangun Pipeline Data

**Apa yang dikerjakan:** Membangun & memelihara infrastruktur data perusahaan. Mereka yang memastikan data dari berbagai sumber (aplikasi mobile, website, sensor IoT, sistem legacy) **mengalir** ke data warehouse / data lake dengan benar, tepat waktu, dan terdokumentasi.

Bayangkan kalau DA adalah chef yang masak makanan, DE adalah supplier yang memastikan bahan baku datang ke dapur tepat waktu, sudah dibersihkan, dan kualitas terjamin.

**Tools utama:** SQL, Python, Apache Spark, Apache Airflow (workflow orchestration), dbt (data build tool), cloud platform (AWS / GCP / Azure), Kafka untuk streaming.

**Output:** ETL/ELT pipelines, data warehouse architecture, schema design, pipeline monitoring, data quality checks.

**Latar belakang umum:** IT, computer science, software engineering. Lebih jarang dari background non-IT karena butuh fundamental coding yang kuat.

**Karakteristik orang yang cocok:** Suka coding, suka memikirkan sistem & arsitektur, sabar dengan debugging pipeline yang gagal jam 3 pagi.

**Gaji indikatif (Indonesia 2026):** Junior 10–18 jt → Senior 30–55 jt → Manager 60–120+ jt. (Lebih tinggi dari DA karena supply lebih sedikit & teknis lebih dalam.)

### 2.3 Analytics Engineer (AE) — Jembatan DE & DA

**Apa yang dikerjakan:** Membangun & memelihara **layer analitik di data warehouse** — yaitu tabel-tabel yang sudah di-clean, di-aggregate, dan siap dipakai DA tanpa perlu mengulang query yang sama. AE muncul karena perusahaan yang pakai modern data stack (BigQuery + dbt + Snowflake) butuh peran khusus untuk "translate" data mentah dari DE jadi data siap-pakai untuk DA.

Kalau DE adalah supplier bahan baku, AE adalah sous chef yang nyiapin "mise en place" — semua bahan sudah dipotong, dimarinasi, dan siap dimasak chef.

**Tools utama:** dbt (sangat sentral), SQL (advanced), Git, BigQuery / Snowflake / Redshift, kadang Python untuk testing.

**Output:** Data models di warehouse, semantic layer (definisi metric standard), dokumentasi data, data testing automation.

**Latar belakang umum:** Sering dari DA senior yang naik level, atau DE yang preferensinya lebih ke business modeling. Profesi yang relatif baru (populer sejak 2020).

**Karakteristik orang yang cocok:** Suka SQL kompleks, suka memikirkan struktur data, peduli dengan dokumentasi & maintainability.

**Gaji indikatif (Indonesia 2026):** Mid 20–35 jt → Senior 35–60 jt. (Profesi langka, banyak diminati.)

### 2.4 Data Scientist (DS) — Peneliti & Modeler

**Apa yang dikerjakan:** Eksperimen & modeling — bikin prediksi (forecasting penjualan, prediksi churn pelanggan), klasifikasi (deteksi fraud transaksi, kategorisasi customer), atau eksperimen statistik kompleks. DS menjawab pertanyaan yang DA tidak bisa hanya dengan SQL: "Kalau kita tweak harga 5%, berapa banyak pelanggan yang akan churn?", "Pelanggan mana yang 80% kemungkinan beli produk premium di 30 hari ke depan?".

Kalau DA adalah chef yang masak menu yang sudah ada, DS adalah food scientist yang riset rasa baru — eksperimen, A/B test menu, develop resep yang belum pernah ada.

**Tools utama:** Python (scikit-learn, statsmodels, pandas), R, SQL, Jupyter Notebook, kadang TensorFlow/PyTorch untuk deep learning.

**Output:** Model prediktif, hasil eksperimen, laporan statistik, recommendation system.

**Latar belakang umum:** Statistika, matematika, ilmu komputer, fisika, ekonometri. Background quantitative kuat sangat membantu.

**Karakteristik orang yang cocok:** Suka eksperimen, suka matematika & statistik, nyaman dengan ambiguity (model jarang sempurna pertama kali).

**Gaji indikatif (Indonesia 2026):** Junior 12–20 jt → Senior 30–60 jt → Manager 60–120+ jt.

### 2.5 Machine Learning Engineer (MLE) — Pembawa Model ke Produksi

**Apa yang dikerjakan:** **Productionize model machine learning** yang dibuat DS supaya bisa dipakai users akhir secara realtime atau batch reliable. Misalnya DS bikin model rekomendasi film di Jupyter Notebook — MLE yang bikin model itu jalan di Netflix backend dengan latency 50ms, scale ke 200 juta user, dan tidak rusak saat traffic spike.

Kalau DS adalah food scientist yang develop resep, MLE adalah manajer pabrik makanan yang scale resep itu jadi 1 juta porsi per hari dengan kualitas konsisten.

**Tools utama:** Python, MLOps tools (MLflow, Kubeflow, SageMaker), Docker, Kubernetes, cloud, monitoring tools.

**Output:** ML system yang jalan di production, CI/CD pipeline untuk model, monitoring model performance, A/B test infrastructure.

**Latar belakang umum:** Software engineering + ML knowledge. Sering dari DS yang suka coding & infrastructure, atau Software Engineer yang pivot ke ML.

**Karakteristik orang yang cocok:** Suka coding & infrastructure, peduli dengan reliability & latency, suka problem rekayasa di scale.

**Gaji indikatif (Indonesia 2026):** Junior 15–25 jt → Senior 40–70+ jt → Manager 80–150+ jt. (Salah satu yang tertinggi karena supply sangat sedikit.)

### 2.6 AI Engineer (AIE) — Pembangun Aplikasi AI

**Apa yang dikerjakan:** Bangun aplikasi yang **memanfaatkan model AI siap-pakai** — terutama LLM (Large Language Model seperti GPT, Claude), generative AI, RAG (Retrieval Augmented Generation), AI agents. Berbeda dari MLE yang men-deploy model custom yang dilatih in-house, AIE biasanya **memanfaatkan API model** dari OpenAI / Anthropic / Google dan membungkusnya jadi aplikasi yang useful.

Profesi ini relatif baru (populer sejak ChatGPT 2022) dan masih membentuk. Banyak overlap dengan Software Engineer + ML Engineer.

Kalau MLE adalah pabrik makanan yang manufactur dari nol, AIE adalah chef yang pakai robot AI untuk masak otomatis sesuai pesanan customer.

**Tools utama:** Python, LangChain / LlamaIndex, vector database (Pinecone, Weaviate, Chroma), API LLM (OpenAI, Anthropic, Google), prompt engineering, RAG patterns.

**Output:** Chatbot, AI agent, document Q&A system, AI-powered features di aplikasi existing.

**Latar belakang umum:** Software engineering, atau MLE/DS yang pivot. Tidak harus mendalami ML theory — fokus lebih ke "bagaimana memanfaatkan model AI dengan efektif".

**Karakteristik orang yang cocok:** Suka eksperimen cepat, comfortable dengan tools yang berubah cepat, kreatif dalam memikirkan use case AI.

**Gaji indikatif (Indonesia 2026):** Junior 15–25 jt → Senior 40–80+ jt. (Tinggi & langka — high demand 2025–2026.)

### 2.7 BI Developer — Spesialis Dashboard & Reporting

**Apa yang dikerjakan:** Spesialisasi **bangun dashboard enterprise yang scalable** — dashboard yang dipakai ratusan stakeholder di perusahaan setiap hari, dengan filter complex, drill-down, dan integrasi ke berbagai data source. BI Dev fokus mendalam ke 1–2 tools (biasanya Power BI atau Tableau) sampai expert level.

Kalau DA bisa bangun dashboard untuk insight 1-shot, BI Dev bangun dashboard yang jadi product internal perusahaan — dipakai berulang, di-maintain bertahun-tahun.

**Tools utama:** Power BI (sangat dalam, termasuk DAX & Power Query), Tableau (advanced), SQL, kadang Python untuk custom visualization.

**Output:** Enterprise dashboard, scheduled reports, paginated reports, semantic models di Power BI.

**Latar belakang umum:** Sering dari DA yang spesialisasi ke BI tools, atau dari background business analyst.

**Karakteristik orang yang cocok:** Detail-oriented, suka design visual, mendalami satu tools sampai expert.

**Gaji indikatif (Indonesia 2026):** Junior 8–15 jt → Senior 20–35 jt → Lead 35–60 jt.

---

## 3. Analogi Restoran — Visual Mental Model

Kalau bingung membedakan, pakai mental model "Restoran" ini sebagai shortcut:

```
                    PERUSAHAAN (RESTORAN)
                    ─────────────────────
                              │
    ┌─────────────┬──────────┴──────────┬─────────────┐
    │             │                     │             │
SUPPLIER     SOUS CHEF              CHEF UTAMA    FOOD SCIENTIST
   │             │                     │             │
   DE            AE                   DA           DS
(antar         (siapin              (racik       (riset menu
 bahan         mise en              menu spesial   baru,
 baku)         place)               buat tamu)    A/B test)

                                      │
                              ┌───────┴────────┐
                              │                │
                        FOOD STYLIST       PABRIK MAKANAN
                        BI Dev             MLE
                        (plating cantik    (scale resep
                        untuk display)     ke produksi
                                            massal)

                              │
                          CHEF DENGAN
                          ROBOT AI
                          AIE
                          (pakai AI tool
                          untuk masak
                          sesuai pesanan)
```

Cara ingatnya:
- Lihat data sebagai **bahan baku makanan** yang harus diproses
- Setiap profesi data adalah **peran berbeda di dapur restoran**
- Tidak ada yang lebih "tinggi" dari yang lain — masing-masing punya value unik untuk operasi restoran

---

## 4. Tabel Komparatif — Skill, Tools, Output

| Profesi | Fokus Utama | Tools Khas | Output Sehari-hari | Gaji Senior (Jakarta, 2026) |
|---|---|---|---|---|
| **Data Analyst** | Insight dari data existing | SQL, Excel, Tableau/PBI, Python | Dashboard, report, A/B test | 22–40 jt |
| **Data Engineer** | Pipeline & infrastructure | SQL, Python, Spark, Airflow, dbt | ETL pipeline, data warehouse | 30–55 jt |
| **Analytics Engineer** | Data modeling di warehouse | dbt, SQL, Git | Tabel siap-pakai, semantic layer | 35–60 jt |
| **Data Scientist** | Modeling & eksperimen | Python (sklearn), R, SQL | Model prediktif, hasil eksperimen | 30–60 jt |
| **ML Engineer** | Productionize ML model | Python, MLOps, Docker, K8s | ML system di production | 40–70+ jt |
| **AI Engineer** | Aplikasi AI (LLM, RAG, agent) | Python, LangChain, vector DB, LLM API | Chatbot, AI agent, RAG system | 40–80+ jt |
| **BI Developer** | Dashboard enterprise | Power BI (DAX), Tableau | Enterprise dashboard, reports | 20–35 jt |

> **Insight kunci:** Skill yang **paling overlap di semua profesi** ini adalah **SQL**. Mau ke arah mana pun di ranah data, SQL wajib dikuasai dengan baik. Itulah kenapa SQL akan dapat porsi besar di Week 1 & 2 kursus ini.

---

## 5. Jenjang Karir Lateral — Pivot Path di Ranah Data

Yang sering tidak disadari pemula: **karir di ranah data tidak harus linear naik di satu profesi**. Banyak orang pivot lateral ke profesi lain seiring waktu. Berikut path yang umum di Indonesia:

### Path A: DA → Analytics Engineer → Data Engineer
Cocok kalau setelah jadi DA kamu sadar lebih suka **bangun infrastructure data** daripada present insight ke stakeholder. Pivot via dbt + SQL advanced + cloud certification.

### Path B: DA → Data Scientist → ML Engineer
Cocok kalau setelah jadi DA kamu suka **modeling & eksperimen**, dan tertarik mendalami statistik / ML. Pivot via belajar Python advanced + scikit-learn + statistik inferensial.

### Path C: DA → AI Engineer
Path baru (sejak 2023+). Cocok kalau kamu sudah nyaman dengan Python dan ingin belajar **bangun aplikasi AI**. Pivot via belajar LangChain + prompt engineering + vector DB.

### Path D: DA → BI Developer → BI Lead
Spesialisasi ke dashboard tools sampai expert level. Cocok kalau kamu suka design visual & ingin jadi spesialis.

### Path E: DA → Analytics Manager → Director of Analytics
Path manajerial. Cocok kalau kamu suka memimpin tim & strategi. Pivot via mengambil tanggung jawab people management & cross-functional projects.

### Path F: DA → Domain Specialist (Product Analyst, Growth Analyst, Risk Analyst)
Spesialisasi ke domain bisnis tertentu. Tetap "DA" tapi sangat dalam di domain spesifik (product analytics di tech, risk analytics di banking).

```
                                ┌───→ Analytics Manager
                                │
                                │           ↓
                                │    Director of Analytics
                                │
                                ├───→ Analytics Engineer ──→ Data Engineer
                                │
   Junior DA → Mid DA → Senior DA ──→ Data Scientist ──────→ ML Engineer
                                │
                                ├───→ AI Engineer
                                │
                                ├───→ BI Developer ──→ BI Lead
                                │
                                └───→ Domain Specialist
                                      (Product, Growth, Risk Analyst)
```

> **Pesan utama:** Mulai dari DA = mulai dari profesi yang **paling banyak pintu**. Kamu tidak terjebak — kamu punya opsi.

---

## 6. Tips Memilih Profesi Yang Cocok

Kalau kamu masih bingung mau mengarah ke mana, berikut beberapa pertanyaan diagnostik:

**Pertanyaan 1: Apakah kamu lebih suka *cari jawaban* atau *bangun sistem*?**
- **Cari jawaban** → DA, DS (analisis-driven)
- **Bangun sistem** → DE, AE, MLE, AIE (engineering-driven)

**Pertanyaan 2: Kalau ada problem, apakah kamu lebih suka *dalam ke 1 problem* atau *cepat ke banyak problem*?**
- **Dalam ke 1 problem** → DS, MLE (deep work)
- **Cepat ke banyak problem** → DA, AIE, BI Dev (broad work)

**Pertanyaan 3: Apakah kamu lebih nyaman dengan *bisnis/orang* atau *kode/sistem*?**
- **Bisnis/orang** → DA, BI Dev (banyak interaksi stakeholder)
- **Kode/sistem** → DE, MLE, AE (lebih banyak coding)

**Pertanyaan 4: Apakah kamu suka *eksperimen yang gagal-gagalan* atau *progress yang stabil*?**
- **Eksperimen** → DS, AIE (model jarang sempurna pertama kali)
- **Progress stabil** → DA, DE, BI Dev (output lebih predictable)

**Pertanyaan 5: Apakah kamu lebih nyaman dengan *bahasa Inggris* atau *Bahasa Indonesia*?**
Hampir semua profesi data butuh English untuk dokumentasi, tutorial, & komunitas global. Tapi DS / MLE / AIE komunitas-nya lebih English-heavy daripada DA / BI Dev. Pertimbangkan kalau English masih jadi kendala.

> **Tips terakhir:** Tidak perlu pilih final sekarang. Selesaikan dulu kursus DA ini — di akhir kamu sudah punya pengalaman konkret (bukan hanya teori), dan keputusan pivot atau lanjut akan jauh lebih jelas.

---

## Apa Selanjutnya?

Kamu sudah selesai Modul 2. Sekarang kamu punya peta lengkap profesi data dan posisi DA di dalamnya.

**Selanjutnya:**

1. **Buka catatan refleksi Modul 1** kamu — review jawaban kamu untuk pertanyaan #3 (DA full-time, hybrid, atau eksplorasi).
2. **Lanjut ke Modul 3: Career Statement** — folder `01-pre-week/03-career-statement/`. Modul terakhir Pre-Week ini akan membantu kamu menulis Career Statement personal: kombinasi dari motivasi, target role, dan skill mapping.
3. **(Opsional)** Coba search di LinkedIn Jobs: cari 1 lowongan dari masing-masing profesi (DA, DE, DS, MLE) di Jakarta. Bandingkan job description-nya. Catat hal-hal yang menarik perhatianmu.

Sampai jumpa di Modul 3.

---

**Akhir Modul 2 · Pre-Week**
*Savvys Education · 2026*

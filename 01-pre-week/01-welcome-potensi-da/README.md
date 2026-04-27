# Pre-Week · Modul 1
# Selamat Datang & Potensi Data Analyst

> **Tujuan modul:** Setelah membaca modul ini, kamu paham apa itu Data Analyst, kenapa profesi ini penting di tahun 2026, kondisi pasar kerja Indonesia, dan kenapa skill ini berlaku di hampir semua profesi modern.
>
> **Estimasi waktu baca:** 45–60 menit · **Format:** modul tertulis untuk dipelajari mandiri.

---

## 1. Selamat Datang

### 1.1 Kenapa Kamu di Sini?

Mungkin kamu sedang berada di salah satu dari posisi ini:

- Kamu **fresh graduate** yang sering dengar "Data Analyst lagi banyak dicari" di LinkedIn dan ingin tahu apakah ini cocok untuk kamu.
- Kamu **profesional yang ingin pivot** dari background non-tech (HR, marketing, finance, ops, atau bidang lain) ke ranah data — karena merasa dunia kerja makin "data-driven" dan tidak mau ketinggalan.
- Kamu **sudah bekerja di bidang lain** dan sadar bahwa skill data sudah jadi bahasa bersama di kantor — atasan kamu mulai sering bilang "berdasarkan data..." dan kamu ingin bisa ikut bicara di level itu.
- Kamu **founder atau pebisnis kecil** yang ingin memahami sendiri data dari toko/usaha kamu, tanpa harus selalu bergantung pada laporan manual.

Apa pun posisinya, kabar baiknya sama: **kamu tidak harus jadi engineer atau lulusan IT untuk bekerja dengan data**. Yang dibutuhkan adalah cara berpikir terstruktur, kemauan belajar tools yang tepat, dan latihan yang konsisten.

Empat minggu ke depan kursus ini akan membangun semua itu — dari nol. Kalau kamu serius mengikuti, di akhir kamu akan punya skill teknikal yang siap dipakai melamar kerja, portofolio nyata yang bisa dipajang di GitHub & LinkedIn, dan setidaknya satu sertifikat resmi yang diakui industri.

### 1.2 Yang Akan Kamu Dapat dari Kursus Ini

Berikut deliverable konkret yang akan kamu pegang setelah 4 minggu:

- **Skill teknikal lintas tools** — Excel (termasuk Power Query), SQL & BigQuery, Python (Pandas), Tableau, Power BI, Looker Studio, dasar web scraping, dan integrasi API.
- **Portofolio nyata** — minimal 9 artefak (mini-project per minggu + capstone) yang langsung bisa dipajang di GitHub dan dirujuk dari CV/LinkedIn.
- **Sertifikasi terkurasi** — kursus akan mengarahkan kamu ke sertifikasi yang relevan: HackerRank (SQL & Python), Google Cloud Skill Badge (BigQuery), Forage (virtual internship simulation dari BCG/Accenture/KPMG/JP Morgan), dan opsional Tableau Desktop Specialist atau Microsoft PL-300.
- **Latihan expert level** — bank soal SQL interview FAANG di DataLemur, problem solving di StrataScratch, dan dataset publik dari Kaggle untuk analisis end-to-end.
- **Cara berpikir analitis** — yang berlaku di profesi apa pun, bukan hanya untuk yang ingin jadi DA full-time.
- **Career Statement personal** — di akhir Pre-Week kamu akan menulis pernyataan karier sendiri yang akan jadi self-anchor saat motivasi turun di tengah kursus.

> **Janji utama:** Modul ini didesain agar setelah selesai, kamu tidak hanya **tahu** Data Analytics, tapi **bisa mengerjakan** pekerjaan Data Analyst entry-level dengan kualitas yang dibandingkan dengan lulusan kursus mahal lain.

---

## 2. Apa itu Data Analyst?

### 2.1 Kenapa Data Itu Penting? — Analogi Warung Kopi

Sebelum bicara tools dan teknik, mari mulai dari yang paling sederhana: **kenapa data perlu diolah sama sekali?**

Bayangkan kamu punya sebuah warung kopi kecil di pinggir jalan. Bulan lalu warung kamu ramai banget, sampai-sampai biji kopi habis sebelum sore. Tapi bulan ini sepi, padahal cuaca dan harga sama saja. **Kenapa?**

Pelanggan kamu yang biasanya datang setiap pagi tiba-tiba jarang muncul. Beberapa pindah ke kompetitor sebelah, beberapa lainnya kamu nggak tahu pergi ke mana. **Kenapa?**

Kamu mau buka cabang baru di lokasi lain — di mall, di dekat kampus, atau di komplek perumahan? Ada modal, tapi cuma cukup untuk satu lokasi. **Lokasi mana yang paling masuk akal?**

Kalau kamu hanya menebak-nebak — ngandelin "feeling" atau "kebiasaan" — kamu mungkin betul, mungkin salah. Risikonya tinggi karena setiap keputusan adalah investasi waktu dan uang.

Tapi kalau kamu **mencatat semua transaksi** (kapan, siapa beli apa, berapa total), **mencatat jam kunjungan** (dari pagi sampai malam), **mencatat menu favorit per pelanggan**, dan **mencatat cuaca** tiap hari — ada ratusan baris data dalam beberapa minggu. Dari tumpukan baris itu kamu bisa **menemukan pola**:

- Mungkin pelanggan tetap kamu adalah karyawan kantor sebelah — dan bulan ini kantor itu lagi WFH, makanya warung sepi.
- Mungkin menu yang paling laku adalah es kopi susu, sementara kopi panas jarang dipesan setelah jam 11 — implikasi: stok susu lebih banyak dari biji kopi panas.
- Mungkin cuaca hujan justru menambah pelanggan yang nongkrong (tidak mau pulang) bukan mengurangi — implikasi: stok lebih banyak saat ada peringatan hujan dari BMKG.

Itulah inti pekerjaan Data Analyst: **menemukan pola dan jawaban dari data yang sudah ada — supaya keputusan tidak ditebak, tapi diukur.**

Dan ini berlaku universal. Warung kopi pakai logika yang sama dengan Tokopedia (kapan promo, produk apa yang naik, region mana yang growth-nya melambat), dengan rumah sakit (pasien kategori apa yang sering relapse, dokter mana yang waktu konsultasinya terlalu pendek), dengan sekolah (mata pelajaran apa yang nilai rata-ratanya turun, kapan siswa paling sering bolos). Skala beda, tapi cara berpikirnya sama.

### 2.2 Definisi Praktis Data Analyst

Seorang Data Analyst adalah profesional yang melakukan **empat hal utama** secara berulang sebagai siklus kerja:

1. **Mengumpulkan & membersihkan data** dari berbagai sumber — bisa database perusahaan, file Excel/CSV dari tim lain, API dari layanan eksternal, atau hasil scraping dari web. Sebagian besar waktu DA sebenarnya dihabiskan di sini, bukan analisis fancy.
2. **Menganalisis data** untuk menemukan pola, tren, dan anomali. Mulai dari yang sederhana (rata-rata, total, top-N) sampai yang lebih kompleks (segmentasi pelanggan, cohort analysis, A/B testing).
3. **Memvisualisasikan** hasil dalam bentuk chart, dashboard, atau laporan yang gampang dicerna oleh orang yang bukan teknis. Visualisasi yang baik bisa menyampaikan insight dalam 5 detik; visualisasi yang buruk bisa menyembunyikan insight selama berjam-jam.
4. **Menceritakan insight** ke stakeholder (atasan, klien, tim lain) agar bisa dipakai untuk keputusan bisnis. Ini biasanya disebut **data storytelling** — dan sering jadi pembeda antara DA biasa dan DA yang dipromosi.

Alur kerjanya terlihat seperti ini:

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌────────────────┐
│ Data Sources │ ──→ │  Data Analyst│ ──→ │   Insight    │ ──→ │ Decision Maker │
│              │     │              │     │              │     │                │
│  Database    │     │  Clean       │     │  Pattern     │     │  Action /      │
│  Files       │     │  Analyze     │     │  Trend       │     │  Strategy      │
│  API         │     │  Visualize   │     │  Anomaly     │     │  Decision      │
│  Scraping    │     │  Storytell   │     │  Number      │     │                │
└──────────────┘     └──────────────┘     └──────────────┘     └────────────────┘
```

> **Yang paling penting untuk dipahami sejak awal:** DA bukan tukang ngolah angka semata. DA adalah **jembatan antara data mentah dan keputusan bisnis**. Tanpa jembatan ini, data hanya jadi tumpukan angka tanpa makna.

### 2.3 Tugas Pokok Data Analyst Sehari-hari

Apa yang persis dikerjakan seorang DA dari Senin sampai Jumat? Berikut yang biasanya muncul di kalender harian — bisa berbeda prioritas tergantung perusahaan, tapi pola umumnya konsisten:

**1. Tarik data sesuai permintaan stakeholder.** Pagi-pagi sudah ada email atau pesan Slack: "Hi, tolong dong kasih saya angka jumlah transaksi minggu lalu per region, untuk meeting jam 10." Kamu buka SQL editor (atau BigQuery), tulis query, run, export hasilnya. Skill: SQL.

**2. Bersihkan data sebelum dianalisis.** Data dunia nyata jarang rapi. Ada nilai kosong (missing), ada duplikat, ada format tanggal yang campur aduk ("2025-12-31", "31/12/2025", "Dec 31, 2025"), ada angka yang masuk sebagai teks ("1,000.50" vs 1000.5). Kamu standarisasi semua ini sebelum analisis. Skill: Python (Pandas), SQL, Excel.

**3. Eksplorasi data awal (Exploratory Data Analysis / EDA).** Sebelum bikin kesimpulan, kamu lihat dulu distribusi datanya — berapa rata-rata, median, berapa yang outlier, bagaimana sebarannya per kategori. Tujuan: paham datanya dulu sebelum analisis lanjutan. Skill: Python, Statistics dasar.

**4. Analisis lanjutan sesuai pertanyaan bisnis.** Setelah data bersih dan dipahami, kamu jawab pertanyaan spesifik: segmentasi pelanggan (siapa yang most valuable), cohort analysis (apakah pelanggan baru bulan ini bertahan lebih lama dari bulan lalu), A/B test analysis (apakah desain tombol baru mengurangi cart abandonment), forecasting sederhana (estimasi penjualan bulan depan). Skill: Statistics, SQL advanced, Python.

**5. Bangun dashboard interaktif.** Data yang hanya kamu lihat sendiri tidak ada gunanya. Stakeholder butuh dashboard yang bisa dibuka kapan saja, dengan filter yang mereka kontrol sendiri. Kamu bangun dashboard di Tableau, Power BI, atau Looker Studio yang refresh otomatis tiap pagi. Skill: BI tools, SQL.

**6. Bikin report dan presentasi.** Selain dashboard, ada laporan formal — slide deck untuk meeting bulanan dengan direksi, atau memo untuk tim produk. Di sini kemampuan storytelling diuji: bagaimana kamu mengubah 50 chart jadi 3 slide yang bermakna. Skill: Data storytelling, presentasi, PowerPoint/Google Slides.

**7. Kolaborasi lintas tim.** DA jarang kerja sendirian. Kamu meeting sama tim Marketing untuk sepakat definisi "active user", sama Finance untuk align angka revenue, sama Product untuk diskusi metric yang harus ditrack di fitur baru. Skill: komunikasi, business knowledge.

**8. Dokumentasi.** Setiap query yang kamu tulis, setiap definisi metric, setiap dashboard yang kamu bangun — perlu didokumentasikan supaya tim lain (atau kamu sendiri 6 bulan kemudian) bisa pakai ulang. Ini sering di-skip pemula, dan jadi penyebab utama "data debt" di perusahaan. Skill: technical writing.

Persentase waktu di tiap tugas berbeda per level. **Junior DA** biasanya banyak di tugas 1, 2, 3, dan 5 (eksekusi). **Senior DA** lebih banyak di tugas 4, 6, 7 (analisis kompleks, storytelling, kolaborasi). **Lead DA** bahkan sebagian besar waktu di tugas 7 (memimpin tim) dan 8 (governance & arsitektur data analytics).

### 2.4 Data Literacy vs Profesi Data Analyst

Banyak orang bingung antara dua istilah ini. Bedanya:

| Aspek | Data Literacy (skill umum) | Data Analyst (profesi) |
|---|---|---|
| **Siapa yang butuh?** | Hampir semua profesional modern | Orang yang khusus mengerjakan analisis sebagai pekerjaan utama |
| **Skill teknikal** | Excel mahir, baca chart & dashboard, SQL dasar (SELECT/WHERE) | Excel + SQL (advanced) + Python + BI tools (Tableau/PBI/Looker) + Statistics |
| **Output sehari-hari** | Bisa baca & memanfaatkan data di pekerjaan utama | Membuat analisis, dashboard, dan insight buat tim/perusahaan |
| **Waktu belajar** | 2–4 minggu basic | 3–6 bulan untuk siap kerja entry-level |
| **Contoh peran** | HR Manager, Finance Staff, Marketing Lead, Product Manager | Junior Data Analyst, BI Analyst, Product Analyst, Marketing Analyst |

Kursus ini akan membawa kamu dari nol sampai siap melamar peran **Profesi Data Analyst**. Tapi semua materi yang akan kamu pelajari juga sangat berguna untuk Data Literacy — jadi kalau setelah belajar kamu memutuskan tetap di profesi sebelumnya, skill yang sudah kamu bangun tetap relevan dan berharga.

Kamu akan menentukan target karier kamu sendiri di Modul 3 (Career Statement), setelah lihat lebih dalam bedanya peran-peran data di Modul 2 berikutnya.

---

## 3. Pasar Kerja Data Analyst Indonesia 2026

### 3.1 Lowongan & Pertumbuhan

Per Q1 2026, pencarian "Data Analyst" di LinkedIn dengan filter lokasi Indonesia menampilkan **lebih dari 5,000 lowongan aktif**. Angka ini belum termasuk JobStreet, Glints, Kalibrr, dan situs karier perusahaan langsung — yang kalau digabung biasanya naik 1.5–2x lipat.

Pertumbuhan year-over-year untuk role ini di Indonesia berada di kisaran **30%+** — salah satu role tercepat tumbuh, bahkan saat industri tech secara global mengalami koreksi. Ini bukan kebetulan: **digitalisasi di Indonesia masih di fase early-mature**, dan setiap industri yang mulai digitalisasi (banking, telco, healthcare, edutech, government) butuh DA untuk mengelola data baru yang mereka generate.

Sebagai indikator: pada tahun 2020, lowongan DA terkonsentrasi di unicorn-unicorn (Tokopedia, Gojek, Traveloka). Pada tahun 2026, lowongan tersebar luas — bahkan perusahaan tradisional seperti Astra, Pertamina, dan Unilever buka divisi data analytics sendiri.

> **[GAMBAR DIPERLUKAN — Screenshot LinkedIn Job Search]**
> **Apa yang harus di-screenshot:** halaman LinkedIn Job Search dengan keyword "Data Analyst" dan filter location "Indonesia". Tampilkan jumlah hasil di pojok kiri atas (misal: "5,200+ jobs"), beserta beberapa company logo (Tokopedia, BCA, Telkomsel, dll) di list hasil pertama.
> **Konteks isi nanti:** Bukti visual bahwa lowongan DA di Indonesia memang banyak. Data ini perlu di-update tiap intake kursus karena angka berubah.

### 3.2 Range Gaji Data Analyst di Indonesia (2026)

Berikut indikasi gaji per level berdasarkan kompilasi Kalibrr Salary Report 2025/26, Glints Talent Trends, dan data publik JobStreet:

| Level | Tahun Pengalaman | Gaji Jakarta (Rp / bulan) | Gaji Luar Jakarta (Rp / bulan) |
|---|---|---|---|
| Junior Data Analyst | 0–2 tahun | 6 – 12 juta | 5 – 9 juta |
| Mid Data Analyst | 2–4 tahun | 12 – 22 juta | 9 – 16 juta |
| Senior Data Analyst | 4–7 tahun | 22 – 40 juta | 16 – 28 juta |
| Lead / Principal DA | 7+ tahun | 40 – 70 juta | 28 – 50 juta |
| Analytics Manager | + leadership 2+ tahun | 50 – 100+ juta | 35 – 70 juta |

**Catatan penting tentang range gaji:**

- Range ini **bersifat indikatif**, bukan janji. Gaji aktual tergantung industri, ukuran perusahaan, lokasi, dan negosiasi.
- **Industri fintech, banking, dan unicorn tech** cenderung membayar di ujung atas range. Industri tradisional (manufaktur, perdagangan) cenderung di tengah-bawah.
- **Skill kombinasi** bisa boost gaji 20–40%: DA + cloud (BigQuery / Snowflake), DA + AI/ML basics, DA + business strategy, DA + bahasa Inggris bisnis aktif.
- **Sertifikasi tertentu** seperti Tableau Desktop Specialist atau Google Cloud Professional bisa jadi bargaining chip negosiasi gaji entry-level (+10–20%).
- **Kemampuan komunikasi** sering underrated — DA yang bisa presentasi insight dengan jelas ke direksi naik jabatan jauh lebih cepat daripada yang skill teknisnya lebih tinggi tapi komunikasinya lemah.

> **[GAMBAR DIPERLUKAN — Salary Report Snippet]**
> **Apa yang harus di-screenshot:** snippet dari Kalibrr Salary Report atau Glints Talent Report bagian Data Analyst Indonesia, yang menampilkan range gaji per level.
> **Konteks isi nanti:** Memberi credibility ke angka yang disebutkan — peserta lihat bukan klaim sembarangan.

### 3.3 Top Industries Hiring Data Analyst di Indonesia

Hampir semua industri yang sudah beroperasi di Indonesia 2026 butuh DA. Tapi yang paling agresif merekrut bisa dikelompokkan ke 4 cluster besar:

**Cluster 1 — Digital & Tech (e-commerce, marketplace, ride-hailing, traveltech, investtech).** Perusahaan: Tokopedia, Shopee, Gojek/GoTo, Grab, Traveloka, Tiket.com, Bibit, Ajaib. Karakteristik: data berskala besar, A/B testing intensif, analytics jadi inti produk. Cocok kalau kamu suka iterasi cepat dan eksperimen.

**Cluster 2 — Financial (banking, fintech, payment, lending).** Perusahaan: BCA, BRI, Bank Mandiri, OVO, DANA, Jenius, Akulaku, Kredivo. Karakteristik: data sangat sensitif (regulasi ketat), fokus ke risk analytics, fraud detection, customer credit scoring. Cocok kalau kamu suka domain bisnis yang regulated dan analitis dalam.

**Cluster 3 — Telco & Media.** Perusahaan: Telkomsel, XL Axiata, Indosat, Telkom, Compas, SCM, MNC Group. Karakteristik: data customer behavior dari jutaan pengguna telekomunikasi, churn analysis, network optimization. Cocok kalau kamu suka data berskala masif.

**Cluster 4 — Tradisional + Digitalisasi.** Perusahaan: Astra International, Pertamina, Unilever, Indofood, Telkom Group, Pegadaian, Pupuk Indonesia, BUMN lainnya. Karakteristik: industri besar yang baru mulai serius investasi di data analytics — banyak peluang "greenfield" (mulai dari nol). Cocok kalau kamu suka tantangan membangun fondasi data dari awal.

> **Insight strategis:** Pertanyaannya bukan "apakah industri X butuh DA" — hampir semua butuh. Pertanyaannya adalah "perusahaan mana di industri X yang sudah mature di analytics" — karena itu yang punya jenjang karier jelas dan mentor senior untuk kamu belajar.

### 3.4 Background Tidak Harus IT

Ini hal yang sering jadi kekhawatiran calon DA: "Saya bukan dari jurusan IT atau Statistik, masih bisa nggak?"

Jawabannya: **bisa, dan sering kali justru jadi keuntungan**. Banyak DA top di Indonesia berasal dari:

- **Statistik & Matematika** — dasar logis kuat, mudah masuk ke advanced statistics dan modeling
- **Ekonomi & Bisnis** — domain knowledge bisnis sudah ada, tinggal belajar tools
- **Teknik Industri & Manajemen** — terbiasa dengan optimasi proses dan KPI
- **Akuntansi & Keuangan** — sangat detail dengan angka, cocok untuk financial analytics
- **Psikologi & Sosiologi** — paham behavioral patterns, kuat di marketing/UX analytics
- **Sastra & Komunikasi** — kemampuan storytelling tinggi, sering jadi DA yang paling diperhitungkan saat presentasi ke direksi

Kalau background-mu salah satu di atas, kamu sebenarnya punya **head start di domain knowledge** yang kompetitor lulusan IT belum tentu punya. Yang perlu kamu kejar hanyalah skill teknikal — dan itu yang akan kursus ini ajarkan.

---

## 4. "Hybrid Role" — Kapan Profesi Lain Tetap Perlu Skill DA

Skill DA bukan eksklusif untuk yang ingin pindah profesi total. Banyak profesional yang tetap di profesi asli mereka, tapi naik level signifikan dengan menambah skill data. Ini disebut **hybrid role** — peran utama tetap, tapi skill data jadi nilai tambah.

**HR + DA = People Analytics.** Seorang HR Manager yang bisa menarik data turnover, melakukan benchmark gaji ke pasar, dan menganalisis pola kapan karyawan paling sering resign — akan jauh lebih berdampak ke perusahaan daripada HR yang hanya bisa kelola administrasi. Di banyak perusahaan modern, posisi "People Analytics" membayar 30–50% lebih tinggi dari HR Generalist standar.

**Marketing + DA = Growth Analytics.** Seorang Marketing Lead yang bisa menganalisis funnel sendiri (dari ad impression sampai checkout), bisa baca hasil A/B test tanpa minta tolong tim DA, bisa setup dashboard campaign sendiri di Looker Studio — keputusan dia 2–3x lebih cepat dari yang harus antri request data. Orang seperti ini adalah kandidat utama untuk role Growth Marketing atau Marketing Manager.

**Finance + DA = Financial Analytics & Automation.** Seorang Finance Officer yang menguasai SQL dan Power BI bisa **otomatisasi 80% reporting bulanan** yang sebelumnya manual di Excel. Selain hemat waktu, akurasi naik karena tidak ada lagi human error copy-paste. Banyak orang Finance senior yang naik jadi Head of FP&A karena skill ini.

**Operations + DA = Operations Analytics.** Manajer pabrik atau supply chain yang bisa menganalisis data sensor IoT, kapasitas mesin, dan inventory turnover — bisa merekomendasikan keputusan operasional berbasis bukti, bukan asumsi. Hasilnya: efisiensi naik, biaya turun, dan posisi kamu jadi indispensable.

**Founder & UMKM + DA = Self-aware Decision Making.** Founder yang bisa baca dashboard penjualan sendiri, bisa lihat metric retention pelanggan, bisa identifikasi produk apa yang growth dan apa yang declining — tidak akan kaget saat pertumbuhan melambat. Banyak UMKM yang gagal bukan karena produknya buruk, tapi karena founder-nya buta data.

> **Pesan utama:** Belajar Data Analytics = belajar **bahasa kerja modern**. Mau lanjut jadi DA full-time atau jadi profesional dengan skill DA — keduanya valid, dan keduanya bernilai. Tidak ada "yang satu lebih baik dari yang lain" — yang penting adalah keputusan kamu konsisten dengan tujuan personal kamu.

---

## 5. Insight & Refleksi

### 5.1 Insight Closing Modul Ini

Kalau ada 1 hal yang harus kamu bawa pulang dari modul ini, ini dia:

> **Data Analyst adalah profesi paling fleksibel dan ramah pemula di ranah data** — bisa jadi destinasi karier akhir (banyak DA senior yang puas dan dibayar tinggi tetap di posisi DA), bisa jadi batu loncatan ke role data lain (Data Scientist, Analytics Engineer, ML Engineer, AI Engineer), bisa jadi skill pendamping untuk profesi non-DA. Pintu masuknya cuma satu: **kemauan kamu untuk mulai dan konsisten.**

Empat minggu ke depan akan terasa berat di beberapa titik (terutama Week 2 saat masuk Python, dan Week 3 saat materi statistics inferential). Itu normal. Yang membedakan peserta yang lulus dengan yang menyerah adalah **kepunyaan reason yang jelas** — kenapa mereka mulai dari awal.

Itulah kenapa di Modul 3 nanti kamu akan menulis Career Statement personal kamu. Itu akan jadi self-anchor saat motivasi turun.

### 5.2 Refleksi Singkat (5 menit)

Sebelum lanjut ke Modul 2 (Diferensiasi Profesi Data), luangkan 5 menit untuk menjawab 3 pertanyaan ini di catatan pribadi (file `.txt`, `.md`, atau notes app — bebas):

1. **Apa yang membuat kamu tertarik belajar Data Analyst?** Tulis 1–2 kalimat dengan jujur. Tidak harus keren atau formal. Contoh jawaban valid:
   - "Saya bosan kerja yang itu-itu saja dan dengar DA punya skill yang bisa dipakai di mana-mana."
   - "Saya HR di perusahaan startup, sering disuruh bikin report tapi saya nggak ngerti caranya."
   - "Saya fresh graduate, dengar DA gajinya bagus dan banyak lowongan."

2. **Industri / bidang apa yang paling kamu minati untuk berkarir?** Pilih dari Cluster 1–4 di Section 3.3, atau tulis bidang lain (healthcare, edutech, government, NGO, dll).

3. **Apakah kamu menargetkan jadi DA full-time, profesional non-DA dengan skill data, atau masih eksplorasi?** Tidak apa-apa kalau belum yakin — kita revisit di Modul 3.

**Output:** simpan jawaban kamu di file pribadi. **Jangan dihapus** — akan dipakai saat menulis Career Statement di Modul 3.

> **Catatan untuk peserta yang ikut kelas grup:** kamu tidak perlu bagikan jawaban ini ke siapa pun kalau tidak nyaman. Refleksi ini untuk diri sendiri dulu.

---

## 6. Bacaan Lanjutan & Sumber

Untuk yang ingin mendalami sebelum lanjut ke Modul 2, berikut sumber yang direkomendasikan. Tidak harus dibaca semua — pilih yang paling relevan dengan posisi kamu sekarang.

### 6.1 Pasar Kerja & Gaji

- **LinkedIn Talent Insights** — buka [linkedin.com/jobs](https://linkedin.com/jobs), search "Data Analyst" + filter location Indonesia. Pelajari 5 lowongan teratas: requirement skill apa yang paling sering muncul, range gaji yang disebut.
- **Kalibrr Salary Report 2025/26** — di [kalibrr.com/blog](https://kalibrr.com/blog), cari laporan gaji per role.
- **Glints Talent Trends Indonesia** — di [glints.com/id/lowongan/talent-trends](https://glints.com/id), update setiap tahun.
- **JobStreet Indonesia** — kategori "Data, IT & Telecommunication", lihat trend posting.

### 6.2 Pemahaman Profesi Data

- **Coursera — Google Data Analytics Professional Certificate** — bisa di-audit gratis. Tidak perlu selesai, cukup buka kursus 1–2 untuk pemahaman umum.
- **Khan Academy — Statistics & Probability** — dasar statistik gratis, bahasa Inggris tapi ada subtitle Indonesia.
- **YouTube — Indonesia Data Analyst community** — channel seperti Data Wrangling Indonesia, DataChick, dan Belajar Data ID kasih konten praktis dalam Bahasa Indonesia.

### 6.3 Komunitas

- **Indonesia Data Analytics Community** di Telegram & Discord — banyak diskusi dan info lowongan.
- **LinkedIn Group "Data Analyst Indonesia"** — networking dan share peluang.
- **Kaggle Indonesia** — komunitas yang aktif kompetisi dan share dataset.

### 6.4 Dataset Free untuk Eksplorasi Mandiri

Untuk yang sudah gatal ingin mencoba sebelum Week 1 dimulai, berikut dataset publik yang bisa di-download gratis (akan dipakai juga di latihan-latihan minggu berikutnya):

- **Kaggle Datasets** — [kaggle.com/datasets](https://kaggle.com/datasets), butuh akun gratis. Dataset populer: Titanic, Superstore Sales, Iris.
- **Data Indonesia** — [data.go.id](https://data.go.id), portal data terbuka pemerintah Indonesia.
- **Badan Pusat Statistik (BPS)** — [bps.go.id](https://bps.go.id), data demografi & ekonomi Indonesia.
- **UCI Machine Learning Repository** — [archive.ics.uci.edu/ml](https://archive.ics.uci.edu/ml), dataset klasik untuk practice.
- **Mockaroo** — [mockaroo.com](https://mockaroo.com), generator dataset palsu untuk latihan tanpa khawatir privasi.

---

## Apa Selanjutnya?

Kamu sudah selesai Modul 1. Selamat — ini langkah pertama dan paling sering jadi titik orang menyerah (banyak yang mendaftar tapi tidak menyelesaikan modul intro).

**Selanjutnya:**

1. **Selesaikan refleksi Section 5.2** kalau belum — simpan jawaban kamu di file pribadi.
2. **Lanjut ke Modul 2: Diferensiasi Profesi Data** — folder `01-pre-week/02-diferensiasi-profesi/`. Modul itu akan bedah perbedaan DA, Data Engineer, Data Scientist, ML Engineer, AI Engineer, dan profesi data lainnya — supaya kamu punya peta lengkap "siapa mengerjakan apa" di ranah data.
3. **(Opsional)** kalau ada waktu, buka 1 dataset di Kaggle dan klik-klik tampilannya — bukan untuk analisis, hanya untuk membiasakan diri lihat data tabular.

Sampai jumpa di Modul 2.

---

**Akhir Modul 1 · Pre-Week**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan Modul

Setelah membaca modul ini, peserta:
1. Paham apa itu Data Analyst dalam konteks dunia kerja Indonesia 2026
2. Mengerti tugas pokok DA sehari-hari (8 daily tasks)
3. Tahu kondisi pasar kerja DA di Indonesia: jumlah lowongan, gaji, perusahaan top hire
4. Paham konsep "hybrid role" — kapan profesi non-DA tetap perlu skill data
5. Termotivasi melanjutkan ke Modul 2 (Diferensiasi Profesi)

## Durasi

~45–60 menit baca mandiri.

## Prasyarat

Tidak ada — ini modul pertama.

## Format Output

- **`materi.md`** — modul tertulis lengkap (~3,500 kata, format ebook chapter)
- **`latihan/soal.md`** — refleksi singkat (5 menit, dijawab di catatan pribadi)
- **`cheatsheet.md`** — ringkasan 1 halaman untuk recap cepat
- **`mentor-notes.md`** — briefing kalau modul ini disampaikan oleh mentor

## Struktur Konten

| Section | Topik |
|---|---|
| 1 | Selamat Datang — Kenapa kamu di sini & yang akan kamu dapat |
| 2 | Apa itu Data Analyst — Analogi warung, definisi, 8 tugas pokok, vs Data Literacy |
| 3 | Pasar Kerja Indonesia 2026 — Lowongan, gaji, top industries, background non-IT |
| 4 | Hybrid Role — Skill DA di profesi HR, Marketing, Finance, Operations, Founder |
| 5 | Insight & Refleksi — Closing + 3 pertanyaan refleksi |
| 6 | Bacaan Lanjutan — Pasar kerja, profesi, komunitas, dataset free |

## Gambar yang Diperlukan

Modul ini punya 2 placeholder `[GAMBAR DIPERLUKAN]` yang perlu di-screenshot manual:

1. **Section 3.1** — LinkedIn Job Search dengan filter "Data Analyst" + Indonesia. Tampilkan jumlah lowongan + beberapa logo perusahaan.
2. **Section 3.2** — Snippet Kalibrr / Glints Salary Report bagian DA Indonesia.

Detail apa yang harus di-capture & isinya nanti, sudah ditulis spesifik di lokasi placeholder masing-masing di `materi.md`.

## Catatan Mentor

- **Section 1.1** — kalau kelas grup, pakai sebagai ice breaker. Tanya posisi peserta sekarang (mahasiswa/transisi karir/profesional non-DA).
- **Section 2.1 (analogi warung)** — boleh diganti analogi lain yang relevan dengan latar belakang peserta. Misalnya untuk peserta HR semua, ganti ke analogi "data karyawan".
- **Section 3** — data pasar kerja perlu **update tahunan**. Cek LinkedIn 1 hari sebelum sesi untuk angka terbaru.
- **Section 5.2** — beri 5 menit hening. **Jangan paksa peserta share** kecuali mereka mau.

## Tugas Selanjutnya

Lanjut ke `02-diferensiasi-profesi/` — Modul 2 yang membedah profesi DA, DE, AE, DS, MLE, AIE, dan BI Developer.

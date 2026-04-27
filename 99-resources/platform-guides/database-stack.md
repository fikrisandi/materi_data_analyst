# Database Stack — Panduan Lengkap untuk Kursus

> **Status:** Wajib dibaca sebelum Week 1 Day 3 (SQL Basics).
> **Tujuan:** Jelaskan database mana yang dipakai di setiap minggu, kenapa, dan cara setup.

---

## 1. Filosofi Pemilihan Stack

Banyak kursus DA langsung loncat ke MySQL atau PostgreSQL — kompleks dan bikin pemula stuck di setup. Kursus ini pakai **3-tier approach**: mulai dari yang paling simple, naik bertahap ke yang real-industry.

```
Week 1: SQLite (file)
   ↓
Week 2: PostgreSQL (server)
   ↓
Week 2-3: BigQuery (cloud)
```

**Mengapa progressive?**
- 95% sintaks SQL **sama** antar database — fokus belajar SQL, bukan setup
- SQLite untuk dasar (no setup pain), PostgreSQL untuk realistic experience, BigQuery untuk skala besar
- DA real di industri pakai kombinasi — bukan 1 database saja

---

## 2. Database Per Tier

### Tier 1: SQLite (Week 1)

**Apa itu:** Database file-based. 1 file `.db` = 1 database. Tidak perlu install server.

**Mengapa pakai:** Pemula tidak terdistraksi setup — fokus belajar SQL.

**Cara akses:**
- File: `02-week-1/day-3-am-sql-basics/data/kopi_kita.db`
- Tools: **SQLTools (VSCode extension)** atau **DBeaver**

**Limitations:** Single-user (tidak cocok production), tidak ada user management, performance buruk untuk dataset > 10 juta baris.

**Use case industri:** mobile apps (offline storage), prototype, embedded systems.

### Tier 2: PostgreSQL (Week 2)

**Apa itu:** Database server-based, open-source, **standar industri** untuk web apps & DA.

**Mengapa pakai:** Realistic experience — sebagian besar perusahaan Indonesia pakai PostgreSQL atau MySQL. DA wajib bisa connect ke server database.

**Cara setup (pilih 1):**

**Option A — Docker (Recommended)**

Install Docker Desktop ([docker.com/products/docker-desktop](https://docker.com/products/docker-desktop)). Lalu:

```bash
docker run -d --name savvys-postgres \
  -e POSTGRES_PASSWORD=savvys2026 \
  -e POSTGRES_DB=kopi_kita \
  -p 5432:5432 \
  postgres:15
```

PostgreSQL jalan di `localhost:5432`. Username default: `postgres`, password: `savvys2026`.

Untuk stop: `docker stop savvys-postgres`. Start lagi: `docker start savvys-postgres`.

**Option B — Supabase (Cloud, gratis)**

1. Sign up di [supabase.com](https://supabase.com)
2. Bikin project baru (free tier — 500MB storage, cukup untuk learning)
3. Database connection string ada di Project Settings → Database
4. Connect lewat DBeaver pakai connection string

**Option C — PostgreSQL Native Install**

[postgresql.org/download](https://postgresql.org/download). Lebih ribet daripada Docker, tidak recommended untuk pemula.

**Cara akses:**
- **DBeaver** (recommended) — GUI client
- **psql** — command line tool yang ikut PostgreSQL install
- VSCode dengan SQLTools + driver PostgreSQL

**Migrate Kopi Kita data ke PostgreSQL:** ada script di `02-week-1/day-3-am-sql-basics/_migrate_to_postgres.py` (akan di-generate kalau peserta sampai sini).

### Tier 3: BigQuery (Week 2-3)

**Apa itu:** Data warehouse cloud Google. **Standar untuk analytics scale besar** (miliaran baris).

**Mengapa pakai:** Pengalaman query dataset publik berskala besar yang tidak bisa di-handle SQLite/PostgreSQL local.

**Cara setup:**
- Sandbox: gratis, tanpa kartu kredit
- Akses: [console.cloud.google.com/bigquery](https://console.cloud.google.com/bigquery) dengan akun Gmail
- Quota: 10 GB storage, 1 TB query/bulan (cukup untuk learning)

**Tools akses:**
- Browser console (default)
- DBeaver (advanced — perlu service account JSON)

**Public datasets bagus untuk latihan:**
- `bigquery-public-data.usa_names`
- `bigquery-public-data.covid19_open_data`
- `bigquery-public-data.new_york_taxi_trips`
- `bigquery-public-data.google_analytics_sample`
- Banyak lagi di [Public Dataset Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset)

---

## 3. DBeaver — Universal Database Client

**Mengapa wajib install:** 1 tools bisa connect ke **semua** database (SQLite, PostgreSQL, MySQL, BigQuery, dll). GUI lebih nyaman dari command line untuk eksplorasi visual.

### 3.1 Install DBeaver Community Edition (Gratis)

1. Buka [dbeaver.io/download](https://dbeaver.io/download/)
2. Download **DBeaver Community Edition** (gratis)
3. Install dengan default options

### 3.2 Connect ke SQLite

1. Buka DBeaver → klik **New Database Connection** (icon plug di kiri atas)
2. Pilih **SQLite**
3. Path: browse ke `kopi_kita.db`
4. Test Connection → Finish
5. Database muncul di sidebar kiri. Expand untuk lihat tabel.

### 3.3 Connect ke PostgreSQL

1. New Database Connection → **PostgreSQL**
2. Server Host: `localhost` (kalau Docker) atau dari Supabase
3. Port: `5432`
4. Database: `kopi_kita` (atau nama yang dibuat)
5. Username: `postgres`
6. Password: `savvys2026` (atau yang dibuat)
7. Saat ditanya download driver — klik Yes
8. Test Connection → Finish

### 3.4 Tour DBeaver

```
┌────────────────────────────────────────────────────────────┐
│ File · Edit · View · Window · Help                         │
├────────────────────┬───────────────────────────────────────┤
│ [DATABASE NAV]     │ [SQL EDITOR]                          │
│                    │                                       │
│ ▼ kopi_kita.db     │  SELECT * FROM transaksi              │
│   ▼ Tables         │  LIMIT 10;                            │
│     ▶ cabang       │                                       │
│     ▶ menu         │  [Execute]  [Format]  [Save]          │
│     ▶ pelanggan    │                                       │
│     ▶ transaksi    │                                       │
├────────────────────┴───────────────────────────────────────┤
│ [RESULTS]                                                  │
│ id_transaksi | tanggal    | id_cabang | ...                │
│ TRX00001     | 2026-01-02 | C001      | ...                │
└────────────────────────────────────────────────────────────┘
```

**Operasi sehari-hari di DBeaver:**
- Klik kanan tabel → **View Data → All Rows** (lihat isi tabel)
- Klik kanan tabel → **Generate SQL → SELECT** (generate query template)
- F5 di SQL editor untuk execute
- Ctrl+Space untuk auto-complete kolom & tabel
- View → ER Diagram untuk visualisasi schema relations

### 3.5 DBeaver vs SQLTools (VSCode)

| Aspek | DBeaver | SQLTools (VSCode) |
|---|---|---|
| Visual exploration | ✅ Bagus (data preview, ER diagram) | OK |
| SQL editing | OK | ✅ Bagus (sama editor dengan code) |
| Multi-database | ✅ Universal | OK (perlu install driver) |
| Performance | OK | Lebih cepat |
| Best for | Eksplor data, schema design | Tulis & test query inline dengan code |

**Rekomendasi:** Pakai **keduanya**. DBeaver untuk eksplor, SQLTools untuk nulis code yang akan di-commit.

---

## 4. Latihan & Workflow Per Sesi

### Week 1 Day 3 AM — SQLite Basic

- **Database:** `kopi_kita.db` (sudah ada di `data/`)
- **Tools:** DBeaver atau SQLTools
- **Latihan:** 12 soal di `latihan/soal.md` — semua di SQLite
- **Output:** `jawaban.sql` di portfolio

### Week 1 Day 3 PM — DQL & BigQuery

- **Database:** SQLite (kopi_kita.db) + BigQuery
- **Tools:** DBeaver untuk SQLite, browser untuk BigQuery
- **Latihan:** 10 soal — sebagian SQLite, sebagian BigQuery public data

### Week 2 Day 4 AM — SQL Advanced

- **Database:** PostgreSQL (Docker) — migrasi data dari SQLite
- **Tools:** DBeaver
- **Latihan:** Window function, CTE, advanced — di PostgreSQL

### Week 2 Day 4 PM — BigQuery Hands-On

- **Database:** BigQuery
- **Tools:** Browser console + DBeaver (advanced)
- **Latihan:** Analytics dataset publik (NYC Taxi, Google Analytics)

---

## 5. Troubleshooting

### Q: "Saya stuck install Docker, pakai apa?"
A: Pakai Supabase free tier — cloud, no install. Atau skip PostgreSQL session, lanjut SQLite + BigQuery saja.

### Q: "DBeaver lambat / freeze."
A: Allocate lebih banyak RAM di `dbeaver.ini` (option `-Xmx2048m` jadi `-Xmx4096m`).

### Q: "Connect Postgres gagal: 'connection refused'."
A: Pastikan container running: `docker ps`. Kalau tidak ada, start: `docker start savvys-postgres`.

### Q: "BigQuery muncul 'billing required'."
A: Mode Sandbox sudah aktif — tapi beberapa operasi (export, scheduled query) butuh billing. Untuk learning cukup query saja, tidak perlu billing.

### Q: "Bisa pakai MySQL aja?"
A: Bisa. Sintaks SQL 95% sama. Tapi kursus standar pakai PostgreSQL karena lebih banyak feature analytics (window function, CTE) yang akan dipakai Week 2 Day 4.

---

## 6. Tools Lain (Opsional)

| Tools | Deskripsi | Kapan Pakai |
|---|---|---|
| **pgAdmin** | GUI khusus PostgreSQL | Kalau prefer interface yang khusus PG |
| **TablePlus** | Modern DB client (paid, ada free tier) | Alternatif DBeaver kalau prefer UX modern |
| **DataGrip** | JetBrains DB IDE (paid) | Kalau pakai PyCharm/IntelliJ |
| **Beekeeper Studio** | Open-source modern client | Alternatif lighter dari DBeaver |

Tidak wajib — DBeaver Community sudah cukup untuk semua kebutuhan kursus.

---

## 7. Cheat Sheet Cepat

```bash
# === SQLite ===
# Buka file di DBeaver atau SQLTools

# === PostgreSQL via Docker ===
docker run -d --name savvys-postgres \
  -e POSTGRES_PASSWORD=savvys2026 \
  -p 5432:5432 \
  postgres:15

# Stop / start
docker stop savvys-postgres
docker start savvys-postgres

# Connect via psql (CLI)
docker exec -it savvys-postgres psql -U postgres

# === BigQuery ===
# Browser: console.cloud.google.com/bigquery
# Login dengan Gmail, sandbox aktif otomatis
```

---

## 8. Update Log

| Tanggal | Perubahan |
|---|---|
| 2026-04-27 | Versi awal — clarify SQLite (W1) → PostgreSQL (W2) → BigQuery (W2-3) |

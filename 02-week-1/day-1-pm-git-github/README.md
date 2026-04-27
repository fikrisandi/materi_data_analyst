# Week 1 · Day 1 PM
# Git & GitHub — Version Control untuk Data Analyst

> **Tujuan modul:** Setelah membaca dan mengerjakan modul ini, kamu paham konsep version control, bisa pakai command Git dasar, punya repo `data-analyst-portfolio` aktif di GitHub, dan sudah push 3 file Pre-Week.
>
> **Estimasi waktu:** 2.5 jam · **Format:** modul step-by-step dengan latihan langsung.

---

## 1. Mengapa Version Control? — Analogi Save Game

Sebelum mulai install dan command, mari pahami **kenapa version control wajib untuk DA professional**.

### 1.1 Skenario yang Mungkin Pernah Kamu Alami

Bayangkan kamu kerjakan analisis di Excel. Kamu nge-save jadi `Analisis Penjualan.xlsx`. Lalu kamu edit, save lagi. Atasan minta versi sebelumnya — tapi kamu sudah ketimpa. Kamu bikin `Analisis Penjualan v2.xlsx`. Edit lagi, save jadi `Analisis Penjualan v3 final.xlsx`. Lalu ada revisi → `Analisis Penjualan v3 final FIX.xlsx`. Dan akhirnya `Analisis Penjualan v3 final FIX TENGAH MALAM REVISI.xlsx`.

Kamu pernah?

Itu **version control manual** — dan caranya sangat tidak scalable. Kalau kamu kerja sama tim, ditambah lagi kekacauan: orang lain edit file yang sama, ada conflict, tidak tahu siapa edit apa kapan.

### 1.2 Analogi Save Game

Bayangkan main RPG. Sebelum boss fight susah, kamu **save game**. Kalau mati, kamu **load** dari save terakhir.

Sekarang bayangkan game yang lebih canggih: kamu bisa save **kapan pun**, dengan **nama save spesifik**, **catatan kenapa save di titik ini**, dan **bisa balik ke save mana pun di history**. Bahkan kalau kamu main multiplayer, semua pemain bisa lihat history save satu sama lain.

**Itu Git.**

> **Definisi:** Git adalah **version control system** yang melacak setiap perubahan file di project kamu, kapan pun kamu mau. Kamu bisa lihat history lengkap, balik ke versi sebelumnya, atau gabungkan kerjaan kamu dengan kerjaan tim.

### 1.3 Mengapa Khusus untuk DA Penting?

Banyak pemula DA mengira Git cuma untuk software engineer. Kenyataannya, untuk DA juga **wajib**, karena:

1. **Code analisis berubah terus.** Query SQL kamu, notebook Python kamu, model statistik kamu — semua berevolusi. Tanpa Git, kamu akan kesulitan track "kenapa di v3 angka revenue beda dari v2?"
2. **Kolaborasi dengan tim.** DA jarang kerja sendiri. Pakai Git supaya tim DA + DE + DS bisa edit project yang sama tanpa saling timpa.
3. **Portfolio di GitHub.** Recruiter DA hampir selalu cek GitHub kamu. Tanpa portofolio Git, kamu kehilangan signal kuat saat melamar.
4. **Reproducibility.** Audit "siapa edit query ini kapan" sering dibutuhkan di perusahaan finansial atau healthcare. Git kasih traceability.

---

## 2. Konsep Dasar Git

Sebelum command, pahami dulu **3 area** yang Git pakai:

```
┌──────────────────┐    add     ┌──────────────────┐   commit   ┌──────────────────┐
│                  │ ─────────→ │                  │ ────────→  │                  │
│  Working Dir     │            │  Staging Area    │            │  Repository      │
│                  │            │                  │            │  (.git folder)   │
│  Folder kerja    │            │  Antrian file    │            │  Snapshot final  │
│  yang kamu edit  │ ←───────── │  yang siap di-   │            │  (history)       │
│                  │  reset     │  commit          │            │                  │
└──────────────────┘            └──────────────────┘            └──────────────────┘
```

### Penjelasan 3 Area

**1. Working Directory** — folder project kamu yang sedang kamu edit. File `.py`, `.md`, `.xlsx`, dll. Git "tahu" semua perubahan di sini, tapi belum melacak.

**2. Staging Area** — antrian file yang **siap di-commit**. Kamu pilih file mana yang masuk antrian ini dengan `git add`. Ini lapisan pemisah antara "perubahan iseng" dengan "perubahan yang sengaja kamu simpan".

**3. Repository** (`.git/` folder) — tempat Git simpan snapshot final dengan history lengkap. Kamu commit file dari staging ke sini dengan `git commit`.

> **Mental model:** kamu lagi packing untuk perjalanan.
> - Working dir = isi kamar berantakan
> - Staging area = koper yang sedang diisi
> - Repository = perjalanan yang sudah mulai (tidak bisa diubah lagi tanpa `revert`)

### Lalu GitHub?

**Git** = software local (di laptop kamu).
**GitHub** = website cloud yang menyimpan Git repository, supaya kamu bisa share & kolaborasi.

Hubungan:
```
┌──────────────────┐                ┌──────────────────┐
│  Git (LOCAL)     │   push    →    │  GitHub (CLOUD)  │
│  di laptop kamu  │                │  github.com/...  │
│                  │ ←   pull       │                  │
└──────────────────┘                └──────────────────┘
```

Analogi: Git seperti **draft di laptop**, GitHub seperti **Google Drive untuk Git** yang bisa dibagi dengan tim.

> **Catatan:** GitLab, Bitbucket adalah alternatif GitHub. Tapi GitHub paling populer & wajib untuk portfolio DA. Kita pakai GitHub.

---

## 3. Command Inti Git

Mari praktik dengan project kecil. Buka terminal:

```bash
cd ~/savvys-da-kursus/portfolio
ls
```

Output akan menampilkan folder yang sudah dibuat di Day 1 AM (`00-career-statement`, `01-excel-foundation`, dst).

### 3.1 `git init` — Inisialisasi Repository

```bash
git init
```

Output:
```
Initialized empty Git repository in C:/Users/YourName/savvys-da-kursus/portfolio/.git/
```

Yang baru terjadi: Git buat folder tersembunyi `.git/` di sini. Folder ini berisi **semua history & metadata** repository. Jangan dihapus, jangan diedit manual.

Cek dengan:

```bash
ls -la
```

Kamu lihat folder `.git/` muncul.

### 3.2 `git status` — Cek Status

```bash
git status
```

Output:
```
On branch main

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        00-career-statement/
        01-excel-foundation/
        ...

nothing added to commit but untracked files present (use "git add" to track)
```

Penjelasan:
- "On branch main" → kamu di branch utama
- "No commits yet" → belum ada commit
- "Untracked files" → file yang Git belum tahu

`git status` adalah command yang akan kamu pakai **paling sering**. Selalu cek status sebelum & sesudah operasi.

### 3.3 `git add` — Pindahkan ke Staging

Add semua file:

```bash
git add .
```

`.` artinya "semua file di folder ini". Atau spesifik:

```bash
git add 00-career-statement/career-statement.md
```

Cek lagi status:

```bash
git status
```

Output sekarang:
```
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   00-career-statement/career-statement.md
        new file:   00-career-statement/skill-mapping.md
        ...
```

File-file sudah masuk staging area (warna hijau di terminal modern).

### 3.4 `git commit` — Save Snapshot

```bash
git commit -m "Initial commit: portfolio structure"
```

Penjelasan:
- `-m "..."` → message yang menjelaskan kenapa kamu commit
- Pesan commit harus **deskriptif** (tidak boleh "update", "fix", "asdf")

Output:
```
[main (root-commit) abc1234] Initial commit: portfolio structure
 9 files changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 00-career-statement/...
```

`abc1234` adalah **commit hash** — ID unik untuk commit ini.

### 3.5 `git log` — Lihat History

```bash
git log
```

Output:
```
commit abc1234567890abcdef (HEAD -> main)
Author: Nama Lengkap <email@gmail.com>
Date:   Mon Apr 27 10:00:00 2026 +0700

    Initial commit: portfolio structure
```

Untuk view yang lebih ringkas:

```bash
git log --oneline
```

Output:
```
abc1234 Initial commit: portfolio structure
```

### 3.6 `git diff` — Lihat Perubahan

Edit file `00-career-statement/career-statement.md` (tambah 1 baris). Lalu:

```bash
git diff
```

Output akan menampilkan perubahan dengan format:
```
diff --git a/00-career-statement/career-statement.md b/00-career-statement/career-statement.md
index abc..def 100644
--- a/00-career-statement/career-statement.md
+++ b/00-career-statement/career-statement.md
@@ -10,3 +10,4 @@
 baris lama 1
 baris lama 2
+baris baru yang ditambah
 baris lama 3
```

Tanda `+` = ditambah, tanda `-` = dihapus.

### 3.7 Cycle Standard

Workflow daily di Git:

```bash
# 1. Cek status (apa yang berubah?)
git status

# 2. Lihat diff (perubahannya apa?)
git diff

# 3. Add file yang mau di-commit
git add <file>

# 4. Commit dengan pesan jelas
git commit -m "Pesan commit yang clear"

# 5. (kalau sudah connect ke GitHub) Push
git push
```

> **[GAMBAR DIPERLUKAN — Terminal dengan Cycle Git Berhasil]**
> **Apa yang harus di-screenshot:** terminal dengan urutan command `git status` → `git add .` → `git commit -m "..."` → `git log --oneline` yang berhasil semua.
> **Konteks isi nanti:** Visual proof "alur Git berhasil" untuk peserta yang mengikuti tutorial.

---

## 4. GitHub — Bikin Akun & Repo Pertama

### 4.1 Bikin Akun GitHub (Skip kalau sudah punya)

1. Buka [github.com](https://github.com), klik "Sign up"
2. Isi email, password, username
3. **Pilih username yang professional** — ini akan jadi URL portofolio kamu (`github.com/USERNAME`). Hindari nama-nama lucu / typo. Contoh baik: `nama-lengkap`, `firstinitial-lastname`, `realname`. Hindari: `xX_DataKing_Xx`, `analyst123`.
4. Verifikasi email
5. Pilih plan **Free** (cukup untuk DA portfolio)

> **[GAMBAR DIPERLUKAN — GitHub Profile Default]**
> **Apa yang harus di-screenshot:** halaman GitHub profile baru (kosong, tanpa repo).
> **Konteks isi nanti:** Starting state — peserta lihat seperti apa GitHub baru, supaya tahu kalau sudah berhasil signup.

### 4.2 Bikin Repository Baru di GitHub

1. Klik tombol "+" di kanan atas → "New repository"
2. **Repository name:** `data-analyst-portfolio`
3. **Description:** "Data Analyst portfolio — Savvys Education 4-week course (2026)"
4. **Public** (bukan Private — supaya bisa di-link dari CV)
5. **JANGAN centang** "Add a README file" (kita sudah punya project local, kalau centang akan conflict)
6. **JANGAN centang** "Add .gitignore"
7. **JANGAN centang** "Choose a license"
8. Klik "Create repository"

GitHub akan tampilkan halaman dengan instruksi setup. **Salin URL repository kamu** — ada di kanan atas, format:
```
https://github.com/USERNAME/data-analyst-portfolio.git
```

### 4.3 Connect Local Repo ke GitHub

Di terminal (di folder `~/savvys-da-kursus/portfolio` yang sudah `git init`):

```bash
git remote add origin https://github.com/USERNAME/data-analyst-portfolio.git
```

Ganti `USERNAME` dengan username GitHub kamu.

Penjelasan:
- `remote` = tempat penyimpanan jauh (GitHub)
- `origin` = nama default untuk remote utama (bisa diganti, tapi biasanya pakai default)

Cek:

```bash
git remote -v
```

Output:
```
origin  https://github.com/USERNAME/data-analyst-portfolio.git (fetch)
origin  https://github.com/USERNAME/data-analyst-portfolio.git (push)
```

### 4.4 Push ke GitHub

```bash
git push -u origin main
```

Penjelasan:
- `-u origin main` = set `origin/main` sebagai upstream branch (cuma perlu sekali)
- Setelah ini, cukup pakai `git push` saja

Saat push pertama kali, akan muncul prompt login. Ada 2 cara:

**Cara A — HTTPS dengan Personal Access Token (PAT):**
1. Di GitHub: Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token (classic), centang scope `repo`
3. Copy token (cuma muncul sekali!)
4. Saat terminal minta password, paste **token**, bukan password GitHub

**Cara B — SSH (recommended untuk jangka panjang):** kita setup di Section 5.

Setelah push berhasil:

```bash
Enumerating objects: 12, done.
Counting objects: 100% (12/12), done.
...
To https://github.com/USERNAME/data-analyst-portfolio.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.
```

🎉 **Refresh halaman repo di GitHub** — file kamu sekarang ada di sana.

> **[GAMBAR DIPERLUKAN — GitHub Repo dengan File Visible]**
> **Apa yang harus di-screenshot:** halaman repo GitHub setelah push pertama berhasil. Tampilkan list file/folder dan commit terakhir di header.
> **Konteks isi nanti:** Bukti visual "kerjaan saya sudah cloud-backed".

---

## 5. SSH Key Setup (Push Tanpa Password)

Pakai HTTPS dengan token harus paste token tiap kali. Lebih praktis pakai SSH.

### 5.1 Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "email-kamu@gmail.com"
```

Saat ditanya:
- "Enter file in which to save the key" → tekan Enter (default OK)
- "Enter passphrase" → boleh kosong (tekan Enter 2x) atau kasih passphrase tambahan untuk security

Output:
```
Your identification has been saved in /Users/yourname/.ssh/id_ed25519
Your public key has been saved in /Users/yourname/.ssh/id_ed25519.pub
```

### 5.2 Copy Public Key

**Mac/Linux:**
```bash
cat ~/.ssh/id_ed25519.pub
```

**Windows (Git Bash):**
```bash
cat ~/.ssh/id_ed25519.pub
```

Copy output (mulai dari `ssh-ed25519 ...`).

### 5.3 Tambahkan ke GitHub

1. GitHub → Settings → SSH and GPG keys → "New SSH key"
2. Title: "Laptop Kerja Savvys" (atau apa pun deskriptif)
3. Paste public key
4. Add SSH key

### 5.4 Ganti Remote dari HTTPS ke SSH

```bash
git remote set-url origin git@github.com:USERNAME/data-analyst-portfolio.git
```

Test:
```bash
ssh -T git@github.com
```

Output expected:
```
Hi USERNAME! You've successfully authenticated, but GitHub does not provide shell access.
```

Sekarang `git push` tidak perlu password lagi.

---

## 6. Workflow Daily

Workflow yang akan kamu pakai setiap hari sepanjang kursus:

```bash
# 1. Pull update terbaru (kalau kerja di banyak laptop)
git pull

# 2. Edit file di VSCode

# 3. Cek apa yang berubah
git status
git diff

# 4. Add file yang mau di-commit
git add 00-career-statement/career-statement.md
# atau add semua: git add .

# 5. Commit dengan pesan clear
git commit -m "Update career statement: tambah TIMELINE komponen"

# 6. Push ke GitHub
git push
```

### Aturan Commit Message yang Baik

✅ **Baik:**
- "Update career statement: tambah TIMELINE komponen"
- "Add VLOOKUP exercise solution"
- "Fix typo in skill mapping template"

❌ **Buruk:**
- "update"
- "fix"
- "asdf"
- "udah"

**Format yang umum dipakai (Conventional Commits, opsional):**

```
<type>: <subject>

contoh:
feat: add SQL exercise solution
fix: typo di README week 1
docs: update career statement template
refactor: rename folder portfolio-da → data-analyst-portfolio
```

---

## 7. .gitignore — File yang Tidak Di-track

Beberapa file **tidak boleh masuk Git**:

- File credential (`.env`, `secret.json`)
- File besar yang bisa regenerate (`__pycache__/`, `node_modules/`)
- File OS (`.DS_Store` di Mac, `Thumbs.db` di Windows)
- File temporary editor (`.vscode/settings.json` — kadang ya, kadang tidak)

Bikin file `.gitignore` di root project (kalau belum ada). Isi:

```gitignore
# Python
__pycache__/
*.pyc
*.pyo
.ipynb_checkpoints/

# Environment
.env
.venv/
venv/

# Editor
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
desktop.ini

# Data files (jangan commit dataset besar — pakai link/Kaggle)
*.csv
*.xlsx
data/raw/
data/big/
```

> **Catatan tentang dataset:** untuk DA portfolio, **dataset kecil (<10 MB)** boleh di-commit. Dataset besar atau berisi data sensitif → jangan. Pakai link ke Kaggle/data publik di README.

Add & commit `.gitignore`:

```bash
git add .gitignore
git commit -m "Add .gitignore"
git push
```

---

## 8. Branching Basic (Intro)

Branch = "garis paralel" tempat kamu bisa eksperimen tanpa ganggu main branch.

Skenario: kamu mau coba ide analisis baru, tapi belum yakin hasilnya benar. Kalau langsung commit ke main, history main jadi kotor dengan eksperimen yang mungkin di-revert.

```bash
# bikin branch baru
git checkout -b coba-segmentasi-baru

# kerja di branch ini
# ... edit, add, commit ...

# kalau hasilnya bagus, merge balik ke main
git checkout main
git merge coba-segmentasi-baru

# atau kalau tidak jadi, hapus
git branch -d coba-segmentasi-baru
```

Branching akan kita bahas lebih dalam di Week 2 saat materi Python project. Untuk sekarang, **cukup pakai `main` branch** untuk semua portofolio Pre-Week + Week 1.

---

## 9. Latihan: Push Folder `00-career-statement/` ke GitHub

Sekarang aplikasikan semua yang kamu pelajari. **Tugas:** push 3 file Pre-Week kamu ke GitHub repo.

### Step 1 — Pastikan File Sudah Ada

Di folder `~/savvys-da-kursus/portfolio/00-career-statement/`, pastikan ada:
- `career-statement.md` (dari Pre-Week Modul 3)
- `skill-mapping.md`
- `target-role.md`

Kalau belum, kamu bisa copy template dari folder kursus:
```
01-pre-week/03-career-statement/latihan/template-career-statement.md
```
Lalu rename & isi sesuai personal kamu.

### Step 2 — Bikin README untuk Repo

Di root portfolio (`~/savvys-da-kursus/portfolio/`), bikin file `README.md`:

```markdown
# Data Analyst Portfolio — [Nama Kamu]

Portofolio belajar Data Analyst di kursus 4 minggu Savvys Education (2026).

## Tentang Saya

[1–2 kalimat singkat tentang kamu — bisa diambil dari Career Statement]

## Struktur Folder

- `00-career-statement/` — Career Statement, Skill Mapping, Target Role
- `01-excel-foundation/` — (akan diisi Week 1)
- `02-sql-bigquery/` — (akan diisi Week 1-2)
- `03-python-pandas/` — (akan diisi Week 2-3)
- `04-data-acquisition/` — (akan diisi Week 3)
- `05-statistics-case/` — (akan diisi Week 3)
- `06-visualization/` — (akan diisi Week 4)
- `07-storytelling-deck/` — (akan diisi Week 4)
- `08-capstone/` — (akan diisi Week 4)

## Status

🚧 In Progress — Week 1
```

### Step 3 — Add, Commit, Push

```bash
cd ~/savvys-da-kursus/portfolio
git add README.md 00-career-statement/
git commit -m "Add Pre-Week deliverables: career statement, skill mapping, target role"
git push
```

### Step 4 — Verify di GitHub

Buka `https://github.com/USERNAME/data-analyst-portfolio` di browser. Pastikan:
- README muncul di halaman utama
- Folder `00-career-statement/` ada
- 3 file di dalamnya bisa diklik & dibaca

🎉 **Selamat — kamu sudah punya portofolio publik DA pertama yang accessible di internet.**

### Step 5 — Update Profile GitHub (Opsional, tapi Recommended)

Di profil GitHub kamu, tambahkan:
- Avatar (foto profesional)
- Bio (1 kalimat — bisa dari Career Statement)
- Link ke LinkedIn

Bonus: bikin "GitHub Profile README" — repo dengan nama persis sama dengan username kamu, isinya `README.md` yang akan muncul di profile page. Banyak template gratis di [github.com/abhisheknaiidu/awesome-github-profile-readme](https://github.com/abhisheknaiidu/awesome-github-profile-readme).

---

## Apa Selanjutnya?

Kamu sudah punya:
- ✅ Environment kerja siap (Day 1 AM)
- ✅ Repo `data-analyst-portfolio` aktif di GitHub
- ✅ 3 file Pre-Week di-push ke cloud

**Selanjutnya:**

1. **Selesaikan latihan Section 9** kalau belum semua
2. **Lanjut ke Day 2 AM — Excel Foundation** — folder `02-week-1/day-2-am-excel-foundation/`. Akan belajar Excel level menengah: pivot table, VLOOKUP, INDEX-MATCH, formula essentials, conditional formatting.
3. **Workflow daily mulai sekarang:** sebelum tutup laptop, jalankan `git status`, `git add .`, `git commit -m "..."`, `git push` — kebiasaan yang akan jadi otomatis.

> **Tip mentor:** kalau peserta selesai sebelum waktu habis, kasih bonus task — explore beberapa repo DA Indonesia yang sudah jadi reference (search "data analyst portfolio site:github.com" + "indonesia"), lihat struktur & README mereka.

Sampai jumpa di Day 2.

---

**Akhir Day 1 PM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan Sesi

Setelah sesi ini, peserta:
1. Paham konsep version control & kenapa Git wajib untuk DA
2. Bisa command Git dasar: init, add, commit, status, log, diff
3. Bisa pakai GitHub: bikin repo, push, pull, clone
4. Punya repo `data-analyst-portfolio` di GitHub
5. Sudah push 3 file Pre-Week (career-statement, skill-mapping, target-role) ke repo

## Durasi

~2.5 jam

## Prasyarat

- Sudah selesai Day 1 AM (Setup Environment) — Git terinstall & terkonfigurasi
- Sudah punya akun GitHub (gratis di [github.com](https://github.com))
- Sudah selesai Pre-Week Modul 3 (3 file output: career-statement.md, skill-mapping.md, target-role.md)

## Format Output

- `materi.md` — modul step-by-step (~3,000 kata)
- `latihan/soal.md` — workflow latihan: bikin repo, commit, push
- `cheatsheet.md` — Git command cheatsheet

## Struktur Konten

| Section | Topik |
|---|---|
| 1 | Mengapa Version Control? Analogi Save Game |
| 2 | Konsep Dasar Git (working dir, staging, repository) |
| 3 | Command Inti: init, add, commit, status, log |
| 4 | GitHub: Bikin Akun & Repo Pertama |
| 5 | SSH Key Setup (push tanpa password) |
| 6 | Workflow Daily: pull → edit → add → commit → push |
| 7 | .gitignore — File yang Tidak Di-track |
| 8 | Branching Basic (intro) |
| 9 | Latihan: Push Folder `00-career-statement/` ke GitHub |

## Output Portfolio

```
data-analyst-portfolio/                ← repo GitHub
├── README.md                          ← dari Pre-Week (intro portofolio)
└── 00-career-statement/
    ├── career-statement.md
    ├── skill-mapping.md
    └── target-role.md
```

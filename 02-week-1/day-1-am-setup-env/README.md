# Week 1 · Day 1 AM
# Setup Environment — VSCode, Python, Git

> **Tujuan modul:** Setelah membaca dan mengerjakan modul ini, kamu punya environment kerja yang siap dipakai sepanjang 4 minggu kursus: VSCode + Python (Miniconda) + Git + project folder yang terstruktur.
>
> **Estimasi waktu:** 2.5–3 jam (termasuk download & install). **Format:** modul tertulis step-by-step.

---

## 1. Mengapa Setup Penting & Apa Saja yang Akan Diinstall

Sebelum mulai install, mari pahami **kenapa kita pakai tools tertentu** — ini bukan acak.

Banyak peserta DA pemula bertanya: "Kenapa nggak langsung pakai Google Colab saja, semua di browser?". Pertanyaan wajar. Jawabnya: **Colab cocok untuk eksperimen cepat, tapi tidak cocok untuk DA professional**. Di dunia kerja DA real, kamu akan kerjakan project yang punya banyak file (data raw, notebook, report, dokumentasi), perlu version control (Git), perlu environment yang konsisten antar laptop pribadi & laptop kantor. Itu semua tidak bisa di Colab.

Berikut tools yang akan kita install hari ini, beserta alasan:

**1. VSCode (Visual Studio Code)** — code editor utama. Gratis, ringan, banyak extension. Industri-standard untuk DA, DE, MLE.

**2. Miniconda** — Python distribution + package manager. Lebih ringan dari Anaconda full (yang 3 GB++). Cukup untuk DA workflow.

**3. Git** — version control system. Wajib untuk DA professional — semua project di GitHub butuh Git.

**4. DBeaver Community Edition** — database GUI client universal. Bisa connect ke SQLite, PostgreSQL, MySQL, BigQuery, dll dalam 1 tools. Wajib untuk DA — akan dipakai mulai Week 1 Day 3.

**5. Terminal (Bash atau PowerShell)** — command line interface. Tidak diinstall (sudah ada di OS), tapi perlu kita pahami cara pakainya.

**6. Beberapa VSCode Extension** — Python, Jupyter, Excel Viewer, GitLens, dll.

**(Opsional — install nanti saat Week 2 Day 4):** Docker Desktop untuk run PostgreSQL local. Bisa di-skip kalau pakai Supabase cloud.

**Total disk space yang dibutuhkan:** ~3.5 GB. **Total waktu install (koneksi normal):** ~50 menit.

> **Alur belajar hari ini:**
>
> ```
> Mengerti ──→ Install ──→ Configure ──→ Verify ──→ First Project
>   alasan       tools       settings     it works    folder ready
> ```

---

## 2. Install VSCode + Extensions Wajib

### 2.1 Download & Install VSCode

**Untuk Windows:**

1. Buka [code.visualstudio.com](https://code.visualstudio.com)
2. Klik tombol "Download for Windows"
3. Buka file `VSCodeUserSetup-x64-x.x.x.exe` yang terdownload
4. Saat installer jalan, **centang semua opsi**:
   - ✅ Add to PATH (recommended)
   - ✅ Add "Open with Code" action to Windows Explorer file context menu
   - ✅ Add "Open with Code" action to Windows Explorer directory context menu
   - ✅ Register Code as an editor for supported file types
5. Klik Install, tunggu sampai selesai
6. Centang "Launch Visual Studio Code" di akhir, klik Finish

**Untuk Mac:**

1. Buka [code.visualstudio.com](https://code.visualstudio.com), klik "Download for Mac"
2. Drag file `Visual Studio Code.app` ke folder `Applications`
3. Buka VSCode dari Applications atau Spotlight (`⌘ + Space`, ketik "Visual Studio Code")
4. Saat ditanya "Are you sure you want to open it?", klik "Open"

**Untuk Linux (Ubuntu/Debian):**

```bash
sudo snap install --classic code
```

Atau via .deb dari website resmi.

> **[GAMBAR DIPERLUKAN — VSCode Welcome Screen]**
> **Apa yang harus di-screenshot:** halaman welcome VSCode setelah pertama kali dibuka. Tampilkan tab "Get Started" yang muncul default.
> **Konteks isi nanti:** memastikan peserta tahu seperti apa VSCode pertama kali. Pakai sebagai referensi visual saat mereka membandingkan dengan laptop mereka.

### 2.2 Install Extensions Wajib

Buka VSCode. Klik icon Extensions di sidebar kiri (icon kotak-kotak), atau shortcut `Ctrl+Shift+X` (Windows/Linux) / `⌘+Shift+X` (Mac).

Install extensions berikut **satu per satu** dengan mengetik nama di kolom search:

| # | Extension | Publisher | Kegunaan |
|---|---|---|---|
| 1 | **Python** | Microsoft | Support Python (autocomplete, debug, run) |
| 2 | **Jupyter** | Microsoft | Run Jupyter notebook di VSCode |
| 3 | **Pylance** | Microsoft | Type checking & faster Python intellisense |
| 4 | **Excel Viewer** | GrapeCity | Lihat file `.xlsx` di VSCode |
| 5 | **Rainbow CSV** | mechatroner | Highlight kolom CSV dengan warna |
| 6 | **GitLens** | GitKraken | Git inline annotations |
| 7 | **SQLTools** | Matheus Teixeira | Run SQL query di VSCode |
| 8 | **SQLTools SQLite Driver** | Matheus Teixeira | Driver untuk SQLite |
| 9 | **Material Icon Theme** | Philipp Kief | Icon yang lebih jelas di file explorer |
| 10 | **Better Comments** | Aaron Bond | Color-code comment (TODO, FIXME, dll) |

Cara install: ketik nama extension di search box, pilih yang author-nya benar (Microsoft / GitKraken / dll), klik "Install".

> **[GAMBAR DIPERLUKAN — Extensions Tab dengan List Installed]**
> **Apa yang harus di-screenshot:** VSCode Extensions tab dengan filter "@installed" — tampilkan minimal 10 extension di atas yang sudah terinstall.
> **Konteks isi nanti:** memastikan peserta install extension yang benar (bukan extension dengan nama mirip dari publisher tidak resmi).

### 2.3 Konfigurasi VSCode Dasar

Buka **Settings**: `Ctrl+,` (Windows/Linux) atau `⌘+,` (Mac).

Ubah settings ini (klik di kolom search settings, ketik nama setting):

- **Editor: Tab Size** → ganti ke `4` (untuk Python)
- **Editor: Insert Spaces** → centang (Python pakai spaces, bukan tab)
- **Editor: Word Wrap** → ganti ke `on` (supaya text tidak overflow ke kanan)
- **Editor: Format On Save** → centang (auto-format saat save)
- **Workbench: Color Theme** → pilih theme yang nyaman (default "Dark+" atau "Light+" sudah OK)
- **Workbench: Icon Theme** → pilih "Material Icon Theme"

> **Tip:** kalau setting di atas susah dicari via UI, klik icon `{}` di pojok kanan atas Settings — ini buka raw JSON. Salin block berikut:
>
> ```json
> {
>   "editor.tabSize": 4,
>   "editor.insertSpaces": true,
>   "editor.wordWrap": "on",
>   "editor.formatOnSave": true,
>   "workbench.iconTheme": "material-icon-theme"
> }
> ```

---

## 3. Install Miniconda + Setup Virtual Environment

### 3.1 Mengapa Miniconda?

Python bisa diinstall langsung dari [python.org](https://python.org), tapi kita pakai **Miniconda** karena:

1. **Manage multiple Python versions** — kursus ini pakai 3.12, project lain mungkin pakai 3.10. Conda bisa switch versi cepat.
2. **Manage packages dengan dependency yang clean** — saat install pandas, numpy, scikit-learn yang punya banyak dependency, conda lebih reliable dari pip biasa.
3. **Standard di industri DA/DS** — sebagian besar tutorial DA pakai conda.

### 3.2 Download & Install Miniconda

**Untuk Windows:**

1. Buka [docs.conda.io/miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Download "Miniconda3 Windows 64-bit"
3. Run installer. **Centang opsi "Add Miniconda3 to my PATH environment variable"** (walau ada warning "not recommended" — kita override karena lebih praktis)
4. Klik Install, tunggu

**Untuk Mac:**

1. Download "Miniconda3 macOS Apple M1" (kalau Mac M1/M2/M3) atau "Miniconda3 macOS 64-bit" (kalau Mac Intel)
2. Buka file `.pkg` yang terdownload
3. Ikuti installer

**Untuk Linux:**

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

### 3.3 Verifikasi Miniconda

Buka terminal baru:
- **Windows:** buka "Anaconda Prompt" dari Start Menu (bukan PowerShell biasa awalnya)
- **Mac/Linux:** buka Terminal

Jalankan:

```bash
conda --version
```

Output yang benar (contoh):

```
conda 24.x.x
```

Kalau muncul "conda is not recognized" → restart komputer atau cek PATH.

### 3.4 Buat Virtual Environment Khusus Kursus

Buat environment Python 3.12 khusus untuk kursus ini:

```bash
conda create -n savvys-da python=3.12 -y
```

Penjelasan command:
- `conda create` — bikin environment baru
- `-n savvys-da` — namanya `savvys-da`
- `python=3.12` — pakai Python versi 3.12
- `-y` — auto-confirm semua prompt

Tunggu sampai selesai. Setelah itu, **aktifkan environment**:

```bash
conda activate savvys-da
```

Kalau berhasil, prompt terminal kamu akan berubah jadi:

```
(savvys-da) C:\Users\YourName>
```

Tanda `(savvys-da)` di awal = kamu lagi di dalam environment ini.

### 3.5 Install Package Wajib

Sekarang install package yang akan dipakai sepanjang kursus:

```bash
conda install -y pandas numpy matplotlib seaborn jupyter openpyxl
pip install plotly beautifulsoup4 requests scikit-learn
```

Penjelasan singkat:
- `pandas` + `numpy` — data manipulation
- `matplotlib` + `seaborn` + `plotly` — visualisasi
- `jupyter` — notebook
- `openpyxl` — read/write Excel
- `beautifulsoup4` + `requests` — web scraping (Week 3)
- `scikit-learn` — basic ML (Week 3 statistics)

Tunggu 5–10 menit. Kalau ada error, coba `conda install` lagi atau tanya mentor.

### 3.6 Verifikasi Python & Package

```bash
python --version
```

Output:
```
Python 3.12.x
```

Test import package:

```bash
python -c "import pandas as pd; print(pd.__version__)"
```

Output (versi aktual mungkin beda):
```
2.2.x
```

> **[GAMBAR DIPERLUKAN — Terminal dengan Verifikasi Sukses]**
> **Apa yang harus di-screenshot:** terminal (Windows/Mac/Linux) dengan output `conda --version`, `python --version`, dan `python -c "import pandas as pd; print(pd.__version__)"` — semua jalan tanpa error.
> **Konteks isi nanti:** memastikan peserta tahu seperti apa "berhasil" — supaya kalau ada error mereka bisa identify cepat.

---

## 4. Install Git & Konfigurasi

### 4.1 Download & Install Git

**Untuk Windows:**

1. Buka [git-scm.com/download/win](https://git-scm.com/download/win)
2. Download Git for Windows (akan auto-detect 32/64-bit)
3. Run installer. Pakai **default semua** kecuali untuk:
   - "Adjusting your PATH environment" → pilih **"Git from the command line and also from 3rd-party software"** (tengah)
   - "Choosing the default editor" → pilih **VSCode** (bukan Vim default)
4. Selesai install

**Untuk Mac:**

```bash
# kalau belum ada Homebrew, install dulu:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install Git:
brew install git
```

**Untuk Linux (Ubuntu):**

```bash
sudo apt-get install git
```

### 4.2 Verifikasi Git

```bash
git --version
```

Output:
```
git version 2.x.x
```

### 4.3 Konfigurasi Git

Set nama & email yang akan tertaut ke setiap commit:

```bash
git config --global user.name "Nama Lengkap Kamu"
git config --global user.email "email-kamu@gmail.com"
```

> **Penting:** email ini **harus sama** dengan email yang akan kamu pakai untuk akun GitHub nanti. Kalau beda, commit kamu tidak akan kelihatan di GitHub profile sebagai "kamu".

Set default branch ke `main`:

```bash
git config --global init.defaultBranch main
```

Set default editor:

```bash
git config --global core.editor "code --wait"
```

Cek konfigurasi:

```bash
git config --list
```

Output yang muncul harus include:
```
user.name=Nama Lengkap Kamu
user.email=email-kamu@gmail.com
init.defaultBranch=main
core.editor=code --wait
```

> **[GAMBAR DIPERLUKAN — Output git config --list]**
> **Apa yang harus di-screenshot:** terminal dengan hasil `git config --list` yang menampilkan user.name, user.email, init.defaultBranch, core.editor.
> **Konteks isi nanti:** memastikan setup Git sudah benar sebelum lanjut ke session PM (Git & GitHub workflow).

### 4.4 Setup SSH Key (Opsional, untuk Push ke GitHub Tanpa Password)

> Skip dulu kalau belum perlu — akan kita bahas di Day 1 PM.

---

## 4B. Install DBeaver Community Edition

**Kapan dipakai:** mulai Week 1 Day 3 (SQLite), Week 2 Day 4 (PostgreSQL), seterusnya.

### Download & Install

1. Buka [dbeaver.io/download](https://dbeaver.io/download/)
2. Download **DBeaver Community Edition** (gratis, free forever)
3. Pilih installer sesuai OS (Windows/Mac/Linux)
4. Install dengan default options

### Verifikasi

Buka DBeaver. Kalau kebuka tanpa error, install OK. Pertama kali kebuka akan ada wizard "New Connection" — **klik Cancel/Skip** dulu (kita connect ke database nanti di Week 1 Day 3).

> **Detail panduan DBeaver lengkap** (cara connect ke SQLite, PostgreSQL, BigQuery) ada di `99-resources/platform-guides/database-stack.md`. Buka kalau perlu reference.

> **[GAMBAR DIPERLUKAN — DBeaver Welcome Screen]**
> **Apa:** screenshot DBeaver pertama kali dibuka, sidebar kosong (belum ada connection).
> **Konteks:** verifikasi peserta install berhasil sebelum lanjut ke Day 1 PM.

---

## 5. Terminal Dasar (Bash & PowerShell)

Sebagai DA, kamu akan banyak pakai terminal. Berikut command paling sering dipakai:

### 5.1 Navigasi Folder

| Command | Fungsi | Contoh |
|---|---|---|
| `pwd` | Print working directory (di mana saya sekarang?) | `pwd` |
| `ls` | List files di folder ini | `ls` |
| `ls -la` | List dengan detail (size, tanggal) | `ls -la` |
| `cd <folder>` | Change directory ke folder | `cd Documents` |
| `cd ..` | Naik 1 folder ke parent | `cd ..` |
| `cd ~` | Pulang ke home folder | `cd ~` |
| `mkdir <nama>` | Buat folder baru | `mkdir savvys-da` |

> **Catatan:** Di Windows PowerShell, `ls`, `pwd`, `mkdir` juga jalan (alias). `cd ..` juga jalan.

### 5.2 File Operation

| Command | Fungsi | Contoh |
|---|---|---|
| `touch <file>` | Bikin file kosong (Mac/Linux/Git Bash) | `touch hello.py` |
| `cat <file>` | Tampilkan isi file | `cat hello.py` |
| `cp <src> <dest>` | Copy file | `cp hello.py backup.py` |
| `mv <src> <dest>` | Move atau rename | `mv hello.py main.py` |
| `rm <file>` | Hapus file (HATI-HATI tidak ada Recycle Bin) | `rm temp.txt` |
| `clear` | Bersihkan layar terminal | `clear` |

### 5.3 Tips Terminal

- **Tab autocomplete** — ketik beberapa huruf, tekan Tab → terminal akan complete otomatis
- **Arrow up** — kembali ke command yang baru saja dipakai
- **Ctrl+C** — batal command yang lagi jalan
- **Ctrl+L** — sama seperti `clear`

### 5.4 Open VSCode dari Terminal

Saat di folder yang ingin dibuka:

```bash
code .
```

Titik `.` = folder saat ini. Ini shortcut sangat berguna — terbiasa pakai ini, jangan klik-klik dari File Explorer.

---

## 6. Project Folder Structure

Sebelum mulai materi besok, kita siapkan folder kerja kamu.

### 6.1 Buat Folder Kursus

```bash
cd ~                                 # pulang ke home folder
mkdir savvys-da-kursus               # bikin folder utama kursus
cd savvys-da-kursus                  # masuk ke folder
mkdir week-1 week-2 week-3 week-4    # bikin sub-folder per minggu
mkdir portfolio                      # folder portfolio
ls                                   # cek struktur
```

Output:
```
portfolio  week-1  week-2  week-3  week-4
```

### 6.2 Buat Folder Portfolio (Akan Jadi Repo GitHub)

```bash
cd portfolio
mkdir 00-career-statement 01-excel-foundation 02-sql-bigquery
mkdir 03-python-pandas 04-data-acquisition 05-statistics-case
mkdir 06-visualization 07-storytelling-deck 08-capstone
ls
```

### 6.3 Buka di VSCode

```bash
cd ~/savvys-da-kursus
code .
```

VSCode akan terbuka dengan folder `savvys-da-kursus` di sidebar. **Bookmark folder ini** — selama 4 minggu, kamu akan kerjakan semua di sini.

### 6.4 Test: Bikin File Python Pertama

Di VSCode, klik kanan di area kosong sidebar → "New File" → namakan `hello.py`.

Ketik:

```python
print("Halo Savvys Education!")
print("Saya siap mulai Week 1 Day 1.")

import pandas as pd
print(f"Pandas version: {pd.__version__}")
```

Save (`Ctrl+S` / `⌘+S`).

Buka terminal di VSCode (`` Ctrl+` `` atau `Terminal → New Terminal`):

```bash
conda activate savvys-da
python hello.py
```

Output:
```
Halo Savvys Education!
Saya siap mulai Week 1 Day 1.
Pandas version: 2.2.x
```

🎉 **Kalau output muncul, environment kamu sudah ready 100%.**

> **[GAMBAR DIPERLUKAN — VSCode dengan File hello.py & Terminal Output]**
> **Apa yang harus di-screenshot:** VSCode terbuka dengan file `hello.py` di editor + terminal di bawah dengan output sukses dari `python hello.py`.
> **Konteks isi nanti:** "moment pertama kerja" peserta — bukti bahwa setup berhasil. Bagus untuk dipakai di slide opening Day 2.

---

## 7. Verifikasi Setup — Checklist Lengkap

Sebelum tutup sesi ini, pastikan kamu bisa centang **semua** item di bawah:

- [ ] VSCode terinstall & bisa dibuka
- [ ] 10 extensions wajib terinstall (cek di Extensions tab dengan filter `@installed`)
- [ ] `conda --version` jalan di terminal
- [ ] Environment `savvys-da` aktif (terlihat `(savvys-da)` di prompt)
- [ ] `python --version` output `Python 3.12.x`
- [ ] `python -c "import pandas"` jalan tanpa error
- [ ] `git --version` jalan
- [ ] `git config --list` menampilkan nama & email
- [ ] **DBeaver terinstall & bisa dibuka**
- [ ] Folder `savvys-da-kursus` terbentuk dengan 5 sub-folder
- [ ] File `hello.py` jalan & output muncul

Kalau ada item yang ✗, **JANGAN lanjut ke Day 1 PM** sebelum di-fix. Tanya mentor atau cari solusi di Section 8 (Troubleshooting).

---

## 8. Troubleshooting Umum

### Problem 1: "conda is not recognized"

**Penyebab:** Miniconda tidak ditambah ke PATH saat install.

**Solusi (Windows):**

1. Search "Environment Variables" di Start Menu
2. Klik "Edit the system environment variables" → "Environment Variables..."
3. Di bagian "User variables for [your-name]", pilih "Path" → klik "Edit"
4. Klik "New", tambahkan:
   - `C:\Users\YourName\miniconda3`
   - `C:\Users\YourName\miniconda3\Scripts`
   - `C:\Users\YourName\miniconda3\Library\bin`
5. OK, OK. **Tutup & buka ulang terminal**.

### Problem 2: Saat `conda activate savvys-da` muncul "command not found" atau prompt tidak berubah

**Solusi:**

```bash
conda init
```

Tutup terminal, buka baru, coba lagi.

Untuk PowerShell di Windows:

```bash
conda init powershell
```

Lalu restart PowerShell.

### Problem 3: VSCode "Python interpreter not found"

**Solusi:**

1. Buka file Python di VSCode
2. Tekan `Ctrl+Shift+P` (Windows/Linux) atau `⌘+Shift+P` (Mac)
3. Ketik "Python: Select Interpreter"
4. Pilih yang ada `savvys-da` di nama (biasanya format `~/miniconda3/envs/savvys-da/python.exe`)

### Problem 4: `pip install xyz` muncul error "Permission denied"

**Penyebab:** Sedang tidak di environment `savvys-da` (sudah keluar)

**Solusi:**

```bash
conda activate savvys-da
```

Cek prompt — harus ada `(savvys-da)` di awal sebelum jalankan `pip install`.

### Problem 5: Mac M1/M2 — Beberapa package error saat install

**Solusi:** Beberapa package belum punya wheel native untuk arm64. Workaround:

```bash
conda config --env --set subdir osx-64
```

Setelah itu, recreate environment:

```bash
conda deactivate
conda env remove -n savvys-da
conda create -n savvys-da python=3.12
conda activate savvys-da
# install package lagi
```

### Problem 6: Internet lambat saat `conda install`

**Solusi:** pakai mirror Indonesia yang lebih cepat (Tsinghua atau alternatif):

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
conda config --set show_channel_urls yes
```

### Kalau Stuck Lebih dari 30 Menit

**Jangan terus berusaha sendirian.** Tanya:
1. Mentor (kalau live class)
2. Stack Overflow dengan pesan error spesifik
3. ChatGPT / Claude — paste pesan error mentahnya
4. Komunitas Indonesia Data Analyst di Telegram

Setup adalah **investasi sekali** — habiskan waktu sekarang dengan benar, sisanya 4 minggu akan lancar.

---

## Apa Selanjutnya?

Kamu sudah punya environment kerja siap. Selamat — ini langkah teknis pertama dan paling sering jadi "blocker" pemula.

**Selanjutnya:**

1. **Selesaikan checklist Section 7** kalau belum semua tercentang
2. **Lanjut ke Day 1 PM — Git & GitHub** — folder `02-week-1/day-1-pm-git-github/`. Akan belajar version control: konsep Git, command dasar (init, add, commit, push), GitHub workflow, dan setup repo portfolio kamu di GitHub.
3. **(Opsional)** kalau ada waktu, eksplorasi VSCode 15 menit:
   - Coba Ctrl+P untuk quick-open file
   - Coba Ctrl+\\ untuk split editor
   - Coba Ctrl+B untuk hide/show sidebar

Sampai jumpa di Day 1 PM.

---

**Akhir Day 1 AM · Week 1**
*Savvys Education · 2026*

---

## Tentang Modul Ini

## Tujuan Sesi

Setelah sesi ini, peserta:
1. Punya VSCode terinstall dengan extensions wajib
2. Punya Python (Miniconda) terinstall dengan virtual environment kerja
3. Punya Git terinstall & dikonfigurasi
4. Bisa buka terminal & menjalankan command dasar
5. Sudah test: bisa `python --version`, `git --version`, dan VSCode bisa buka folder

## Durasi

~3 jam (banyak install — sediakan waktu lebih kalau koneksi lambat)

## Prasyarat

- Sudah selesai Pre-Week
- Komputer dengan akses install software (admin rights)
- Koneksi internet stabil (akan download ~2 GB total)

## Format Output

- `materi.md` — panduan step-by-step (~3,500 kata, banyak placeholder gambar untuk SS tutorial)
- `latihan/soal.md` — checklist verifikasi setup berhasil
- `cheatsheet.md` — daftar shortcut & command yang sering dipakai

## Struktur Konten

| Section | Topik |
|---|---|
| 1 | Mengapa Setup Penting & Apa Saja yang Akan Diinstall |
| 2 | Install VSCode + Extensions Wajib |
| 3 | Install Miniconda + Setup Virtual Environment |
| 4 | Install Git & Konfigurasi |
| 5 | Terminal Dasar (Bash & PowerShell) |
| 6 | Project Folder Structure |
| 7 | Verifikasi Setup |
| 8 | Troubleshooting Umum |

## Gambar yang Diperlukan

Section 2, 3, 4, 7 banyak butuh screenshot tutorial. Detail di placeholder masing-masing di `materi.md`.

## Catatan Mentor

- **Siapkan plan B kalau install gagal** — beberapa peserta akan punya OS/laptop yang bermasalah.
- **Pair up peserta yang stuck** — biasanya peserta lain yang sudah berhasil bisa bantu lebih cepat dari mentor sendirian.
- **Akhir sesi: pastikan semua bisa run `python --version` dan `git --version`** — kalau tidak, sisanya minggu ini akan kacau.

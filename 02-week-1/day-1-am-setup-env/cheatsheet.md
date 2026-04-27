# Cheatsheet — Setup Environment (Day 1 AM)

## Daftar Tools Terinstall

| Tool | Versi (akhir 2026) | Cek versi |
|---|---|---|
| VSCode | latest | `code --version` |
| Miniconda | 24.x+ | `conda --version` |
| Python | 3.12 | `python --version` |
| Git | 2.40+ | `git --version` |

## Conda — Command Cheatsheet

| Command | Fungsi |
|---|---|
| `conda --version` | Cek versi conda |
| `conda create -n NAMA python=3.12` | Bikin environment baru |
| `conda activate NAMA` | Masuk ke environment |
| `conda deactivate` | Keluar dari environment |
| `conda env list` | List semua environment |
| `conda env remove -n NAMA` | Hapus environment |
| `conda install PACKAGE` | Install package via conda |
| `conda list` | List package terinstall |
| `pip install PACKAGE` | Install via pip (pakai dalam env aktif) |

## Git — Konfigurasi Sekali Pakai Selamanya

```bash
git config --global user.name "Nama Lengkap"
git config --global user.email "email@gmail.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

## Terminal — Navigasi

| Command | Fungsi |
|---|---|
| `pwd` | Sekarang di mana? |
| `ls` (Windows: `dir` juga) | List file di folder ini |
| `ls -la` | List dengan detail |
| `cd <folder>` | Pindah ke folder |
| `cd ..` | Naik 1 folder |
| `cd ~` | Pulang ke home |
| `mkdir <nama>` | Bikin folder |
| `code .` | Buka VSCode di folder saat ini |

## Terminal — File

| Command | Fungsi |
|---|---|
| `touch FILE` | Bikin file kosong (Mac/Linux/Git Bash) |
| `cat FILE` | Lihat isi file |
| `cp SRC DEST` | Copy file |
| `mv SRC DEST` | Move/rename |
| `rm FILE` | Hapus (HATI-HATI!) |
| `clear` (atau Ctrl+L) | Bersihkan layar |

## VSCode — Shortcut Wajib

| Shortcut | Fungsi |
|---|---|
| `Ctrl+P` | Quick open file |
| `Ctrl+Shift+P` | Command palette |
| `Ctrl+,` | Settings |
| `Ctrl+B` | Hide/show sidebar |
| `Ctrl+\\` | Split editor |
| `` Ctrl+` `` | Open/close terminal |
| `Ctrl+/` | Toggle comment |
| `Ctrl+S` | Save |
| `Ctrl+Shift+K` | Hapus baris |
| `Alt+↑/↓` | Pindah baris naik/turun |

> Mac: ganti `Ctrl` dengan `⌘`

## Workflow Daily

```bash
# 1. Buka terminal (Windows: Anaconda Prompt; Mac/Linux: Terminal)
# 2. Aktifkan environment
conda activate savvys-da

# 3. Pindah ke folder kerja
cd ~/savvys-da-kursus

# 4. Buka VSCode
code .

# 5. Mulai kerja
```

## Troubleshooting Cepat

| Masalah | Solusi Cepat |
|---|---|
| "conda not recognized" | Restart terminal / cek PATH |
| Prompt tidak berubah saat `conda activate` | `conda init` lalu restart terminal |
| VSCode tidak deteksi Python | Ctrl+Shift+P → "Python: Select Interpreter" → pilih `savvys-da` |
| `pip install` "Permission denied" | Pastikan environment aktif (lihat `(savvys-da)` di prompt) |
| Mac M1 install package error | `conda config --env --set subdir osx-64` |

## Next Step

✅ Setup beres → lanjut ke `day-1-pm-git-github/`

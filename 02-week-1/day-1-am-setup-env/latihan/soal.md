# Latihan — Verifikasi Setup Environment

> **Format:** Bukan latihan teknikal — ini checklist verifikasi. Tidak ada solusi karena setiap output unik per komputer.

## Bagian A — Checklist Setup (wajib)

Pastikan semua tercentang sebelum lanjut Day 1 PM.

### VSCode
- [ ] VSCode terinstall & bisa dibuka
- [ ] 10 extensions wajib terinstall:
  - [ ] Python (Microsoft)
  - [ ] Jupyter (Microsoft)
  - [ ] Pylance (Microsoft)
  - [ ] Excel Viewer
  - [ ] Rainbow CSV
  - [ ] GitLens
  - [ ] SQLTools
  - [ ] SQLTools SQLite Driver
  - [ ] Material Icon Theme
  - [ ] Better Comments
- [ ] Setting `editor.tabSize: 4`, `formatOnSave: true` aktif

### Python
- [ ] `conda --version` jalan
- [ ] Environment `savvys-da` terbuat
- [ ] `conda activate savvys-da` jalan, prompt berubah
- [ ] `python --version` output `3.12.x`
- [ ] `python -c "import pandas as pd; print(pd.__version__)"` jalan

### Git
- [ ] `git --version` jalan
- [ ] `git config user.name` set
- [ ] `git config user.email` set
- [ ] `git config init.defaultBranch` = `main`

### Project Folder
- [ ] Folder `savvys-da-kursus` terbentuk di home
- [ ] Sub-folder `week-1`, `week-2`, `week-3`, `week-4`, `portfolio` ada
- [ ] Sub-folder portfolio (00-career-statement, 01-excel-foundation, dst) ada

### Test Run
- [ ] `hello.py` dibuat & jalan
- [ ] Output muncul: "Halo Savvys Education!" + Pandas version

## Bagian B — Latihan Tambahan (opsional, untuk yang sudah selesai)

### B.1 — Eksplorasi VSCode

Coba pakai shortcut berikut, catat fungsi tiap shortcut:

| Shortcut Windows/Linux | Mac | Fungsi (isi sendiri) |
|---|---|---|
| `Ctrl+P` | `⌘+P` | _ |
| `Ctrl+Shift+P` | `⌘+Shift+P` | _ |
| `Ctrl+B` | `⌘+B` | _ |
| `Ctrl+\\` | `⌘+\\` | _ |
| `` Ctrl+` `` | `` ⌘+` `` | _ |
| `Ctrl+/` | `⌘+/` | _ |

### B.2 — Latihan Terminal

Di folder `savvys-da-kursus/week-1`, jalankan command berikut **tanpa pakai mouse**, catat output:

1. `pwd` → output: ___
2. `mkdir test-folder` → cek: apakah folder muncul?
3. `cd test-folder` → cek: prompt berubah?
4. `touch file1.txt file2.txt` → cek dengan `ls`: ada 2 file?
5. `mv file1.txt renamed.txt` → cek dengan `ls`: file1 jadi renamed?
6. `rm file2.txt renamed.txt` → cek: 2 file hilang?
7. `cd ..` → balik ke parent
8. `rm -r test-folder` → hapus folder kosong (kalau ada error: pakai `rmdir test-folder` di Windows PowerShell)

### B.3 — First Python Mini Project

Bikin file `latihan/cek_env.py` dengan isi berikut, lalu run:

```python
import sys
import platform
import pandas as pd
import numpy as np
import matplotlib

print("=" * 50)
print("SAVVYS EDUCATION — Environment Check")
print("=" * 50)
print(f"OS: {platform.system()} {platform.release()}")
print(f"Python: {sys.version.split()[0]}")
print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Path: {sys.executable}")
print("=" * 50)
print("Setup verified! Ready for Week 1.")
```

Output expected (versi pasti beda per peserta):

```
==================================================
SAVVYS EDUCATION — Environment Check
==================================================
OS: Windows 10
Python: 3.12.x
Pandas: 2.2.x
NumPy: 1.26.x
Matplotlib: 3.8.x
Path: C:\Users\YourName\miniconda3\envs\savvys-da\python.exe
==================================================
Setup verified! Ready for Week 1.
```

## Bagian C — Reflection

Setelah selesai setup, jawab di catatan pribadi (1–2 kalimat saja):

1. **Bagian setup mana yang paling sulit / butuh waktu paling lama?**
2. **Apakah ada tools yang masih bingung kenapa diinstall?**
3. **Apakah kamu PD lanjut ke Day 1 PM (Git & GitHub)?**

Refleksi ini bantu mentor identify peserta yang butuh extra support.

---

## Submission

Kalau di kelas grup: kirim screenshot output `cek_env.py` ke channel grup sebagai bukti setup beres.

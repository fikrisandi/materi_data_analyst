# Latihan — Git & GitHub Workflow

## Tugas Utama

**Push 3 file Pre-Week (career-statement.md, skill-mapping.md, target-role.md) ke GitHub repo `data-analyst-portfolio` kamu.**

Detail step-by-step ada di `materi.md` Section 9.

## Checklist Verifikasi

- [ ] Punya akun GitHub
- [ ] Repo `data-analyst-portfolio` terbuat di GitHub (public)
- [ ] Local `~/savvys-da-kursus/portfolio/` sudah `git init`
- [ ] Remote `origin` connected ke GitHub repo
- [ ] SSH key di-setup (atau pakai PAT)
- [ ] File `README.md` ada di root
- [ ] Folder `00-career-statement/` berisi 3 file kamu
- [ ] `.gitignore` ada
- [ ] Commit message clear (bukan "update" / "asdf")
- [ ] `git push` sukses
- [ ] Repo bisa diakses publik di `github.com/USERNAME/data-analyst-portfolio`

## Latihan Tambahan

### Tugas 1 — Latihan Git Cycle

Bikin folder kerja sementara `~/git-practice/`. Lakukan urutan command berikut. **Setiap step, jalankan `git status`** dan catat output:

```bash
# 1. Setup
mkdir ~/git-practice && cd ~/git-practice
git init

# 2. Bikin file
echo "Line 1" > test.txt

# 3. Cek status (harusnya: untracked)
git status

# 4. Add
git add test.txt

# 5. Cek status (harusnya: staged)
git status

# 6. Commit
git commit -m "Add test.txt"

# 7. Edit file (tambah baris baru)
echo "Line 2" >> test.txt

# 8. Cek status (harusnya: modified, not staged)
git status

# 9. Lihat diff
git diff

# 10. Commit ulang
git add test.txt && git commit -m "Add Line 2 to test.txt"

# 11. Lihat history
git log --oneline
```

**Pertanyaan:**
1. Setelah `git init`, kenapa file belum keliatan kalau ada perubahan?
2. Apa beda "untracked" vs "modified" vs "staged"?
3. Apa yang muncul di `git diff`?
4. Berapa commit total di history setelah step 11?

### Tugas 2 — Bikin & Merge Branch

```bash
# Pastikan di folder ~/git-practice
cd ~/git-practice

# Bikin branch baru
git checkout -b experiment

# Edit file (tambah baris di branch experiment)
echo "Line 3 (experiment)" >> test.txt

# Commit
git add test.txt
git commit -m "Experiment: add Line 3"

# Lihat isi file
cat test.txt
# Output: Line 1, Line 2, Line 3

# Pindah ke main
git checkout main

# Lihat isi file
cat test.txt
# Output: Line 1, Line 2 (TIDAK ada Line 3 — beda branch)

# Merge experiment ke main
git merge experiment

# Cek
cat test.txt
# Output: Line 1, Line 2, Line 3 (sekarang ada)

# Hapus branch experiment
git branch -d experiment
```

**Pertanyaan:**
1. Kenapa Line 3 tidak muncul saat di branch main sebelum merge?
2. Apa yang terjadi saat `git merge experiment`?

### Tugas 3 — Bikin .gitignore Test

```bash
cd ~/git-practice

# Bikin file yang HARUSNYA tidak di-track
touch secret.env
echo "API_KEY=12345" > secret.env

# Cek status
git status
# Harusnya: secret.env muncul sebagai untracked

# Bikin .gitignore
cat > .gitignore << 'EOF'
*.env
EOF

# Cek status lagi
git status
# Sekarang: secret.env tidak muncul lagi
# Tapi .gitignore muncul sebagai untracked

# Commit .gitignore
git add .gitignore
git commit -m "Add .gitignore"
```

**Pertanyaan:**
1. Kenapa `secret.env` tidak muncul lagi setelah `.gitignore` dibuat?
2. Apa yang akan terjadi kalau `secret.env` sudah keburu di-commit sebelum `.gitignore` dibuat? (Hint: jawaban di Stack Overflow / mentor.)

## Submission

Kalau di kelas grup:
1. Kirim **link GitHub repo** kamu ke channel grup
2. Mentor akan cek apakah:
   - Repo public & accessible
   - File-file Pre-Week ada
   - Commit message readable
   - README ada

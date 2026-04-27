# Cheatsheet — Git & GitHub (Day 1 PM)

## Konsep Inti

```
Working Dir → (git add) → Staging → (git commit) → Repository → (git push) → GitHub
```

## Setup Sekali Selamanya

```bash
git config --global user.name "Nama Lengkap"
git config --global user.email "email@gmail.com"
git config --global init.defaultBranch main
git config --global core.editor "code --wait"
```

## Command Inti

| Command | Fungsi |
|---|---|
| `git init` | Inisialisasi repo di folder ini |
| `git status` | Cek status (apa yang berubah?) |
| `git add <file>` | Pindahkan file ke staging |
| `git add .` | Add semua file |
| `git commit -m "msg"` | Commit staged files |
| `git log` | Lihat history |
| `git log --oneline` | History ringkas |
| `git diff` | Lihat perubahan unstaged |
| `git diff --staged` | Lihat perubahan yang sudah staged |
| `git restore <file>` | Buang perubahan unstaged |
| `git restore --staged <file>` | Unstage file |

## GitHub Integration

| Command | Fungsi |
|---|---|
| `git remote add origin URL` | Connect local ke GitHub |
| `git remote -v` | List remote |
| `git remote set-url origin URL` | Ganti URL remote |
| `git push -u origin main` | Push pertama kali |
| `git push` | Push lanjutan |
| `git pull` | Tarik update terbaru dari GitHub |
| `git clone URL` | Download repo dari GitHub |

## SSH Key Setup

```bash
ssh-keygen -t ed25519 -C "email@gmail.com"
cat ~/.ssh/id_ed25519.pub        # copy & paste ke GitHub Settings
ssh -T git@github.com            # test connection
```

## Branching Basic

| Command | Fungsi |
|---|---|
| `git branch` | List branch |
| `git branch <name>` | Bikin branch |
| `git checkout <name>` | Pindah branch |
| `git checkout -b <name>` | Bikin & pindah sekaligus |
| `git merge <branch>` | Merge branch ke yang sedang aktif |
| `git branch -d <name>` | Hapus branch yang sudah merge |

## Workflow Daily

```bash
git pull                          # 1. Sync dengan remote
# ...edit di VSCode...
git status                        # 2. Cek perubahan
git diff                          # 3. (opsional) lihat detail
git add .                         # 4. Stage semua
git commit -m "Update X"          # 5. Commit
git push                          # 6. Push ke GitHub
```

## Aturan Commit Message

✅ **Baik:**
- "Add Excel pivot table exercise solution"
- "Update SQL query: pakai window function untuk ranking"
- "Fix typo in README week 1"

❌ **Buruk:**
- "update"
- "fix"
- "asdf"

## .gitignore Template untuk DA

```gitignore
# Python
__pycache__/
*.pyc
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

# Big data files
data/raw/
data/big/
*.parquet
```

## Troubleshooting

| Masalah | Solusi |
|---|---|
| Push minta password padahal sudah SSH | Cek `git remote -v` — kalau HTTPS, ganti ke SSH dengan `git remote set-url origin git@github.com:USER/REPO.git` |
| "Permission denied (publickey)" | SSH key belum ditambah ke GitHub. Re-do step Section 5 |
| Conflict saat `git pull` | Resolve manual di file conflicted, atau `git stash` perubahan lokal lalu pull |
| Salah commit, mau undo | `git reset --soft HEAD~1` (commit terakhir di-undo, file kembali ke staging) |
| Add file rahasia (`.env`) tidak sengaja | Hapus dari Git history (advanced — tanya mentor) |

## Next Step

✅ Day 1 selesai (Setup + Git) → lanjut ke `day-2-am-excel-foundation/`

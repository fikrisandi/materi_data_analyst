# Rubrik Penilaian — Latihan & Capstone

## Skala Penilaian

| Score | Level | Deskripsi |
|---|---|---|
| 90-100 | Excellent | Above expectation, ada extra effort |
| 75-89 | Good | Meet expectation, semua wajib done dengan baik |
| 60-74 | Adequate | Mostly meet expectation, ada beberapa lacking |
| < 60 | Needs Improvement | Banyak yang missing atau salah |

---

## Rubrik Latihan Mingguan

### Bobot

| Aspek | Bobot |
|---|---|
| **Correctness** — code/query benar, output sesuai expected | 50% |
| **Code Quality** — readable, well-structured, comment | 20% |
| **Insight Statement** — interpretasi bisnis (bukan cuma report angka) | 20% |
| **Effort Bonus** — tackle bonus task | 10% |

### Detail per Aspek

**Correctness**
- 90-100: Semua soal benar, output match
- 75-89: 1-2 soal salah/incomplete
- 60-74: 30-40% soal salah
- < 60: Lebih dari 50% soal salah

**Code Quality**
- 90-100: Indented, named clearly, comment sesuai, no dead code
- 75-89: Mostly clean, minor issues
- 60-74: Cukup readable tapi banyak yang bisa improve
- < 60: Hard to read

**Insight Statement**
- 90-100: Selalu tambahkan interpretasi bisnis yang actionable
- 75-89: Ada insight tapi kadang generic
- 60-74: Cuma report angka, sedikit interpretasi
- < 60: No insight, hanya output mentah

---

## Rubrik Capstone Project (Week 4)

### Bobot

| Aspek | Bobot |
|---|---|
| **Data Cleaning** — handle missing, outlier, dengan justifikasi | 15% |
| **EDA** — kedalaman eksplorasi awal | 15% |
| **Analysis Quality** — pertanyaan dijawab dengan metric tepat | 20% |
| **Statistical Rigor** — pakai test yang tepat, valid | 10% |
| **Visualization** — chart proper, insight-driven title | 10% |
| **Insight Quality** — bukan cuma report, ada interpretasi bisnis | 15% |
| **Recommendations** — actionable, ada expected impact | 10% |
| **Communication** — README + deck polished | 5% |

### Detail per Aspek

**Data Cleaning**
- 90-100: Cleaning step explicit, justifikasi ditulis untuk tiap decision
- 75-89: Cleaning OK tapi kurang transparan
- 60-74: Skip beberapa step penting
- < 60: Tidak ada cleaning explicit

**EDA**
- 90-100: Ekspolasi distribusi, korelasi, anomali. Bukan cuma `head()` & `info()`
- 75-89: Ada EDA tapi kurang dalam
- 60-74: Surface-level
- < 60: No EDA

**Analysis Quality**
- 90-100: Pertanyaan didekomposisi dengan baik, metric specific dipilih dengan reasoning
- 75-89: Pertanyaan dijawab tapi metric kadang generic
- 60-74: Pertanyaan dijawab partial
- < 60: Pertanyaan tidak terjawab clear

**Statistical Rigor**
- 90-100: Pakai test yang tepat, interpret hasil dengan benar (bukan p-hacking)
- 75-89: Test OK tapi interpretasi kadang weak
- 60-74: Test pakai tapi misinterpret
- < 60: No statistical test atau salah

**Visualization**
- 90-100: Chart proper, title insight-driven, annotated, sesuai best practice
- 75-89: Chart OK, title agak generic
- 60-74: Default chart Pandas tanpa polish
- < 60: Misleading atau missing

**Insight Quality**
- 90-100: Setiap insight = fakta + interpretasi + implication. Ada surprise insight
- 75-89: Insight OK tapi predictable
- 60-74: Cuma report angka
- < 60: No insight

**Recommendations**
- 90-100: 3 actions konkret, dengan expected impact (kalau bisa diukur)
- 75-89: Actions ada tapi general
- 60-74: Recommendations vague
- < 60: No recommendations atau "more data needed"

**Communication**
- 90-100: README polished, deck rapi, dapat present 10 min dengan smooth
- 75-89: Documentation OK
- 60-74: Minimal documentation
- < 60: README/deck missing

---

## Self-Assessment Form

Peserta isi form berikut sebelum submit ke mentor:

```
PROYEK: [Nama capstone]
TANGGAL SUBMIT: [YYYY-MM-DD]

Self-Score per Aspek (1-10):
[ ] Data Cleaning:  __/10
[ ] EDA:            __/10
[ ] Analysis:       __/10
[ ] Statistics:     __/10
[ ] Viz:            __/10
[ ] Insight:        __/10
[ ] Recommendations:__/10
[ ] Communication:  __/10

Pertanyaan refleksi:
1. Apa bagian yang paling kamu banggakan?
2. Apa bagian yang masih bisa improve kalau punya 1 minggu lagi?
3. Apa skill yang paling kamu pelajari dari capstone ini?
```

---

## Mentor Action

- Review hasil dalam 3 hari
- Kasih written feedback per aspek (min 1 sentence)
- Suggest 1-2 specific improvement
- Tag peserta yang struggle untuk extra mentoring

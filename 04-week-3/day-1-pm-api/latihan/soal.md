# Latihan — API

## Tugas Utama: Multi-API Mini Case

Combine **3 API** jadi 1 analisis:

### Setup
1. Sign up untuk API key OpenWeather (free)
2. Bikin file `.env` dengan API key
3. Add `.env` ke `.gitignore`

### Tugas
1. **Pakai REST Countries** ([restcountries.com](https://restcountries.com/v3.1/region/asia)) — ambil 10 negara Asia, simpan: nama, capital, population, currency, flag URL
2. **Pakai OpenWeather** — untuk tiap capital, ambil suhu sekarang & cuaca
3. **Pakai JSONPlaceholder** — bikin fake "tourist user" untuk tiap negara dengan endpoint `/users/{id}`
4. Combine semua jadi 1 DataFrame, save ke `latihan/asia-weather.csv`

## Bonus

### Bonus 1 — Visualisasi
Bar chart suhu Asia, sorted desc.

### Bonus 2 — Cache
Implement caching: kalau sudah pernah fetch, jangan fetch ulang. Simpan JSON ke folder `cache/`.

### Bonus 3 — BPS Indonesia
Sign up di webapi.bps.go.id. Fetch data inflasi 2020-2024. Visualisasi line chart trend inflasi.

## Submission
`latihan/multi-api-analysis.ipynb`. Push ke `04-data-acquisition/api/` portfolio.

⚠️ **Pastikan `.env` TIDAK ke-commit** ke Git.

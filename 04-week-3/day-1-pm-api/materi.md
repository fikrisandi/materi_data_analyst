# Week 3 · Day 1 PM
# API — Mengambil Data dari Layanan Publik

> **Tujuan:** Setelah modul ini kamu paham apa itu REST API, bisa pakai `requests` untuk hit endpoint, parse response JSON, handle authentication (API key), dan punya pengalaman dengan API Indonesia (BPS) + global (OpenWeather, JSONPlaceholder).
>
> **Estimasi:** 3 jam.

---

## 1. Apa itu API?

**API** = **Application Programming Interface**. Dalam konteks DA: cara untuk **request data** dari layanan via internet **secara terstruktur** (vs scraping yang ekstrak dari HTML).

**Mengapa prefer API daripada scraping?**

- **Resmi & legal** — provider sudah expose endpoint untuk public consumption
- **Format JSON terstruktur** — tidak perlu parse HTML
- **Stable** — endpoint jarang berubah; HTML bisa berubah random
- **Rate limit jelas** — tahu batas request per menit/hari
- **Authentication kalau perlu** — API key untuk track usage

### Analogi Restoran

- Scraping = masuk ke dapur restoran, ambil makanan sendiri (kotor, ilegal, bisa di-tendang keluar)
- API = order via menu di kasir (rapi, sah, dengan harga jelas)

---

## 2. REST API Basics

REST = **Representational State Transfer**. Standar paling umum untuk API.

### 2.1 HTTP Method

| Method | Fungsi |
|---|---|
| `GET` | Ambil data (paling sering DA pakai) |
| `POST` | Bikin data baru |
| `PUT` / `PATCH` | Update data |
| `DELETE` | Hapus data |

DA hampir 100% pakai `GET` — read-only.

### 2.2 Anatomy URL Endpoint

```
https://api.openweather.org/data/2.5/weather?q=Jakarta&appid=YOUR_KEY
└──────────────────────────┬──────────────────┘ └──────┬──────┘
              base URL                          query parameters
```

- **Base URL** + **path** = tujuan endpoint
- **Query parameters** (?key=value&key=value) = filter / option

### 2.3 Response — JSON

API return data dalam format JSON (mirip Python dict):

```json
{
  "name": "Jakarta",
  "main": {
    "temp": 305.15,
    "humidity": 70
  },
  "weather": [
    {"description": "scattered clouds"}
  ]
}
```

### 2.4 Status Code

| Code | Artinya |
|---|---|
| `200` | OK — sukses |
| `400` | Bad request — input salah |
| `401` | Unauthorized — API key salah |
| `403` | Forbidden — tidak boleh akses |
| `404` | Not found — endpoint tidak ada |
| `429` | Too many requests — rate limit |
| `500` | Server error |

---

## 3. requests + JSON Parsing

```python
import requests

# Hit endpoint sederhana (tanpa auth)
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

print(response.status_code)    # 200
print(response.json())          # parse JSON ke dict otomatis
```

### 3.1 Pakai Query Parameters

```python
url = "https://jsonplaceholder.typicode.com/posts"
params = {"userId": 1}
response = requests.get(url, params=params)
data = response.json()

print(len(data))   # 10 posts dari user 1
```

### 3.2 Response Headers & Method Lain

```python
print(response.headers)        # dict header
print(response.headers["Content-Type"])
print(response.url)            # URL final dengan params
```

---

## 4. API dengan Authentication

Sebagian besar API butuh **API key** atau **token**.

### 4.1 OpenWeather API (Free Tier)

1. Sign up di [openweathermap.org/api](https://openweathermap.org/api)
2. Dapat API key (gratis, 60 req/min)
3. Endpoint: `https://api.openweathermap.org/data/2.5/weather?q=Jakarta&appid=YOUR_KEY`

```python
import requests
from os import getenv

API_KEY = getenv("OPENWEATHER_KEY")  # store in env, jangan hardcode

url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": "Jakarta",
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)
data = response.json()

print(f"Suhu Jakarta: {data['main']['temp']}°C")
print(f"Cuaca: {data['weather'][0]['description']}")
```

### 4.2 Authentication via Header

```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Accept": "application/json",
}
response = requests.get(url, headers=headers)
```

### 4.3 .env File untuk API Key

**JANGAN hardcode API key di code yang di-commit ke Git.**

Bikin file `.env`:

```
OPENWEATHER_KEY=your_actual_key_here
BPS_KEY=another_key
```

Tambah `.env` ke `.gitignore`. Lalu:

```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENWEATHER_KEY")
```

`pip install python-dotenv` kalau belum ada.

---

## 5. Skenario Real — API BPS Indonesia

**BPS** (Badan Pusat Statistik) punya API resmi untuk data ekonomi & demografi Indonesia: [webapi.bps.go.id](https://webapi.bps.go.id).

### Setup

1. Sign up di [webapi.bps.go.id](https://webapi.bps.go.id)
2. Dapat API key
3. Endpoint: `https://webapi.bps.go.id/v1/api/list/...`

### Contoh: Data Inflasi Indonesia

```python
import requests
import pandas as pd

API_KEY = os.getenv("BPS_KEY")

url = "https://webapi.bps.go.id/v1/api/list"
params = {
    "model": "data",
    "domain": "0000",          # Indonesia
    "var": 1387,               # ID variable Inflasi
    "key": API_KEY,
    "lang": "ind",
}

response = requests.get(url, params=params)
data = response.json()

# Parse — struktur biasanya nested
records = data.get("data", {}).get("data", [])
df = pd.DataFrame(records)
print(df.head())
```

> **Catatan:** struktur API BPS agak ribet. Pakai dokumentasi resmi mereka. Untuk learning, JSONPlaceholder + OpenWeather lebih ramah pemula.

---

## 6. Pagination & Rate Limit

### 6.1 Pagination

Banyak API return data per page. Loop sampai habis:

```python
all_results = []
page = 1
while True:
    response = requests.get(url, params={"page": page, "per_page": 100})
    data = response.json()

    if not data.get("results"):
        break  # tidak ada data lagi

    all_results.extend(data["results"])
    page += 1

    time.sleep(0.5)   # rate limit

print(f"Total: {len(all_results)}")
```

### 6.2 Rate Limit

Cek response header `X-RateLimit-Remaining` atau dokumentasi API.

```python
def fetch_with_retry(url, params, max_retries=3):
    for attempt in range(max_retries):
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 429:
            print(f"Rate limited, wait {2 ** attempt} sec")
            time.sleep(2 ** attempt)   # exponential backoff
        else:
            response.raise_for_status()
    return None
```

---

## 7. Latihan: Mini Case dengan API

Buka `latihan/soal.md`. Tugas: combine 3 API:

1. **JSONPlaceholder** (no auth) — fake user data
2. **OpenWeather** (API key) — cuaca beberapa kota Indonesia
3. **REST Countries** (no auth) — info negara

---

## 8. Tips Praktis untuk DA

1. **Pakai API kalau ada** — selalu prefer dari scraping
2. **Cache hasil request** — request sama berulang? simpan ke file
3. **Parse JSON pakai pandas** — `pd.json_normalize()` untuk flatten nested
4. **Schedule kalau recurring** — pakai cron / Airflow / GitHub Actions
5. **Dokumentasikan API yang dipakai** — endpoint, auth, rate limit

---

## Apa Selanjutnya?

Lanjut **Day 2 AM — Business Knowledge** (KPI, funnel, cohort, North Star Metric).

> **Tip portfolio:** notebook integrasi 2-3 API jadi 1 analysis → push ke `04-data-acquisition/api/` portfolio.

---

**Akhir Day 1 PM · Week 3**
*Savvys Education · 2026*

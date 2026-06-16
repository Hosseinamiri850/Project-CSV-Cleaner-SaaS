# PROJECT_STRUCTURE.md

ساختار کامل فایل‌های پروژه CSV Cleaner SaaS.

---

## درخت فایل‌ها

```
Project CSV Cleaner SaaS/
│
├── main.py                    # FastAPI app — نقطه ورود backend
├── ai_cleaning.py             # AI integration (فعلاً placeholder)
│
├── requirements.txt           # Python dependencies
├── .env                       # API keys — هرگز commit نکن
├── .gitignore                 # فایل‌های ignore شده از git
│
├── README.md                  # مستندات اصلی (فارسی + انگلیسی)
├── CLAUDE.md                  # راهنمای Claude برای این پروژه
├── MEMORY.md                  # تاریخچه تصمیمات و context
├── CHANGELOG.md               # تاریخچه تغییرات
├── DESIGN.md                  # مستندات UI/UX
├── PRD.md                     # Product Requirements Document
├── PROJECT_STRUCTURE.md       # این فایل
│
├── venv/                      # Python virtual environment (git ignore)
│   └── ...
│
└── frontend/
    ├── package.json           # Node.js config
    ├── node_modules/          # npm packages (git ignore)
    │   └── ...
    └── src/
        ├── index.html         # Single-page UI
        ├── input.css          # Tailwind + DaisyUI source
        └── output.css         # CSS build شده — serve می‌شه
```

---

## توضیح فایل‌های کلیدی

### `main.py`

```python
# Routes:
GET  /        → FileResponse("frontend/src/index.html")
POST /clean   → پردازش CSV و برگشت JSON
GET  /static  → StaticFiles از frontend/src/
```

**وابستگی‌ها**: `ai_cleaning.py`

---

### `ai_cleaning.py`

یه تابع async که sample از CSV می‌گیره و پیشنهاد AI برمی‌گردونه.

```python
async def ai_suggest(df_sample: str) -> str
```

فعلاً placeholder — بعداً به Gemini یا Anthropic وصل می‌شه.

---

### `frontend/src/index.html`

Single-page app — همه UI توی یه فایل:
- Drag & drop zone
- Loading spinner
- Stats cards (DaisyUI `stats`)
- Preview table (DaisyUI `table-zebra`)
- Download button
- Error alert

با `fetch("http://127.0.0.1:8000/clean")` به backend وصل می‌شه.

---

### `frontend/src/input.css`

```css
@import "tailwindcss";
@plugin "daisyui" {
  themes: light;
}
```

با `npm run build` به `output.css` کامپایل می‌شه.

---

### `.env`

```
ANTHROPIC_API_KEY=sk-ant-xxxxx
GEMINI_API_KEY=AIza-xxxxx
```

با `python-dotenv` لود می‌شه. هرگز commit نکن.

---

## Data Flow

```
[Browser]
    │
    │ drag & drop CSV file
    ▼
[frontend/src/index.html]
    │
    │ POST /clean (multipart/form-data)
    ▼
[main.py → clean_csv()]
    │
    ├── pandas: read_csv()
    ├── pandas: drop_duplicates()
    ├── pandas: dropna(thresh=50%)
    ├── pandas: normalize columns
    │
    ├── ai_cleaning.py: ai_suggest()  ← placeholder
    │
    └── return JSON {report, ai_notes, preview, csv}
    │
    ▼
[frontend/src/index.html]
    │
    ├── render stats cards
    ├── render preview table
    └── enable download button
```

---

## npm Scripts

```json
{
  "build": "tailwindcss -i ./src/input.css -o ./src/output.css",
  "watch": "tailwindcss -i ./src/input.css -o ./src/output.css --watch"
}
```

---

## Python Dependencies

```
fastapi
uvicorn
pandas
anthropic
python-multipart
python-dotenv
aiofiles
```

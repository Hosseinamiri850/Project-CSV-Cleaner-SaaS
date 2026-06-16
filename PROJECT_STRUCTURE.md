# PROJECT_STRUCTURE.md

Full file structure of the CSV Cleaner SaaS project.

---

## File Tree

```
Project CSV Cleaner SaaS/
│
├── main.py                    # FastAPI app — backend entry point
├── ai_cleaning.py             # AI integration (placeholder for now)
│
├── requirements.txt           # Python dependencies
├── .env                       # API keys — never commit
├── .gitignore                 # Files excluded from git
├── .graphifyignore            # Files excluded from graphify
│
├── README.md                  # Main docs (Farsi + English)
├── CLAUDE.md                  # Claude guidance file
├── MEMORY.md                  # Decision history and context
├── CHANGELOG.md               # Change history
├── DESIGN.md                  # UI/UX documentation
├── PRD.md                     # Product Requirements Document
├── PROJECT_STRUCTURE.md       # This file
│
├── docs/
│   └── csv_cleaner_structure.png   # Architecture diagram
│
├── graphify-out/              # graphify output (git ignored)
│   ├── graph.json             # Knowledge graph (8 nodes, 11 edges)
│   └── .graphify_analysis.json
│
├── venv/                      # Python virtual environment (git ignored)
└── frontend/
    ├── package.json           # Node.js config
    ├── node_modules/          # npm packages (git ignored)
    └── src/
        ├── index.html         # Single-page UI
        ├── input.css          # Tailwind + DaisyUI source
        └── output.css         # Built CSS — served to browser
```

---

## Key File Details

### `main.py`

```python
# Routes:
GET  /        → FileResponse("frontend/src/index.html")
POST /clean   → processes CSV, returns JSON
GET  /static  → StaticFiles from frontend/src/
```

**Functions**: `clean_value()`, `clean_dict()`, `root()`, `clean_csv()`

---

### `ai_cleaning.py`

```python
async def ai_suggest(df_sample: str) -> str:
    return "AI feature coming soon."
```

Placeholder only — will connect to Gemini or Anthropic after billing is set up.

---

### `frontend/src/index.html`

Single-page app with all UI in one file:
- Drag & drop upload zone
- Loading spinner (DaisyUI)
- Stats cards (DaisyUI `stats`)
- Data preview table (DaisyUI `table-zebra`)
- Download button
- Error alert

Connects to backend via `fetch("http://127.0.0.1:8000/clean")`.

---

### `frontend/src/input.css`

```css
@import "tailwindcss";
@plugin "daisyui" {
  themes: light;
}
```

Compiled to `output.css` by running `npm run build`.

---

### `.graphifyignore`

```
venv/
node_modules/
frontend/
__pycache__/
graphify-out/
requirements.txt
test.csv
```

---

## Data Flow

```
[Browser]
    │
    │  drag & drop CSV file
    ▼
[frontend/src/index.html]
    │
    │  POST /clean (multipart/form-data)
    ▼
[main.py → clean_csv()]
    ├── pandas: read_csv()
    ├── pandas: drop_duplicates()
    ├── pandas: dropna(thresh=50%)
    ├── pandas: normalize column names
    ├── clean_value() / clean_dict()  →  NaN to None
    └── ai_cleaning.py: ai_suggest()  →  placeholder
    │
    └── return JSON {report, ai_notes, preview, csv}
    │
    ▼
[frontend/src/index.html]
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

## graphify Knowledge Graph

Last run: 2026-06-17
- **4 code files** found (with `--code-only`)
- **8 nodes**, **11 edges**, **3 communities**

| Community | Contains |
|-----------|---------|
| 0 | main.py, ai_cleaning.py, ai_suggest(), root() |
| 1 | clean_csv(), UploadFile |
| 2 | clean_value(), clean_dict() |

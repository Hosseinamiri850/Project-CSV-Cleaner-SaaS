# CLAUDE.md

Guidance for Claude when working on this project.

## Project Overview

CSV Cleaner SaaS is a web tool that automatically cleans CSV files.
Backend: Python + FastAPI. Frontend: HTML + DaisyUI + Tailwind CSS v4.

## Stack

- **Backend**: Python 3.14, FastAPI, pandas
- **Frontend**: HTML, DaisyUI v4, Tailwind CSS v4
- **AI**: Disabled (placeholder) — Gemini or Anthropic later
- **Deploy target**: Railway

## Commands

### Start dev server
```powershell
cd "Project CSV Cleaner SaaS"
venv\Scripts\activate
uvicorn main:app --reload
```

### Build frontend CSS
```powershell
cd frontend
npm run build
```

### Install Python dependencies
```powershell
pip install -r requirements.txt
```

### Run graphify (knowledge graph)
```powershell
$env:PATH = "C:\Users\Padidar\.local\bin;$env:PATH"
graphify . --code-only
```

## Architecture

```
Browser → GET /        → serves frontend/src/index.html
Browser → POST /clean  → FastAPI processes CSV → returns JSON
```

## Key Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app, `/` and `/clean` endpoints, static file serving |
| `ai_cleaning.py` | AI placeholder (returns "coming soon") |
| `frontend/src/index.html` | Single-page UI |
| `frontend/src/output.css` | Built Tailwind+DaisyUI CSS — do not edit directly |
| `frontend/src/input.css` | Tailwind source — edit this, then run build |
| `.env` | API keys — never commit |

## Environment Variables

```
ANTHROPIC_API_KEY=   # optional, for AI features
GEMINI_API_KEY=      # optional, free alternative
```

## Important Notes

- NaN must be converted to None before returning JSON (pandas quirk)
- CORS is currently open (`*`) — restrict before production
- No `tailwind.config.js` — Tailwind v4 reads config from `input.css`
- graphify only works on code files without an API key (`--code-only`)
- PATH must be set for graphify/uv in each new PowerShell session (or run `uv tool update-shell` once)

## Next Session TODOs

- [ ] Deploy on Railway
- [ ] Landing page
- [ ] Paddle payment setup

## Known Issues

- [ ] AI feature disabled (403 from Anthropic, Gemini setup issue)
- [ ] CORS must be restricted in production
- [ ] `test.csv` should be removed from repo or added to `.gitignore`

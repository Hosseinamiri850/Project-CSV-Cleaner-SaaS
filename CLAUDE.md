# CLAUDE.md

This file provides guidance for Claude when working on this project.

## Project Overview

CSV Cleaner SaaS is a web tool that automatically cleans CSV files using Python (FastAPI) on the backend and DaisyUI + Tailwind CSS on the frontend.

## Stack

- **Backend**: Python 3.10+, FastAPI, pandas
- **Frontend**: HTML, DaisyUI v4, Tailwind CSS v4
- **AI**: Anthropic / Gemini API (currently disabled)
- **Deploy target**: Railway (backend) + static serving via FastAPI

## Commands

### Start development server
```bash
cd "Project CSV Cleaner SaaS"
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
uvicorn main:app --reload
```

### Build frontend CSS
```bash
cd frontend
npm run build
```

### Install Python dependencies
```bash
pip install -r requirements.txt
```

## Architecture

```
Browser → GET /        → serves frontend/src/index.html
Browser → POST /clean  → FastAPI processes CSV → returns JSON
```

## Key Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app, `/clean` endpoint, static file serving |
| `ai_cleaning.py` | AI suggestion function (currently returns placeholder) |
| `frontend/src/index.html` | Single-page UI |
| `frontend/src/output.css` | Built Tailwind+DaisyUI CSS |
| `.env` | API keys (never commit this) |

## Environment Variables

```
ANTHROPIC_API_KEY=   # optional, for AI features
GEMINI_API_KEY=      # optional, alternative AI
```

## Code Conventions

- Python: async functions for all FastAPI routes
- NaN values must be converted to None before JSON serialization
- CORS is open (`*`) for now — restrict before production
- Frontend communicates with backend via `http://127.0.0.1:8000` in dev

## Known Issues / TODOs

- [ ] AI feature disabled — needs valid API key
- [ ] No authentication yet
- [ ] No usage limits / rate limiting
- [ ] No database — stateless for now
- [ ] CORS should be restricted in production

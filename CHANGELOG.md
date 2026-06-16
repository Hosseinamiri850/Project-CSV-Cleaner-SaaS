# CHANGELOG

All notable changes to CSV Cleaner SaaS are documented here.

---

## [0.2.0] - 2026-06-17 — Documentation & Tooling

### Added
- `CLAUDE.md` — Claude guidance file for this project
- `MEMORY.md` — Architecture decisions and context
- `CHANGELOG.md` — This file
- `DESIGN.md` — UI/UX documentation
- `PRD.md` — Product Requirements Document
- `PROJECT_STRUCTURE.md` — Full project structure reference
- `docs/csv_cleaner_structure.png` — Architecture diagram
- Architecture diagram added to README (both languages)
- graphify installed and knowledge graph generated
- `.graphifyignore` to exclude non-essential files from graph
- Initial push to GitHub

### Changed
- README updated with diagram and correct clone URL

---

## [0.1.0] - 2026-05-18 — MVP

### Added
- `POST /clean` endpoint — accepts CSV, returns cleaned data + report
- Auto-removal of duplicate rows
- Auto-removal of rows with >50% empty values
- Column name normalization (strip + lowercase)
- JSON report: rows_before, rows_after, duplicates, nulls per column
- Preview of first 5 rows of cleaned data
- Cleaned CSV string in response for download
- CORS middleware (open for development)
- Frontend: drag & drop file upload
- Frontend: stats cards (rows before/after, duplicates, nulls)
- Frontend: zebra table preview
- Frontend: download button for cleaned CSV
- DaisyUI + Tailwind CSS v4 (local install, no CDN)
- FastAPI serves frontend statically at `/`
- AI placeholder in `ai_cleaning.py` — returns "coming soon"

### Fixed
- `NaN` values converted to `None` for JSON compliance
- PowerShell execution policy workaround documented
- DaisyUI builds correctly via `@plugin` in `input.css` (Tailwind v4)

### Known Issues
- AI feature disabled (needs API key with billing)
- No authentication
- No usage limits
- CORS is open — must restrict before production

---

## [Unreleased] — upcoming

### Planned
- Deploy to Railway
- Landing page
- Paddle payment integration
- User authentication (Supabase)
- Usage limits per plan (Free: 5 files/month, Starter: 50, Pro: unlimited)
- AI suggestions via Gemini or Anthropic API
- Rate limiting
- File size validation (max 10MB)

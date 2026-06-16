# CHANGELOG

All notable changes to CSV Cleaner SaaS are documented here.

Format: `[version] - date - description`

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
- DaisyUI + Tailwind CSS v4 styling
- FastAPI serves frontend statically at `/`
- AI placeholder (`ai_cleaning.py`) — returns "coming soon"

### Fixed
- `NaN` values converted to `None` for JSON compliance
- PowerShell execution policy workaround documented
- DaisyUI build via `@plugin` in `input.css` (Tailwind v4 compatible)

### Known Issues
- AI feature disabled (needs API key with billing)
- No authentication
- No usage limits
- CORS open — must restrict before production

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
- File size validation

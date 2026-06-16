# MEMORY.md

Decision history and project context for future reference.

## Architecture Decisions

### Why FastAPI?
- Async native
- Auto-generated docs at `/docs`
- Faster than Django for API-only projects

### Why pandas?
- Standard Python data processing library
- Built-in `drop_duplicates`, `dropna`, and column normalization

### Why DaisyUI + Tailwind v4?
- Component-based, minimal custom CSS needed
- Good RTL support
- Installed locally via npm (no CDN dependency)

### Why no Auth yet?
- MVP must validate sales first
- Auth will be added after the first paying customer
- Current model: stateless, every request is independent

### Why is AI disabled?
- Anthropic API requires billing (got 403)
- Gemini free tier had issues during setup
- Decision: keep placeholder for now, enable after first revenue

---

## Solved Problems

### NaN in JSON
pandas converts empty values to `NaN` which is not JSON-compliant.
**Fix**: Convert `NaN` to `None` before returning response.
```python
def clean_value(v):
    if isinstance(v, float) and math.isnan(v):
        return None
    return v
```

### PowerShell Execution Policy
Windows blocked script execution.
**Fix**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### DaisyUI build (Tailwind v4)
Tailwind v4 no longer uses `tailwind.config.js`.
**Fix**: Use `@plugin` directive in `input.css`:
```css
@import "tailwindcss";
@plugin "daisyui" {
  themes: light;
}
```

### graphify and doc files
graphify can't process doc files without an API key.
**Fix**: Add `.graphifyignore` with `frontend/` and non-essential files, use `--code-only` flag.

### PATH reset for uv/graphify in PowerShell
PATH resets every time a new terminal opens.
**Permanent fix**: Run `uv tool update-shell` once.

---

## Installed Tools

| Tool | Install | Purpose |
|------|---------|---------|
| Python venv | `python -m venv venv` | Isolated environment |
| FastAPI + uvicorn | pip | Backend server |
| pandas | pip | CSV processing |
| python-dotenv | pip | Load .env file |
| aiofiles | pip | Serve static files |
| DaisyUI + Tailwind v4 | npm | Frontend styling |
| uv | pip | Fast package manager |
| graphify | `uv tool install graphifyy` | Project knowledge graph |

---

## Completed Steps

- [x] FastAPI backend
- [x] CSV cleaning with pandas
- [x] NaN in JSON fix
- [x] DaisyUI frontend (local install, no CDN)
- [x] FastAPI serves frontend at `/`
- [x] CORS middleware
- [x] Documentation files (README, CLAUDE, MEMORY, CHANGELOG, DESIGN, PRD, PROJECT_STRUCTURE)
- [x] Pushed to GitHub
- [x] Installed graphify and generated knowledge graph
- [x] Added architecture diagram to README

---

## Next Steps (prioritized)

- [ ] **First** — Deploy on Railway
- [ ] **Second** — Landing page for sales
- [ ] **Third** — Payment with Paddle
- [ ] **Later** — Auth and database (Supabase)
- [ ] **Later** — Enable AI feature (after billing setup)
- [ ] **Later** — Usage limits per plan

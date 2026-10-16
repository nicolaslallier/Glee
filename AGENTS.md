# Glee — AGENTS.md

> Living file. Add repo-specific facts as the project is built; delete anything that becomes stale.

## Project state

- **Python 3.13+** managed with `uv`
- **FastAPI** backend, flat `glee/` package

## How to use this file

### Dev commands

- **Install deps**: `uv sync`
- **Run dev server**: `make run` (or `uv run uvicorn glee.main:app --reload`)
- **Run Python**: `uv run python -m ...`
- **Install a package**: `uv add <pkg>` / `uv add --dev <pkg>`

### Monorepo layout

```
glee/           # Python backend package
  __init__.py
  main.py       # FastAPI app, routes
```

### Framework conventions

- `uv run` for all Python execution (resolves venv automatically)
- FastAPI app lives in `glee/main.py`

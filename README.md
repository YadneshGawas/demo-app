# CodeGuard AI – Intentionally Vulnerable Demo Repository

This repository is a **safe, intentionally vulnerable test fixture** for validating CodeGuard AI's multi-ecosystem discovery and scanning pipeline.

It contains:
- `frontend/`: React + Vite application with pinned, outdated JavaScript dependencies.
- `backend/`: Flask API with pinned, outdated Python dependencies and deliberately insecure code patterns.

## Expected CodeGuard discovery

| Project path | Ecosystem | Manifest |
|---|---|---|
| `frontend/` | JavaScript / React | `frontend/package.json` |
| `backend/` | Python / Flask | `backend/requirements.txt` |

A correct repository coordinator should discover both projects and dispatch **two child scans** (one per ecosystem/project).

## Test setup

Push this repository to a Git provider, register its clone URL in CodeGuard AI, and scan the `main` branch.

For the frontend, use Node.js 18 or a compatible runtime:
```bash
cd frontend
npm install
npm run build
```

For the backend, use Python 3.10:
```bash
cd backend
python -m venv .venv
. .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

The app is a demo only. Do not deploy it publicly or use its dependencies in production.

## Intentional findings

- Outdated dependency versions that should be checked against current advisory databases.
- Hardcoded demo credential.
- Debug mode enabled.
- Wildcard CORS configuration.
- Insecure subprocess invocation using `shell=True`.
- Weak MD5 password digest example.

These are test signals, not an assertion that every scanner will flag every item. Vulnerability findings should be confirmed against current OSV/npm advisory data and the exact dependency resolution.

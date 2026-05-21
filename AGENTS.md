# Linked — Automated LinkedIn Job Matcher

LinkedIn job matcher and applier automation project using AI (Vertex AI / Gemini for CV parsing and matching), FastAPI backend, and React (Vite) frontend.

## Architecture Overview

The project uses a **Domain-Driven Design (DDD)** folder structure within `backend/app/`.

- **Frontend:** React + Vite (located in `frontend/Linked/`).
- **Backend:** FastAPI + SQLAlchemy + Alembic. DDD structure: `domain/`, `application/`, `infrastructure/`, `interfaces/`.
- **AI Stack:** Google Vertex AI (Gemini) for CV parsing, semantic matching, and cover letter generation. Fallback: Llama 3.2 local.
- **Storage:** Google Cloud Storage for CV PDFs.
- **Git Workflow:** Follows **Git Flow** (see `use_gitflow.md`).

---

## Building and Running

### Backend (FastAPI)

1. **Prerequisites:** Python 3.11+
2. **Setup:**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate    # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env        # fill in your credentials
   ```
3. **Run migrations:**
   ```bash
   alembic upgrade head
   ```
4. **Run dev server:**
   ```bash
   uvicorn app.interfaces.fastapi_api.main:app --reload
   ```

### Frontend (React + Vite)

1. **Prerequisites:** Node.js + npm
2. **Setup:**
   ```bash
   cd frontend/Linked
   npm install
   npm run dev
   ```

---

## Development Conventions

- **Git Flow:**
  - Features: `feature/LINKED-<ID>-description`
  - Commits: `LINKED-<ID> descriptive message`
  - Branches: Always branch from `develop`.
- **Backend Logic:** Use the DDD structure in `backend/app/` for all core logic.
- **Python Style:** FastAPI conventions — Pydantic schemas, dependency injection, async where needed.
- **Frontend Style:** Modern React components with hooks, Zustand for state, TailwindCSS.

---

## Project Status

Current state is **Initialization Phase**:
- [x] Folder structure for DDD established.
- [x] FastAPI entry point wired.
- [x] Vite frontend initialized.
- [ ] Implement CV parsing (Vertex AI).
- [ ] Implement Job scraping/matching engine.
- [ ] Connect Frontend and Backend APIs.

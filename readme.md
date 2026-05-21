# Linked — Automated LinkedIn Job Matcher & Applier

Linked es una plataforma de automatización diseñada para revolucionar la búsqueda de empleo desde la perspectiva del candidato. El sistema permite que un profesional suba su CV y, mediante Inteligencia Artificial (Vertex AI / Gemini), estructure su perfil. A partir de ahí, el sistema extrae ofertas laborales de LinkedIn, realiza matcheo semántico, redacta cartas de presentación personalizadas y postula al usuario de forma automática.

---

## 🚀 Objetivo del Proyecto

1. El usuario sube su CV (PDF) → la IA lo parsea y genera un perfil estructurado.
2. El sistema scrapea ofertas de LinkedIn evadiendo anti-bots.
3. Se calcula un score de compatibilidad (matcheo semántico con embeddings + LLM).
4. Se genera una carta de presentación personalizada por oferta.
5. Se aplica automáticamente vía Gmail API o bot de formularios.
6. El usuario monitorea todo desde un dashboard con métricas e historial.

---

## 🏛️ Arquitectura

```
frontend/          → React + Vite (SPA)
backend/
  app/
    domain/        → Entidades, repositorios, value objects (DDD)
    application/   → Use cases
    infrastructure/
      ai/          → Vertex AI / Gemini (CV parser, matching engine)
      auth/        → JWT
      persistence/ → SQLAlchemy + Alembic (PostgreSQL)
      storage/     → Google Cloud Storage (CVs en PDF)
    interfaces/
      fastapi_api/ → Routers, schemas, entry point
```

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología |
|------|-----------|
| Frontend | React 19 + Vite 7 + TailwindCSS |
| Backend | FastAPI + Pydantic + SQLAlchemy |
| Base de datos | PostgreSQL + Alembic (migraciones) |
| IA / LLM | Google Vertex AI (Gemini) — fallback: Llama 3.2 local |
| Storage (CVs) | Google Cloud Storage |
| Scraping | Playwright + Selenium |
| Email | Gmail API (OAuth 2.0) |
| Task queue | Celery + Redis |
| Auth | JWT (OAuth2 password bearer) |
| CI/CD | GitHub Actions + Docker |
| Deploy futuro | Google Cloud Run |

---

## 🛠️ Cómo correr el proyecto

### Backend (FastAPI)

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Variables de entorno
cp .env.example .env            # completar con tus credenciales

# Migraciones
alembic upgrade head

# Servidor de desarrollo
uvicorn app.interfaces.fastapi_api.main:app --reload
```

### Frontend (React + Vite)

```bash
cd frontend/Linked
npm install
npm run dev
```

---

## ☁️ Servicios Google Cloud Platform

| Servicio | Uso |
|----------|-----|
| Vertex AI (Gemini) | Parser de CV + matching semántico + generación de cartas |
| Cloud Storage | Almacenamiento de CVs en PDF |
| Cloud SQL (futuro) | PostgreSQL gestionado en producción |
| Cloud Run (futuro) | Deploy del backend en contenedores |

> **Nota:** En desarrollo, PostgreSQL corre localmente. Cloud SQL y Cloud Run se usarán en producción.

---

## 👥 Equipo

- Esteban Agüero
- Daniel Vildoza
- Mauro Banegas
- Ezequiel Navarro

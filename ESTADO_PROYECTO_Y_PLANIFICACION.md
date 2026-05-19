# 📋 Proyecto Linked - Estado Actual y Planificación

**Última actualización:** Mayo 2026  
**Rama:** master (último commit: `8a1d5a6` - Merge PR #8)  
**Repositorio:** [Linked](https://github.com/Aguerit0/Linked)  
**Board Jira:** [SCRUM Board](https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1)

---

## 🛠️ Stack Tecnológico Confirmado

### Backend (Python)
| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Django** | 5.2.6 | Framework web principal |
| **FastAPI** | 0.117.1 | API REST para módulos de IA |
| **Uvicorn** | 0.36.0 | ASGI server para FastAPI |
| **Gunicorn** | 23.0.0 | WSGI server para producción |
| **Playwright** | 1.57.0 | Scraping de LinkedIn |
| **Selenium** | 4.32.0 | Scraping alternativo |
| **PyTorch** | 2.7.0 | Motor de embeddings/IA |
| **Psycopg2** | 2.9.9 | Driver PostgreSQL |

### Frontend (JavaScript/TypeScript)
| Tecnología | Versión | Uso |
|------------|---------|-----|
| **React** | 19.2.0 | Framework UI |
| **Vite** | 7.2.4 | Build tool + dev server |
| **ESLint** | 9.39.1 | Linting de código |

### Base de Datos
| Tecnología | Versión | Uso |
|------------|---------|-----|
| **PostgreSQL** | TBD | BD principal (configurada vía psycopg2) |
| **SQLite** | 3.x | BD de desarrollo (default Django) |

### Infraestructura
- **Apache Airflow** 2.10.0 - Orquestación de pipelines (disponible)
- **Redis** - Cache y colas (por configurar)
- **Docker** - Contenedorización (pendiente)

---

## 👥 Equipo y Asignaciones

### 🔵 Backend/Datos (26 tareas en Jira)
- **Mauro Banegas** (maurobanegas43@gmail.com)
  - Backend API (SCRUM-17): 5 tareas
  - Scraping (SCRUM-27): 2 tareas
  - Motor IA (SCRUM-32): 3 tareas
  - App Automática (SCRUM-38): 2 tareas
  - Infraestructura (SCRUM-53): 3 tareas
  
- **Esteban Agüero**
  - Backend API (SCRUM-17): 4 tareas
  - Scraping (SCRUM-27): 2 tareas
  - Motor IA (SCRUM-32): 2 tareas
  - App Automática (SCRUM-38): 2 tareas
  - Infraestructura (SCRUM-53): 3 tareas

### 🔴 UX/UI - Frontend (16 tareas en Jira)
- **Daniel Vildoza** (vildozadaniel640)
  - Frontend (SCRUM-43): 5 tareas
  - Testing/Docs (SCRUM-60): 2 tareas
  
- **Ezequiel Navarro Sahad**
  - Frontend (SCRUM-43): 4 tareas
  - Testing/Docs (SCRUM-60): 3 tareas

---

## 📊 Estado Actual del Proyecto

### ✅ Lo Implementado (Scaffolding)

#### Backend (Django 5.2.6)
- ✅ Proyecto Django inicializado (`django_project/`)
- ✅ Apps creadas: `users`, `jobs`, `app`
- ✅ Estructura Clean Architecture en `backend/app/`:
  - `domain/` - Entidades, value objects, servicios, repositorios (vacíos)
  - `application/` - Casos de uso (vacíos)
  - `infrastructure/` - Implementaciones (vacías)
  - `interfaces/` - API Django + FastAPI (esqueleto)
- ✅ `requirements.txt` con dependencias básicas (Django, FastAPI, etc.)

#### Frontend (React 19 + Vite)
- ✅ Proyecto Vite inicializado
- ✅ Template básico (App.jsx con contador)
- ✅ Configuración ESLint + Prettier
- ❌ Sin componentes reales
- ❌ Sin router, sin state management, sin UI library

#### Git/GitHub
- ✅ Repositorio activo con 8 PRs mergeados
- ✅ Ramas: master (principal), develop (integración), feature/*
- ✅ Últimos merges: `feature/init_backend`, `feature/init/fronted`

### ❌ Lo que Falta Implementar

#### Backend - Prioridad ALTA
- [ ] Models Django reales (User, Profile, CV, JobOffer, Application, Match)
- [ ] Django REST Framework (serializers, viewsets, routers)
- [ ] Autenticación JWT
- [ ] Endpoints CRUD completos
- [ ] Scraping de LinkedIn (Playwright/Selenium)
- [ ] Motor de matching con embeddings
- [ ] Generación de cartas con IA
- [ ] Integración Gmail API

#### Frontend - Prioridad ALTA
- [ ] React Router
- [ ] State management (Zustand/Context API)
- [ ] UI Library (Tailwind/Material UI)
- [ ] Páginas: Login, Registro, Dashboard, Perfil, Ofertas, Configuración
- [ ] Componentes reutilizables
- [ ] Integración API backend

#### Infraestructura - Prioridad MEDIA
- [ ] Docker + docker-compose
- [ ] PostgreSQL (migrar de SQLite)
- [ ] GitHub Actions (CI/CD)
- [ ] Despliegue en cloud

#### Testing/Docs - Prioridad MEDIA
- [ ] Tests unitarios backend
- [ ] Tests E2E frontend
- [ ] Documentación API (Swagger)
- [ ] README actualizado

---

## 🗂️ Tareas Asignadas en Jira (42 tareas)

### 📌 Épica 1: Backend - Modelos y API REST (SCRUM-17)

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-18 | Aprender Django ORM y Models | Mauro | 10d |
| SCRUM-19 | Crear models de Django con migraciones | Esteban | 7d |
| SCRUM-20 | Instalar y configurar Django REST Framework | Mauro | 7d |
| SCRUM-21 | Implementar autenticación JWT | Esteban | 5d |
| SCRUM-22 | CRUD de Perfil de Usuario | Mauro | 5d |
| SCRUM-23 | CRUD de Ofertas de Trabajo | Esteban | 5d |
| SCRUM-24 | CRUD de Aplicaciones y Matches | Mauro | 5d |
| SCRUM-25 | Migrar de SQLite a PostgreSQL | Esteban | 3d |
| SCRUM-26 | Tests del Backend | Mauro | 7d |

### 📌 Épica 2: Backend - Scraping LinkedIn (SCRUM-27)

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-28 | Aprender Playwright/Selenium para scraping | Esteban | 10d |
| SCRUM-29 | Scraper de ofertas LinkedIn | Mauro | 14d |
| SCRUM-30 | Manejo de rate limits y anti-bots | Esteban | 5d |
| SCRUM-31 | Scheduler de scraping periódico | Mauro | 5d |

### 📌 Épica 3: Backend - Motor de IA y Matching (SCRUM-32)

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-33 | Aprender embeddings y modelos NLP locales | Mauro | 15d |
| SCRUM-34 | Pipeline de embeddings para perfiles y ofertas | Esteban | 7d |
| SCRUM-35 | Algoritmo de matching por similitud | Mauro | 7d |
| SCRUM-36 | Generación de cartas de presentación con IA | Esteban | 10d |
| SCRUM-37 | Endpoint de matching completo | Mauro | 5d |

### 📌 Épica 4: Backend - Aplicación Automática (SCRUM-38)

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-39 | Aprender Gmail API y automatización de formularios | Esteban | 7d |
| SCRUM-40 | Integración con Gmail API | Mauro | 7d |
| SCRUM-41 | Bot de aplicación automática en LinkedIn | Esteban | 10d |
| SCRUM-42 | Sistema de cola de aplicaciones | Mauro | 5d |

### 📌 Épica 5: Frontend - Aplicación React Completa (SCRUM-43)
**Equipo UX/UI: Daniel & Ezequiel**

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-44 | Aprender React avanzado y ecosistema | Daniel | 10d |
| SCRUM-45 | Setup del proyecto: Router, State, UI Library | Ezequiel | 5d |
| SCRUM-46 | Páginas de Autenticación (Login/Registro) | Daniel | 5d |
| SCRUM-47 | Página de Perfil Profesional | Ezequiel | 7d |
| SCRUM-48 | Dashboard de Ofertas Matcheadas | Daniel | 10d |
| SCRUM-49 | Página de Historial de Aplicaciones | Ezequiel | 5d |
| SCRUM-50 | Página de Configuración | Daniel | 5d |
| SCRUM-51 | Componentes reutilizables y UI | Ezequiel | 7d |
| SCRUM-52 | Integración completa con API Backend | Daniel | 5d |

### 📌 Épica 6: Infraestructura y DevOps (SCRUM-53)

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-54 | Aprender Docker y docker-compose | Mauro | 7d |
| SCRUM-55 | Dockerizar Backend + Frontend + PostgreSQL | Esteban | 7d |
| SCRUM-56 | Configurar GitFlow y pre-commit hooks | Mauro | 3d |
| SCRUM-57 | Aprender GitHub Actions | Esteban | 5d |
| SCRUM-58 | Pipeline CI: lint + tests + build | Mauro | 5d |
| SCRUM-59 | Pipeline CD: despliegue automático | Esteban | 7d |

### 📌 Épica 7: Testing, Calidad y Documentación (SCRUM-60)
**Equipo UX/UI: Daniel & Ezequiel**

| Issue | Tarea | Assignee | Días |
|-------|-------|----------|------|
| SCRUM-61 | Aprender testing E2E con Cypress/Playwright | Ezequiel | 7d |
| SCRUM-62 | Tests E2E de flujos críticos | Daniel | 7d |
| SCRUM-63 | Documentación API con Swagger/OpenAPI | Ezequiel | 3d |
| SCRUM-64 | Auditoría de seguridad | Daniel | 5d |
| SCRUM-65 | Documentación del proyecto | Ezequiel | 5d |

---

## 📅 Cronograma Recomendado por Fases

### Fase 1: Setup y Aprendizaje (Semanas 1-3)
**Objetivo:** Que cada equipo aprenda las tecnologías base

| Equipo | Tareas | Duración |
|--------|--------|----------|
| **Backend** (Mauro/Esteban) | SCRUM-18 (Django ORM) | 10 días |
| **Frontend** (Daniel/Ezequiel) | SCRUM-44 (React avanzado) | 10 días |
| **Infra** (Mauro/Esteban) | SCRUM-54 (Docker) | 7 días |

**Entregable Fase 1:**
- Backend: Models definidos en papel + POC de Django ORM
- Frontend: Prototipos en Figma + setup de React Router
- Infra: Dockerfile básico funcional

### Fase 2: Desarrollo Core (Semanas 4-10)
**Objetivo:** Tener backend y frontend funcionales

| Equipo | Tareas | Duración |
|--------|--------|----------|
| **Backend** | SCRUM-19 → SCRUM-26 (Models, DRF, Auth, CRUDs) | 6 semanas |
| **Frontend** | SCRUM-45 → SCRUM-49 (Auth, Perfil, Dashboard) | 6 semanas |

**Entregable Fase 2:**
- Backend: API REST completa con autenticación
- Frontend: Login + Perfil de usuario funcional

### Fase 3: Features Avanzadas (Semanas 11-16)
**Objetivo:** Scraping, IA y matching

| Equipo | Tareas | Duración |
|--------|--------|----------|
| **Backend** | SCRUM-28 → SCRUM-37 (Scraping, Embeddings, Matching) | 5 semanas |
| **Frontend** | SCRUM-50 → SCRUM-52 (Config, Componentes, Integración) | 3 semanas |

**Entregable Fase 3:**
- Scraper de LinkedIn funcionando
- Motor de matching con scores
- Dashboard completo con ofertas matcheadas

### Fase 4: Automatización e Infra (Semanas 17-20)
**Objetivo:** Aplicación automática y CI/CD

| Equipo | Tareas | Duración |
|--------|--------|----------|
| **Backend** | SCRUM-39 → SCRUM-42 (Gmail API, Bot LinkedIn) | 4 semanas |
| **Infra** | SCRUM-55 → SCRUM-59 (Docker, CI/CD, Deploy) | 4 semanas |

**Entregable Fase 4:**
- Aplicaciones automáticas funcionando
- Pipelines CI/CD en GitHub Actions
- Despliegue en staging/producción

### Fase 5: Testing y Calidad (Semanas 21-22)
**Objetivo:** Asegurar calidad antes de release

| Equipo | Tareas | Duración |
|--------|--------|----------|
| **Frontend** | SCRUM-61 → SCRUM-65 (Tests E2E, Docs, Auditoría) | 2 semanas |

**Entregable Fase 5:**
- Tests E2E de flujos críticos
- Documentación completa
- Auditoría de seguridad aprobada

---

## 🎯 Hitos Clave (Milestones)

| Hito | Fecha Estimada | Issues Críticos |
|------|----------------|-----------------|
| **M1:** Models + API básica | Semana 6 | SCRUM-19, SCRUM-20, SCRUM-21 |
| **M2:** Frontend Auth + Perfil | Semana 8 | SCRUM-46, SCRUM-47 |
| **M3:** Scraper LinkedIn | Semana 12 | SCRUM-29 |
| **M4:** Motor de Matching | Semana 14 | SCRUM-34, SCRUM-35 |
| **M5:** Bot Aplicación Automática | Semana 18 | SCRUM-41 |
| **M6:** CI/CD + Deploy | Semana 20 | SCRUM-58, SCRUM-59 |
| **M7:** Release v1.0 | Semana 22 | Todos completados |

---

## 🔗 Links de Acceso

| Recurso | Link |
|---------|------|
| **Board Jira** | https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1 |
| **Repositorio GitHub** | https://github.com/Aguerit0/Linked |
| **Épicas Jira** | https://cuentauniversidading.atlassian.net/projects/SCRUM/issues |

---

## 📈 Métricas de Progreso

| Métrica | Valor |
|---------|-------|
| Total de Tareas | 42 |
| Tareas Completadas | 0 (0%) |
| Tareas en Progreso | 0 (0%) |
| Tareas Pendientes | 42 (100%) |
| Estimación Total | 281 días |
| Equipo | 4 personas |
| Velocidad Esperada | ~8-10 tareas/sprint (2 semanas) |

---

## ⚠️ Riesgos y Mitigación

| Riesgo | Impacto | Mitigación |
|--------|---------|------------|
| Curva de aprendizaje más lenta | Alto | Pair programming, tutorías, documentación extra |
| LinkedIn bloquea scraping | Medio | Usar API oficial si es posible, delays aleatorios |
| Modelo de IA requiere muchos recursos | Medio | Usar modelos pequeños (Phi-3, Qwen 1.5B) |
| Cambios en requirements | Bajo | Reuniones quincenales de revisión |

---

**Documentación generada automáticamente desde Jira + análisis del código**  
**Última sync:** Mayo 2026

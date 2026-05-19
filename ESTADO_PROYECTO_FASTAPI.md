# 📋 Proyecto Linked - Estado Actual y Planificación

**Última actualización:** Mayo 2026  
**Rama:** master (último commit: `cb9e4e4`)  
**Repositorio:** [Linked](https://github.com/Aguerit0/Linked)  
**Board Jira:** [SCRUM Board](https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1)

---

## 🛠️ Stack Tecnológico Confirmado

### Backend (Python - FastAPI Only)
| Tecnología | Versión | Uso | Estado |
|------------|---------|-----|--------|
| **FastAPI** | 0.117.1 | Framework API REST | ✅ Instalado |
| **Uvicorn** | 0.36.0 | ASGI server | ✅ Instalado |
| **Pydantic** | 2.x | Validación de datos | ✅ Incluido |
| **SQLAlchemy** | 2.x | ORM para BD | ⏳ Por configurar |
| **Alembic** | 1.13.2 | Migraciones BD | ✅ Disponible |
| **Playwright** | 1.57.0 | Scraping LinkedIn | ✅ Instalado |
| **PyTorch** | 2.7.0 | Motor de embeddings/IA | ✅ Instalado |
| **Psycopg2** | 2.9.9 | Driver PostgreSQL | ✅ Instalado |

### Frontend (JavaScript/TypeScript)
| Tecnología | Versión | Uso | Estado |
|------------|---------|-----|--------|
| **React** | 19.2.0 | Framework UI | ✅ Instalado |
| **Vite** | 7.2.4 | Build tool + dev server | ✅ Instalado |
| **Zustand** | TBD | State management | ⏳ Por instalar |
| **React Router** | TBD | Routing | ⏳ Por instalar |
| **TailwindCSS** | TBD | Estilos | ⏳ Por instalar |

### Base de Datos
| Tecnología | Uso | Estado |
|------------|-----|--------|
| **PostgreSQL** | BD principal | ⏳ Por configurar |
| **SQLite** | Desarrollo temporal | ✅ Default |

---

## 👥 Equipo y Asignaciones en Jira

### 🔵 Backend/Datos (26 tareas)
- **Mauro Banegas** (Reporter de épicas)
  - SCRUM-17: Backend API FastAPI - 5 tareas
  - SCRUM-27: Scraping - 2 tareas  
  - SCRUM-32: Motor IA - 3 tareas
  - SCRUM-38: App Automática - 2 tareas
  - SCRUM-53: Infraestructura - 3 tareas
  
- **Esteban Agüero**
  - SCRUM-17: Backend API FastAPI - 4 tareas
  - SCRUM-27: Scraping - 2 tareas
  - SCRUM-32: Motor IA - 2 tareas
  - SCRUM-38: App Automática - 2 tareas
  - SCRUM-53: Infraestructura - 3 tareas

### 🔴 UX/UI - Frontend (16 tareas)
- **Daniel Vildoza**
  - SCRUM-43: Frontend - 5 tareas
  - SCRUM-60: Testing/Docs - 2 tareas
  
- **Ezequiel Navarro Sahad**
  - SCRUM-43: Frontend - 4 tareas
  - SCRUM-60: Testing/Docs - 3 tareas

---

## 📅 Cronograma con Fechas Estimadas

### Sprint 0: Setup Inicial (10-24 Mayo 2026)
| Tarea | Assignee | Start Date | Due Date | Estado |
|-------|----------|------------|----------|--------|
| SCRUM-18 | Mauro | 2026-05-20 | 2026-05-30 | Por hacer |
| SCRUM-44 | Daniel | 2026-05-20 | 2026-05-30 | Por hacer |
| SCRUM-54 | Mauro | 2026-05-20 | 2026-05-27 | Por hacer |

### Sprint 1: Backend FastAPI Core (25 Mayo - 14 Junio 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-19 | Esteban | 2026-05-25 | 2026-06-01 | 5 |
| SCRUM-20 | Mauro | 2026-06-01 | 2026-06-08 | 5 |
| SCRUM-21 | Esteban | 2026-06-08 | 2026-06-12 | 3 |
| SCRUM-22 | Mauro | 2026-06-12 | 2026-06-17 | 3 |
| SCRUM-23 | Esteban | 2026-06-17 | 2026-06-22 | 3 |
| SCRUM-24 | Mauro | 2026-06-22 | 2026-06-27 | 3 |
| SCRUM-25 | Esteban | 2026-06-27 | 2026-06-30 | 2 |
| SCRUM-26 | Mauro | 2026-06-30 | 2026-07-07 | 5 |

### Sprint 2: Frontend Setup (25 Mayo - 14 Junio 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-45 | Ezequiel | 2026-05-25 | 2026-05-30 | 3 |
| SCRUM-46 | Daniel | 2026-05-30 | 2026-06-04 | 3 |
| SCRUM-47 | Ezequiel | 2026-06-04 | 2026-06-11 | 5 |

### Sprint 3: Scraping + Motor IA (15 Junio - 12 Julio 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-28 | Esteban | 2026-06-15 | 2026-06-25 | 8 |
| SCRUM-29 | Mauro | 2026-06-25 | 2026-07-09 | 13 |
| SCRUM-30 | Esteban | 2026-07-09 | 2026-07-14 | 3 |
| SCRUM-31 | Mauro | 2026-07-14 | 2026-07-19 | 3 |
| SCRUM-33 | Mauro | 2026-06-20 | 2026-07-05 | 10 |
| SCRUM-34 | Esteban | 2026-07-05 | 2026-07-12 | 5 |
| SCRUM-35 | Mauro | 2026-07-12 | 2026-07-19 | 5 |
| SCRUM-36 | Esteban | 2026-07-19 | 2026-07-29 | 8 |
| SCRUM-37 | Mauro | 2026-07-29 | 2026-08-03 | 3 |

### Sprint 4: Frontend Dashboard (15 Junio - 12 Julio 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-48 | Daniel | 2026-06-15 | 2026-06-25 | 8 |
| SCRUM-49 | Ezequiel | 2026-06-25 | 2026-06-30 | 3 |
| SCRUM-50 | Daniel | 2026-06-30 | 2026-07-05 | 3 |
| SCRUM-51 | Ezequiel | 2026-07-05 | 2026-07-12 | 5 |
| SCRUM-52 | Daniel | 2026-07-12 | 2026-07-17 | 3 |

### Sprint 5: App Automática + Infra (20 Julio - 16 Agosto 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-39 | Esteban | 2026-07-20 | 2026-07-27 | 5 |
| SCRUM-40 | Mauro | 2026-07-27 | 2026-08-03 | 5 |
| SCRUM-41 | Esteban | 2026-08-03 | 2026-08-13 | 8 |
| SCRUM-42 | Mauro | 2026-08-13 | 2026-08-18 | 3 |
| SCRUM-55 | Esteban | 2026-07-20 | 2026-07-27 | 5 |
| SCRUM-56 | Mauro | 2026-07-27 | 2026-07-30 | 2 |
| SCRUM-57 | Esteban | 2026-07-30 | 2026-08-04 | 3 |
| SCRUM-58 | Mauro | 2026-08-04 | 2026-08-09 | 3 |
| SCRUM-59 | Esteban | 2026-08-09 | 2026-08-16 | 5 |

### Sprint 6: Testing + Release (17-30 Agosto 2026)
| Tarea | Assignee | Start Date | Due Date | Story Points |
|-------|----------|------------|----------|--------------|
| SCRUM-61 | Ezequiel | 2026-08-17 | 2026-08-24 | 5 |
| SCRUM-62 | Daniel | 2026-08-17 | 2026-08-24 | 5 |
| SCRUM-63 | Ezequiel | 2026-08-24 | 2026-08-27 | 2 |
| SCRUM-64 | Daniel | 2026-08-24 | 2026-08-29 | 3 |
| SCRUM-65 | Ezequiel | 2026-08-27 | 2026-08-30 | 3 |

---

## 📊 Resumen de Fechas Clave

| Hito | Fecha | Descripción |
|------|-------|-------------|
| **Kickoff** | 2026-05-20 | Inicio Sprint 0 |
| **M1: API FastAPI funcional** | 2026-07-07 | Endpoints CRUD + Auth |
| **M2: Frontend Login+Perfil** | 2026-06-11 | Primeras pantallas |
| **M3: Scraper LinkedIn** | 2026-07-19 | Scraping operativo |
| **M4: Motor Matching** | 2026-08-03 | IA generando scores |
| **M5: Bot Aplicación** | 2026-08-18 | Auto-aplicación lista |
| **M6: Deploy Producción** | 2026-08-16 | CI/CD + staging |
| **M7: Release v1.0** | 2026-08-30 | Versión final |

---

## 🎯 Tareas Prioritarias (Highest Priority)

### Épica SCRUM-17: Backend FastAPI (Mauro - Reporter)
| Tarea | Assignee | Story Points | Start | Due |
|-------|----------|--------------|-------|-----|
| SCRUM-18 | Mauro | 8 | 2026-05-20 | 2026-05-30 |
| SCRUM-19 | Esteban | 5 | 2026-05-25 | 2026-06-01 |
| SCRUM-20 | Mauro | 5 | 2026-06-01 | 2026-06-08 |
| SCRUM-21 | Esteban | 3 | 2026-06-08 | 2026-06-12 |
| SCRUM-22 | Mauro | 3 | 2026-06-12 | 2026-06-17 |
| SCRUM-23 | Esteban | 3 | 2026-06-17 | 2026-06-22 |
| SCRUM-24 | Mauro | 3 | 2026-06-22 | 2026-06-27 |
| SCRUM-25 | Esteban | 2 | 2026-06-27 | 2026-06-30 |
| SCRUM-26 | Mauro | 5 | 2026-06-30 | 2026-07-07 |

---

## ⚠️ Cambios vs Plan Original

| Aspecto | Plan Original | Plan Actualizado |
|---------|--------------|------------------|
| **Backend Framework** | Django + FastAPI | **Solo FastAPI** |
| **Complejidad** | Alta (2 frameworks) | Media (1 framework) |
| **Curva aprendizaje** | 2 semanas Django + 1 FastAPI | 2 semanas FastAPI |
| **Tareas Backend** | 9 (con Django) | 8 (FastAPI puro) |
| **ORM** | Django ORM | SQLAlchemy |
| **Migraciones** | Django Migrations | Alembic |
| **Duración total** | 22 semanas | **20 semanas** (ahorro 2) |

---

## 🔗 Links de Acceso

| Recurso | Link |
|---------|------|
| **Board Jira** | https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1 |
| **Repositorio GitHub** | https://github.com/Aguerit0/Linked |
| **Épicas Jira** | https://cuentauniversidading.atlassian.net/projects/SCRUM/issues |

---

**Documentación generada automáticamente desde Jira + análisis del código**  
**Última sync:** Mayo 2026  
**Próxima revisión:** 2026-05-27 (fin Sprint 0)

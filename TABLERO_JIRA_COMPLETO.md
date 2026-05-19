# 🎯 Tablero Jira - Proyecto Linked (Automatizador LinkedIn)

## ✅ Configuración Completada

**Proyecto Jira:** [SCRUM - Linked](https://cuentauniversidading.atlassian.net/projects/SCRUM/issues)
**Board:** [SCRUM board](https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1)
**Tipo:** Kanban (next-gen/simplified)
**Columnas:** Por hacer → En curso → En revisión → Finalizado

---

## 📊 Resumen del Tablero

| Métrica | Valor |
|---------|-------|
| **Total de Issues** | 49 (7 épicas + 42 tareas) |
| **Épicas Configuradas** | 7 |
| **Tareas Vinculadas** | 42/42 ✅ |
| **Estado Actual** | Todas en "Por hacer" |
| **Estimación Total** | ~281 días de desarrollo |

---

## 🗂️ Estructura del Board por Épicas

### 🔵 SCRUM-17: Backend - Modelos y API REST (9 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-18 | Aprender Django ORM y Models | 10d |
| SCRUM-19 | Crear models de Django con migraciones | 7d |
| SCRUM-20 | Instalar y configurar Django REST Framework | 7d |
| SCRUM-21 | Implementar autenticación JWT | 5d |
| SCRUM-22 | CRUD de Perfil de Usuario | 5d |
| SCRUM-23 | CRUD de Ofertas de Trabajo | 5d |
| SCRUM-24 | CRUD de Aplicaciones y Matches | 5d |
| SCRUM-25 | Migrar de SQLite a PostgreSQL | 3d |
| SCRUM-26 | Tests del Backend | 7d |

### 🟢 SCRUM-27: Backend - Scraping LinkedIn (4 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-28 | Aprender Playwright/Selenium para scraping | 10d |
| SCRUM-29 | Scraper de ofertas LinkedIn | 14d |
| SCRUM-30 | Manejo de rate limits y anti-bots | 5d |
| SCRUM-31 | Scheduler de scraping periódico | 5d |

### 🟡 SCRUM-32: Backend - Motor de IA y Matching (5 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-33 | Aprender embeddings y modelos NLP locales | 15d |
| SCRUM-34 | Pipeline de embeddings para perfiles y ofertas | 7d |
| SCRUM-35 | Algoritmo de matching por similitud | 7d |
| SCRUM-36 | Generación de cartas de presentación con IA | 10d |
| SCRUM-37 | Endpoint de matching completo | 5d |

### 🟠 SCRUM-38: Backend - Aplicación Automática (4 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-39 | Aprender Gmail API y automatización de formularios | 7d |
| SCRUM-40 | Integración con Gmail API | 7d |
| SCRUM-41 | Bot de aplicación automática en LinkedIn | 10d |
| SCRUM-42 | Sistema de cola de aplicaciones | 5d |

### 🔴 SCRUM-43: Frontend - Aplicación React Completa (9 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-44 | Aprender React avanzado y ecosistema | 10d |
| SCRUM-45 | Setup del proyecto: Router, State, UI Library | 5d |
| SCRUM-46 | Páginas de Autenticación (Login/Registro) | 5d |
| SCRUM-47 | Página de Perfil Profesional | 7d |
| SCRUM-48 | Dashboard de Ofertas Matcheadas | 10d |
| SCRUM-49 | Página de Historial de Aplicaciones | 5d |
| SCRUM-50 | Página de Configuración | 5d |
| SCRUM-51 | Componentes reutilizables y UI | 7d |
| SCRUM-52 | Integración completa con API Backend | 5d |

### 🟣 SCRUM-53: Infraestructura y DevOps (6 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-54 | Aprender Docker y docker-compose | 7d |
| SCRUM-55 | Dockerizar Backend + Frontend + PostgreSQL | 7d |
| SCRUM-56 | Configurar GitFlow y pre-commit hooks | 3d |
| SCRUM-57 | Aprender GitHub Actions | 5d |
| SCRUM-58 | Pipeline CI: lint + tests + build | 5d |
| SCRUM-59 | Pipeline CD: despliegue automático | 7d |

### ⚫ SCRUM-60: Testing, Calidad y Documentación (5 tareas)
| Tarea | Descripción | Días |
|-------|------------|------|
| SCRUM-61 | Aprender testing E2E con Cypress/Playwright | 7d |
| SCRUM-62 | Tests E2E de flujos críticos | 7d |
| SCRUM-63 | Documentación API con Swagger/OpenAPI | 3d |
| SCRUM-64 | Auditoría de seguridad | 5d |
| SCRUM-65 | Documentación del proyecto | 5d |

---

## 📋 Flujo de Trabajo del Board

```
┌─────────────┐    ┌──────────┐    ┌──────────────┐    ┌───────────┐
│  Por hacer   │───▶│ En curso  │───▶│ En revisión   │───▶│ Finalizado │
│  (Backlog)   │    │ (Active)  │    │ (Code Review) │    │ (Done)    │
└─────────────┘    └──────────┘    └──────────────┘    └───────────┘
```

---

## 🎯 Orden Recomendado de Ejecución

### Fase 1 (Semanas 1-4): Fundamentos
1. **SCRUM-18** - Aprender Django ORM (equipo backend)
2. **SCRUM-44** - Aprender React avanzado (equipo frontend)
3. **SCRUM-54** - Aprender Docker (equipo infra)

### Fase 2 (Semanas 4-8): Backend Core
1. **SCRUM-19** → **SCRUM-26** - Models, API REST, Auth, Tests
2. En paralelo: **SCRUM-45** → **SCRUM-47** - Setup frontend, Auth, Perfil

### Fase 3 (Semanas 8-14): Funcionalidades Clave
1. **SCRUM-28** → **SCRUM-31** - Scraping LinkedIn
2. **SCRUM-33** → **SCRUM-37** - Motor de IA y Matching
3. **SCRUM-48** → **SCRUM-52** - Dashboard frontend

### Fase 4 (Semanas 14-18): Automatización
1. **SCRUM-39** → **SCRUM-42** - Aplicación automática
2. **SCRUM-55** → **SCRUM-59** - Infraestructura y CI/CD

### Fase 5 (Semanas 18-20): Calidad
1. **SCRUM-61** → **SCRUM-65** - Tests E2E, Docs, Auditoría

---

## 🔗 Links Rápidos

- **Board Principal:** https://cuentauniversidading.atlassian.net/jira/software/projects/SCRUM/boards/1
- **Todas las Issues:** https://cuentauniversidading.atlassian.net/projects/SCRUM/issues
- **Épica Backend API:** https://cuentauniversidading.atlassian.net/browse/SCRUM-17
- **Épica Scraping:** https://cuentauniversidading.atlassian.net/browse/SCRUM-27
- **Épica Motor IA:** https://cuentauniversidading.atlassian.net/browse/SCRUM-32
- **Épica Auto-Aplicación:** https://cuentauniversidading.atlassian.net/browse/SCRUM-38
- **Épica Frontend:** https://cuentauniversidading.atlassian.net/browse/SCRUM-43
- **Épica Infraestructura:** https://cuentauniversidading.atlassian.net/browse/SCRUM-53
- **Épica Testing:** https://cuentauniversidading.atlassian.net/browse/SCRUM-60

---

**Última actualización:** Mayo 2026
**Estado:** ✅ Tablero configurado y listo para usar

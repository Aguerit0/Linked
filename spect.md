# Especificación del Proyecto — Linked

## Descripción General

Linked es una plataforma de automatización diseñada para revolucionar la búsqueda de empleo desde la perspectiva del candidato. El sistema permitirá que un profesional suba su currículum (CV) y, mediante Inteligencia Artificial (Google Vertex AI / Gemini), estructure su perfil. A partir de ahí, el sistema utilizará técnicas avanzadas de extracción de datos (evadiendo sistemas anti-bot de LinkedIn) para buscar ofertas laborales. Luego, realizará un matcheo semántico, redactará cartas de presentación personalizadas y postulará al usuario de forma automática, ahorrándole horas de búsqueda y aplicación manual.

---

## Requerimientos Funcionales

**R01. Parser de CVs:**
El sistema deberá extraer el texto del CV del usuario (PDF) y convertirlo en un perfil estructurado (JSON) mediante Vertex AI (Gemini). El PDF original se almacenará en Google Cloud Storage.

**R02. Gestión de Cuenta y Preferencias:**
El sistema deberá permitir el registro seguro de usuarios y la configuración de sus preferencias laborales (rango salarial, tipo de contrato, modalidad remota/híbrida). Las credenciales se almacenarán cifradas con autenticación JWT.

**R03. Scraping de Ofertas:**
El sistema deberá extraer ofertas laborales de LinkedIn de forma automatizada, utilizando Playwright y Selenium con técnicas de evasión de anti-bots (delays, rotación de user-agents, manejo de CAPTCHAs).

**R04. Matcheo Semántico:**
El sistema deberá comparar el perfil del usuario contra cada oferta encontrada y calcular un porcentaje de compatibilidad (Score) utilizando embeddings de Vertex AI.

**R05. Generación de Cartas:**
El sistema deberá redactar automáticamente una carta de presentación adaptada a la oferta específica utilizando Vertex AI (Gemini). Las cartas deberán completarse en menos de 120 segundos.

**R06. Postulación Automática:**
El sistema deberá enviar la candidatura de forma automática a través de la API de Gmail (CV adjunto + carta personalizada) o completando formularios en LinkedIn mediante Playwright.

**R07. Dashboard y Seguimiento:**
El sistema deberá proveer un panel de control con métricas clave (total de ofertas matcheadas, aplicaciones enviadas) y un historial de postulaciones con estado.

**R08. Sistema de Notificaciones:**
El sistema deberá alertar al usuario (vía email) cuando se detecten nuevas ofertas con alta compatibilidad (score por encima del umbral configurado).

---

## Requerimientos No Funcionales

**RNF01. Seguridad (PII y Credenciales):**
Las contraseñas, tokens de acceso a Gmail/LinkedIn y datos personales del usuario deberán almacenarse cifrados. Autenticación mediante JWT (OAuth2 password bearer).

**RNF02. Almacenamiento Cloud:**
Los PDFs originales de los usuarios deberán guardarse de forma segura en **Google Cloud Storage (GCS)**.

**RNF03. Rendimiento y Tiempos de Respuesta:**
Las operaciones críticas (cálculo de matching, generación de carta) deberán completarse en menos de 120 segundos. El scraping periódico se ejecutará en segundo plano mediante Celery + Redis.

**RNF04. Usabilidad:**
La plataforma deberá contar con una curva de aprendizaje mínima, permitiendo que un usuario nuevo complete su registro y carga de CV sin asistencia.

**RNF05. Restricción Ética / Calidad:**
El sistema NO se postulará a ofertas laborales que estén por debajo del umbral salarial o preferencias de modalidad configuradas por el usuario.

---

## Stack Tecnológico Definitivo

| Capa | Tecnología | Notas |
|------|-----------|-------|
| Backend | FastAPI + SQLAlchemy + Alembic | DDD: domain / application / infrastructure / interfaces |
| Base de datos (dev) | PostgreSQL local | En producción: Cloud SQL (PostgreSQL gestionado) |
| IA / LLM | Google Vertex AI (Gemini) | Fallback: Llama 3.2 local si presupuesto no alcanza |
| Storage CVs | Google Cloud Storage | RNF02 |
| Scraping | Playwright + Selenium | R03 |
| Email | Gmail API (OAuth 2.0) | R06 |
| Task queue | Celery + Redis | Scraping periódico, notificaciones |
| Auth | JWT (python-jose + passlib) | RNF01 |
| Frontend | React 19 + Vite 7 + TailwindCSS | SPA |
| Deploy (futuro) | Google Cloud Run | Contenedores Docker |
| CI/CD | GitHub Actions | Lint + tests + build |

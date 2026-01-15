# Automated LinkedIn Job Matcher & Applier

Este proyecto tiene como objetivo automatizar la búsqueda y postulación a empleos en LinkedIn mediante:

- Análisis del perfil del usuario en lenguaje natural.
- Scraping de ofertas laborales y publicaciones.
- Matcheo inteligente entre perfil y ofertas.
- Aplicación automática con CV y carta personalizada generada por IA.
- Sistema completo con frontend, backend, base de datos y pipeline de IA.

---

## 🚀 Objetivo del Proyecto

Crear una plataforma que permita:
1. Cargar el perfil profesional del usuario (experiencia, stack, seniority, inglés, etc.).
2. Scrappear ofertas laborales y publicaciones de LinkedIn.
3. Matchear ofertas usando embeddings + un modelo de IA local (a definir).
4. Generar cartas de presentación personalizadas.
5. Aplicar automáticamente vía email o bot.

---

## 🧩 Arquitectura Propuesta

### **Frontend**
- Formulario de registro.
- Carga de CV.
- Preferencias laborales.
- Panel de ofertas matcheadas.

### **Backend**
- API REST para usuarios, ofertas, matcheo y aplicaciones.
- Módulo de Scraping (LinkedIn job posts + publicaciones).
- Motor de matcheo basado en:
  - Embeddings (MiniLM / E5-small).
  - Modelo generativo liviano (Qwen, Phi-3, Llama 3.x — aún a definir).
- Generación de cartas de presentación.
- Envío automatizado vía Gmail API.

### **Base de Datos**
- Perfiles de usuario.
- CV + metadata.
- Ofertas obtenidas del scraping.
- Historial de aplicaciones.

---

## 🛠️ Tecnologías (propuestas, no definitivas)

- **Frontend:** React / Next.js / Vite (a definir).
- **Backend:** FastAPI / Streamlit / Node.js (a definir).
- **Modelos de IA:** Qwen 2.5, Phi-3 Mini o modelos similares corriendo en local.
- **Scraping:** Playwright / Selenium / BeautifulSoup.
- **DB:** PostgreSQL / MongoDB (a definir).
- **Infraestructura:** Docker, despliegue en nube (servicio TBD).
- **Gestión del proyecto:** GitHub + Jira.

---

## 👥 Equipo

- Esteban Agüero  
- Daniel Vildoza
- Mauro Banegas
- Ezequiel Navarro


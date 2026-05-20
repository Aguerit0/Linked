# Análisis Técnico de Desarrollo - LinkedIn Job Matcher

## 1. Arquitectura del Sistema

### 1.1 Visión General

```
┌─────────────────────────────────────────────────────────────────────────┐
│                            FRONTEND                                      │
│  (React/Next.js o SvelteKit)                                           │
│  - Dashboard                                                             │
│  - Gestión de perfil                                                    │
│  - Búsqueda de ofertas                                                  │
│  - Editor de cartas                                                     │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │ REST API / GraphQL
                                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                            BACKEND                                       │
│  (Python/FastAPI o Go)                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────────┐   │
│  │ Auth Module │ │  Profile    │ │  Scraping   │ │ Matching Engine │   │
│  │             │ │  Module     │ │  Module     │ │                 │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────────┘   │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐                        │
│  │   CV        │ │  Cover      │ │ Application │                        │
│  │  Parser     │ │  Generator  │ │  Module     │                        │
│  └─────────────┘ └─────────────┘ └─────────────┘                        │
└────────────────────────────────┬────────────────────────────────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        ▼                        ▼                        ▼
┌───────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  PostgreSQL   │     │  Model Files    │     │  LinkedIn/Gmail │
│  (Data)       │     │  (/models)      │     │  (External APIs)│
└───────────────┘     └─────────────────┘     └─────────────────┘
```

### 1.2 Estilo Arquitectónico

- **Monolito modular**: Un solo deploy, pero dividido en módulos bien separados
- **API REST**: Endpoints RESTful con JSON
- **Separación de responsabilidades**: Cada módulo tiene su propia responsabilidad

### 1.3 Capas del Backend

```
┌────────────────────────────────────┐
│       API Layer (Routes/Views)     │  → Endpoints HTTP
├────────────────────────────────────┤
│     Business Logic (Services)      │  → Lógica de negocio
├────────────────────────────────────┤
│      Domain Layer (Models)         │  → Entidades y reglas
├────────────────────────────────────┤
│    Infrastructure (DB, External)   │  → Repositorios, APIs
└────────────────────────────────────┘
```

---

## 2. Estructura del Proyecto

### 2.1 Estructura Sugerida (Python/FastAPI)

```
linkedin-job-matcher/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Entry point, configuración
│   ├── config.py              # Settings, variables de entorno
│   ├── deps.py                # Dependencies injection
│   │
│   ├── api/                   # Endpoints HTTP
│   │   ├── v1/
│   │   │   ├── auth.py        # /auth/register, /auth/login
│   │   │   ├── profile.py    # /profile, /profile/experience
│   │   │   ├── cv.py          # /cv/upload, /cv/parse
│   │   │   ├── jobs.py        # /jobs, /jobs/search, /jobs/{id}
│   │   │   ├── matching.py    # /matching, /matching/{job_id}
│   │   │   ├── cover_letter.py
│   │   │   └── applications.py
│   │   └── dependencies.py    # Dependencias comunes
│   │
│   ├── core/                  # Configuración central
│   │   ├── security.py        # JWT, password hashing
│   │   ├── config.py         # Settings class
│   │   └── exceptions.py     # Custom exceptions
│   │
│   ├── models/                # Modelos SQLAlchemy / ORM
│   │   ├── user.py
│   │   ├── job.py
│   │   ├── application.py
│   │   └── enums.py
│   │
│   ├── schemas/               # Pydantic models (request/response)
│   │   ├── user.py
│   │   ├── job.py
│   │   └── ...
│   │
│   ├── services/              # Lógica de negocio
│   │   ├── auth_service.py
│   │   ├── profile_service.py
│   │   ├── cv_parser_service.py
│   │   ├── scraper_service.py
│   │   ├── matching_service.py
│   │   ├── cover_letter_service.py
│   │   └── application_service.py
│   │
│   ├── repositories/          # Acceso a datos
│   │   ├── user_repo.py
│   │   ├── job_repo.py
│   │   └── ...
│   │
│   └── utils/                 # Utilidades
│       ├── embeddings.py      # Modelo de embedding
│       ├── llm_generator.py   # Generación de cartas
│       ├── cv_parser.py      # Parsing de CV
│       └── scraper/           # LinkedIn scraper
│           ├── linkedin_client.py
│           └── ...
│
├── models/                    # Modelos IA (embeddings, LLM)
│   ├── embeddings/
│   │   └── model files
│   └── generators/
│       └── model files
│
├── scripts/
│   ├── init_db.py
│   ├── seed_data.py
│   └── run_scraper.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── alembic/                  # Migraciones de DB
│   └── versions/
│
├── docker-compose.yml        # Desarrollo local
├── Dockerfile
├── requirements.txt
├── .env.example
└── README.md
```

### 2.2 Estructura del Frontend (React/Next.js)

```
frontend/
├── src/
│   ├── app/                   # Next.js App Router
│   │   ├── (auth)/
│   │   │   ├── login/
│   │   │   └── register/
│   │   ├── (dashboard)/
│   │   │   ├── dashboard/
│   │   │   ├── profile/
│   │   │   ├── jobs/
│   │   │   ├── applications/
│   │   │   └── settings/
│   │   ├── layout.tsx
│   │   └── page.tsx
│   │
│   ├── components/
│   │   ├── ui/               # Componentes base (Button, Input, etc.)
│   │   ├── auth/
│   │   ├── profile/
│   │   ├── jobs/
│   │   ├── matching/
│   │   └── cover-letter/
│   │
│   ├── hooks/                # Custom hooks
│   │   ├── useAuth.ts
│   │   ├── useJobs.ts
│   │   └── useMatching.ts
│   │
│   ├── lib/                  # Utilidades
│   │   ├── api.ts            # Axios/Fetch wrapper
│   │   ├── auth.ts           # Auth utilities
│   │   └── utils.ts
│   │
│   ├── stores/               # Estado global (Zustand/Context)
│   │   └── authStore.ts
│   │
│   └── types/                # TypeScript types
│       └── index.ts
│
├── public/
├── package.json
├── tailwind.config.js
├── tsconfig.json
└── next.config.js
```

---

## 3. Stack Tecnológico

### 3.1 Backend

| Componente | Tecnología | Justificación |
|------------|------------|---------------|
| **Lenguaje** | Python 3.11+ o Go 1.21+ | Python tiene ecosistema rico para IA; Go para performance |
| **Framework** | FastAPI (Python) o Gin (Go) | FastAPI: async, automatic docs, type hints. Gin: rápido, simple |
| **ORM** | SQLAlchemy 2.0 o GORM | SQLAlchemy: maduro, flexible. GORM: Go estándar |
| **Base de datos** | PostgreSQL 15+ | Robusto, JSON support, full-text search |
| **Migration** | Alembic (Python) o golang-migrate | Gestión de schemas |
| **Auth** | python-jose / jwt-go | JWT con HS256/RS256 |
| **Password** | bcrypt o argon2 | Hash seguro |
| **Validation** | Pydantic | Validación de datos |
| **Scheduler** | APScheduler o Celery | Jobs periódicos (scraping) |
| **Caching** | Redis | Cache de queries, sesiones |

### 3.2 Modelos de IA

| Función | Modelo | Tamaño | Notas |
|---------|--------|--------|-------|
| **Embedding** | MiniLM-L6-v2 o E5-small-v2 | ~90MB | 384 dimensiones, CPU-friendly |
| **Generación (LLM)** | Qwen2.5-1.5B o Phi-3-mini-4k | ~3GB | Context 2048+, generación <10s |
| **Parsing CV** | modelo basado enNER oregex + LLM | - | Extraer entidades del CV |

### 3.3 Frontend

| Componente | Tecnología |
|------------|------------|
| **Framework** | Next.js 14 (App Router) o SvelteKit |
| **Lenguaje** | TypeScript |
| **UI** | Tailwind CSS + shadcn/ui o Radix |
| **Estado** | Zustand o React Context |
| **Forms** | React Hook Form + Zod |
| **HTTP** | Axios o Fetch |
| **Gráficos** | Recharts o Chart.js (dashboard) |

### 3.4 Scraping

| Herramienta | Uso |
|------------|-----|
| **Playwright** | Automatización del browser |
| **Selenium** | Alternativa a Playwright |
| **BeautifulSoup** | Parseo de HTML |

### 3.5 Infraestructura

| Servicio | Tecnología |
|----------|------------|
| **Container** | Docker |
| **Orchestración** | Docker Compose (dev) / Kubernetes (prod) |
| **CI/CD** | GitHub Actions |
| **Logging** | structured logging (json) + Elasticsearch/Kibana (opcional) |
| **Monitoring** | Prometheus + Grafana (opcional) |

---

## 4. Schema de Base de Datos

### 4.1 Diagrama ER (Entidades principales)

```
┌─────────────────┐       ┌─────────────────┐
│      user       │       │   user_profile  │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │──1:1──│ id (PK, FK)      │
│ email (unique)  │       │ full_name       │
│ password_hash   │       │ location        │
│ is_active       │       │ linkedin_url    │
│ is_verified     │       │ phone           │
│ created_at      │       │ summary         │
│ updated_at      │       │ seniority_level  │
└─────────────────┘       └─────────────────┘
        │
        │ 1:N
        ▼
┌─────────────────────────────────────────────┐
│              user_experience                 │
├─────────────────────────────────────────────┤
│ id (PK)                                      │
│ user_id (FK)                                 │
│ company                                      │
│ job_title                                    │
│ location                                     │
│ start_date                                   │
│ end_date (nullable - current job)           │
│ description                                  │
│ is_remote                                    │
└─────────────────────────────────────────────┘
         │
         │ 1:N
         ▼
┌─────────────────┐
│  user_education │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ institution     │
│ title           │
│ field_of_study │
│ start_date     │
│ end_date       │
│ description     │
└─────────────────┘

┌─────────────────┐
│  user_skill     │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ name            │
│ category        │  # enum: technical, soft, language
│ level (1-5)     │
└─────────────────┘

┌─────────────────┐
│ user_preferences│
├─────────────────┤
│ id (PK)         │
│ user_id (FK, unique) │
│ preferred_locations (json) │
│ salary_min      │
│ salary_max      │
│ contract_types (json) │  # full-time, part-time, contract
│ remote_preference │     # enum: remote, hybrid, onsite, any
│ seniority_target │
│ languages_needed (json) │
└─────────────────┘


┌─────────────────┐       ┌─────────────────┐
│   job_posting   │       │   cv_version    │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ url_original    │       │ user_id (FK)    │
│ title           │       │ version_number  │
│ company         │       │ parsed_data (json) │
│ location        │       │ original_file    │
│ description     │       │ created_at       │
│ requirements (json) │    │ is_active       │
│ benefits        │       └─────────────────┘
│ salary_min      │
│ salary_max      │
│ salary_currency │
│ contract_type   │
│ remote_option   │
│ posted_date     │
│ expires_at      │
│ scraped_at      │
│ scrape_status   │
│ url_hash        │  # para detección duplicados
│ content_hash    │
│ is_active       │
└─────────────────┘

        │
        │ 1:N
        ▼
┌─────────────────┐
│  match_result  │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ job_id (FK)     │
│ score_total     │
│ embeddings_score│
│ seniority_score │
│ location_score  │
│ salary_score    │
│ requirements_score│
│ classification  │  # enum: alta, media, baja
│ is_read         │
│ calculated_at   │
└─────────────────┘

        │
        │ 1:N
        ▼
┌─────────────────┐
│  application   │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ job_id (FK)     │
│ cover_letter_id │  # FK opcional
│ method          │  # enum: email, linkedin_bot
│ status          │  # enum: pending, sent, failed, rejected, interview
│ sent_at         │
│ response_at     │
│ notes           │
│ created_at      │
└─────────────────┘


┌─────────────────┐
│ cover_letter   │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ job_id (FK)     │
│ content         │
│ language        │
│ is_custom       │  # vs generado por IA
│ created_at      │
│ updated_at      │
└─────────────────┘


┌─────────────────┐
│   cv_template   │
├─────────────────┤
│ id (PK)         │
│ user_id (FK)    │
│ name            │
│ content         │  # plantilla base
│ is_default      │
│ created_at      │
└─────────────────┘
```

### 4.2 Tablas de Sistema

```sql
-- Tablas de auditoría
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    user_id (FK, nullable),
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id UUID,
    ip_address INET,
    user_agent TEXT,
    result VARCHAR(20) NOT NULL,  -- success, failure
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tablas de autenticación
CREATE TABLE refresh_token (
    id SERIAL PRIMARY KEY,
    user_id (FK) NOT NULL,
    token_hash VARCHAR(255) NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Tablas de jobs programados
CREATE TABLE scraping_job (
    id SERIAL PRIMARY KEY,
    status VARCHAR(20) NOT NULL,  -- pending, running, completed, failed
    started_at TIMESTAMP,
    finished_at TIMESTAMP,
    error_message TEXT,
    jobs_found INTEGER,
    jobs_new INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 4.3 Índices Suggested

```sql
-- Búsqueda de ofertas
CREATE INDEX idx_jobs_location ON job_posting(location);
CREATE INDEX idx_jobs_posted_date ON job_posting(posted_date DESC);
CREATE INDEX idx_jobs_scrape_status ON job_posting(scrape_status);
CREATE INDEX idx_jobs_company_title ON job_posting(company, title);

-- Matching
CREATE INDEX idx_matching_user_score ON match_result(user_id, score_total DESC);
CREATE INDEX idx_matching_job_user ON match_result(job_id, user_id);

-- Aplicaciones
CREATE INDEX idx_applications_user_status ON application(user_id, status);
CREATE INDEX idx_applications_sent_at ON application(sent_at DESC);

-- Búsqueda full-text (opcional)
CREATE INDEX idx_jobs_description_fts ON job_posting USING gin(to_tsvector('spanish', description));
```

---

## 5. API Endpoints

### 5.1 Autenticación

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/auth/register` | Registrar nuevo usuario |
| POST | `/api/v1/auth/login` | Login, retorna JWT |
| POST | `/api/v1/auth/refresh` | Refresh token |
| POST | `/api/v1/auth/verify-email` | Verificar email |
| POST | `/api/v1/auth/forgot-password` | Solicitar reseteo |
| POST | `/api/v1/auth/reset-password` | Nueva contraseña |
| POST | `/api/v1/auth/logout` | Invalida refresh token |

### 5.2 Perfil

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/profile` | Obtener perfil completo |
| PUT | `/api/v1/profile` | Actualizar perfil básico |
| GET | `/api/v1/profile/experiences` | Listar experiencias |
| POST | `/api/v1/profile/experiences` | Agregar experiencia |
| PUT | `/api/v1/profile/experiences/{id}` | Editar experiencia |
| DELETE | `/api/v1/profile/experiences/{id}` | Eliminar experiencia |
| GET | `/api/v1/profile/education` | Listar educación |
| POST | `/api/v1/profile/education` | Agregar educación |
| PUT | `/api/v1/profile/education/{id}` | Editar educación |
| DELETE | `/api/v1/profile/education/{id}` | Eliminar educación |
| GET | `/api/v1/profile/skills` | Listar habilidades |
| POST | `/api/v1/profile/skills` | Agregar habilidad |
| DELETE | `/api/v1/profile/skills/{id}` | Eliminar habilidad |
| GET | `/api/v1/profile/preferences` | Ver preferencias |
| PUT | `/api/v1/profile/preferences` | Actualizar preferencias |
| GET | `/api/v1/profile/seniority` | Obtener seniority calculado |

### 5.3 CV

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/cv/upload` | Subir archivo CV |
| GET | `/api/v1/cv/parsed` | Ver último CV parseado |
| PUT | `/api/v1/cv/parsed` | Editar CV parseado |
| POST | `/api/v1/cv/confirm` | Confirmar y guardar versión |
| GET | `/api/v1/cv/versions` | Listar historial de versiones |
| POST | `/api/v1/cv/versions/{id}/restore` | Restaurar versión |
| GET | `/api/v1/cv/templates` | Listar plantillas |
| POST | `/api/v1/cv/templates` | Crear plantilla |
| PUT | `/api/v1/cv/templates/{id}` | Editar plantilla |
| DELETE | `/api/v1/cv/templates/{id}` | Eliminar plantilla |

### 5.4 Ofertas (Jobs)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/jobs` | Listar ofertas (paginado) |
| GET | `/api/v1/jobs/search` | Buscar con filtros |
| GET | `/api/v1/jobs/{id}` | Ver detalles de oferta |
| POST | `/api/v1/jobs/scrape` |触发 scrape manual (admin) |
| GET | `/api/v1/jobs/{id}/match` | Ver match para mi perfil |

### 5.5 Matching

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/matching` | Listar matches (paginado) |
| GET | `/api/v1/matching/jobs/{job_id}` | Ver match específico |
| POST | `/api/v1/matching/recalculate` | Recalcular todos mis matches |
| GET | `/api/v1/matching/config` | Ver configuración de pesos |
| PUT | `/api/v1/matching/config` | Actualizar pesos |

### 5.6 Cover Letter

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| POST | `/api/v1/cover-letter/generate` | Generar carta para oferta |
| GET | `/api/v1/cover-letter/{job_id}` | Ver carta para oferta |
| PUT | `/api/v1/cover-letter/{job_id}` | Editar carta |
| GET | `/api/v1/cover-letter/templates` | Listar mis plantillas |
| POST | `/api/v1/cover-letter/templates` | Crear plantilla |

### 5.7 Aplicaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/applications` | Listar aplicaciones |
| GET | `/api/v1/applications/{id}` | Ver detalle |
| POST | `/api/v1/applications` | Aplicar (con confirmación) |
| POST | `/api/v1/applications/auto` | Aplicar automáticamente |
| DELETE | `/api/v1/applications/{id}` | Cancelar aplicación |
| POST | `/api/v1/applications/{id}/retry` | Reintentar si falló |

### 5.8 Dashboard

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/dashboard/stats` | Estadísticas generales |
| GET | `/api/v1/dashboard/trends` | Datos para gráfico de tendencias |

### 5.9 Notificaciones

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/notifications` | Listar notificaciones |
| PUT | `/api/v1/notifications/{id}/read` | Marcar como leída |
| GET | `/api/v1/notifications/settings` | Ver configuración |
| PUT | `/api/v1/notifications/settings` | Actualizar configuración |

---

## 6. Flujos de Desarrollo

### 6.1 Flujo de Registro y Setup

```
1. Usuario se registra → AUTH-001, AUTH-002
   POST /auth/register → create user (inactive)
   → send verification email

2. Usuario verifica email
   POST /auth/verify-email → set is_verified = true

3. Usuario inicia sesión
   POST /auth/login → validate credentials → return JWT

4. Usuario sube CV
   POST /cv/upload → save file → trigger parsing

5. IA parsea CV (async)
   cv_parser_service.extract() → extract entities

6. Usuario revisa y confirma
   PUT /cv/parsed → edit fields
   POST /cv/confirm → create version → update profile
```

### 6.2 Flujo de Scraping y Matching

```
1. Scheduler activa scraping (configurable: 1/6/12/24h)
   scraping_job.run()

2. LinkedInScraper.fetch_jobs(filters)
   → rate limiting (1 req/3s)
   → rotate user agents

3. Save jobs to DB
   job_repo.upsert() → detect duplicates via url_hash

4. Para cada job, calcular match
   matching_service.calculate(user_id, job_id)

5. Si score >= threshold, notificar usuario
   notification_service.send_alert()
```

### 6.3 Flujo de Aplicación

```
1. Usuario ve oferta matcheada
   GET /jobs/{id} → show job + match score

2. Usuario genera carta (opcional)
   POST /cover-letter/generate
   → llm_generator.generate(profile, job)

3. Usuario revisa y confirma
   POST /applications
   → validate (user has CV, profile complete)
   → show confirmation screen

4. Sistema envía aplicación
   if method == 'email':
       gmail_api.send_email()
   elif method == 'linkedin_bot':
       linkedin_bot.submit_form()

5. Guardar en historial
   application_repo.create()
```

---

## 7. Seguridad

### 7.1 Autenticación

```python
# JWT Token payload
{
    "sub": "user_id",
    "email": "user@example.com",
    "exp": "timestamp + 24h",
    "iat": "timestamp",
    "type": "access"  # vs "refresh"
}

# Password hashing
# Using bcrypt or argon2
hash = bcrypt.hash(password, rounds=12)
```

### 7.2 Protecciones

| Protección | Implementación |
|------------|----------------|
| **SQL Injection** | ORM (SQLAlchemy) + parameterization |
| **XSS** | Sanitize output en frontend |
| **CSRF** | JWT en httpOnly cookie o header |
| **Rate Limiting** | SlowAPI o middleware |
| **Input Validation** | Pydantic models + Zod |
| **Data Encryption** | AES-256 para datos sensibles en BD |
| **Password Storage** | bcrypt/argon2 (no plaintext) |

### 7.3 Permisos

```python
# Ejemplo: verificar que usuario solo acceda a sus datos
async def get_current_user(user_id: UUID = Depends(get_current_user_id)):
    user = await user_repo.get_by_id(user_id)
    if not user:
        raise HTTPException(404)
    return user

# En endpoints
@router.get("/profile", dependencies=[Depends(get_current_user)])
async def get_profile(user = Depends(get_current_user)):
    return user.profile
```

---

## 8. Modelos de IA - Integración

### 8.1 Embedding para Matching

```python
from sentence_transformers import SentenceTransformer

class EmbeddingService:
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
    
    def encode(self, text: str) -> list[float]:
        # Returns 384-dim vector
        return self.model.encode(text, normalize_embeddings=True)
    
    def calculate_similarity(self, text1: str, text2: str) -> float:
        # Cosine similarity
        emb1 = self.encode(text1)
        emb2 = self.encode(text2)
        return float(np.dot(emb1, emb2))
```

### 8.2 LLM para Cover Letter

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

class CoverLetterGenerator:
    def __init__(self, model_path: str = "./models/qwen2.5-1.5b"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForCausalLM.from_pretrained(model_path)
    
    def generate(self, profile: dict, job: dict, template: str = None) -> str:
        prompt = self._build_prompt(profile, job, template)
        inputs = self.tokenizer(prompt, return_tensors="pt", max_length=2048, truncation=True)
        
        outputs = self.model.generate(
            **inputs,
            max_new_tokens=400,
            temperature=0.7,
            do_sample=True
        )
        
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### 8.3 CV Parser

```python
class CVParserService:
    def parse(self, file_path: str) -> dict:
        # 1. Extract text from PDF/DOCX/TXT
        text = self._extract_text(file_path)
        
        # 2. Use LLM or regex patterns to extract entities
        parsed = self._extract_entities(text)
        
        return parsed
    
    def _extract_entities(self, text: str) -> dict:
        # Use LLM with prompting
        prompt = f"""
        Extract from this CV:
        - Full name
        - Email
        - Phone
        - Work experience (company, title, dates, description)
        - Education (institution, title, dates)
        - Skills (technical, soft, languages)
        
        CV text:
        {text}
        """
        # Call LLM to extract
        ...
```

---

## 9. Configuración y Variables de Entorno

```bash
# .env.example

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/linkedin_matcher

# Auth
SECRET_KEY=your-secret-key-min-32-chars
JWT_ALGORITHM=HS256
JWT_EXPIRATION_HOURS=24

# LinkedIn
LINKEDIN_SESSION_COOKIE=
LINKEDIN_USER_AGENT=

# Gmail API
GMAIL_CLIENT_ID=
GMAIL_CLIENT_SECRET=
GMAIL_REDIRECT_URI=http://localhost:3000/auth/gmail/callback

# AI Models
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
LLM_MODEL_PATH=./models/qwen2.5-1.5b

# Scraping
SCRAPER_RATE_LIMIT=3  # seconds between requests
SCRAPER_USER_AGENTS=["...", "..."]

# App
APP_HOST=0.0.0.0
APP_PORT=8000
DEBUG=true

# Optional: Redis
REDIS_URL=redis://localhost:6379
```

---

## 10. Testing

### 10.1 Estrategia

| Tipo | Cobertura objetivo | Herramientas |
|------|-------------------|--------------|
| **Unit** | Funciones individuales | pytest (Python) / testing package (Go) |
| **Integration** | APIs y DB | pytest + TestClient |
| **E2E** | Flujos completos | Playwright / Cypress |
| **Performance** | Load testing | k6 / Locust |

### 10.2 Ejemplo de Test (Python/FastAPI)

```python
# tests/test_matching.py
import pytest
from app.services.matching_service import MatchingService

@pytest.fixture
def matching_service():
    return MatchingService()

def test_calculate_match_with_perfect_seniority(matching_service):
    user = User(
        seniority="senior",
        experience_years=5
    )
    job = JobPosting(
        seniority_required="senior"
    )
    
    result = matching_service.calculate(user, job)
    
    assert result.seniority_score == 1.0  # 100%

def test_calculate_match_salary(matching_service):
    user = User(preferences=UserPreferences(salary_min=1000))
    job = JobPosting(salary_min=1500)
    
    result = matching_service.calculate(user, job)
    
    assert result.salary_score == 1.0

def test_calculate_match_requirements_not_met(matching_service):
    user = User(skills=["Python", "FastAPI"])
    job = JobPosting(requirements=["Python", "React", "AWS"])
    
    result = matching_service.calculate(user, job)
    
    assert result.requirements_score == 0.0
```

---

## 11. CI/CD (GitHub Actions)

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest --cov=app tests/
      - name: Lint
        run: ruff check app/

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker
        run: docker build -t linkedin-matcher:${{ github.sha }} .
```

---

## 12. Deployment

### 12.1 Desarrollo Local (Docker Compose)

```yaml
# docker-compose.yml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/linkedin_matcher
    depends_on:
      - db
      - redis

  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=linkedin_matcher
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"

volumes:
  postgres_data:
```

### 12.2 Producción (Kubernetes -概要)

- **Backend**: 3+ pods con HPA
- **PostgreSQL**: Managed service (RDS/Cloud SQL) o replica
- **Redis**: Managed service o cluster
- **Models**: PVC mount o object storage
- **Logs**: Stdout → cloud logging

---

## 13. Próximos Pasos para Iniciar

1. **Setup inicial**: Crear repositorio, configurar Docker, instalar dependencias
2. **DB Schema**: Crear migrations con Alembic
3. **Auth Module**: Registrar, login, JWT
4. **Profile Module**: CRUD de perfil, experiencias, skills
5. **CV Parser**: Integrar modelo de parsing
6. **Scraper**: LinkedIn client básico
7. **Matching**: Embedding service + cálculo de scores
8. **Cover Letter**: LLM integration
9. **Application**: Gmail API + LinkedIn bot
10. **Frontend**: Dashboard y flujos principales
11. **Testing**: Integrar tests en CI/CD

---

*Documento de análisis técnico orientado a desarrollo. Stack, arquitectura y estructura basadas en SPEC.md original.*
# 🚀 FastAPI Backend - Linked

Backend del proyecto **Linked** construido con **FastAPI** y **SQLite** (desarrollo).

---

## 📋 Requisitos Previos

- Python 3.10+
- pip / venv
- SQLite3 (incluido en Python)

---

## ⚙️ Setup Inicial

### 1. Clonar repositorio y navegar al backend

```bash
cd backend
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate  # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

```bash
cp .env.example .env
# Editar .env si es necesario (por defecto SQLite está configurado)
```

---

## 🎯 Ejecutar la Aplicación

### Opción 1: Directamente con Python

```bash
python -m app.main
```

Acceso: **http://localhost:8000**

### Opción 2: Con Uvicorn (recomendado)

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Documentación interactiva

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

---

## 📚 Endpoints Principales

### Authentication
```
POST   /api/v1/auth/register     - Registrar usuario
POST   /api/v1/auth/login        - Login y obtener tokens
POST   /api/v1/auth/refresh      - Refrescar access token
```

### Users (Requiere Bearer Token)
```
GET    /api/v1/users/me          - Obtener perfil actual
PUT    /api/v1/users/me          - Actualizar perfil
DELETE /api/v1/users/me          - Eliminar cuenta
```

### Jobs (Requiere Bearer Token)
```
POST   /api/v1/jobs              - Crear oferta
GET    /api/v1/jobs              - Listar ofertas
GET    /api/v1/jobs/{id}         - Obtener oferta
GET    /api/v1/jobs/saved        - Listar ofertas guardadas
PUT    /api/v1/jobs/{id}         - Actualizar oferta
DELETE /api/v1/jobs/{id}         - Eliminar oferta
```

### Applications (Requiere Bearer Token)
```
POST   /api/v1/applications      - Crear aplicación
GET    /api/v1/applications      - Listar aplicaciones
GET    /api/v1/applications/{id} - Obtener aplicación
GET    /api/v1/applications/status/{status}  - Filtrar por status
PUT    /api/v1/applications/{id} - Actualizar aplicación
DELETE /api/v1/applications/{id} - Eliminar aplicación
```

---

## 🧪 Testing

### Ejecutar tests

```bash
pytest tests/ -v
```

### Con coverage

```bash
pytest tests/ --cov=app --cov-report=html
```

### Tests específicos

```bash
pytest tests/unit/ -v
pytest tests/integration/ -v
```

---

## 🗄️ Base de Datos

### Ubicación de SQLite

```bash
# El archivo linked.db se crea automáticamente en:
./linked.db
```

### Ver datos en SQLite

```bash
sqlite3 linked.db
> .tables
> SELECT * FROM users;
```

### Limpiar BD (desarrollo)

```bash
rm linked.db
# La BD se recreará al iniciar la app
```

---

## 📝 Ejemplo de Uso (cURL)

### 1. Registrar usuario

```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "username123",
    "password": "SecurePassword123!",
    "full_name": "John Doe"
  }'
```

### 2. Login

```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePassword123!"
  }'

# Respuesta:
# {
#   "access_token": "eyJhbGc...",
#   "refresh_token": "eyJhbGc...",
#   "token_type": "bearer"
# }
```

### 3. Obtener perfil (con token)

```bash
curl -X GET http://localhost:8000/api/v1/users/me \
  -H "Authorization: Bearer <access_token>"
```

### 4. Crear oferta

```bash
curl -X POST http://localhost:8000/api/v1/jobs \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "linkedin_id": "job_123456",
    "title": "Senior Python Developer",
    "company": "Tech Corp",
    "location": "Remote",
    "description": "We are looking for...",
    "salary_min": 80000,
    "salary_max": 120000
  }'
```

---

## 🔑 JWT Tokens

- **Access Token**: Válido por 30 minutos (por defecto)
- **Refresh Token**: Válido por 7 días
- **Algoritmo**: HS256
- **Header**: `Authorization: Bearer <token>`

---

## ⚠️ Errores Comunes

### `ModuleNotFoundError: No module named 'app'`

Asegúrate de estar ejecutando desde el directorio `backend`:

```bash
cd backend
python -m app.main
```

### `OperationalError: unable to open database file`

Verifica que tengas permisos de escritura en el directorio:

```bash
chmod 755 .
```

### Conexión rechazada en puerto 8000

El puerto está en uso. Especifica otro:

```bash
uvicorn app.main:app --port 8001
```

---

## 📦 Estructura del Proyecto

```
backend/
├── app/
│   ├── api/v1/
│   │   ├── routes/         # Endpoints
│   │   └── dependencies.py # Auth & DI
│   ├── core/               # Config, security, exceptions
│   ├── models/             # SQLAlchemy models
│   ├── schemas/            # Pydantic schemas
│   ├── services/           # Business logic
│   ├── repositories/       # Data access
│   ├── database.py         # DB connection
│   └── main.py             # Entry point
├── tests/                  # Test suite
├── requirements.txt        # Dependencies
├── .env.example           # Environment template
└── README.md              # This file
```

---

## 🔄 Migración a PostgreSQL

Cuando pasemos a producción, consulta:  
**`../MIGRACION_SQLITE_A_POSTGRESQL.md`**

---

## 📖 Documentación

- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/
- **Pydantic**: https://docs.pydantic.dev/
- **JWT**: https://python-jose.readthedocs.io/

---

## 🤝 Contribuyendo

1. Crea una rama: `git checkout -b feature/nueva-feature`
2. Commit cambios: `git commit -am 'Add nueva feature'`
3. Push: `git push origin feature/nueva-feature`
4. PR a main

---

**Last updated:** Mayo 2026  
**Maintainers:** Mauro Banegas, Esteban Agüero

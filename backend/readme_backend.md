# Linked – Backend

Backend del proyecto **Linked**, compuesto por dos servicios Python independientes:

- **Django**: gestión de modelos, ORM, admin y lógica principal
- **FastAPI**: exposición de endpoints API para el frontend

Ambos servicios comparten el mismo entorno virtual y configuración.

---

## 📁 Estructura

```
backend/
├── api/                    # FastAPI
│   └── api.py
├── linked_django/          # Django
│   ├── core/
│   ├── linked_django/
│   └── manage.py
├── .venv/                  # Virtual environment
├── requirements.txt
├── .env
└── README.md
```

---

## Requisitos

- Python 3.10 o superior
- pip
- PostgreSQL (opcional en esta etapa)

---

## Configuración inicial

### 1️⃣ Crear y activar entorno virtual

```bash
cd backend
python -m venv .venv
source .venv/bin/activate     # Mac / Linux
# .venv\Scripts\activate      # Windows
```

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3️⃣ Variables de entorno

Crear archivo `.env` en la carpeta `backend/`:

```env
DEBUG=True
SECRET_KEY=change-me
DB_NAME=linked_db
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

Estas variables son utilizadas tanto por Django como por FastAPI.

---

## Levantar el backend

### Django

Desde la carpeta `backend/linked_django`:

```bash
python manage.py runserver
```

Por defecto Django se levanta en:

```
http://127.0.0.1:8000
```

**Cambiar puerto de Django**

```bash
python manage.py runserver 0.0.0.0:8010
```

Formato:

```bash
python manage.py runserver <host>:<puerto>
```

### FastAPI

Desde la carpeta `backend/api`:

```bash
uvicorn api:app --reload --port 8001
```

FastAPI queda disponible en:

```
http://127.0.0.1:8001
```

Documentación automática (Swagger):

```
http://127.0.0.1:8001/docs
```

**Cambiar puerto de FastAPI**

```bash
uvicorn api:app --reload --port 8011
```

---

## Puertos y convivencia de servicios

- Django y FastAPI son procesos distintos
- Cada uno debe usar un puerto diferente
- No existe conflicto mientras los puertos sean únicos

### Configuración recomendada en desarrollo

| Servicio | Puerto |
|----------|--------|
| Django   | 8000   |
| FastAPI  | 8001   |

### Alternativa (ejemplo)

| Servicio | Puerto |
|----------|--------|
| Django   | 8010   |
| FastAPI  | 8011   |

---

## Notas sobre arquitectura

- **Django se encarga de:**
  - Modelos
  - ORM
  - Admin
  - Autenticación

- **FastAPI se encarga de:**
  - Endpoints API
  - Comunicación con frontend

- **Ambos servicios:**
  - Comparten base de datos
  - Comparten `.env`
  - Comparten entorno virtual
# 📋 Especificación de Migración: SQLite → PostgreSQL

**Última actualización:** Mayo 2026  
**Estado:** Listo para cuando migremos a producción

---

## 1. Overview

Este documento especifica cómo migrar la base de datos del proyecto **Linked** de **SQLite (desarrollo)** a **PostgreSQL (producción)**.

---

## 2. Diferencias Clave: SQLite vs PostgreSQL

| Aspecto | SQLite | PostgreSQL |
|--------|--------|-----------|
| **Tipo** | Archivo embebido | Servidor remoto/local |
| **Conexiones** | Single thread | Multi-connection |
| **Tipos de datos** | Limitados | Extensos (UUID, JSONB, etc.) |
| **Foreign Keys** | Opcionales | Forzados |
| **Índices** | Básicos | Avanzados (B-tree, GiST, etc.) |
| **Transactions** | Simples | Full ACID |
| **Performance** | Dev/testing | Production |

---

## 3. Cambios Necesarios en el Código

### 3.1 Configuración (app/core/config.py)

**Actual (SQLite):**
```python
database_url: str = "sqlite:///./linked.db"
connect_args = {"check_same_thread": False}
```

**Después (PostgreSQL):**
```python
database_url: str = os.getenv(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/linked"
)
connect_args = {}  # Remove SQLite-specific args
```

### 3.2 Connection Pool (app/database.py)

**Agregar:**
```python
from sqlalchemy.pool import NullPool  # Para prod sin pooling
# O usar QueuePool (default)

if "postgresql" in settings.database_url:
    engine = create_engine(
        settings.database_url,
        echo=settings.echo_sql,
        pool_size=10,
        max_overflow=20,
        pool_recycle=3600,  # Recycle connections every hour
    )
else:
    # SQLite
    engine = create_engine(
        settings.database_url,
        echo=settings.echo_sql,
        connect_args={"check_same_thread": False},
    )
```

### 3.3 Migraciones Alembic

**Generar script de migración inicial:**
```bash
cd backend
alembic init migrations
alembic revision --autogenerate -m "Initial schema for PostgreSQL"
alembic upgrade head
```

---

## 4. Pasos de Migración (Paso a Paso)

### Paso 1: Preparar PostgreSQL
```bash
# En el servidor PostgreSQL
createdb linked
createuser linked_user
psql -c "ALTER USER linked_user WITH PASSWORD 'secure_password';"
psql -c "GRANT ALL PRIVILEGES ON DATABASE linked TO linked_user;"
```

### Paso 2: Exportar datos desde SQLite
```bash
# Usar herramienta de migración
sqlite3 linked.db .mode INSERT | pg_restore

# O usar un script Python personalizado
python scripts/migrate_sqlite_to_postgres.py
```

### Paso 3: Actualizar .env
```bash
# Cambiar DATABASE_URL
DATABASE_URL=postgresql://linked_user:secure_password@localhost:5432/linked
```

### Paso 4: Ejecutar migraciones Alembic
```bash
alembic upgrade head
```

### Paso 5: Validar integridad
```bash
# Contar registros en ambas BDs
sqlite3 linked.db "SELECT COUNT(*) FROM users;"
psql -U linked_user -d linked -c "SELECT COUNT(*) FROM users;"
```

### Paso 6: Deploy a producción
- Actualizar en .env de producción
- Reiniciar Uvicorn
- Monitorear logs

---

## 5. Script de Migración Python

**Archivo: `backend/scripts/migrate_sqlite_to_postgres.py`**

```python
"""SQLite to PostgreSQL migration script."""

import os
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from app.models.base import Base
from app.models.user import User
from app.models.job import Job
from app.models.application import Application

# Conexiones
sqlite_engine = create_engine("sqlite:///./linked.db")
postgres_url = os.getenv("DATABASE_URL")

if not postgres_url:
    raise ValueError("DATABASE_URL not set. Check .env")

postgres_engine = create_engine(postgres_url)

# Crear tablas en PostgreSQL
Base.metadata.create_all(bind=postgres_engine)

# Copiar datos
SQLiteSession = sessionmaker(bind=sqlite_engine)
PostgresSession = sessionmaker(bind=postgres_engine)

sqlite_session = SQLiteSession()
postgres_session = PostgresSession()

# Copiar users
print("Migrando users...")
users = sqlite_session.query(User).all()
for user in users:
    postgres_session.add(user)
postgres_session.commit()

# Copiar jobs
print("Migrando jobs...")
jobs = sqlite_session.query(Job).all()
for job in jobs:
    postgres_session.add(job)
postgres_session.commit()

# Copiar applications
print("Migrando applications...")
apps = sqlite_session.query(Application).all()
for app in apps:
    postgres_session.add(app)
postgres_session.commit()

print("✅ Migración completada")
```

---

## 6. Consideraciones de Tipos de Datos

### Cambios Recomendados para PostgreSQL

```python
# models/user.py
from sqlalchemy import UUID
import uuid

class User(BaseModel):
    # Cambiar de Integer a UUID
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Cambiar de String a tipos nativos PostgreSQL
    email = Column(String(255), unique=True, nullable=False)  # OK
    
    # Agregar índices más específicos
    __table_args__ = (
        Index("idx_users_email", "email", unique=True),
        Index("idx_users_username", "username", unique=True),
    )
```

---

## 7. Performance Optimization (PostgreSQL)

### Índices Recomendados
```sql
-- Para búsquedas comunes
CREATE INDEX idx_applications_user_status 
ON applications(user_id, status);

CREATE INDEX idx_jobs_company 
ON jobs(company);

CREATE INDEX idx_jobs_created_at 
ON jobs(created_at DESC);

-- Para full-text search (futuro)
CREATE INDEX idx_jobs_description_fts 
ON jobs USING gin(to_tsvector('english', description));
```

### Connection Pooling
```python
# app/database.py - Para producción
engine = create_engine(
    settings.database_url,
    pool_size=20,              # Conexiones en el pool
    max_overflow=40,           # Conexiones adicionales temporales
    pool_pre_ping=True,        # Verificar conexiones antes de usar
    pool_recycle=3600,         # Reciclar cada hora
    echo=False,                # No loguear SQL en producción
)
```

---

## 8. Variables de Entorno

### Desarrollo (SQLite)
```bash
DATABASE_URL=sqlite:///./linked.db
ECHO_SQL=True
DEBUG=True
```

### Producción (PostgreSQL)
```bash
DATABASE_URL=postgresql://linked_user:PASSWORD@db.example.com:5432/linked
ECHO_SQL=False
DEBUG=False
```

---

## 9. Testing Post-Migración

```bash
# Verificar conexión
psql -U linked_user -d linked -c "SELECT COUNT(*) FROM users;"

# Verificar integridad de ForeignKeys
psql -U linked_user -d linked << EOF
SELECT COUNT(*) FROM jobs WHERE user_id NOT IN (SELECT id FROM users);
SELECT COUNT(*) FROM applications WHERE user_id NOT IN (SELECT id FROM users);
SELECT COUNT(*) FROM applications WHERE job_id NOT IN (SELECT id FROM jobs);
EOF

# Esperar resultados 0 en todas
```

---

## 10. Rollback Plan

Si algo falla en producción:

1. **Revertir DNS** a servidor antiguo
2. **Ejecutar:**
   ```bash
   alembic downgrade -1  # O el número de revisión
   ```
3. **Restaurar desde backup** de SQLite
4. **Notificar al equipo**

---

## 11. Timeline Estimado

| Fase | Duración | Notas |
|------|----------|-------|
| Preparar PostgreSQL | 30 min | Setup DB + usuario |
| Exportar datos | 10 min | Depende del volumen |
| Ejecutar script migración | 5 min | Validar sin errores |
| Testing | 15 min | Verificar integridad |
| Deploy a prod | 5 min | Actualizar .env + restart |
| **Total** | **~1 hora** | **En ventana de mantenimiento** |

---

## 12. Checklist Pre-Migración

- [ ] Backup de SQLite (`linked.db`)
- [ ] Backup de PostgreSQL (si migrar otro DB)
- [ ] Actualizar `app/core/config.py`
- [ ] Actualizar `app/database.py` con pool config
- [ ] Ejecutar script de migración en staging primero
- [ ] Testing completo en staging
- [ ] Validar indices se crearon
- [ ] Notificar al equipo
- [ ] Preparar rollback plan
- [ ] Ejecutar en ventana de mantenimiento

---

**Documentación generada:** Mayo 2026  
**Próxima revisión:** Cuando pasemos a Producción

# 🧩 Git Workflow (Git Flow)

Este proyecto utiliza Git Flow como modelo de ramificación para mantener un flujo de trabajo ordenado y consistente entre todo el equipo.

## 🌿 Ramas principales

**`master`**
- Contiene código estable y listo para producción.

**`develop`**
- Rama principal de desarrollo.
- Todas las features se integran aquí antes de llegar a master.

⚠️ **Nunca se pushea directo a `master` ni a `develop`. Todo entra por Pull Request.**

## 🚀 Inicialización de Git Flow (una sola vez por desarrollador)

Si no tenés Git Flow instalado:

```bash
# macOS
brew install git-flow

# Ubuntu / Debian
sudo apt install git-flow
```

Luego, desde la raíz del repositorio:

```bash
git flow init
```

Aceptar los valores por defecto:
- `master` como rama de producción
- `develop` como rama de desarrollo

## 🛠️ Cómo trabajar una tarea (feature)

Supongamos una tarea de Jira:

**LINKED-12 Inicializar backend**

### 1️⃣ Crear la feature

```bash
git flow feature start LINKED-12-init-backend
```

Esto:
- Parte desde `develop`
- Crea `feature/LINKED-12-init-backend`
- Te deja posicionado en esa rama

### 2️⃣ Desarrollar normalmente

Trabajá y hacé commits como siempre.

📌 **Regla importante:**  
Los commits deben incluir el ID de Jira.

```bash
git add .
git commit -m "LINKED-12 initialize backend structure"
```

### 3️⃣ Subir la rama a GitHub

```bash
git push -u origin feature/LINKED-12-init-backend
```

### 4️⃣ Crear Pull Request

En GitHub:
- **Base branch:** `develop`
- **Compare:** `feature/LINKED-12-init-backend`

**Título del PR:**
```
LINKED-12 Initialize backend
```

Una vez aprobado, se mergea a `develop`.

## 🧹 Cierre de la feature

### Opción recomendada (equipo)

1. El PR se mergea desde GitHub
2. Se elimina la rama remota desde GitHub
3. En local:

```bash
git checkout develop
git pull
git branch -d feature/LINKED-12-init-backend
```

### Opción alternativa (Git Flow)

```bash
git flow feature finish LINKED-12-init-backend
git push origin develop
git push origin --delete feature/LINKED-12-init-backend
```

⚠️ **Usar esta opción solo si todos entienden bien el flujo.**

## 📦 Releases (develop → master)

Cuando `develop` está estable y listo para producción:

```bash
git flow release start 1.0.0
```

Finalizar release:

```bash
git flow release finish 1.0.0
git push origin develop
git push origin master --tags
```

Esto:
- Mergea a `master`
- Mergea de vuelta a `develop`
- Crea un tag de versión

## 🐞 Hotfix (errores en producción)

```bash
git flow hotfix start 1.0.1
```

Luego:

```bash
git flow hotfix finish 1.0.1
git push origin master develop --tags
```

## 📌 Convenciones obligatorias

### Ramas
```
feature/LINKED-<ID>-descripcion-corta
```

### Commits
```
LINKED-<ID> short description
```

### Pull Requests
```
LINKED-<ID> Short description
```

👉 **Esto permite que Jira detecte automáticamente commits, ramas y PRs.**

## ✅ Resumen rápido

- Todo el desarrollo va en `feature/*`
- Todo PR apunta a `develop`
- `master` solo recibe releases
- Git Flow se usa para crear y cerrar ramas
- GitHub se usa para PRs y reviews
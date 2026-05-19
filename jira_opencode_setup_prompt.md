# 🔧 Prompt Automático: Conectar Jira MCP a OpenCode

## **Opción 1: REMOTA (Atlassian Oficial) - Recomendado**

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "jira": {
      "type": "remote",
      "url": "https://mcp.atlassian.com/v1/sse",
      "enabled": true,
      "oauth": {}
    }
  }
}
```

**Pasos:**
1. Abre tu `~/.config/opencode/opencode.json`
2. Copia la sección `mcp` arriba en tu archivo
3. Guarda el archivo
4. Ejecuta en terminal:
   ```bash
   opencode mcp auth jira
   ```
5. Se abrirá una ventana del navegador para autenticarte con Atlassian
6. ¡Listo! Jira MCP está conectado automáticamente

---

## **Opción 2: LOCAL (Más Avanzado - Sin OAuth)**

Si prefieres tener control total y usar API tokens:

### Paso 1: Obtener credenciales de Jira
1. Ve a https://id.atlassian.com/manage-profile/security/api-tokens
2. Crea un nuevo API Token
3. Cópialo (lo necesitarás)

### Paso 2: Crear archivo de configuración Jira

Crea `~/.jira-config.json`:

```json
{
  "host": "https://tu-dominio.atlassian.net",
  "email": "tu-email@ejemplo.com",
  "apiToken": "tu-api-token-aqui"
}
```

**Alternativa con variable de entorno:**
```bash
export JIRA_HOST="https://tu-dominio.atlassian.net"
export JIRA_EMAIL="tu-email@ejemplo.com"
export JIRA_API_TOKEN="tu-token"
```

### Paso 3: Configurar OpenCode

Edita `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "jira": {
      "type": "local",
      "command": ["npx", "-y", "mcp-jira"],
      "enabled": true,
      "environment": {
        "JIRA_CONFIG_PATH": "~/.jira-config.json"
      }
    }
  }
}
```

### Paso 4: Reinicia OpenCode

```bash
opencode
```

---

## **Opción 3: COMPOSIO (1000+ Integraciones)**

Si quieres Jira + muchas otras herramientas en un solo endpoint:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "composio": {
      "type": "remote",
      "url": "https://connect.composio.dev/mcp",
      "enabled": true
    }
  }
}
```

**Pasos:**
1. Copia la config arriba
2. Guarda en `~/.config/opencode/opencode.json`
3. En OpenCode, pide: `"Conecta mi cuenta de Jira usando Composio"`
4. Se abrirá un prompt de autenticación OAuth
5. Autentifícate
6. ¡Listo! Tendrás acceso a Jira + Gmail + Slack + 1000+ apps

---

## **Verificar que Funciona**

```bash
# Ver MCPs configurados
opencode /mcps

# Ver estado de cada MCP
opencode mcp debug jira
```

**En OpenCode, prueba con:**
```
Usa Jira MCP para mostrarme mis issues asignados
```

---

## **Troubleshooting Rápido**

| Problema | Solución |
|----------|----------|
| `Command not found: opencode` | Instala: `npm install -g opencode` |
| `JSON syntax error` | Valida JSON: `cat ~/.config/opencode/opencode.json \| python3 -m json.tool` |
| `No OAuth-enabled MCP servers` | Asegúrate de tener `"oauth": {}` en la config remota |
| `Permission denied` | Permisos: `chmod 644 ~/.config/opencode/opencode.json` |
| `MCP no aparece en /mcps` | Reinicia OpenCode: `pkill opencode && opencode` |

---

## **¿Cuál elegir?**

- **Opción 1 (REMOTA)**: Si quieres lo más simple y oficial. ✅ Recomendado
- **Opción 2 (LOCAL)**: Si necesitas control total o trabajas offline
- **Opción 3 (COMPOSIO)**: Si necesitas múltiples integraciones además de Jira

---

## **Mi Recomendación**

Comienza con **Opción 1**. Es la más rápida, segura (OAuth oficial) y mantenida por Atlassian.

Solo tienes que:
1. Copiar 9 líneas de JSON
2. Ejecutar 1 comando
3. Autenticarte en el navegador

**¡Nada más!** 🚀

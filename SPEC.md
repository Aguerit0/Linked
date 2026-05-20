# Sistema de Requisitos: LinkedIn Job Matcher

## Historial de Versiones

| Versión | Fecha | Descripción | Autor |
|--------|-------|------------|-------|
| 1.0.0 | 2026-05-05 | Versión inicial del documento de requisitos | Equipo de Desarrollo |

## 1. Introducción y Visión del Sistema

### 1.1 Propósito del Documento

Este documento establece los requisitos completos y detallados para el sistema **LinkedIn Job Matcher**, una plataforma de automatización para la búsqueda y postulación a empleos en LinkedIn. El documento está dirigido al equipo de desarrollo, stakeholders técnicos y cualquier persona involucrada en la validación, implementación o mantenimiento del sistema. Sirve como contrato formal entre las expectativas del negocio y la implementación técnica, proporcionando una referencia autoritativa para decisiones de diseño y criterios de aceptación.

### 1.2 Alcance del Sistema

LinkedIn Job Matcher es una plataforma integrada que automatiza el proceso completo de búsqueda de empleo en LinkedIn, desde la carga del perfil profesional del usuario hasta la postulación automática a ofertas laborales. El sistema comprende cinco funcionalidades principales: gestión de perfiles de usuario con parsing de CV, scraping de ofertas laborales desde LinkedIn, motor de matching inteligente basado en embeddings y modelos de IA locales, generación automática de cartas de presentación personalizadas, y aplicación automática vía correo electrónico o bot.

El sistema está diseñado para operar completamente en infraestructura local, sin dependencias de servicios cloud externos más allá de la conexión a internet para acceder a LinkedIn y enviar correos electrónicos. Esta decisión arquitectónica garantiza la privacidad de los datos del usuario y reduce los costos operativos recurrentes.

### 1.3 Definiciones, Acrónimos y Abreviaturas

| Término | Definición |
|---------|-----------|
| CV | Currículum Vitae, documento que describe la experiencia profesional y habilidades del candidato |
| Embedding | Representación vectorial densa de texto que captura significado semántico |
| Scraping | Técnica de extracción automática de datos de páginas web |
| Matching | Proceso de emparejamiento entre perfil de candidato y ofertas de empleo |
| Seniority | Nivel de experiencia profesional (junior, semi-senior, senior, lead, principal) |
| JWT | JSON Web Token, estándar para autenticación stateless |
| RAG | Retrieval-Augmented Generation, arquitectura de IA que combina recuperación con generación |
| DDD | Domain-Driven Design, metodología de diseño de software orientada al dominio |

---

## 2. Requisitos de Negocio

### 2.1 Registro y Gestión de Usuarios

El sistema debe permitir el registro de nuevos usuarios mediante correo electrónico y contraseña segura. Cada usuario gestiona un único perfil profesional que contiene su información personal, experiencia laboral, educación, habilidades técnicas y no técnicas, idiomas, y preferencias laborales. El sistema debe almacenar esta información de forma segura y permitir su edición en cualquier momento posterior al registro inicial.

La gestión de usuarios incluye funcionalidades de recuperación de contraseña mediante enlace por correo electrónico, cambio de contraseña periódica recomendada, y eliminación de cuenta con eliminación asociada de todos los datos personales. El sistema debe cumplir con las normativas aplicables de protección de datos personales, garantizando el derecho a la eliminación completa de información.

### 2.2 Carga y Parsing de Currículum Vitae

El sistema debe permitir la carga de documentos de CV en formatosPDF, DOCX, y TXT. Upon successful upload, el sistema extrae automáticamente la información relevante utilizando modelos de IA locales para parsing de documentos. La información extraída incluye nombre completo, resumen profesional, experiencia laboral con fechas y responsabilidades, educación con títulos y fechas, habilidades técnicas categorizadas, habilidades blandas, e idiomas con nivel de proficiencia estimado.

El usuario debe poder revisar y editar la información extraída antes de confirmar su perfil. El sistema debe mantener un historial de versiones del CV parseado, permitiendo restaurar versiones anteriores si el usuario detecta errores en la extracción automática. El parsing debe manejar CVs en español e inglés como mínimo, con capacidad de extensión para otros idiomas.

### 2.3 Búsqueda y Scraping de Ofertas Laborales

El sistema debe permitir la búsqueda de ofertas laborales en LinkedIn utilizando criterios diversos: posición laboral, ubicación geográfica, rango salarial, tipo de contrato (remoto, híbrido, presencial), nivel de seniority, y fecha de publicación. Los resultados deben mostrarse de forma paginada con información resumida de cada oferta.

El scraping debe ejecutarse de forma periódica y configurable para mantener actualizada la base de datos de ofertas. El sistema debe manejar las limitaciones de la API de LinkedIn y las políticas de scraping responsable, implementando tiempos de espera apropiados entre solicitudes y rotando User Agents cuando sea necesario. Las ofertas scraped deben almacenarse con metadatos completos incluyendo URL original, fecha de scrapeo, y fecha de vencimiento estimada.

### 2.4 Matcheo Inteligente Perfil-Oferta

El sistema debe implementar un algoritmo de matching que evalúe la compatibilidad entre el perfil de un candidato y cada oferta laboral disponible. El matching utiliza embeddings vectoriales para representar semánticamente el perfil del usuario y las descripciones de las ofertas, calculando similitud coseno entre ambos vectores. Adicionalmente, el sistema debe considerar criterios explícitos como seniority requerido versus actual, ubicación geográfica, rango salarial, y requisitos técnicos obligatorios.

El resultado del matching debe incluir una puntuación numerica de compatibilidad, un desglose de los factores que contribuyen a la puntuación, y una clasificación categórica (alta, media, baja compatibilidad). El usuario debe poder configurar umbrales mínimos de compatibilidad y filtros adicionales para refinar los resultados mostrados.

### 2.5 Generación Automática de Cartas de Presentación

Para cada oferta con alta compatibilidad, el sistema debe generar automáticamente una carta de presentación personalizada. La generación utiliza un modelo de lenguaje local que combina la información del perfil del usuario con los requisitos específicos de la oferta, produciendo una carta profesional y gramáticamente correcta. La carta debe seguir estructuras reconocidas de carta de presentación: saludo, introducción, párrafos de desarrollo highlights relevantes, y cierre con llamada a la acción.

El usuario debe poder revisar y editar la carta generada antes de la postulación. El sistema debe mantener plantillas de carta personalizables que el usuario puede modificar según sus preferencias. La generación debe producir cartas en el idioma de la oferta objetivo.

### 2.6 Aplicación Automática

El sistema debe permitir la postulación automática a ofertas laborales matcheadas. La postulación incluye el envío del CV del candidato, la carta de presentación personalizada, y cualquier formulario requerido por LinkedIn. El sistema debe soportar dos modalidades de postulación: mediante integración con Gmail API para enviar solicitudes por correo electrónico al reclutador, y mediante bot automatizado que completa formularios en LinkedIn.

El sistema debe registrar el historial completo de aplicaciones realizadas, incluyendo fecha, oferta, estado de la aplicación, y cualquier respuesta recibida. El usuario debe poder configurar preferencias de postulación automática, incluyendo confirmación manual antes de cada postulación versus postulación completamente automática sin intervención.

### 2.7 Dashboard y Notificaciones

El sistema debe proporcionar un dashboard que muestre estadísticas relevantes: número de ofertas matcheadas, número de aplicaciones enviadas, tasa de respuesta estimada, y gráfico de tendencias temporales. El dashboard debe ser personalizable para mostrar métricas específicas感兴趣的 por cada usuario.

Las notificaciones deben enviarse por correo electrónico y dentro de la aplicación cuando ocurran eventos importantes: nuevas ofertas altamente matcheadas, actualizaciones en el estado de aplicaciones previas, y alertas de-configuración del sistema. El usuario debe poder configurar sus preferencias de notificación, incluyendo frecuencia y tipos de notificaciones deseadas.

---

## 3. Requisitos Funcionales

Los siguientes requisitos utilizan las palabras clave definidas en RFC 2119 para indicar niveles obligatorios de cumplimiento:

### 3.1 Gestión de Autenticación

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| AUTH-001 | MUST | El sistema debe permitirRegistro de nuevos usuarios con correo electrónico y contraseña | El formulario de registro acepta email válidoy contraseña de al menos 8 caracteres con combinación de letras, números y símbolos. La cuenta se crea exitosamente y el usuario recibe correo de verificación. |
| AUTH-002 | MUST | El sistema debe verificar el correo electrónico del usuario | El usuario recibe un correo con enlace de verificación al registrase. Hasta verificar el correo, el usuario no puede acceder a funcionalidades privadas. |
| AUTH-003 | MUST | El sistema debe permitir inicio de sesión con credenciales correctas | Ingresando email y contraseña válidos, el usuario accede a su cuenta en menos de 3 segundos. Credenciales incorrectas muestran mensaje de error apropiado. |
| AUTH-004 | MUST | El sistema debe implementar autenticación stateless con JWT | Cada request autenticado incluye token JWT válido en header Authorization. Los tokens expiran después de 24 horas y requieren renovación. |
| AUTH-005 | SHOULD | El sistema debe permitir recuperación de contraseña | El usuario puede solicitar reseteo de contraseña recibirá un correo con enlace válido por 1 hora. Cambiar contraseña correctamente actualiza la cuenta. |
| AUTH-006 | MAY | El sistema debe soportar autenticación de dos factores (2FA) | El usuario puede habilitar 2FA con Google Authenticator o similar. El login requiere código adicional además de contraseña. |

### 3.2 Gestión de Perfiles de Usuario

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| PROFILE-001 | MUST | El sistema debe permitir crear y editar perfil profesional | El formulario de perfil permite ingresar: nombre completo, ubicación,-linkedIn URL, resumen profesional (máx 500 palabras), y información de contacto adicional. Los datos se guardan y muestran correctamente. |
| PROFILE-002 | MUST | El sistema debe gestionar experiencia laboral | El usuario puede agregar, editar y eliminar experiencias laborales con: empresa, cargo, fecha inicio, fecha fin (o presente), descripción, y ubicación. Las experiencias se ordenan cronológicamente inversamente. |
| PROFILE-003 | MUST | El sistema debe gestionar educación | El usuario puede agregar, editar y eliminar entradas de educación con: institución, título, campo de estudio, fecha inicio, fecha fin, y descripción. |
| PROFILE-004 | MUST | El sistema debe gestionar habilidades | El usuario puede agregar y eliminar habilidades categorizadas como técnicas, blandas, e idiomas. Cada habilidad tiene nombre y nivel de proficiencia estimado (1-5). |
| PROFILE-005 | MUST | El sistema debe gestionar preferencias laborales | El usuario puede configurar: ubicaciones deseadas, rango salarial mínimo y máximo, tipos de contrato preferidos, y remote preference (remoto/híbrido/presencial). |
| PROFILE-006 | SHOULD | El sistema debe calcular automáticamente el seniority del usuario | Analizando experiencia laboral y educación, el sistema sugiere nivel de seniority actual (junior/semi-senior/senior/lead/principal). El usuario puede aceptar o modificar la sugerencia. |

### 3.3 Parsing de Currículum Vitae

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| CV-001 | MUST | El sistema debe aceptar carga de archivos PDF, DOCX, y TXT | El usuario puede subir archivos de hasta 10MB en estos formatos. Archivos mayores o de otros formatos muestran mensaje de error apropiado. |
| CV-002 | MUST | El sistema debe extraer información automaticamente del CV carregado | Utilizando IA local, el sistema extrae: nombre, email, teléfono, experiencia laboral (empresa, cargo, fechas), educación (institución, título, fechas), habilidades, e idiomas. |
| CV-003 | MUST | El sistema debe permitir revisar y editar información extraída | Después del parsing, el usuario ve la información extraída en formularios editables. Puede modificar cualquier campo antes de confirmar. |
| CV-004 | MUST | El sistema debe guardar versiones del CV | Cada vez que el usuario confirma un CV parseado, se crea una nueva versión. El usuario puede ver historial y restaurar versiones anteriores. |
| CV-005 | SHOULD | El sistema debe manejar CVs con formato no estándar | Si el parsing falla parcialmente, el sistema indica qué campos no pudieron extraerse y permite entrada manual. |
| CV-006 | SHOULD | El sistema debe detectar incoherencias en el CV | Si el CV contiene información inconsistente (fechas que no cuadran, cargos decrecientes sin explicación), el sistema warns el usuario. |

### 3.4 Scraping de Ofertas Laborales

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| SCRAPE-001 | MUST | El sistema debe buscar ofertas por criterios múltiples | El usuario puede buscar por: keywords, ubicación, salary range, tipo de contrato, seniority, y fecha de publicación. Los resultados reflejan los filtros aplicados. |
| SCRAPE-002 | MUST | El sistema debe mostrar resultados de forma paginada | Los resultados muestran 20 ofertas por página con navegación. La paginación carga más resultados sin refresh completo. |
| SCRAPE-003 | MUST | El sistema debe almacenar ofertas scrapeadas con metadatos completos | Cada oferta almacenada incluye: título, empresa, ubicación, descripción completa, requisitos, salary range (si disponible), fecha de publicación, URL original, y fecha de scrapeo. |
| SCRAPE-004 | MUST | El sistema debe actualizar ofertas periódicamente | Un job scheduler ejecuta scraping configurable (cada 1/6/12/24 horas). Las ofertas nuevas se agregan, las existentes se actualizan si hay cambios. |
| SCRAPE-005 | SHOULD | El sistema debe manejar rate limiting de LinkedIn | Si LinkedIn responde con HTTP 429, el sistema espera el tiempo indicado y reintenta automáticamente. Registra intentos fallidos. |
| SCRAPE-006 | SHOULD | El sistema debe detectar ofertas duplicadas | Si la misma oferta ya existe en DB (misma URL o mismo título+empresa+ubicación), se marca como duplicada y no se crea nueva entrada. |

### 3.5 Motor de Matching

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| MATCH-001 | MUST | El sistema debe calcular compatibilidad mediante embeddings | Cada perfil y oferta se convierten a vectores embedding usando modelo local (MiniLM/E5). La similitud coseno entre vectores produce puntuación base 0-100. |
| MATCH-002 | MUST | El sistema debe considerar criterios explícitos en el matching | Além de embeddings, el matching considera: seniority match (100% si coincide, 50% si uno nivel de diferencia), ubicación (100% si coincide, 0% si no), salary (100% si oferta ≥ mínimo usuario), y requisitos técnicos (0% si no cumple requerimiento obligatorio). |
| MATCH-003 | MUST | El sistema debe mostrar resultado con desglose | Cada matchee结果显示: puntuación total (0-100), desglose por factor (embeddings 40%, seniority 20%, ubicación 15%, salary 15%, requisitos 10%), y clasificación (alta ≥75, media 50-74, baja <50). |
| MATCH-004 | MUST | El sistema debe aplicar filtros configurables | El usuario puede filtrar resultados por: puntuación mínima, clasificación, ubicación, salary mínimo, y tipo de contrato. |
| MATCH-005 | SHOULD | El sistema debe explicar por qué no hay match alto | Si una oferta tiene puntuación baja, el sistema indica los factores negativos: "No cumples requisitos técnicos: Python, React", "Ubicación no coincide: OFF" (offline significa "no remote"). |
| MATCH-006 | SHOULD | El sistema debe re-calcular matches al actualizar perfil | Cada vez que el usuario guarda cambios en su perfil, los scores de matchee se recalculan automáticamente. |

### 3.6 Generación de Cartas de Presentación

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| COVER-001 | MUST | El sistema debe generar carta personalizada para cada oferta | Utilizando LLM local, la carta incorpora: nombre del reclutador (si disponible), empresa, cargo específico, y referencias aquisitos relevantes de la oferta que coincidan con experiencia del usuario. |
| COVER-002 | MUST | El sistema debe seguir estructura profesional de carta | La carta incluye: saludo formal ("Estimado/a [Nombre]"), introducción (por qué le interesa el cargo), desarrollo (2-3 párrafos highlights relevantes), y cierre (agradecimiento y disposición a entrevistar). Longitud: 250-400 palabras. |
| COVER-003 | MUST | El sistema debe permitir editar antes de enviar | Después de generar, el usuario puede modificar cualquier parte de la carta. Los cambios se guardan por oferta. |
| COVER-004 | MUST | El sistema debe mantener múltiples plantillas | El usuario puede crear y guardar múltiples plantillas de carta. Al generar, puede elegir qué plantilla usar como base. |
| COVER-005 | SHOULD | El sistema debe detectar el idioma de la oferta | La carta se genera en el mismo idioma de la descripción de la oferta. Si la oferta está en inglés, la carta se genera en inglés. |
| COVER-006 | MAY | El sistema debe sugerir mejoras en la carta | Después de generar, el sistema sugiere: partes que podrían加强了, palabras de transición que podrían agregarse, y longitud recomendada. |

### 3.7 Aplicación Automática

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| APPLY-001 | MUST | El sistema debe aplicar via email (Gmail API) | El usuario configura credenciales Gmail OAuth, el sistema envía email con CV adjunto y carta al endereço de reclutador cuando esté disponible. |
| APPLY-002 | MUST | El sistema debe aplicar via LinkedIn Bot | Para ofertas que permiten Easy Apply o tienen formulario, el sistema automatiza el filling del formulario con datos del perfil y adjunta CV. |
| APPLY-003 | MUST | El sistema debe registrar historial de aplicaciones | Cada aplicación se registra con: oferta, fecha/hora, método (email/bot), carta utilizada, y estado (enviada/fallida/pending). |
| APPLY-004 | SHOULD | El sistema debe ofrecer postulación con confirmación | Modo "confirmar antes de aplicar" muestra oferta, match score, y carta antes de enviar. El usuario debe aprobar manualmente cada aplicación. |
| APPLY-005 | SHOULD | El sistema debe reintentar aplicaciones fallidas | Si el envío falla (error de red, cuenta bloqueada), el sistema reintenta hasta 3 veces con backoff exponencial. Después de 3 intentos fallidos, marca como fallida. |
| APPLY-006 | MAY | El sistema debe detectar ofertas ya aplicadas | Al cargar ofertas, el sistema marca si el usuario ya aplicó a esa oferta (en sistema o en LinkedIn via API) para evitar duplicación. |

### 3.8 Dashboard y Notificaciones

| ID | Prioridad | Descripción | Criterios de Aceptación |
|----|----------|-------------|-------------------------|
| DASH-001 | MUST | El sistema debe mostrar dashboard con métricas clave | El dashboard muestra: TOTAL ofertas disponibles, TOTAL matcheadas (alta), TOTAL aplicadas, tasa de respuesta (calculada de replies recibidas). |
| DASH-002 | MUST | El sistema debe mostrar gráfico de tendencias | Gráfico de líneas muestra aplicaciones por día/semana/mes y respuesta rate a lo largo del tiempo. |
| DASH-003 | MUST | El sistema debe notificar nuevas ofertas matcheadas | Cuando scraping encuentra oferta con match score ≥80 para el usuario, se envía notificación email y push (si la app lo permite). |
| DASH-004 | SHOULD | El sistema debe permitir configurar frecuencia de notificaciones | El usuario puede elegir: immédiat, digest diario, o digest semanal. Por defecto: digest diario. |
| DASH-005 | SHOULD | El sistema debe mostrar estadísticas por fecha | El usuario puede filtrar dashboard por período: última semana, último mes, últimos 3 meses, todo el tiempo. |
| DASH-006 | MAY | El sistema debe comparar con benchmarks | Muestra cómo el usuario performs versus otros usuarios del sistema en términos de aplicación rate y respuesta rate. Sin datos personales identificables. |

---

## 4. Requisitos No Funcionales

### 4.1 Requisitos de Rendimiento

Los requisitos de rendimiento establecen las expectativas de velocidad y eficiencia del sistema bajo condiciones operativas normales. El objetivo es proporcionar una experiencia de usuario fluida que no frustraré las expectativas del usuario por tiempos de espera excesivos.

Tiempo de respuesta máximo para operaciones comunes: El login y autenticación deben completarse en menos de 2 segundos bajo condiciones normales de red. La búsqueda y visualización de ofertas debe mostrar resultados en menos de 3 segundos para consultas simples. La generación de carta de presentación debe completarse en menos de 10 segundos. El cálculo de matching para 100 ofertas debe completarse en menos de 5 segundos. La carga de páginas del dashboard debe completarse en menos de 2 segundos.

Rendimiento bajo carga: El sistema debe manejar hasta 100 usuarios concurrentes manteniendo tiempos de respuesta dentro de los límites especificados. El scraping debe poder procesar al menos 50 ofertas por hora sin degradar el rendimiento de otras operaciones. La base de datos debe manejar consultas de hasta 10,000 ofertas sin degradar significativamente el rendimiento.

### 4.2 Requisitos de Escalabilidad

La arquitectura debe soportar crecimiento en número de usuarios y volumen de datos sin requerir re-arquitectura significativa. El diseño debe considerar las siguientes proyecciones de crecimiento para las decisiones de escalabilidad horizontal versus vertical.

Capacidad de usuarios: El sistema debe soporta 1,000 usuarios activos inicialmente, con capacidad de escalar a 10,000 mediante adición de instancias adicionales. Cada usuario puede mantener hasta 5 CVs versions保存adosy hasta 100 búsquedas guardadas. Las ofertas scrapeadas deben almacenarse Efficiently para soportar hasta 100,000 ofertas activas en la base de datos.

Escalabilidad de scraping: El sistema debe ejecutar múltiples jobs de scraping en paralelo, hasta 5 concurrentes sin detectar conflictos. El scraping debe ser configurable para escalar horizontalmente agregando más workers.

### 4.3 Requisitos de Seguridad

La seguridad es crítica dado que el sistema maneja datos personales sensibles, credenciales de usuario, y acceso a cuentas de LinkedIn y Gmail de los usuarios. Toda la información personal almacenada debe estar cifrada en reposo utilizando AES-256. Las contraseñas deben almacenarse hasheadas con bcrypt o Argon2, nunca en texto plano. Los tokens JWT deben firmarse con algoritmos seguros (HS256 o RS256) y tener tiempos de expiración cortos (máximo 24 horas).

Transmisión de datos: Toda comunicación entre cliente y servidor debe usar TLS 1.2 o superior. Las credenciales de Gmail y LinkedIn deben manejarse con OAuth 2.0, nunca almacenar passwords directamente. Los tokens de acceso deben cifrarse en la base de datos.

Control de acceso: Cada usuario solo puede acceder a sus propios datos. No debe existir forma de que un usuario acceda a datos de otro usuario mediante manipulación de parámetros. Todos los endpoints privados deben verificar autenticación Y autorización.

Auditoría: El sistema debe registrar logs de autenticación (login, logout, intentos fallidos). Los logs deben incluir timestamp, usuario (o email si no autenticado), IP, y resultado. Los logs deben retentionarse por al menos 90 días.

### 4.4 Requisitos de Disponibilidad

El sistema debe estar disponible para los usuarios cuando lo necesiten. El objetivo es minimizar el downtime no planificado y proporcionar tiempos de recuperación razonables.

Disponibilidad objetivo: El sistema debe mantener disponibilidad del 99.5% medida mensualmente, excluyendo mantenimiento planificado. El downtime planificado debe comunicarse con al menos 48 horas de anticipación. El mantenimiento routine debe programarse en horarios de bajo uso (preferiblemente noches UTC).

Recuperación ante desastres: El sistema debe realizar backups diarios de la base de datos. Los backups deben almacenarse en location diferente del servidor principal. El tiempo máximo de recuperación (RTO) objetivo es 4 horas. El punto máximo de pérdida de datos (RPO) objetivo es 24 horas.

### 4.5 Requisitos de Usabilidad

La experiencia de usuario debe ser intuitiva y accesible para usuarios sin conocimientos técnicos avanzados. El sistema debe ser usable sin consultar documentación externa.

Curva de aprendizaje: Un usuario new debe poder completar su registro y carga de CV en menos de 10 minutos sin asistencia. La búsqueda de ofertas y aplicación debe ser discoverable sin tutorial. Todo error debe mostrar mensaje claro en lenguaje natural, no códigos técnicos.

Accesibilidad: El sistema debe cumplir con WCAG 2.1 nivel AA como mínimo. Esto incluye contraste suficiente, navegación por teclado completa, y compatibilidad con screen readers. Los formularios deben tener labels claros y mensajes de error específicos.

Internacionalización: La interfaz debe soportar español e inglés como mínimo, con capacidad de extensión a otros idiomas. Las fechas y números deben formatearse según locale del usuario.

---

## 5. Requisitos Específicos del Dominio

### 5.1 Entidad Usuario

La entidad Usuario representa al candidato que utiliza el sistema. Los atributos de la entidad comprenden información personal básica: user_id (UUID único), email (único, verificado), password_hash, created_at, updated_at, y is_active. El perfil profesional incluye full_name, location (ciudad, país), LinkedIn_URL (opcional), phone (opcional), y summary_professional (texto libre, máx 500 caracteres).

La experiencia laboral se modela como colección de Experience con: empresa, job_title, location, start_date, end_date (nullable, indica que es trabajo actual), description, y es_remote (boolean). La educación se modela como colección de Education con: institución, título, campo_de_estudio, start_date, end_date, y descripción. Las habilidades se categorizan como Skills con: nombre, categoría (técnica/inglesa/blanda), y nivel (1-5).

Las preferencias laborales establecen los filtros default para matching: ubicaciones_preferidas (lista), salary_min (integer), salary_max (integer), tipos_contrato (lista: full-time/part-time/contract), remote_preference (enum: remote/hybrid/onsite/any), seniority_buscado (enum), y idiomas_necesarios (lista).

### 5.2 Entidad Oferta

La entidad JobPosting representa una oferta laboral scrappeada de LinkedIn. Atributos: job_id (UUID único), url_original (URL única de LinkedIn), título (required), empresa (required), ubicación, description (texto completo), requisitos_técnicos (lista extraída), beneficios (texto si disponible), salary_min, salary_max, salary_currency, tipo_contrato (full-time/part-time/contract/intern), remote_option (remote/hybrid/onsite), fecha_publicación, fecha_vencimiento_estimada, scraped_at, y is_active.

La información de scraping metadata incluye: last_scraped_at, scrape_status (success/failed/pending), y error_message si falló. Los hashes de detección de duplicados incluyen: url_hash y content_hash para identificación de ofertas duplicadas.

### 5.3 Entidad Matching

El matching entre Usuario y JobPosting produce la entidad MatchResult. Atributos: match_id, user_id, job_id, score_total (0-100), desglose (JSON con scores por factor), Classification (enum: alta/media/baja), calculated_at, y is_read (boolean).

Factores de matching con pesos configurables: embeddings_score (peso default 0.4), seniority_match (peso default 0.2), ubicación_match (peso default 0.15), salary_match (peso default 0.15), requisitos_match (peso default 0.1). El usuario administrator puede ajustar estos pesos.

### 5.4 Entidad Aplicación

La entidad Application representa una postulación realizada. Atributos: application_id, user_id, job_id, cover_letter_id (referencia a carta utilizada), método (enum: email/linkedin_bot), estado (enum: pending/sent/failed/rejected/interview), sent_at, response_received_at (nullable), y notas (texto libre para tracking manual).

---

## 6. Historias de Usuario y Escenarios

Las siguientes historias de usuario siguen el formato "Como [rol], quiero [acción], para [beneficio]". Cada historia incluye escenarios Given-When-Then para clarificar el comportamiento esperado.

### 6.1 Historias de Gestión de Cuenta

**HU-001: Registro de nuevo usuario**
Como profesional activamente buscando empleo,
Quiero registrarme en la plataforma con mi correo electrónico,
Para poder acceder a las funcionalidades de búsqueda y postulación automática.

Escenarios:

- **Registro exitoso**: Given que estoy en la página de registro, When ingreso un correo electrónico válido y una contraseña válida (mínimo 8 caracteres con mezcla de letras y números), And confirmo mi contraseña, Then debo ver un mensaje de éxito indicando que revisé mi correo para verificar mi cuenta.

- **Contraseña débil**: Given que estoy en la página de registro, When ingreso una contraseña de menos de 8 caracteres, Then debo ver un mensaje de error indicando los requisitos de contraseña.

- **Correo duplicado**: Given que estoy en la página de registro, When ingreso un correo electrónico ya registrado, Then debo ver un mensaje de error indicating que el correo ya está en uso.

**HU-002: Inicio de sesión**
Como usuario registrado,
Quiero iniciar sesión con mi correo y contraseña,
Para acceder a mi dashboard y funcionalidades.

Escenarios:

- **Login exitoso**: Given que tengo una cuenta registrada, When ingresgo mi correo y contraseña correctos, Then debo acceder a mi dashboard sin re-dirección.

- **Credenciales incorrectas**: Given que tengo una cuenta registrada, When ingresgo mi correo correcto pero contraseña incorrecta, Then debo ver mensaje de error y mantener la sesión cerrada.

**HU-003: Recuperación de contraseña**
Como usuario que olvidó su contraseña,
Quiero poder recuperar mi cuenta mediante correo electrónico,
Para volver a acceder sin perder mis datos.

Escenarios:

- **Solicitar reseteo**: Given que estoy en la página de login, When hago clic en "Olvidé mi contraseña" e ingreso mi correo registrado, Then debo recibir un correo con enlace de recuperación.

- **Cambiar contraseña**: Given que recibí el correo de recuperación, When hago clic en el enlace y establezco nueva contraseña, Then debo poder iniciar sesión con la nueva contraseña.

### 6.2 Historias de Perfil y CV

**HU-004: Carga de CV**
Como usuario wanting automatizar mi perfil,
Quiero cargar mi CV en formato PDF,
Para que el sistema extraiga mi información automáticamente.

Escenarios:

- **Carga exitosa**: Given que estoy en la sección "Mi CV", When subo un archivo PDF válido de menos de 10MB, Then debo ver una vista previa de la información extraída.

- **Archivo muy grande**: Given que estoy en la sección "Mi CV", When subo un archivo mayor a 10MB, Then debo ver mensaje de error indicando el límite de tamaño.

- **Formato no soportado**: Given que estoy en la sección "Mi CV", When subo un archivo en formato no soportado (ej. imágenes), Then debo ver mensaje listando los formatos soportados.

**HU-005: Revisar y confirmar CV parseado**
Como usuario wanting verificar que el parsing fue correcto,
Quiero revisar la información extraída de mi CV antes de confirmar,
Para corregir errores si los hay.

Escenarios:

- **Revisión**: Given que cargué mi CV, When veo la información extraída, Then debo poder editar cualquier campo antes de confirmar.

- **Confirmar**: Given que revisé y编辑é la información, When hago clic en "Confirmar", Then mi perfil se actualiza con la información confirmada.

### 6.3 Historias de Búsqueda y Matching

**HU-006: Buscar ofertas**
Como usuario buscando empleo,
Quiero buscar ofertas con filtros específicos,
Para encontrar ofertas relevantes a mi perfil.

Escenarios:

- **Búsqueda basic**: Given que estoy en el panel de búsqueda, When ingreso "Python developer" y selecciono "Remoto", Then debo ver ofertas relacionadas con ese término.

- **Búsqueda sin resultados**: Given que estoy en el panel de búsqueda, When busco con criterios muy restrictivos que no coinciden con ninguna oferta, Then debo ver mensaje indicando que no hay resultados.

**HU-007: Ver ofertas matcheadas**
Como usuario wanting ver las mejores ofertas,
Quiero ver las ofertas ordenadas por compatibilidad con mi perfil,
Para enfocarme en las más relevantes.

Escenarios:

- **Ver matches de alta compatibilidad**: Given que tengo un perfil completo, When voy a "Ofertas Matcheadas", Then debo ver ofertas ordenadas por score, las de alta compatibilidad primero.

- **Ver detalles de match**: Given que estoy en la lista de ofertas matcheadas, When hago clic en una oferta, Then debo ver los detalles incluyendo el desglose de compatibilidad.

**HU-008: Generar carta de presentación**
Como usuario wanting aplicar a una oferta,
Quiero generar una carta de presentación personalizada,
Para acelerar mi proceso de postulación.

Escenarios:

- **Generar carta**: Given que estoy viendo una oferta con match alto, When hago clic en "Generar Carta", Then debo ver una carta generada automáticamente.

- **Editar carta**: Given que veo la carta generada, When hago clic en "Editar", Then debo poder modificar el contenido.

- **Guardar carta**: Given que编辑é la carta, When hago clic en "Guardar", Then la carta debe guardarse para esa oferta específica.

### 6.4 Historias de Aplicación

**HU-009: Aplicar a oferta manualmente**
Como usuario wanting confirmar cada aplicación,
Quiero revisar la oferta y carta antes de enviar,
Para asegurarme de que todo está correcto.

Escenarios:

- **Revisar antes de aplicar**: Given que tengo una carta generada, When hago clic en "Aplicar", Then debo ver un resumen de la oferta, match score, y carta antes de confirmar.

- **Confirmar aplicación**: Given que revisé todo, When hago clic en "Confirmar Aplicación", Then debo ver confirmación de éxito y la aplicación debe aparecer en mi historial.

**HU-010: Aplicación automática**
Como usuario wanting automatizar completamente,
Quiero que el sistema aplique automáticamente a ofertas de alta compatibilidad,
Para ahorrar tiempo en postulaciones rutinarias.

Escenarios:

- **Configurar auto-apply**: Given que estoy en configuración, When habilito "Auto-apply" y configuro threshold (ej. score ≥ 80), Then el sistema debe aplique automáticamente sin confirmación.

- **Auto-apply deshabilitado**: Given que tengo auto-apply habilitado, When lo deshabilito, Then el sistema debe detener aplicaciones automáticas.

### 6.5 Historias de Dashboard

**HU-011: Ver estadísticas**
Como usuario wanting seguir mi progreso,
Quiero ver un dashboard con métricas clave,
Para entender cómo va mi búsqueda de empleo.

Escenarios:

- **Ver overview**: Given que estoy logueado, When miro mi dashboard, Then debo ver: total ofertas disponibles, ofertas matcheadas, aplicaciones enviadas, y tasa de respuesta.

- **Filtrar por fecha**: Given que estoy en el dashboard, When selecciono "Último mes", Then las métricas deben corresponder solo al último mes.

---

## 7. Restricciones Técnicas

### 7.1 Restricciones del Modelo de IA Local

El sistema está diseñado para ejecutarse completamente en infraestructura local, sin依赖 de APIs externas de lenguaje natural. Esta decisión impone restricciones específicas en la selección y operación de modelos.

Requisitos de hardware: El sistema debe ejecutarse en hardware accesible para el usuario objetivo. Se asume un mínimo de 16GB RAM para el servidor, aunque 32GB es recomendado para producción. Para embedding inference, se recomienda GPU con al menos 8GB VRAM (NVIDIA RTX series o equivalente). Sin GPU, la inferencia será más lenta pero funcional.

Modelos de embedding: Deberán utilizarse modelos de embedding eficientes como E5-small-v2 o MiniLM-L6-v2, cuyo tamaño permite inferencia razonable en CPU. El dimensionamiento de vectores debe ser 384 o menor para minimizar almacenamiento. El batching debe soportar al menos 32 documentos por batch.

Modelos de generación: Para generación de cartas de presentación, deben utilizarse modelos pequeños de lenguaje. Modelos candidatos incluyen Qwen2.5-1.5B, Phi-3-mini-4k, o TinyLlama-1.1B. El contexto máximo debe ser al menos 2048 tokens para caber la oferta + perfil + carta. La generación debe completarse en menos de 10 segundos por carta.

Actualización de modelos: El sistema debe permitir actualizar los modelos sin re-desplegar toda la aplicación. Los modelos deben cargarse desde archivos externos (por ejemplo, en directorio /models). Debe haber logging de qué modelo está cargado actualmente.

### 7.2 Restricciones de LinkedIn

LinkedIn tiene políticas estrictas contra scraping automatizado. El sistema debe respetar estas políticas para evitar banning de IPs y posibles acciones legales.

Rate limiting: No deben realizarse más de 1 solicitud cada 3 segundos a LinkedIn desde una misma IP. El scraping debe implementarse con backoff exponencial si se reciben errores 429. El sistema debe rotar User Agents y Headers de request para mimetizar navegación humana.

No monetización: El sistema no debe utilizarse para comercialización de datos de LinkedIn. Los datos scrapeados son para uso exclusivo del usuario registrado. No está permitido redistribuir información de LinkedIn a terceros.

Cuenta LinkedIn: El scraping requiere una sesión de LinkedIn activa. El usuario debe proporcionar sus credenciales de LinkedIn (almacenadas cifradamente) o iniciar sesión manualmente via browser automatizado. El sistema debe soportar la necesidad de re-autenticación periódica.

Políticas: El sistema debe incluir aviso prominent cuando el usuario lo utiliza de que el scraping puede violate los Términos de Servicio de LinkedIn. La responsabilidad del uso inadecuado recae en el usuario.

### 7.3 Restricciones de Email

Para el envío de aplicaciones por email, se utilizarán las APIs de Gmail, lo cual impone sus propias restricciones.

OAuth 2.0: El sistema no debe almacenar passwords de Gmail. Solo debe usarse OAuth 2.0 con scopes apropiados. El access token debe renovarse automáticamente antes de expirar.

Límites de Gmail: Gmail tiene límites de envío (500 emails por día para cuentas gratuitas, 2000 para Google Workspace). El sistema debe respectar estos límites y warnnear al usuario si se acerca a ellos. El sistema debe implement retries suaves con backoff.

Spam: El sistema debe generar emails que no sean marcados como spam. Esto incluye no enviar emails masivos sin personalization, usar SPF/DKIM correctamente configurados por el dominio del usuario, y no incluir links sospechosos.

### 7.4 Restricciones de Base de Datos

La base de datos PostgreSQL debe dimensionarse adecuadamente para el volumen de datos proyectado.

Diseño de esquema: El esquema debe ser normalizado hasta al menos 3NF para minimizar redundancia. Los índices deben crearse en campos frecuentemente queryados (user_id, job_id, created_at para búsqueda por fecha, composite indexes para filtros comunes).

Rendimientos: Queries simples (< 100 результат) deben ejecutarse en < 100ms. Queries complejas con agregaciones deben ejecutarse en < 1 segundo. Para queries lentos, debe implementarse query resultado caching.

Backup y retención: Los datos de ofertas anticuadas (> 30 días) deben archivalse o eliminarse. Los backups deben hacerse diariamente con retention de 30 días. Los logs de aplicación deben retentionarse por al menos 90 días.

---

## 8. Glosario

| Término | Descripción |
|---------|-------------|
| Aplicación | Postulación formal a una oferta de empleo |
| Carta de presentación | Documento personalizado que acompaña el CV al aplicar a un empleo |
| Contraseña | Secreto compartido entre usuario y sistema para autenticación |
| CV | Currículum Vitae, documento que describe la trayectoria profesional |
| Dashboard | Panel de control con métricas y estadísticas |
| DDD | Domain-Driven Design, metodología de desarrollo |
| Embedding | Representación vectorial de texto |
| JWT | JSON Web Token, token de autenticación |
| Matching | Proceso de emparejamiento perfil-oferta |
| Oferta | Publicación de empleo en LinkedIn |
| Parsing | Extracción de información estructurada de documento |
| Scraping | Extracción automatizada de datos web |
| Seniority | Nivel de experiencia profesional |
| Stakeholder | Persona interesada en el proyecto |
| Token | Credencial de autenticación stateless |
| User Agent | Cadena que identifica el cliente web |

---

## 9. Referencias

- RFC 2119: Key words for use in RFCs to Indicate Requirement Levels
- WCAG 2.1: Web Content Accessibility Guidelines
- LinkedIn Terms of Service: https://www.linkedin.com/legal/user-agreement
- Gmail API Documentation: https://developers.google.com/gmail/api
- OWASP Top 10: Security vulnerabilities y mejores prácticas

---

## 10. Aprobaciones

| Rol | Nombre | Fecha | Firma |
|-----|--------|-------|-------|
| Product Owner | | | |
| Tech Lead | | | |
| QA Lead | | | |
| Security Lead | | | |

---

*Documento generado según estándar de especificaciones de requisitos de software (SRS). Este documento sirve como referencia autoritativa para todas las decisiones de implementación y verification.*
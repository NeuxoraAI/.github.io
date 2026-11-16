"""Canonical site data, services, and verified project metadata for Neuxora."""

SITE = {
    "name": "Neuxora",
    "base_url": "https://neuxoraai.github.io/.github.io",
    "email": "neuxoraia@gmail.com",
    "location": "León, Guanajuato, México",
    "github": "https://github.com/NeuxoraAI",
    "instagram": "https://www.instagram.com/neuxora_ia/",
    "tagline": "Consultora de ingeniería y desarrollo de software desde Guanajuato.",
    "theme_color": "#ffffff",
}

NAV_ITEMS = [
    {"label": "Servicios", "href": "index.html#servicios", "key": "servicios"},
    {"label": "Proyectos", "href": "proyectos.html", "key": "proyectos"},
    {"label": "Investigación", "href": "investigacion.html", "key": "investigacion"},
    {"label": "Cuaderno", "href": "noticias.html", "key": "noticias"},
    {"label": "Nosotros", "href": "neuxora.html", "key": "neuxora"},
]

SERVICES = [
    {
        "id": "plataformas",
        "icon": "plataformas",
        "short": "Desarrollo de Plataformas",
        "title": "Sistemas web y aplicaciones completas para la operación diaria.",
        "lead": (
            "Construimos aplicaciones ordenadas por áreas, con acceso por perfil de usuario, "
            "historial de cambios y pruebas antes de salir a operación."
        ),
        "use_cases": [
            "Portales para estudiantes, clientes o personal administrativo",
            "Captura de formularios y expedientes desde celular o computadora",
            "Control de permisos, sesiones activas y registro de auditoría",
            "Reemplazo de hojas de cálculo dispersas por un sistema central",
            "Puesta en marcha continua sin interrumpir al equipo",
        ],
        "deliverables": [
            "Flujo completo de pantallas adaptado a quienes lo usan todos los días",
            "Interfaces cómodas en celular para trabajo en campo o ventanilla",
            "Pruebas de funcionamiento y registro claro de acciones importantes",
        ],
        "evidence_links": [
            {"label": "Web-App Idiomas UG", "href": "proyecto-idiomas-ug.html", "internal": True},
            {"label": "Sillas Rotary", "href": "proyecto-sillas-rotary.html", "internal": True},
        ],
    },
    {
        "id": "llm",
        "icon": "llm",
        "short": "Inferencia de modelos LLM",
        "title": "Modelos de lenguaje respondiendo dentro de tus sistemas, con costo y velocidad bajo control.",
        "lead": (
            "Ponemos modelos de lenguaje a trabajar dentro de tus aplicaciones: elegimos el modelo, "
            "lo desplegamos en la nube o en tus propios equipos y medimos calidad, velocidad y costo."
        ),
        "use_cases": [
            "Asistentes que responden con base en tus documentos y manuales internos",
            "Extracción de datos desde expedientes, formularios o correos",
            "Clasificación y resumen de grandes volúmenes de texto",
            "Modelos abiertos corriendo en tu infraestructura cuando los datos no pueden salir",
            "Reducción del costo y del tiempo de respuesta de un modelo ya en uso",
        ],
        "deliverables": [
            "Comparativa de modelos con tus propios datos antes de elegir",
            "Servicio de inferencia integrado a tu aplicación, con límites de uso y registro",
            "Medición continua de calidad, tiempo de respuesta y costo por consulta",
        ],
        "evidence_links": [
            {
                "label": "Platicar sobre inferencia de LLM",
                "href": "mailto:neuxoraia@gmail.com?subject=Proyecto%20de%20inferencia%20LLM",
                "internal": False,
            },
        ],
    },
    {
        "id": "vision",
        "icon": "vision",
        "short": "Visión Artificial",
        "title": "Lectura de documentos, análisis visual y revisión de imágenes.",
        "lead": (
            "Armamos flujos para pasar fotografías de documentos a información ordenada, "
            "analizar imágenes de laboratorio o automatizar revisiones visuales."
        ),
        "use_cases": [
            "Digitalización automática de expedientes, recetas o formularios en foto",
            "Limpieza previa de fotografías movidas, inclinadas o con poca luz",
            "Segmentación y medición visual sobre imágenes médicas o técnicas",
            "Comparación objetiva entre modelos usando los mismos datos de prueba",
            "Integración directa con la operación diaria del equipo",
        ],
        "deliverables": [
            "Pruebas comparativas claras entre opciones con el mismo conjunto de datos",
            "Herramientas que procesan imágenes y entregan datos listos para guardar",
            "Reporte honesto de resultados, alcance y límites de uso",
        ],
        "evidence_links": [
            {"label": "Comparativa Mamba-UNet", "href": "investigacion.html#mamba", "internal": True},
            {"label": "medscan CLI", "href": "proyectos.html#medscan", "internal": True},
        ],
    },
    {
        "id": "ml",
        "icon": "ml",
        "short": "Machine Learning",
        "title": "Modelos entrenados y probados sobre datos reales.",
        "lead": (
            "Antes de proponer redes neuronales o modelos complejos, comparamos opciones más "
            "sencillas para elegir la que mejor funciona según tu costo y tus datos."
        ),
        "use_cases": [
            "Clasificación y ordenamiento automático de textos, solicitudes o imágenes",
            "Comparación práctica frente a reglas simples antes de complicar el sistema",
            "Medición real de tiempos de respuesta y costo operativo",
            "Seguimiento ordenado de pruebas para repetir resultados sin sorpresas",
        ],
        "deliverables": [
            "Línea base clara comparada contra alternativas sencillas",
            "Flujo repetible de limpieza de datos, entrenamiento y validación",
            "Integración con los sistemas actuales del equipo",
        ],
        "evidence_links": [
            {"label": "Ver comparativa Mamba-UNet", "href": "investigacion.html#mamba", "internal": True},
            {"label": "Ver medscan CLI", "href": "https://github.com/NeuxoraAI/medscan-CLI", "internal": False},
        ],
    },
    {
        "id": "datos",
        "icon": "datos",
        "short": "Análisis de Datos",
        "title": "Ordenar registros dispersos para poder consultarlos y entenderlos.",
        "lead": (
            "Pasamos formularios en papel, archivos sueltos y capturas distintas a registros "
            "limpios, fáciles de consultar y listos para tomar decisiones."
        ),
        "use_cases": [
            "Unificación de hojas de cálculo o papel en una sola fuente confiable",
            "Historiales completos por persona, paciente, sede o equipo",
            "Detección y limpieza de registros duplicados o incompletos",
            "Consultas y reportes operativos sin armarlos a mano cada semana",
        ],
        "deliverables": [
            "Estructura de información adaptada a cómo opera el equipo",
            "Carga inicial y limpieza desde archivos, formularios o documentos previos",
            "Vistas y exportaciones listas para seguimiento diario",
        ],
        "evidence_links": [
            {"label": "Sillas Rotary", "href": "proyecto-sillas-rotary.html", "internal": True},
            {"label": "WebDiabetes DM", "href": "proyectos.html#webdiabetes", "internal": True},
        ],
    },
]

IDIOMAS_MODULES = [
    {
        "id": "sustentantes",
        "icon": "sustentantes",
        "name": "Registro de sustentantes",
        "desc": "Alta y verificación de estudiantes o personas externas que solicitan examen de regularización en el Departamento de Idiomas UG Campus León.",
    },
    {
        "id": "examenes",
        "icon": "examenes",
        "name": "Administración de niveles",
        "desc": "Configuración y consulta de exámenes de regularización organizados por idioma, nivel y convocatoria activa.",
    },
    {
        "id": "aplicacion",
        "icon": "aplicacion",
        "name": "Aplicación de exámenes",
        "desc": "Experiencia clara y sin distracciones para que cada persona presente su examen desde computadora o celular.",
    },
    {
        "id": "intentos",
        "icon": "intentos",
        "name": "Control de intentos",
        "desc": "Seguimiento preciso de cada intento realizado, tiempos de sesión y estado del examen para evitar duplicados.",
    },
    {
        "id": "administracion",
        "icon": "administracion",
        "name": "Cuentas y permisos",
        "desc": "Acceso diferenciado entre coordinación, personal administrativo y sustentantes, con alta controlada de administradores.",
    },
    {
        "id": "auditoria",
        "icon": "auditoria",
        "name": "Historial y auditoría",
        "desc": "Registro automático de acciones clave dentro de la plataforma para respaldar revisiones y aclaraciones.",
    },
    {
        "id": "seguridad",
        "icon": "seguridad",
        "name": "Seguridad de acceso",
        "desc": "Resguardo de credenciales y manejo ágil de sesiones activas para soportar varios usuarios al mismo tiempo.",
    },
    {
        "id": "calidad",
        "icon": "calidad",
        "name": "Validación operativa",
        "desc": "Pruebas continuas sobre registro, examen e historial para detectar fallas antes de liberar cualquier cambio.",
    },
]

PROJECTS = [
    {
        "id": "idiomas-ug",
        "icon": "idiomas",
        "title": "Web-App Idiomas UG",
        "status": "En construcción",
        "badge_class": "card-badge--building",
        "category_label": "Plataforma web",
        "categories": ["plataformas"],
        "summary": (
            "Aplicación web para realizar exámenes de regularización de nivel en distintos idiomas "
            "en el Departamento de Idiomas de la Universidad de Guanajuato, Campus León."
        ),
        "context_line": "Universidad de Guanajuato · Campus León · En construcción",
        "href": "proyecto-idiomas-ug.html",
        "internal": True,
        "cta": "Ver cómo funciona",
    },
    {
        "id": "sillas-rotary",
        "icon": "rotary",
        "title": "Sillas Rotary",
        "status": "Documentado",
        "badge_class": "card-badge--active",
        "category_label": "Sistema de campo",
        "categories": ["plataformas", "datos"],
        "summary": (
            "Aplicación pensada para celular que reemplaza formularios en papel por captura digital "
            "de estudios socioeconómicos, solicitudes técnicas y fotografías en el programa «200 sillas para 200 campeones»."
        ),
        "context_line": "Programa «200 sillas para 200 campeones» · Captura móvil en campo",
        "href": "proyecto-sillas-rotary.html",
        "internal": True,
        "cta": "Ver caso y fotos",
    },
    {
        "id": "medscan",
        "icon": "medscan",
        "title": "medscan CLI",
        "status": "Open Source",
        "badge_class": "card-badge--active",
        "category_label": "Digitalización",
        "categories": ["vision-ml", "cli", "datos"],
        "summary": (
            "Herramienta que prepara fotografías de expedientes, ordena la información "
            "de forma automática y la guarda localmente lista para consultar."
        ),
        "context_line": "Proyecto abierto · Lectura de expedientes desde imagen",
        "href": "https://github.com/NeuxoraAI/medscan-CLI",
        "internal": False,
        "cta": "Ver en GitHub",
    },
    {
        "id": "webdiabetes",
        "icon": "webdiabetes",
        "title": "WebDiabetes DM",
        "status": "Prototipo",
        "badge_class": "card-badge--building",
        "category_label": "Plataforma web",
        "categories": ["plataformas", "datos"],
        "summary": (
            "Prototipo web para llevar seguimiento de registros, cuestionarios clínicos "
            "y mensajes entre perfiles de paciente y médico."
        ),
        "context_line": "Prototipo clínico · Seguimiento entre paciente y médico",
        "href": "https://github.com/NeuxoraAI/WebDiabetes-DM-2026-06/tree/develop",
        "internal": False,
        "cta": "Ver en GitHub",
    },
    {
        "id": "mamba",
        "icon": "mamba",
        "title": "U-Net vs Mamba-UNet",
        "status": "Experimento",
        "badge_class": "",
        "category_label": "Visión artificial",
        "categories": ["vision-ml"],
        "summary": (
            "Comparación de dos arquitecturas para segmentación celular usando los mismos 670 pares "
            "de imagen y máscara del conjunto público BBBC038."
        ),
        "context_line": "Investigación aplicada · 670 pares de imagen celular (BBBC038)",
        "href": "investigacion.html#mamba",
        "internal": True,
        "cta": "Ver resultados",
    },
]

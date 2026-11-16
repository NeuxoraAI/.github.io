"""Clean 24x24 geometric SVG icon system (Lucide / Antigravity line style)."""

import html


ICONS: dict[str, str] = {
    # Service verticals
    "plataformas": (
        '<rect x="3" y="4" width="18" height="15" rx="2.5"/>'
        '<path d="M3 9h18"/>'
        '<path d="M9 9v10"/>'
    ),
    "llm": (
        '<path d="M20 11.5a7.5 7.5 0 0 1-7.5 7.5H9l-4.5 2.5.9-4A7.5 7.5 0 1 1 20 11.5z"/>'
        '<path d="M12.5 7.8l.9 2.3 2.3.9-2.3.9-.9 2.3-.9-2.3-2.3-.9 2.3-.9z"/>'
    ),
    "close": (
        '<path d="M6 6l12 12"/>'
        '<path d="M18 6L6 18"/>'
    ),
    "arrow-up": (
        '<path d="M12 19V5"/>'
        '<path d="M6 11l6-6 6 6"/>'
    ),
    "vision": (
        '<path d="M4 8V6a2 2 0 0 1 2-2h2"/>'
        '<path d="M16 4h2a2 2 0 0 1 2 2v2"/>'
        '<path d="M20 16v2a2 2 0 0 1-2 2h-2"/>'
        '<path d="M8 20H6a2 2 0 0 1-2-2v-2"/>'
        '<path d="M7 12s2.2-3.5 5-3.5 5 3.5 5 3.5-2.2 3.5-5 3.5-5-3.5-5-3.5Z"/>'
        '<circle cx="12" cy="12" r="1.4"/>'
    ),
    "ml": (
        '<circle cx="5.5" cy="7" r="2"/>'
        '<circle cx="5.5" cy="17" r="2"/>'
        '<circle cx="12" cy="12" r="2.2"/>'
        '<circle cx="18.5" cy="7" r="2"/>'
        '<circle cx="18.5" cy="17" r="2"/>'
        '<path d="M7.2 8.2 10.2 10.7"/>'
        '<path d="M7.2 15.8 10.2 13.3"/>'
        '<path d="M13.8 10.7 16.8 8.2"/>'
        '<path d="M13.8 13.3 16.8 15.8"/>'
    ),
    "datos": (
        '<path d="M4 19h16"/>'
        '<path d="M7 16v-5"/>'
        '<path d="M12 16V8"/>'
        '<path d="M17 16V5"/>'
    ),
    # Showcase & project cards
    "idiomas": (
        '<path d="M4 6.5A2.5 2.5 0 0 1 6.5 4H12v15H6.5A2.5 2.5 0 0 0 4 21z"/>'
        '<path d="M20 6.5A2.5 2.5 0 0 0 17.5 4H12v15h5.5A2.5 2.5 0 0 1 20 21z"/>'
    ),
    "rotary": (
        '<rect x="6" y="4" width="12" height="16" rx="2"/>'
        '<path d="M9 4.5h6"/>'
        '<path d="M9 11l2 2 4-4"/>'
        '<path d="M9 16h6"/>'
    ),
    "medscan": (
        '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/>'
        '<path d="M14 3v5h5"/>'
        '<path d="M8 13h8"/>'
        '<path d="M8 17h5"/>'
    ),
    "webdiabetes": (
        '<path d="M3 12h4l2.5-6 4 12 2.5-6h5"/>'
    ),
    "mamba": (
        '<rect x="4" y="4" width="7" height="7" rx="1.5"/>'
        '<rect x="13" y="4" width="7" height="7" rx="1.5"/>'
        '<rect x="4" y="13" width="7" height="7" rx="1.5"/>'
        '<circle cx="16.5" cy="16.5" r="3.5"/>'
    ),
    # Idiomas UG functional modules
    "sustentantes": (
        '<circle cx="9.5" cy="7.5" r="3"/>'
        '<path d="M3.5 19.5c0-3 2.5-5 6-5s6 2 6 5"/>'
        '<path d="m16.5 11.5 1.8 1.8 3.2-3.3"/>'
    ),
    "examenes": (
        '<path d="m12 3 9 4.5-9 4.5-9-4.5z"/>'
        '<path d="m3 12 9 4.5 9-4.5"/>'
        '<path d="m3 16.5 9 4.5 9-4.5"/>'
    ),
    "aplicacion": (
        '<rect x="4" y="4" width="16" height="16" rx="2.5"/>'
        '<path d="m9 12 2 2 4-4"/>'
    ),
    "intentos": (
        '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/>'
        '<path d="M3 3v5h5"/>'
        '<path d="M12 7.5v4.5l3 1.8"/>'
    ),
    "administracion": (
        '<path d="M4 21v-7"/>'
        '<path d="M4 10V3"/>'
        '<path d="M12 21v-9"/>'
        '<path d="M12 8V3"/>'
        '<path d="M20 21v-5"/>'
        '<path d="M20 12V3"/>'
        '<path d="M2 14h4"/>'
        '<path d="M10 8h4"/>'
        '<path d="M18 16h4"/>'
    ),
    "auditoria": (
        '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/>'
        '<path d="M14 3v5h5"/>'
        '<path d="m9.5 14.5 1.8 1.8 3.2-3.6"/>'
    ),
    "seguridad": (
        '<path d="M12 3 5 6v6c0 4.5 3 7.8 7 9 4-1.2 7-4.5 7-9V6z"/>'
        '<rect x="9.5" y="11" width="5" height="4" rx="1"/>'
        '<path d="M10.5 11V9.5a1.5 1.5 0 0 1 3 0V11"/>'
    ),
    "calidad": (
        '<path d="M12 3l2.2 2.2 3.1-.4.4 3.1L20 10l-2.2 2.2.4 3.1-3.1.4L12 18l-3.1-.3-.4-3.1L6.2 12l.4-3.1L4 6.7l3.1.4L9.8 5z"/>'
        '<path d="m9.5 11.2 1.8 1.8 3.4-3.5"/>'
    ),
    # Process & principles
    "compass": (
        '<circle cx="12" cy="12" r="9"/>'
        '<polygon points="15.5,8.5 13.3,13.3 8.5,15.5 10.7,10.7"/>'
    ),
    "flask": (
        '<path d="M9 3h6"/>'
        '<path d="M10 3v5.5L5.2 17a2 2 0 0 0 1.7 3h10.2a2 2 0 0 0 1.7-3L14 8.5V3"/>'
        '<path d="M7.5 14h9"/>'
    ),
    "cubes": (
        '<path d="m12 3 7 4v10l-7 4-7-4V7z"/>'
        '<path d="M12 12 5 7"/>'
        '<path d="m12 12 7-5"/>'
        '<path d="M12 12v9"/>'
    ),
    "shield-check": (
        '<path d="M12 3 5 6v6c0 4.5 3 7.8 7 9 4-1.2 7-4.5 7-9V6z"/>'
        '<path d="m9.5 12 1.8 1.8 3.5-3.6"/>'
    ),
    # UI & actions
    "play": (
        '<polygon points="7,5 19,12 7,19"/>'
    ),
    "check": (
        '<path d="m5 12.5 4.2 4.2L19 7"/>'
    ),
    "arrow-right": (
        '<path d="M5 12h14"/>'
        '<path d="m13 6 6 6-6 6"/>'
    ),
    "arrow-up-right": (
        '<path d="M7 17 17 7"/>'
        '<path d="M8 7h9v9"/>'
    ),
    "mail": (
        '<rect x="3" y="5" width="18" height="14" rx="2"/>'
        '<path d="m3.5 7 8.5 6 8.5-6"/>'
    ),
    "github": (
        '<path d="M9 19c-4 1.2-4-2-5.5-2.5"/>'
        '<path d="M15 21v-3.5a3 3 0 0 0-.9-2.4c3-.3 6.1-1.5 6.1-6.6a5.2 5.2 0 0 0-1.4-3.6 4.8 4.8 0 0 0-.1-3.5s-1.1-.4-3.7 1.4a12.8 12.8 0 0 0-6.8 0C5.6 1 4.5 1.4 4.5 1.4a4.8 4.8 0 0 0-.1 3.5A5.2 5.2 0 0 0 3 8.5c0 5.1 3.1 6.3 6.1 6.6a3 3 0 0 0-.9 2.4V21"/>'
    ),
    "instagram": (
        '<rect x="3" y="3" width="18" height="18" rx="5"/>'
        '<circle cx="12" cy="12" r="4"/>'
        '<circle cx="17.5" cy="6.5" r="0.8" fill="currentColor" stroke="none"/>'
    ),
    "map-pin": (
        '<path d="M12 21s-6-5.3-6-10a6 6 0 1 1 12 0c0 4.7-6 10-6 10z"/>'
        '<circle cx="12" cy="11" r="2"/>'
    ),
    "sparkles": (
        '<path d="m12 3 1.4 4.1L17.5 8.5l-4.1 1.4L12 14l-1.4-4.1L6.5 8.5l4.1-1.4z"/>'
        '<path d="M18.5 15l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>'
    ),
    "book-open": (
        '<path d="M3 6.5A2.5 2.5 0 0 1 5.5 4H12v15H5.5A2.5 2.5 0 0 0 3 21z"/>'
        '<path d="M21 6.5A2.5 2.5 0 0 0 18.5 4H12v15h6.5A2.5 2.5 0 0 1 21 21z"/>'
    ),
    "award": (
        '<circle cx="12" cy="8.5" r="5"/>'
        '<path d="M8.5 13 7 21l5-2.5L17 21l-1.5-8"/>'
    ),
}


def icon(name: str, cls: str = "ui-icon") -> str:
    """Return an accessible inline SVG icon without duplicate IDs."""
    body = ICONS.get(name)
    if not body:
        return ""
    safe_cls = html.escape(cls, quote=True)
    return (
        f'<svg class="{safe_cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        f'stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
        f"{body}</svg>"
    )

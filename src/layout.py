"""Shared HTML document layout, navigation, JSON-LD, and reusable UI blocks."""

import html
import json
from src.data import NAV_ITEMS, SITE
from src.icons import icon


LOGO_SVG = (
    '<svg viewBox="0 0 40 40" aria-hidden="true">'
    '<path fill="currentColor" d="M7 6h5.2l15.6 20.6V6H33v28h-5.2L12.2 13.4V34H7z"/>'
    "</svg>"
)


def orbit_art(uid: str) -> str:
    """Decorative planet with tilted orbits and moons; uid keeps gradient ids unique per page."""
    orbits = "".join(
        f'<ellipse rx="{rx}" ry="{ry}" fill="none" stroke="currentColor" stroke-opacity="0.2" stroke-dasharray="{dash}"/>'
        f'<circle r="{r}" fill="{fill}"><animateMotion dur="{dur}s" begin="-{begin}s" repeatCount="indefinite" '
        f'path="M{rx},0 A{rx},{ry} 0 1,1 -{rx},0 A{rx},{ry} 0 1,1 {rx},0"/></circle>'
        for rx, ry, r, fill, dur, begin, dash in (
            (88, 34, 4, "#e8a84a", 16, 3, "none"),
            (132, 52, 6, "#5b6cff", 26, 11, "2 7"),
            (182, 72, 3.5, "#2fa58c", 40, 22, "none"),
        )
    )
    return (
        f'<svg class="orbit-art" viewBox="-200 -200 400 400" aria-hidden="true" focusable="false">'
        f'<defs><linearGradient id="{uid}-planet" x1="0" y1="0" x2="1" y2="1">'
        f'<stop offset="0" stop-color="#5b6cff"/><stop offset="0.55" stop-color="#965feb"/><stop offset="1" stop-color="#d97757"/>'
        f'</linearGradient><radialGradient id="{uid}-glow">'
        f'<stop offset="0" stop-color="#965feb" stop-opacity="0.4"/><stop offset="1" stop-color="#965feb" stop-opacity="0"/>'
        f'</radialGradient></defs>'
        f'<circle r="120" fill="url(#{uid}-glow)"/>'
        f'<g transform="rotate(-18)">{orbits}'
        f'<g class="orbit-planet"><circle r="30" fill="url(#{uid}-planet)"/>'
        f'<ellipse rx="50" ry="11" fill="none" stroke="#e8a84a" stroke-opacity="0.75" stroke-width="2.5"/>'
        f'<path d="M-30,0 A30,30 0 0,1 30,0 Z" fill="url(#{uid}-planet)"/></g>'
        f'</g></svg>'
    )


def esc(value: str) -> str:
    """Escape HTML special characters safely."""
    return html.escape(value, quote=True)


def render_json_ld() -> str:
    """Return structured ProfessionalService schema JSON-LD."""
    payload = {
        "@context": "https://schema.org",
        "@type": "ProfessionalService",
        "name": SITE["name"],
        "url": f"{SITE['base_url']}/",
        "description": (
            "Consultora mexicana de ingeniería y desarrollo de software: "
            "plataformas web, inferencia de modelos LLM, visión artificial, machine learning y análisis de datos."
        ),
        "email": SITE["email"],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "León",
            "addressRegion": "Guanajuato",
            "addressCountry": "MX",
        },
        "sameAs": [SITE["github"], SITE["instagram"]],
    }
    return json.dumps(payload, ensure_ascii=False, indent=2)


def render_nav(active_key: str) -> str:
    """Render clean sticky navigation bar and mobile drawer."""
    desktop_links = []
    mobile_links = []
    for item in NAV_ITEMS:
        current_attr = ' aria-current="page"' if item["key"] == active_key else ""
        desktop_links.append(
            f'<a class="nav-link" href="{esc(item["href"])}"{current_attr}>{esc(item["label"])}</a>'
        )
        mobile_links.append(
            f'<a class="mobile-menu-link" href="{esc(item["href"])}"{current_attr}>{esc(item["label"])}</a>'
        )

    home_current = ' aria-current="page"' if active_key == "home" else ""
    mailto_cta = f"mailto:{SITE['email']}?subject=Contacto%20Neuxora"

    return f"""  <a class="skip-link" href="#main">Saltar al contenido</a>
  <nav id="nav" aria-label="Navegación principal">
    <div class="nav-inner">
      <a class="brand-mark" href="index.html"{home_current} aria-label="Neuxora, inicio">
        {LOGO_SVG}
        <span class="brand-wordmark">Neuxora</span>
      </a>
      <div class="nav-links">
        {"".join(desktop_links)}
        <a class="nav-cta" href="{mailto_cta}">{icon("mail", "ui-icon ui-icon--sm")}<span>Contacto</span></a>
      </div>
      <button class="nav-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="mobile-menu">
        <span class="nav-toggle-bars" aria-hidden="true"><span></span><span></span></span>
      </button>
    </div>
  </nav>
  <aside class="mobile-menu" id="mobile-menu" aria-hidden="true" aria-label="Menú móvil">
    <nav class="mobile-menu-list">
      {"".join(mobile_links)}
      <a class="mobile-menu-link" href="{mailto_cta}">Contacto</a>
    </nav>
    <div class="mobile-menu-meta">
      <span class="meta-line">{icon("map-pin", "ui-icon ui-icon--sm")}<span>{esc(SITE['location'])}</span></span>
      <span class="meta-line">{icon("mail", "ui-icon ui-icon--sm")}<span>{esc(SITE['email'])}</span></span>
    </div>
  </aside>"""


def render_footer() -> str:
    """Render clean dark footer."""
    return f"""  <footer class="footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <a class="brand-mark" href="index.html">
            {LOGO_SVG}
            <span class="brand-wordmark">Neuxora</span>
          </a>
          <p class="footer-tagline">Consultora de ingeniería, desarrollo de productos e investigación aplicada en {esc(SITE['location'])}.</p>
        </div>
        <div>
          <span class="footer-label">Servicios</span>
          <a class="footer-link" href="index.html#servicios">Desarrollo de Plataformas</a>
          <a class="footer-link" href="index.html#servicios">Inferencia de modelos LLM</a>
          <a class="footer-link" href="index.html#servicios">Visión Artificial</a>
          <a class="footer-link" href="index.html#servicios">Machine Learning</a>
          <a class="footer-link" href="index.html#servicios">Análisis de Datos</a>
        </div>
        <div>
          <span class="footer-label">Proyectos</span>
          <a class="footer-link" href="proyecto-idiomas-ug.html">Web-App Idiomas UG</a>
          <a class="footer-link" href="proyecto-sillas-rotary.html">Sillas Rotary</a>
          <a class="footer-link" href="proyectos.html#medscan">medscan CLI</a>
          <a class="footer-link" href="proyectos.html#webdiabetes">WebDiabetes DM</a>
          <a class="footer-link" href="investigacion.html#mamba">Mamba-UNet</a>
        </div>
        <div>
          <span class="footer-label">Explorar</span>
          <a class="footer-link" href="proyectos.html">Proyectos</a>
          <a class="footer-link" href="noticias.html">Cuaderno</a>
          <a class="footer-link" href="neuxora.html">Nosotros</a>
          <a class="footer-link" href="mailto:{esc(SITE['email'])}">{esc(SITE['email'])}</a>
          <a class="footer-link" href="{esc(SITE['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a>
          <a class="footer-link" href="{esc(SITE['instagram'])}" target="_blank" rel="noopener noreferrer">Instagram</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>© <span id="year">2026</span> {esc(SITE['name'])}</span>
        <span>{esc(SITE['location'])}</span>
      </div>
    </div>
  </footer>"""


def render_overlays() -> str:
    """Shared native dialogs (contact, photo lightbox) and the back-to-top control."""
    email = esc(SITE["email"])
    return f"""  <dialog class="modal" id="contact-dialog" aria-labelledby="contact-dialog-title">
    <form method="dialog"><button class="modal-close" aria-label="Cerrar">{icon("close", "ui-icon")}</button></form>
    <span class="eyebrow"><span class="kicker-dot" aria-hidden="true"></span>Contacto</span>
    <h2 class="modal-title" id="contact-dialog-title">Platiquemos sobre tu proyecto.</h2>
    <p class="modal-copy">Cuéntanos qué necesitas resolver y te respondemos con una propuesta clara de trabajo por etapas.</p>
    <div class="modal-actions">
      <a class="btn btn-primary" data-contact-mail href="mailto:{email}">{icon("mail", "ui-icon ui-icon--sm")}<span>Escribir por correo</span></a>
      <button type="button" class="btn btn-secondary" data-copy="{email}"><span data-copy-label>Copiar {email}</span></button>
    </div>
    <div class="modal-links">
      <a class="text-link" href="{esc(SITE['github'])}" target="_blank" rel="noopener noreferrer">GitHub</a>
      <a class="text-link" href="{esc(SITE['instagram'])}" target="_blank" rel="noopener noreferrer">Instagram</a>
      <span class="modal-meta">{esc(SITE['location'])}</span>
    </div>
  </dialog>
  <dialog class="modal modal--media" id="lightbox" aria-label="Foto ampliada">
    <form method="dialog"><button class="modal-close" aria-label="Cerrar">{icon("close", "ui-icon")}</button></form>
    <img data-lightbox-img src="assets/logo-n.svg" alt="">
    <p class="modal-caption" data-lightbox-caption></p>
  </dialog>
  <a class="to-top" href="#main" aria-label="Volver arriba">{icon("arrow-up", "ui-icon")}</a>"""


def render_cta_section(eyebrow: str = "Contacto", title: str = "Platiquemos sobre lo que necesitas construir.") -> str:
    """Render shared conversion CTA section with natural copy and crisp SVG icons."""
    email = SITE["email"]
    return f"""    <section class="section" aria-labelledby="cta-conversion">
      <div class="container">
        <div class="cta-panel reveal" data-spotlight-card>
          {orbit_art("orbit-cta")}
          <div>
            <span class="eyebrow"><span class="kicker-dot" aria-hidden="true"></span>{esc(eyebrow)}</span>
            <h2 class="section-title" id="cta-conversion">{esc(title)}</h2>
            <p class="section-intro">Cuéntanos cómo funciona hoy tu proceso, qué datos tienes y qué necesitas resolver. Te respondemos con una propuesta clara de trabajo por etapas.</p>
            <div class="hero-actions">
              <a class="btn btn-primary" href="mailto:{email}?subject=Platicar%20sobre%20un%20proyecto">{icon("mail", "ui-icon ui-icon--sm")}<span>Escribir por correo</span></a>
              <a class="btn btn-secondary" href="{esc(SITE['github'])}" target="_blank" rel="noopener noreferrer">{icon("github", "ui-icon ui-icon--sm")}<span>Ver repositorios en GitHub</span></a>
            </div>
          </div>
          <div class="cta-quick-links" aria-label="Consultas por especialidad">
            <a class="cta-option" href="mailto:{email}?subject=Consulta%20-%20Desarrollo%20de%20Plataforma">
              <span class="cta-option-label"><span class="icon-badge icon-badge--sm">{icon("plataformas")}</span><span>Desarrollo de Plataformas</span></span>
              <span class="cta-option-arrow" aria-hidden="true">{icon("arrow-right", "ui-icon ui-icon--sm")}</span>
            </a>
            <a class="cta-option" href="mailto:{email}?subject=Consulta%20-%20Inferencia%20de%20modelos%20LLM">
              <span class="cta-option-label"><span class="icon-badge icon-badge--sm">{icon("llm")}</span><span>Inferencia de modelos LLM</span></span>
              <span class="cta-option-arrow" aria-hidden="true">{icon("arrow-right", "ui-icon ui-icon--sm")}</span>
            </a>
            <a class="cta-option" href="mailto:{email}?subject=Consulta%20-%20Visi%C3%B3n%20Artificial%20y%20ML">
              <span class="cta-option-label"><span class="icon-badge icon-badge--sm">{icon("vision")}</span><span>Visión Artificial y Machine Learning</span></span>
              <span class="cta-option-arrow" aria-hidden="true">{icon("arrow-right", "ui-icon ui-icon--sm")}</span>
            </a>
            <a class="cta-option" href="mailto:{email}?subject=Consulta%20-%20An%C3%A1lisis%20de%20Datos">
              <span class="cta-option-label"><span class="icon-badge icon-badge--sm">{icon("datos")}</span><span>Análisis de Datos</span></span>
              <span class="cta-option-arrow" aria-hidden="true">{icon("arrow-right", "ui-icon ui-icon--sm")}</span>
            </a>
          </div>
        </div>
      </div>
    </section>"""


def render_page(
    *,
    title: str,
    description: str,
    slug: str,
    active_key: str,
    body_html: str,
    og_type: str = "website",
    robots: str = "index, follow",
    extra_head: str = "",
) -> str:
    """Wrap page body inside a complete, accessible HTML5 document."""
    canonical_url = f"{SITE['base_url']}/" if slug == "index.html" else f"{SITE['base_url']}/{slug}"
    og_image_url = f"{SITE['base_url']}/assets/og-image.svg"
    head_extra = f"\n  {extra_head}" if extra_head else ""

    return f"""<!doctype html>
<html lang="es-MX">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}">
  <meta name="theme-color" content="{esc(SITE['theme_color'])}">
  <meta name="robots" content="{esc(robots)}">
  <link rel="canonical" href="{esc(canonical_url)}">
  <meta property="og:site_name" content="{esc(SITE['name'])}">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(description)}">
  <meta property="og:type" content="{esc(og_type)}">
  <meta property="og:url" content="{esc(canonical_url)}">
  <meta property="og:image" content="{esc(og_image_url)}">
  <meta property="og:locale" content="es_MX">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)}">
  <meta name="twitter:description" content="{esc(description)}">
  <meta name="twitter:image" content="{esc(og_image_url)}">
  <link rel="icon" href="assets/logo-n.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=JetBrains+Mono:wght@400;500&amp;family=Plus+Jakarta+Sans:wght@500;600;700&amp;display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/neuxora.css">
  <script type="application/ld+json">
{render_json_ld()}
  </script>{head_extra}
  <script defer src="assets/nav.js"></script>
</head>
<body>
{render_nav(active_key)}

  <main id="main">
{body_html}
  </main>

{render_footer()}
{render_overlays()}
</body>
</html>
"""

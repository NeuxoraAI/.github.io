"""Projects and proprietary products catalog page."""

from src.data import PROJECTS
from src.icons import icon
from src.layout import esc, render_cta_section


def render_projects() -> str:
    """Render clean filterable catalog of systems, CLI products, and benchmarks."""
    cards_html = []
    for proj in PROJECTS:
        cats = " ".join(proj["categories"])
        target_attr = "" if proj["internal"] else ' target="_blank" rel="noopener noreferrer"'
        link_cls = "text-link internal" if proj["internal"] else "text-link"
        badge_cls = f' {proj["badge_class"]}' if proj["badge_class"] else ""

        cards_html.append(
            f'<article class="surface-card" id="{esc(proj["id"])}" '
            f'data-filter-item data-categories="{esc(cats)}" data-spotlight-card>'
            f"<div>"
            f'<div class="card-meta">'
            f'<span class="card-meta-cat"><span class="icon-badge icon-badge--sm">{icon(proj["icon"])}</span><span>{esc(proj["category_label"])}</span></span>'
            f'<span class="card-badge{badge_cls}">{esc(proj["status"])}</span>'
            f"</div>"
            f'<h2>{esc(proj["title"])}</h2>'
            f'<p>{esc(proj["summary"])}</p>'
            f"</div>"
            f'<div class="card-footer">'
            f'<span class="stack-line">{esc(proj["context_line"])}</span>'
            f'<a class="{link_cls}" href="{esc(proj["href"])}"{target_attr}>{esc(proj["cta"])}</a>'
            f"</div>"
            f"</article>"
        )

    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container hero-header-split">
        <div>
          <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Proyectos y herramientas</span>
          <h1 class="page-title">Sistemas, prototipos y herramientas aplicadas.</h1>
        </div>
        <p class="hero-lede">Aquí reunimos lo que está en construcción activa, lo que ya está documentado y los experimentos que compartimos de forma abierta.</p>
      </div>
    </header>

    <section class="section section-subtle" aria-labelledby="catalogo-titulo" data-filter-group>
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Portafolio</span>
            <h2 class="section-title" id="catalogo-titulo">Filtrar por tipo de proyecto.</h2>
          </div>
          <div class="filter-bar" role="group" aria-label="Filtrar proyectos por categoría" data-sliding-tabs>
            <button type="button" class="filter-btn" data-filter="all" aria-pressed="true">Todos</button>
            <button type="button" class="filter-btn" data-filter="plataformas" aria-pressed="false">Plataformas</button>
            <button type="button" class="filter-btn" data-filter="vision-ml" aria-pressed="false">Visión y ML</button>
            <button type="button" class="filter-btn" data-filter="cli" aria-pressed="false">Digitalización</button>
            <button type="button" class="filter-btn" data-filter="datos" aria-pressed="false">Datos</button>
          </div>
        </div>

        <div class="card-grid-2 reveal">
          {"".join(cards_html)}
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="taxonomia-titulo">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Sobre el estado</span>
          <h2 class="section-title" id="taxonomia-titulo">Qué significa cada etiqueta.</h2>
          <p class="section-intro">Publicar avances muestra cómo operan nuestros proyectos en la práctica; no reemplaza las mediciones de uso cuando una plataforma apenas arranca.</p>
        </div>
        <div class="grid-3 reveal">
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("check")}</span>
                <span class="card-category">Documentado</span>
              </div>
              <h3>Sistema completo</h3>
              <p>El proyecto completo, su flujo de trabajo y sus pantallas están documentados para revisarse.</p>
            </div>
          </article>
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("sparkles")}</span>
                <span class="card-category">En construcción</span>
              </div>
              <h3>Trabajo activo</h3>
              <p>Plataforma en desarrollo continuo o prototipo listo para pruebas de campo y retroalimentación.</p>
            </div>
          </article>
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("flask")}</span>
                <span class="card-category">Experimento</span>
              </div>
              <h3>Comparativa abierta</h3>
              <p>Pruebas reproducibles con conjuntos públicos, métricas completas y alcance declarado.</p>
            </div>
          </article>
        </div>
      </div>
    </section>

{render_cta_section("Contacto", "¿Tienes en mente una plataforma o herramienta similar?")}"""

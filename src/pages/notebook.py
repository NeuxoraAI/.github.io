"""Technical notebook and verified external mentions page (Cuaderno)."""

from src.icons import icon
from src.layout import render_cta_section


def render_notebook() -> str:
    """Render Cuaderno Neuxora with interactive category filters."""
    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container hero-header-split">
        <div>
          <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Cuaderno</span>
          <h1 class="page-title">Notas de proyectos, pruebas y menciones.</h1>
        </div>
        <p class="hero-lede">Apuntes técnicos sobre cómo armamos cada sistema, experimentos abiertos y publicaciones externas donde aparece nuestro trabajo.</p>
      </div>
    </header>

    <section class="section section-subtle" aria-labelledby="cuaderno-entradas" data-filter-group>
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Entradas</span>
            <h2 class="section-title" id="cuaderno-entradas">Trabajo abierto para revisar.</h2>
          </div>
          <div class="filter-bar" role="group" aria-label="Filtrar notas del cuaderno" data-sliding-tabs>
            <button type="button" class="filter-btn" data-filter="all" aria-pressed="true">Todo</button>
            <button type="button" class="filter-btn" data-filter="caso" aria-pressed="false">Casos</button>
            <button type="button" class="filter-btn" data-filter="experimento" aria-pressed="false">Experimentos</button>
            <button type="button" class="filter-btn" data-filter="herramienta" aria-pressed="false">Herramientas</button>
            <button type="button" class="filter-btn" data-filter="mencion" aria-pressed="false">Menciones</button>
          </div>
        </div>

        <div class="grid-3 reveal">
          <article class="card-panel" data-filter-item data-categories="caso" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("idiomas")}</span>
                <span class="card-category">Caso en curso</span>
              </div>
              <h3>Plataforma para exámenes de idiomas UG.</h3>
              <p>Cómo organizamos el registro de sustentantes, la aplicación por idioma y nivel, el control de intentos y la auditoría para el Departamento de Idiomas Campus León.</p>
            </div>
            <a class="text-link internal" href="proyecto-idiomas-ug.html">Ver caso</a>
          </article>

          <article class="card-panel" data-filter-item data-categories="caso mencion" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("rotary")}</span>
                <span class="card-category">Caso de proyecto · 2 menciones</span>
              </div>
              <h3>Sillas Rotary: del formulario en papel a un expediente conectado.</h3>
              <p>Captura pensada para celular, fotografía vinculada y seguimiento centralizado para el programa «200 sillas para 200 campeones». La entrega y el reconocimiento a la Universidad de Guanajuato como aliada estratégica fueron publicados por Ecosistema VIDA UG y el Club Rotario Bajío.</p>
            </div>
            <div class="card-links">
              <a class="text-link internal" href="proyecto-sillas-rotary.html">Ver caso y fotos</a>
              <a class="text-link" href="https://www.facebook.com/share/19EhFHTa9H/" target="_blank" rel="noopener noreferrer">Publicación de la entrega</a>
              <a class="text-link" href="https://www.facebook.com/share/p/19BtT6cZnh/" target="_blank" rel="noopener noreferrer">Reconocimiento a la UG</a>
            </div>
          </article>

          <article class="card-panel" data-filter-item data-categories="experimento" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("mamba")}</span>
                <span class="card-category">Experimento</span>
              </div>
              <h3>Qué cambia entre U-Net y Mamba-UNet.</h3>
              <p>Lectura de Dice, IoU, pérdida de validación y especificidad sobre 670 pares de BBBC038, y por qué una sola métrica no basta.</p>
            </div>
            <a class="text-link internal" href="investigacion.html#mamba">Ver comparativa</a>
          </article>

          <article class="card-panel" data-filter-item data-categories="herramienta" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("medscan")}</span>
                <span class="card-category">Digitalización</span>
              </div>
              <h3>Extraer expedientes desde fotografías.</h3>
              <p>medscan CLI prepara imágenes localmente, ordena los datos clave del documento y los guarda para consulta sin salir del equipo.</p>
            </div>
            <a class="text-link" href="https://github.com/NeuxoraAI/medscan-CLI" target="_blank" rel="noopener noreferrer">Ver repositorio</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="criterio-editorial">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Organización</span>
          <h2 class="section-title" id="criterio-editorial">Qué incluye cada categoría.</h2>
        </div>
        <dl class="spec-list">
          <div class="spec-row"><dt>Caso</dt><dd>Explica el problema, cómo está construido el sistema, qué código está disponible y sus alcances actuales.</dd></div>
          <div class="spec-row"><dt>Experimento</dt><dd>Presenta la pregunta, los datos usados, las métricas completas y hasta dónde aplica el resultado.</dd></div>
          <div class="spec-row"><dt>Herramienta</dt><dd>Describe utilidades de consola o librerías propias junto a su repositorio.</dd></div>
          <div class="spec-row"><dt>Publicación</dt><dd>Se reserva para artículos o preprints con enlace estable (todavía sin publicaciones formales listadas).</dd></div>
        </dl>
      </div>
    </section>

{render_cta_section("Contacto", "¿Quieres revisar alguno de los proyectos o platicar sobre un problema?")}"""

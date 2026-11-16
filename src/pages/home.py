"""Landing page builder for Neuxora."""

from src.data import IDIOMAS_MODULES, PROJECTS, SERVICES
from src.icons import icon
from src.layout import esc, orbit_art, render_cta_section


def _render_hero_showcase() -> str:
    """Build the clean, dark-surface product showcase below the centered hero."""
    arch_buttons = []
    for idx, mod in enumerate(IDIOMAS_MODULES):
        active_cls = " is-active" if idx == 0 else ""
        pressed = "true" if idx == 0 else "false"
        arch_buttons.append(
            f'<button type="button" class="arch-node{active_cls}" data-arch-node '
            f'aria-pressed="{pressed}" data-node-icon="{esc(mod["icon"])}" '
            f'data-node-title="{esc(mod["name"])}" '
            f'data-node-desc="{esc(mod["desc"])}">'
            f'{icon(mod["icon"], "ui-icon ui-icon--sm")}<span>{esc(mod["name"])}</span></button>'
        )

    default_mod = IDIOMAS_MODULES[0]

    return f"""        <div class="showcase-wrap">
          <div class="showcase" aria-label="Ejemplos interactivos de proyectos Neuxora">
            <div class="showcase-toolbar">
              <div class="showcase-toolbar-left">
                <div class="showcase-chrome" aria-hidden="true"><span></span><span></span><span></span></div>
                <div class="showcase-tabs" role="tablist" aria-label="Proyectos en vista previa" data-sliding-tabs>
                  <button type="button" class="showcase-tab" role="tab" id="wb-tab-idiomas" aria-selected="true" aria-controls="wb-panel-idiomas" data-workbench-tab="idiomas">{icon("idiomas", "ui-icon ui-icon--sm")}<span>Idiomas UG</span></button>
                  <button type="button" class="showcase-tab" role="tab" id="wb-tab-rotary" aria-selected="false" aria-controls="wb-panel-rotary" data-workbench-tab="rotary">{icon("rotary", "ui-icon ui-icon--sm")}<span>Sillas Rotary</span></button>
                  <button type="button" class="showcase-tab" role="tab" id="wb-tab-medscan" aria-selected="false" aria-controls="wb-panel-medscan" data-workbench-tab="medscan">{icon("medscan", "ui-icon ui-icon--sm")}<span>medscan CLI</span></button>
                  <button type="button" class="showcase-tab" role="tab" id="wb-tab-mamba" aria-selected="false" aria-controls="wb-panel-mamba" data-workbench-tab="mamba">{icon("mamba", "ui-icon ui-icon--sm")}<span>Mamba-UNet</span></button>
                </div>
              </div>
              <button type="button" class="showcase-action" data-terminal-replay>{icon("play", "ui-icon ui-icon--sm")}<span>Ver demostración</span></button>
            </div>

            <div role="tabpanel" id="wb-panel-idiomas" aria-labelledby="wb-tab-idiomas" data-workbench-panel="idiomas">
              <div class="showcase-grid">
                <div class="showcase-copy">
                  <span class="showcase-label">En construcción · Universidad de Guanajuato</span>
                  <h2>Plataforma para exámenes de regularización de idiomas.</h2>
                  <p>La estamos construyendo para el Departamento de Idiomas de la Universidad de Guanajuato, Campus León, para gestionar sustentantes, aplicación de exámenes por nivel, control de intentos y seguimiento administrativo.</p>
                  <a class="text-link internal" href="proyecto-idiomas-ug.html">Ver cómo funciona</a>
                </div>
                <div class="showcase-artifact" data-arch-inspector>
                  <div class="arch-nodes" aria-label="Módulos de Idiomas UG">
                    {"".join(arch_buttons)}
                  </div>
                  <div class="arch-detail" data-arch-detail aria-live="polite">
                    <strong>{esc(default_mod["name"])}: </strong>{esc(default_mod["desc"])}
                  </div>
                </div>
              </div>
            </div>

            <div role="tabpanel" id="wb-panel-rotary" aria-labelledby="wb-tab-rotary" data-workbench-panel="rotary" hidden>
              <div class="showcase-grid">
                <div class="showcase-copy">
                  <span class="showcase-label">Sistema documentado · Trabajo en campo</span>
                  <h2>Registro digital de expedientes para trabajo en campo.</h2>
                  <p>Reemplaza los formularios en papel por captura desde el celular con estudios socioeconómicos, medidas técnicas y fotografías vinculadas dentro del programa «200 sillas para 200 campeones».</p>
                  <a class="text-link internal" href="proyecto-sillas-rotary.html">Ver caso y galería de fotos</a>
                </div>
                <div class="showcase-artifact">
                  <div class="showcase-media-pair">
                    <figure class="showcase-media">
                      <img src="assets/img/rotary/equipo-neuxora.jpg" alt="Equipo completo de Neuxora con reconocimiento del programa 200 sillas para 200 campeones" loading="lazy">
                      <figcaption>El equipo de Neuxora con el reconocimiento recibido.</figcaption>
                    </figure>
                    <figure class="showcase-media">
                      <img src="assets/img/rotary/presentacion-proyecto.jpg" alt="Presentación del proyecto Sillas Rotary con Neuxora y Ecosistema VIDA UG" loading="lazy">
                      <figcaption>Presentación junto a Ecosistema VIDA UG.</figcaption>
                    </figure>
                  </div>
                </div>
              </div>
            </div>

            <div role="tabpanel" id="wb-panel-medscan" aria-labelledby="wb-tab-medscan" data-workbench-panel="medscan" hidden>
              <div class="showcase-grid">
                <div class="showcase-copy">
                  <span class="showcase-label">Open Source · Visión y datos</span>
                  <h2>Extraer datos desde fotografías de expedientes.</h2>
                  <p>Herramienta abierta que limpia fotografías de expedientes, ordena la información clave en texto estructurado y la guarda en local lista para consultar.</p>
                  <a class="text-link" href="https://github.com/NeuxoraAI/medscan-CLI" target="_blank" rel="noopener noreferrer">Ver en GitHub</a>
                </div>
                <div class="showcase-artifact">
                  <div class="terminal-log" data-terminal-stream>
                    <span class="term-line"><span class="term-prompt">$</span> <span class="term-cmd">medscan process ./expediente_042.jpg</span></span>
                    <span class="term-line">Imagen preparada localmente</span>
                    <span class="term-line">Campos extraídos y ordenados</span>
                    <span class="term-line"><span class="term-ok">Registro #42 guardado en local</span></span>
                    <pre class="term-json term-line">{{
  "expediente": "EXP-042",
  "estado": "guardado localmente"
}}</pre>
                  </div>
                </div>
              </div>
            </div>

            <div role="tabpanel" id="wb-panel-mamba" aria-labelledby="wb-tab-mamba" data-workbench-panel="mamba" hidden>
              <div class="showcase-grid">
                <div class="showcase-copy">
                  <span class="showcase-label">Experimento abierto · Dataset BBBC038</span>
                  <h2>Comparación de U-Net y Mamba-UNet en segmentación celular.</h2>
                  <p>Probamos ambas redes neuronales con los mismos 670 pares de imágenes del conjunto público BBBC038 para ver qué cambia entre Dice, IoU, pérdida de validación, precisión y especificidad.</p>
                  <a class="text-link internal" href="investigacion.html#mamba">Ver resultados completos</a>
                </div>
                <div class="showcase-artifact">
                  <div class="metric-rows">
                    <div>
                      <div class="metric-item-head">
                        <span>Solapamiento (Dice / IoU)</span>
                        <span class="metric-winner">Mejor: U-Net</span>
                      </div>
                      <div class="metric-bars">
                        <div class="metric-bar-row">
                          <span>U-Net</span>
                          <div class="metric-track"><div class="metric-fill metric-fill--unet" style="width:88%"></div></div>
                          <span>Mayor Dice / IoU</span>
                        </div>
                        <div class="metric-bar-row">
                          <span>Mamba-UNet</span>
                          <div class="metric-track"><div class="metric-fill metric-fill--mamba" style="width:81%"></div></div>
                          <span>Comparada</span>
                        </div>
                      </div>
                    </div>
                    <div>
                      <div class="metric-item-head">
                        <span>Pérdida de validación, Precisión y Especificidad</span>
                        <span class="metric-tradeoff">Mejor: Mamba-UNet</span>
                      </div>
                      <div class="metric-bars">
                        <div class="metric-bar-row">
                          <span>Mamba-UNet</span>
                          <div class="metric-track"><div class="metric-fill metric-fill--mamba" style="width:90%"></div></div>
                          <span>Menor val. loss</span>
                        </div>
                        <div class="metric-bar-row">
                          <span>U-Net</span>
                          <div class="metric-track"><div class="metric-fill metric-fill--unet" style="width:82%"></div></div>
                          <span>Referencia</span>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>"""


def _render_services_section() -> str:
    """Render the clean 5-vertical engineering capabilities selector."""
    tabs_html = []
    panels_html = []

    for idx, svc in enumerate(SERVICES):
        selected = "true" if idx == 0 else "false"
        tabindex = "0" if idx == 0 else "-1"
        hidden_attr = "" if idx == 0 else " hidden"

        tabs_html.append(
            f'<button type="button" class="service-tab" role="tab" '
            f'id="svc-tab-{svc["id"]}" aria-selected="{selected}" tabindex="{tabindex}" '
            f'aria-controls="svc-panel-{svc["id"]}" data-service-tab="{svc["id"]}">'
            f'{icon(svc["icon"], "ui-icon ui-icon--sm")}<span>{esc(svc["short"])}</span>'
            f"</button>"
        )

        use_cases_li = "".join(
            f'<li>{icon("check", "ui-icon ui-icon--check")}<span>{esc(item)}</span></li>'
            for item in svc["use_cases"]
        )
        deliv_li = "".join(
            f'<li>{icon("check", "ui-icon ui-icon--check")}<span>{esc(item)}</span></li>'
            for item in svc["deliverables"]
        )
        links_html = "".join(
            f'<a class="text-link{" internal" if link["internal"] else ""}" '
            f'href="{esc(link["href"])}"'
            f'{"" if link["internal"] or link["href"].startswith("mailto:") else " target=\"_blank\" rel=\"noopener noreferrer\""}>'
            f'{esc(link["label"])}</a>'
            for link in svc["evidence_links"]
        )

        panels_html.append(
            f'<article class="service-panel" role="tabpanel" id="svc-panel-{svc["id"]}" '
            f'aria-labelledby="svc-tab-{svc["id"]}" data-service-panel="{svc["id"]}" data-spotlight-card{hidden_attr}>'
            f"<div>"
            f'<div class="service-panel-head">'
            f'<span class="icon-badge icon-badge--lg">{icon(svc["icon"])}</span>'
            f'<span class="eyebrow" style="margin-bottom:0">{esc(svc["short"])}</span>'
            f"</div>"
            f'<h3>{esc(svc["title"])}</h3>'
            f'<p class="service-panel-lead">{esc(svc["lead"])}</p>'
            f'<div style="display:flex;flex-wrap:wrap;gap:1.25rem">{links_html}</div>'
            f"</div>"
            f'<div class="service-specs">'
            f'<div class="service-spec-block"><h4>Problemas que resolvemos</h4><ul class="spec-check-list">{use_cases_li}</ul></div>'
            f'<div class="service-spec-block"><h4>Qué incluye el trabajo</h4><ul class="spec-check-list">{deliv_li}</ul></div>'
            f"</div>"
            f"</article>"
        )

    return f"""    <section class="section section-subtle" id="servicios" aria-labelledby="servicios-heading">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Qué hacemos</span>
            <h2 class="section-title" id="servicios-heading">Cinco áreas de trabajo.</h2>
          </div>
          <p class="section-intro">Unimos desarrollo web, modelos de lenguaje y ciencia de datos según lo que necesite el proyecto.</p>
        </div>
        <div class="reveal">
          <div class="service-pills" role="tablist" aria-label="Áreas de trabajo en Neuxora" data-sliding-tabs>
            {"".join(tabs_html)}
          </div>
          {"".join(panels_html)}
        </div>
      </div>
    </section>"""


def _render_featured_projects() -> str:
    """Render clean 2-column white surface cards for core projects."""
    featured = PROJECTS[:4]
    cards = []
    for proj in featured:
        target_attr = "" if proj["internal"] else ' target="_blank" rel="noopener noreferrer"'
        link_cls = "text-link internal" if proj["internal"] else "text-link"
        badge_cls = f' {proj["badge_class"]}' if proj["badge_class"] else ""
        cards.append(
            f'<article class="surface-card" data-spotlight-card>'
            f"<div>"
            f'<div class="card-meta">'
            f'<span class="card-meta-cat"><span class="icon-badge icon-badge--sm">{icon(proj["icon"])}</span><span>{esc(proj["category_label"])}</span></span>'
            f'<span class="card-badge{badge_cls}">{esc(proj["status"])}</span>'
            f"</div>"
            f'<h3>{esc(proj["title"])}</h3>'
            f'<p>{esc(proj["summary"])}</p>'
            f"</div>"
            f'<div class="card-footer">'
            f'<span class="stack-line">{esc(proj["context_line"])}</span>'
            f'<a class="{link_cls}" href="{esc(proj["href"])}"{target_attr}>{esc(proj["cta"])}</a>'
            f"</div>"
            f"</article>"
        )

    return f"""    <section class="section" id="sistemas" aria-labelledby="sistemas-heading">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Proyectos y herramientas</span>
            <h2 class="section-title" id="sistemas-heading">Lo que estamos construyendo.</h2>
          </div>
          <a class="btn btn-secondary" href="proyectos.html"><span>Ver todos los proyectos</span>{icon("arrow-right", "ui-icon ui-icon--sm")}</a>
        </div>
        <div class="card-grid-2 reveal">
          {"".join(cards)}
        </div>
      </div>
    </section>"""


def render_home() -> str:
    """Render the complete home page main body."""
    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container">
        <div class="hero-centered">
          <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Consultora de ingeniería y desarrollo de software</span>
          <h1 class="hero-title">Plataformas, modelos LLM, visión artificial y datos para problemas reales.</h1>
          <p class="hero-lede">Trabajamos como consultora de ingeniería y desarrollamos productos propios desde León, Guanajuato. Nuestro código, experimentos y proyectos están abiertos para que puedas revisarlos.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="mailto:neuxoraia@gmail.com?subject=Platicar%20sobre%20un%20proyecto">{icon("mail", "ui-icon ui-icon--sm")}<span>Platicar sobre un proyecto</span></a>
            <a class="btn btn-secondary" href="proyectos.html"><span>Ver proyectos</span>{icon("arrow-right", "ui-icon ui-icon--sm")}</a>
          </div>
        </div>

{_render_hero_showcase()}
      </div>
    </header>

    <section class="section statement" aria-labelledby="statement-heading">
      <div class="container reveal">
        <h2 class="statement-text" id="statement-heading">Neuxora es un equipo de ingeniería en León, Guanajuato, que construye plataformas, pone modelos en producción y comparte su trabajo de forma abierta.</h2>
      </div>
    </section>

{_render_services_section()}

{_render_featured_projects()}

    <section class="section section-dark" aria-labelledby="rd-heading">
      {orbit_art("orbit-rd")}
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Investigación aplicada</span>
          <h2 class="section-title" id="rd-heading">Probar antes de elegir una tecnología.</h2>
          <p class="section-intro">Cuando evaluamos modelos de visión artificial o machine learning, corremos experimentos con datos públicos y compartimos tanto en qué destaca cada opción como qué sacrifica.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="investigacion.html"><span>Ver experimentos</span>{icon("arrow-right", "ui-icon ui-icon--sm")}</a>
            <a class="btn btn-secondary" href="neuxora.html">Sobre Neuxora</a>
          </div>
        </div>
        <div class="benchmark-box" style="border:1px solid var(--line-dark)">
          <div class="benchmark-controls">
            <div>
              <span class="eyebrow" style="margin-bottom:0.2rem">Dataset público BBBC038</span>
              <strong style="font-size:1.05rem;font-weight:600">U-Net frente a Mamba-UNet (670 pares)</strong>
            </div>
          </div>
          <div class="metric-rows">
            <div>
              <div class="metric-item-head">
                <span>Dice y IoU (solapamiento de máscara)</span>
                <span class="metric-winner">Mejor: U-Net</span>
              </div>
              <p class="muted-copy" style="font-size:0.9rem">U-Net obtuvo mayor Dice e IoU al delimitar las máscaras celulares en la corrida documentada.</p>
            </div>
            <div>
              <div class="metric-item-head">
                <span>Pérdida de validación, precisión y especificidad</span>
                <span class="metric-tradeoff">Mejor: Mamba-UNet</span>
              </div>
              <p class="muted-copy" style="font-size:0.9rem">Mamba-UNet obtuvo menor pérdida de validación y mejor precisión y especificidad, mostrando que ninguna métrica decide sola.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="proceso-heading">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Forma de trabajo</span>
            <h2 class="section-title" id="proceso-heading">Cómo avanzamos en cada proyecto.</h2>
          </div>
          <p class="section-intro">Cuatro pasos claros para que siempre sepas qué se está construyendo y por qué.</p>
        </div>
        <ol class="process-grid reveal">
          <li class="process-step" data-spotlight-card>
            <div class="process-step-top">
              <span class="icon-badge">{icon("compass")}</span>
              <span class="process-num">01</span>
            </div>
            <h3>Entender el problema</h3>
            <p>Revisamos cómo opera tu equipo hoy, qué restricciones hay en campo o en red y qué necesitas resolver primero.</p>
          </li>
          <li class="process-step" data-spotlight-card>
            <div class="process-step-top">
              <span class="icon-badge">{icon("flask")}</span>
              <span class="process-num">02</span>
            </div>
            <h3>Probar alternativas</h3>
            <p>Cuando hay dudas técnicas o modelos de IA de por medio, corremos pruebas pequeñas con datos reales antes de construir todo.</p>
          </li>
          <li class="process-step" data-spotlight-card>
            <div class="process-step-top">
              <span class="icon-badge">{icon("cubes")}</span>
              <span class="process-num">03</span>
            </div>
            <h3>Construir por módulos</h3>
            <p>Armamos la plataforma o herramienta en partes claras, con permisos bien definidos y pruebas automáticas.</p>
          </li>
          <li class="process-step" data-spotlight-card>
            <div class="process-step-top">
              <span class="icon-badge">{icon("shield-check")}</span>
              <span class="process-num">04</span>
            </div>
            <h3>Entregar con claridad</h3>
            <p>Dejamos el código documentado, los accesos ordenados y claros los alcances de lo que hace el sistema.</p>
          </li>
        </ol>
      </div>
    </section>

    <section class="section section-subtle" aria-labelledby="notas-heading">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Cuaderno</span>
            <h2 class="section-title" id="notas-heading">Últimas notas.</h2>
          </div>
          <a class="btn btn-secondary" href="noticias.html"><span>Ver el cuaderno</span>{icon("arrow-right", "ui-icon ui-icon--sm")}</a>
        </div>
        <div class="grid-3 reveal">
          <article class="card-panel" data-spotlight-card>
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
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("rotary")}</span>
                <span class="card-category">Caso de proyecto</span>
              </div>
              <h3>Del formulario en papel a un expediente conectado.</h3>
              <p>Captura pensada para celular, fotografía vinculada y seguimiento centralizado en Sillas Rotary, además de fotos del equipo y presentación.</p>
            </div>
            <a class="text-link internal" href="proyecto-sillas-rotary.html">Ver caso y fotos</a>
          </article>
          <article class="card-panel" data-spotlight-card>
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
        </div>
      </div>
    </section>

{render_cta_section()}"""

"""Applied research & ML benchmarking page."""

from src.icons import icon
from src.layout import render_cta_section


def render_research() -> str:
    """Render applied R&D page with interactive U-Net vs Mamba-UNet metric comparator."""
    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container hero-header-split">
        <div>
          <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Investigación aplicada</span>
          <h1 class="page-title">Comparar modelos con datos antes de decidir.</h1>
        </div>
        <p class="hero-lede">Evaluamos arquitecturas de visión artificial y machine learning en condiciones controladas. Publicamos los datos de cada corrida y aclaramos hasta dónde llegan sus resultados.</p>
      </div>
    </header>

    <section class="section section-subtle" id="mamba" aria-labelledby="mamba-heading">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Experimento</span>
          <h2 class="section-title" id="mamba-heading">U-Net frente a Mamba-UNet en segmentación celular.</h2>
          <p class="section-intro">Con la misma preparación de datos y configuración de entrenamiento sobre 670 pares imagen-máscara del conjunto público BBBC038, medimos qué gana y qué sacrifica cada arquitectura.</p>
          <dl class="spec-list" style="margin-top:2rem">
            <div class="spec-row"><dt>Conjunto de datos</dt><dd>670 pares imagen / máscara · BBBC038 (público)</dd></div>
            <div class="spec-row"><dt>Modelos</dt><dd>U-Net estándar vs Mamba-UNet con <em>selective scan</em></dd></div>
            <div class="spec-row"><dt>Métricas</dt><dd>Dice, IoU, precisión, recall, especificidad, pérdida y tiempo</dd></div>
            <div class="spec-row"><dt>Repositorio</dt><dd><a class="text-link" href="https://github.com/AndreRaz/Mamba" target="_blank" rel="noopener noreferrer">AndreRaz/Mamba</a></dd></div>
          </dl>
        </div>

        <div class="benchmark-box reveal">
          <div class="benchmark-controls">
            <div>
              <span class="eyebrow" style="margin-bottom:0.2rem;color:var(--ink-on-dark-muted)">Selector de métrica</span>
              <strong style="font-size:1.05rem;font-weight:600">Resultados registrados en BBBC038</strong>
            </div>
            <div class="metric-tabs" role="tablist" aria-label="Criterios de comparación" data-sliding-tabs>
              <button type="button" class="metric-tab" role="tab" id="met-tab-overlap" aria-selected="true" aria-controls="met-panel-overlap" data-metric-tab="overlap">Dice y IoU</button>
              <button type="button" class="metric-tab" role="tab" id="met-tab-tradeoff" aria-selected="false" aria-controls="met-panel-tradeoff" data-metric-tab="tradeoff">Precisión y pérdida</button>
            </div>
          </div>

          <div role="tabpanel" id="met-panel-overlap" aria-labelledby="met-tab-overlap" data-metric-panel="overlap">
            <div class="metric-rows">
              <div>
                <div class="metric-item-head">
                  <span>Solapamiento global (Dice y IoU)</span>
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
                    <span>Comparado</span>
                  </div>
                </div>
              </div>
              <p class="muted-copy" style="color:var(--ink-on-dark-muted);font-size:0.9rem;margin-top:0.5rem">La exactitud por píxel suele quedar dominada por el fondo; por eso usamos Dice e IoU para medir el solapamiento real de las máscaras celulares. En la corrida documentada, U-Net obtuvo los valores más altos.</p>
            </div>
          </div>

          <div role="tabpanel" id="met-panel-tradeoff" aria-labelledby="met-tab-tradeoff" data-metric-panel="tradeoff" hidden>
            <div class="metric-rows">
              <div>
                <div class="metric-item-head">
                  <span>Pérdida de validación, precisión y especificidad</span>
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
              <p class="muted-copy" style="color:var(--ink-on-dark-muted);font-size:0.9rem;margin-top:0.5rem">Mamba-UNet tuvo menor pérdida de validación y mejor precisión y especificidad. Estos resultados aplican a estas corridas y no demuestran que una arquitectura gane en cualquier problema.</p>
            </div>
          </div>

          <div class="callout" style="margin-top:1.5rem">
            <strong>Alcance del experimento</strong>
            <p>Segmentar células en un conjunto público sirve para comparar arquitecturas técnicas. No es una validación clínica ni una herramienta de diagnóstico médico.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="estados" aria-labelledby="lineas-rd">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Cómo se conecta con el trabajo diario</span>
            <h2 class="section-title" id="lineas-rd">Para qué usamos estas pruebas.</h2>
          </div>
          <p class="section-intro">Probar en pequeño evita elegir tecnologías por moda o gastar recursos en modelos que no aportan valor al problema.</p>
        </div>
        <div class="grid-3 reveal">
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("vision")}</span>
                <span class="card-category">Visión y modelos</span>
              </div>
              <h3>Comparativas reproducibles</h3>
              <p>Antes de recomendar una red neuronal o proveedor de IA, corremos pruebas base medibles para ver tiempos, costos y trade-offs.</p>
            </div>
            <a class="text-link internal" href="#mamba">Revisar Mamba-UNet</a>
          </article>
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("datos")}</span>
                <span class="card-category">Flujos y datos</span>
              </div>
              <h3>Instrumentación de procesos</h3>
              <p>Convertimos tareas físicas y clínicas en sistemas ordenados con bases de datos claras y control de permisos.</p>
            </div>
            <a class="text-link internal" href="proyecto-sillas-rotary.html">Ver Sillas Rotary</a>
          </article>
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("book-open")}</span>
                <span class="card-category">Publicaciones</span>
              </div>
              <h3>Referencias estables</h3>
              <p>Mientras un trabajo no tenga un preprint o artículo publicado, lo mostramos por lo que es: experimento técnico o implementación revisable.</p>
            </div>
            <a class="text-link internal" href="noticias.html">Abrir Cuaderno</a>
          </article>
        </div>
      </div>
    </section>

{render_cta_section("Visión artificial y ML", "¿Necesitas probar modelos de visión o ML sobre tus propios datos?")}"""

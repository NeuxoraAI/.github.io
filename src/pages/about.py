"""Company identity, consulting model, and engineering principles page (Neuxora)."""

from src.icons import icon
from src.layout import render_cta_section


def render_about() -> str:
    """Render Neuxora institutional & engineering page in natural Spanish."""
    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container hero-header-split">
        <div>
          <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Sobre Neuxora · León, Guanajuato</span>
          <h1 class="page-title">Somos un equipo de ingeniería que construye software y productos propios.</h1>
        </div>
        <p class="hero-lede">Trabajamos desde León, Guanajuato desarrollando plataformas a medida, inferencia de modelos LLM, herramientas de visión artificial y análisis de datos, combinando trabajo para organizaciones con proyectos e investigación propia.</p>
      </div>
    </header>

    <section class="section section-subtle" aria-labelledby="identidad-modelo">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Qué hacemos</span>
          <h2 class="section-title" id="identidad-modelo">Consultoría y productos propios.</h2>
        </div>
        <div class="grid-2 reveal">
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("compass")}</span>
                <span class="card-category">Consultoría</span>
              </div>
              <h3>Trabajo con organizaciones</h3>
              <p>Diseñamos plataformas web, inferencia de modelos LLM, análisis de datos y modelos de visión o machine learning según lo que necesite cada equipo.</p>
            </div>
            <a class="text-link internal" href="index.html#servicios">Ver áreas de trabajo</a>
          </article>
          <article class="card-panel" data-spotlight-card>
            <div>
              <div class="card-panel-head">
                <span class="icon-badge icon-badge--sm">{icon("flask")}</span>
                <span class="card-category">Productos e I+D</span>
              </div>
              <h3>Herramientas y pruebas abiertas</h3>
              <p>Desarrollamos utilidades como <code>medscan CLI</code> y corremos comparativas como <code>U-Net vs Mamba-UNet</code> para respaldar nuestras decisiones técnicas.</p>
            </div>
            <a class="text-link internal" href="proyectos.html">Ver proyectos</a>
          </article>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="equipo-neuxora">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">El equipo</span>
          <h2 class="section-title" id="equipo-neuxora">Quiénes están detrás del código.</h2>
          <p class="section-intro">Detrás de cada proyecto hay un grupo multidisciplinario que diseña, programa, prueba en campo y documenta junto a cada organización.</p>
        </div>
        <figure class="photo-card reveal">
          <img src="assets/img/rotary/equipo-neuxora.jpg" alt="Equipo de Neuxora reunido sosteniendo el reconocimiento recibido en el programa 200 sillas para 200 campeones" loading="lazy">
          <figcaption>
            <strong>Equipo Neuxora</strong>
            Fotografía grupal con el reconocimiento recibido durante la presentación del programa «200 sillas para 200 campeones» junto a Ecosistema VIDA UG y el Club Rotario.
          </figcaption>
        </figure>
      </div>
    </section>

    <section class="section section-subtle" aria-labelledby="principios-ingenieria">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Criterios de trabajo</span>
          <h2 class="section-title" id="principios-ingenieria">Cómo preferimos construir software.</h2>
        </div>
        <ol class="principles-list reveal">
          <li>
            <span class="num">01</span>
            <div>
              <h3>Entender primero el proceso</h3>
              <p>Revisamos cómo trabaja la gente en el día a día antes de elegir bases de datos, librerías o modelos de IA.</p>
            </div>
          </li>
          <li>
            <span class="num">02</span>
            <div>
              <h3>Código ordenado por módulos</h3>
              <p>Separamos responsabilidades, cuidamos los permisos y agregamos pruebas automáticas para que el sistema pueda crecer sin problemas.</p>
            </div>
          </li>
          <li>
            <span class="num">03</span>
            <div>
              <h3>Hablar claro sobre lo que prueba cada cosa</h3>
              <p>Que un programa funcione en pruebas técnicas no prueba por sí solo un impacto médico o social; cada afirmación necesita su propia evidencia.</p>
            </div>
          </li>
          <li>
            <span class="num">04</span>
            <div>
              <h3>Decir qué falta</h3>
              <p>Dejamos por escrito qué ya funciona, qué está en desarrollo y qué queda pendiente por probar.</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

{render_cta_section("Contacto", "¿Tienes en puerta un proyecto de software, datos, modelos LLM o visión artificial?")}"""

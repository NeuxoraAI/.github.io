"""Case study page for Sillas Rotary."""

from src.layout import render_cta_section


def render_case_rotary() -> str:
    """Render Sillas Rotary engineering case study with event and team photography."""
    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container">
        <nav class="breadcrumb" aria-label="Ruta de navegación">
          <a href="index.html">Inicio</a>
          <span aria-hidden="true">/</span>
          <a href="proyectos.html">Proyectos</a>
          <span aria-hidden="true">/</span>
          <span>Sillas Rotary</span>
        </nav>
        <div class="hero-header-split">
          <div>
            <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Caso de proyecto · Documentado</span>
            <h1 class="page-title">Sillas Rotary.</h1>
          </div>
          <p class="hero-lede">Aplicación web pensada para celular que reemplaza los formularios en papel por captura digital, fotografías vinculadas y consulta ordenada de expedientes.</p>
        </div>
      </div>
    </header>

    <section class="section section-subtle" aria-labelledby="rotary-flow">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">El problema</span>
          <h2 class="section-title" id="rotary-flow">Capturar en campo sin perder el hilo del expediente.</h2>
          <p class="section-intro">El trabajo dependía de hojas en papel que después se capturaban a mano, lo que complicaba mantener juntos los datos socioeconómicos, las medidas técnicas, las fotos y el seguimiento por región.</p>
          <div class="hero-actions">
            <a class="btn btn-primary" href="https://github.com/NeuxoraAI/Sillas-Rotary/tree/branch-beta03" target="_blank" rel="noopener noreferrer">Ver repositorio</a>
          </div>
        </div>
        <div class="showcase">
          <div class="showcase-toolbar" style="margin-bottom:1rem;padding-bottom:0.85rem">
            <div class="showcase-chrome" aria-hidden="true"><span></span><span></span><span></span></div>
            <span class="showcase-label" style="margin-bottom:0">Presentación en «200 sillas para 200 campeones»</span>
          </div>
          <figure class="showcase-media" style="margin-top:0.75rem">
            <img src="assets/img/rotary/presentacion-proyecto.jpg" alt="Presentación del proyecto Sillas Rotary con Neuxora, Universidad de Guanajuato y Ecosistema VIDA UG Campus León">
            <figcaption>Presentación del proyecto junto a la Universidad de Guanajuato y Ecosistema VIDA UG Campus León.</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="rotary-galeria">
      <div class="container">
        <div class="section-header-row">
          <div>
            <span class="eyebrow">Fotografías del evento</span>
            <h2 class="section-title" id="rotary-galeria">El equipo de Neuxora y la presentación del proyecto.</h2>
          </div>
          <p class="section-intro">Fotos de la jornada vinculada al programa «200 sillas para 200 campeones» y del reconocimiento que recibió el equipo junto a colaboradores.</p>
        </div>
        <div class="photo-grid reveal">
          <figure class="photo-card photo-card--featured">
            <img src="assets/img/rotary/equipo-neuxora.jpg" alt="Todo el equipo de Neuxora posando con el reconocimiento otorgado por el programa 200 sillas para 200 campeones">
            <figcaption>
              <strong>El equipo de Neuxora</strong>
              Todos los integrantes junto al reconocimiento entregado durante la jornada del programa en colaboración con el Club Rotario y Ecosistema VIDA UG.
            </figcaption>
          </figure>
          <figure class="photo-card">
            <img src="assets/img/rotary/presentacion-proyecto.jpg" alt="Presentación en escenario del proyecto Sillas Rotary con logos de Neuxora y Ecosistema VIDA UG" loading="lazy">
            <figcaption>
              <strong>Trabajo en conjunto</strong>
              Presentación de los antecedentes del proyecto y el trabajo en campo con la Universidad de Guanajuato.
            </figcaption>
          </figure>
          <figure class="photo-card">
            <img src="assets/img/rotary/presentacion-servicios.jpg" alt="Exposición de líneas tecnológicas en transformación digital, ingeniería de software e inteligencia artificial" loading="lazy">
            <figcaption>
              <strong>Líneas de trabajo</strong>
              Exposición de las áreas tecnológicas de automatización, transformación digital, ingeniería de software e IA.
            </figcaption>
          </figure>
          <figure class="photo-card">
            <img src="assets/img/rotary/presentacion-solucion.jpg" alt="Ponente explicando la solución digital diseñada para mejorar la experiencia de todos los involucrados" loading="lazy">
            <figcaption>
              <strong>Pensado para quien captura</strong>
              Explicación de la herramienta diseñada para hacer más sencillo el registro y consulta en campo.
            </figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section section-subtle" aria-labelledby="rotary-componentes">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Qué incluye el sistema</span>
          <h2 class="section-title" id="rotary-componentes">Del papel a registros conectados.</h2>
        </div>
        <ol class="principles-list reveal">
          <li>
            <span class="num">01</span>
            <div>
              <h3>Captura socioeconómica</h3>
              <p>Formulario desde el celular para registrar al beneficiario, su domicilio, tutores y datos del estudio.</p>
            </div>
          </li>
          <li>
            <span class="num">02</span>
            <div>
              <h3>Solicitud técnica</h3>
              <p>Registro del entorno de uso, postura, medidas, observaciones y prioridad de cada solicitud.</p>
            </div>
          </li>
          <li>
            <span class="num">03</span>
            <div>
              <h3>Fotografías vinculadas</h3>
              <p>Cada foto se sube y queda ligada directo al expediente y solicitud correspondiente, sin archivos sueltos.</p>
            </div>
          </li>
          <li>
            <span class="num">04</span>
            <div>
              <h3>Control por roles y regiones</h3>
              <p>El sistema conecta usuarios, regiones, beneficiarios, estudios y solicitudes con acceso diferenciado por perfil.</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <section class="section" aria-labelledby="rotary-contexto">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Ficha del proyecto</span>
          <h2 class="section-title" id="rotary-contexto">Alcance y organización actual.</h2>
        </div>
        <div>
          <dl class="spec-list">
            <div class="spec-row"><dt>Contexto</dt><dd>Capturistas de campo del programa «200 sillas para 200 campeones» (menciones a Ecosistema VIDA UG, UG y Rotary 200 en repositorio y redes)</dd></div>
            <div class="spec-row"><dt>Experiencia de uso</dt><dd>Pensada para celular: acceso rápido, selección regional, captura guiada y panel administrativo</dd></div>
            <div class="spec-row"><dt>Seguridad y permisos</dt><dd>Control de acceso por perfil para proteger expedientes y separar capturas por región</dd></div>
            <div class="spec-row"><dt>Respaldo</dt><dd>Expedientes, fotografías y solicitudes centralizados en un solo historial consultable</dd></div>
            <div class="spec-row"><dt>Repositorio</dt><dd><a class="text-link" href="https://github.com/NeuxoraAI/Sillas-Rotary/tree/branch-beta03" target="_blank" rel="noopener noreferrer">NeuxoraAI/Sillas-Rotary (branch-beta03)</a></dd></div>
          </dl>
          <div class="callout" style="margin-top:2rem">
            <strong>Qué muestra este repositorio</strong>
            <p>El repositorio contiene el código, la estructura de seguridad y pruebas técnicas; no incluye mediciones de ahorro de tiempo en campo ni es un dispositivo médico.</p>
          </div>
        </div>
      </div>
    </section>

{render_cta_section("Sistemas para campo", "¿Tu equipo en campo sigue registrando datos en papel o archivos sueltos?")}"""

"""Case study page for Web-App Idiomas UG."""

from src.data import IDIOMAS_MODULES
from src.icons import icon
from src.layout import esc, render_cta_section


def render_case_idiomas() -> str:
    """Render Web-App Idiomas UG engineering case study."""
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

    return f"""    <header class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container">
        <nav class="breadcrumb" aria-label="Ruta de navegación">
          <a href="index.html">Inicio</a>
          <span aria-hidden="true">/</span>
          <a href="proyectos.html">Proyectos</a>
          <span aria-hidden="true">/</span>
          <span>Web-App Idiomas UG</span>
        </nav>
        <div class="hero-header-split">
          <div>
            <span class="hero-kicker"><span class="kicker-dot" aria-hidden="true"></span>Caso de proyecto · En construcción</span>
            <h1 class="page-title">Web-App Idiomas UG.</h1>
          </div>
          <p class="hero-lede">Plataforma web para realizar exámenes de regularización de nivel en distintos idiomas del Departamento de Idiomas de la Universidad de Guanajuato, Campus León.</p>
        </div>
      </div>
    </header>

    <section class="section section-subtle" aria-labelledby="idiomas-arch">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Qué resuelve</span>
          <h2 class="section-title" id="idiomas-arch">Cómo está organizado el sistema.</h2>
          <p class="section-intro">La plataforma separa la experiencia de quien presenta el examen del trabajo de coordinación, registro, control de intentos y auditoría.</p>
        </div>
        <div class="showcase" data-arch-inspector>
          <span class="showcase-label">Capacidades de Web-App-IdiomasUG</span>
          <div class="arch-nodes" style="margin-top:0.75rem">
            {"".join(arch_buttons)}
          </div>
          <div class="arch-detail" data-arch-detail aria-live="polite">
            <strong>{esc(default_mod["name"])}: </strong>{esc(default_mod["desc"])}
          </div>
        </div>
      </div>
    </section>

    <section class="section" aria-labelledby="idiomas-capas">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Funcionamiento</span>
          <h2 class="section-title" id="idiomas-capas">Piezas principales de la plataforma.</h2>
        </div>
        <ol class="principles-list reveal">
          <li>
            <span class="num">01</span>
            <div>
              <h3>Experiencia para sustentantes y coordinación</h3>
              <p>Cada persona entra a pantallas claras según su rol: solicitar examen y contestarlo sin distracciones, o administrar convocatorias y resultados.</p>
            </div>
          </li>
          <li>
            <span class="num">02</span>
            <div>
              <h3>Operación ordenada por áreas</h3>
              <p>Separamos registro de sustentantes, exámenes por idioma y nivel, intentos realizados, cuentas administrativas e historial para mantener el sistema claro.</p>
            </div>
          </li>
          <li>
            <span class="num">03</span>
            <div>
              <h3>Sesiones activas, seguridad y auditoría</h3>
              <p>Mantiene el control de sesiones simultáneas durante la aplicación y deja un registro de acciones clave para respaldar revisiones académicas.</p>
            </div>
          </li>
          <li>
            <span class="num">04</span>
            <div>
              <h3>Alta administrativa y validación continua</h3>
              <p>Cuenta con herramientas de arranque para dar de alta administradores y pruebas automatizadas que validan el flujo completo antes de cada cambio.</p>
            </div>
          </li>
        </ol>
      </div>
    </section>

    <section class="section section-subtle" aria-labelledby="idiomas-ficha">
      <div class="container split-grid">
        <div>
          <span class="eyebrow">Ficha del proyecto</span>
          <h2 class="section-title" id="idiomas-ficha">Alcance y estado actual.</h2>
        </div>
        <div>
          <dl class="spec-list">
            <div class="spec-row"><dt>Institución</dt><dd>Departamento de Idiomas · Universidad de Guanajuato, Campus León</dd></div>
            <div class="spec-row"><dt>Estado</dt><dd>En construcción activa</dd></div>
            <div class="spec-row"><dt>Uso principal</dt><dd>Exámenes de regularización de nivel en distintos idiomas</dd></div>
            <div class="spec-row"><dt>Capacidades</dt><dd>Registro de sustentantes, convocatorias por nivel, control de intentos, permisos y auditoría</dd></div>
            <div class="spec-row"><dt>Operación</dt><dd>Sesiones activas controladas y pruebas continuas sobre flujos clave</dd></div>
          </dl>
          <div class="callout" style="margin-top:2rem">
            <strong>Estado actual</strong>
            <p>Este sistema sigue en desarrollo activo. Conforme avance hacia pruebas con usuarios y puesta en marcha, actualizaremos esta ficha con esos detalles.</p>
          </div>
        </div>
      </div>
    </section>

{render_cta_section("Desarrollo de plataformas", "¿Tu equipo o institución necesita una plataforma web armada a la medida?")}"""

"""Legacy redirect page for areas.html -> proyectos.html."""


def render_areas() -> str:
    """Render clean fallback body for the /areas.html redirect."""
    return """    <section class="hero hero--dark">
      <canvas class="hero-canvas" data-antigravity-canvas aria-hidden="true"></canvas>
      <div class="container narrow">
        <span class="hero-kicker">Ruta actualizada</span>
        <h1 class="page-title">Ahora organizamos el catálogo por sistemas y líneas técnicas.</h1>
        <p class="hero-lede" style="margin-top:1.5rem">Si tu navegador no redirige automáticamente, <a class="text-link internal" href="proyectos.html">abre el índice de proyectos</a> o revisa <a class="text-link internal" href="index.html#servicios">nuestras 5 líneas de ingeniería</a>.</p>
      </div>
    </section>"""

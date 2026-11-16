"""Page registry for Neuxora static site generation."""

from src.pages.about import render_about
from src.pages.areas import render_areas
from src.pages.case_idiomas import render_case_idiomas
from src.pages.case_rotary import render_case_rotary
from src.pages.home import render_home
from src.pages.notebook import render_notebook
from src.pages.projects import render_projects
from src.pages.research import render_research

PAGES = [
    {
        "slug": "index.html",
        "title": "Neuxora | Consultora de Ingeniería y Desarrollo de Software",
        "description": (
            "Consultora mexicana de ingeniería y desarrollo de productos propios: "
            "plataformas web, inferencia de modelos LLM, visión artificial, machine learning y análisis de datos."
        ),
        "active_key": "home",
        "og_type": "website",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_home,
        "include_in_sitemap": True,
    },
    {
        "slug": "proyectos.html",
        "title": "Proyectos y Herramientas | Neuxora",
        "description": (
            "Sistemas en construcción, implementaciones documentadas, herramientas de consola "
            "y experimentos abiertos de Neuxora."
        ),
        "active_key": "proyectos",
        "og_type": "website",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_projects,
        "include_in_sitemap": True,
    },
    {
        "slug": "proyecto-idiomas-ug.html",
        "title": "Web-App Idiomas UG | Neuxora",
        "description": (
            "Plataforma web para exámenes de regularización de idiomas del Departamento de "
            "Idiomas de la Universidad de Guanajuato, Campus León."
        ),
        "active_key": "proyectos",
        "og_type": "article",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_case_idiomas,
        "include_in_sitemap": True,
    },
    {
        "slug": "proyecto-sillas-rotary.html",
        "title": "Sillas Rotary | Neuxora",
        "description": (
            "Aplicación móvil para digitalizar capturas en campo, "
            "fotografías y seguimiento de expedientes, junto con fotografías del equipo."
        ),
        "active_key": "proyectos",
        "og_type": "article",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_case_rotary,
        "include_in_sitemap": True,
    },
    {
        "slug": "investigacion.html",
        "title": "Investigación Aplicada | Neuxora",
        "description": (
            "Comparativas experimentales en visión artificial y machine learning, "
            "incluyendo U-Net vs Mamba-UNet sobre BBBC038."
        ),
        "active_key": "investigacion",
        "og_type": "website",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_research,
        "include_in_sitemap": True,
    },
    {
        "slug": "noticias.html",
        "title": "Cuaderno | Neuxora",
        "description": (
            "Notas sobre arquitectura de proyectos, experimentos, herramientas propias "
            "y menciones externas de Neuxora."
        ),
        "active_key": "noticias",
        "og_type": "website",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_notebook,
        "include_in_sitemap": True,
    },
    {
        "slug": "neuxora.html",
        "title": "Sobre Neuxora | Consultora de Ingeniería",
        "description": (
            "Quiénes somos, el equipo de Neuxora, cómo trabajamos y cómo construir proyectos juntos "
            "desde León, Guanajuato."
        ),
        "active_key": "neuxora",
        "og_type": "website",
        "robots": "index, follow",
        "extra_head": "",
        "renderer": render_about,
        "include_in_sitemap": True,
    },
    {
        "slug": "areas.html",
        "title": "Proyectos | Neuxora",
        "description": "Redirección al catálogo actualizado de proyectos de Neuxora.",
        "active_key": "proyectos",
        "og_type": "website",
        "robots": "noindex, follow",
        "extra_head": '<meta http-equiv="refresh" content="0; url=proyectos.html">',
        "renderer": render_areas,
        "include_in_sitemap": False,
    },
]

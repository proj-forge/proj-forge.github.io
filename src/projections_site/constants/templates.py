from __future__ import annotations

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("projections_site"),
    autoescape=select_autoescape(),
)

TEMPLATES = {
    "crs": env.get_template("crs.html.j2"),
    # "datum": ...,
    # "homepage": ...,
}

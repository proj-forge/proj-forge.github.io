from pprint import pprint

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(
    loader=PackageLoader("projections_site"),
    autoescape=select_autoescape(),
)
# TODO: Why can't this be set at init-time??
env.globals.update(
    {
        "pprint": pprint,
    }
)

TEMPLATES = {
    "crs": env.get_template("crs.html.j2"),
    # "datum": ...,
    # "homepage": ...,
}

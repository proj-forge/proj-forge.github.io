from pprint import pformat

from jinja2 import Environment, PackageLoader, select_autoescape

from projections_site import __version__

env = Environment(
    loader=PackageLoader("projections_site"),
    autoescape=select_autoescape(),
)
# TODO: Why can't this be set at init-time??
env.globals.update(
    {
        "pformat": pformat,
        "version": __version__,
    }
)

TEMPLATES = {
    "index": env.get_template("index.html.j2"),
    "crs": env.get_template("crs.html.j2"),
    # "datum": ...,
    # "homepage": ...,
}

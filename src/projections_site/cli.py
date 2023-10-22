from __future__ import annotations

import click
from pyproj import CRS

from projections_site.constants.paths import SITE_DIR
from projections_site.constants.templates import TEMPLATES
from projections_site.crs import get_all_crs

OUTPUT_DIR = "_site"


@click.command
def cli() -> None:
    all_crs = get_all_crs()
    for crs_id in all_crs:
        output_fn = f"{crs_id.authority}-{crs_id.code}.html"
        output_path = SITE_DIR / output_fn
        SITE_DIR.mkdir(exist_ok=True)

        crs = CRS((crs_id.authority, crs_id.code))

        rendered = TEMPLATES["crs"].render(crs=crs, version="foo")

        with output_path.open("w") as f:
            f.write(rendered)


if __name__ == "__main__":
    cli()

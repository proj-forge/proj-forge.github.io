# Enables using e.g. built-in `list` in annotations in Python 3.8:
from __future__ import annotations

from pathlib import Path

import util
from pyproj import CRS

from projections_site.constants.paths import SITE_DIR
from projections_site.constants.templates import TEMPLATES
from projections_site.crs import AuthorityCode


def _crs_html_filepath(crs_id: AuthorityCode) -> Path:
    output_fn = f"{crs_id.authority}-{crs_id.code}.html"
    return SITE_DIR / output_fn


def _write_to_file(output_path: Path, content: str) -> None:
    with output_path.open("w") as f:
        f.write(content)


def render_crs_to_html(crs_id: AuthorityCode) -> None:
    crs = CRS((crs_id.authority, crs_id.code))
    rendered = TEMPLATES["crs"].render(crs=crs, util=util)

    output_path = _crs_html_filepath(crs_id)
    output_path.parent.mkdir(exist_ok=True)
    _write_to_file(output_path=output_path, content=rendered)


def render_crs_index_html(all_crs: list[AuthorityCode]) -> None:
    elements = [
        {
            "name": f"{crs_id.authority}:{crs_id.code}",
            "href": _crs_html_filepath(crs_id).name,
        }
        for crs_id in all_crs
    ]

    rendered = TEMPLATES["index"].render(elements=elements)
    _write_to_file(
        output_path=SITE_DIR / "index.html",
        content=rendered,
    )

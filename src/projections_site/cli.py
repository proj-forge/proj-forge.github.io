import click

from projections_site.crs import get_all_crs
from projections_site.render import render_crs_index_html, render_crs_to_html

OUTPUT_DIR = "_site"


@click.command
def cli() -> None:
    all_crs = get_all_crs()
    for crs_id in all_crs:
        render_crs_to_html(crs_id)

    render_crs_index_html(all_crs)


if __name__ == "__main__":
    cli()

"""Utilities for parsing CRS"""

from typing import Any

import pyproj


def get_datum(crs: pyproj.CRS) -> Any:
    """Returns datum name"""
    try:
        datum_name = crs.datum
    except Exception:
        datum_name = "Undefined"
    return datum_name


def get_coordinate_system(crs: pyproj.CRS) -> Any:
    """Returns coordinate system name"""
    try:
        coord_system = crs.coordinate_system.name
    except Exception:
        coord_system = "Undefined"
    return coord_system


def get_coordinate_operation(crs: pyproj.CRS) -> Any:
    """Returns name of projection"""
    try:
        proj_name = crs.coordinate_operation.name
    except Exception:
        proj_name = "Undefined"
    return proj_name


def get_epsg_version_string() -> str:
    """Returns version and revision date of EPSG Database"""
    return (
        f"{pyproj.database.get_database_metadata('EPSG.VERSION')} "
        f"{pyproj.database.get_database_metadata('EPSG.DATE')}"
    )

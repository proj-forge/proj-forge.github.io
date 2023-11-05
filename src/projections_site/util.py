"""Utilities for parsing CRS"""

import pyproj


def get_datum(crs: pyproj.CRS) -> str:
    """Returns datum name"""
    try:
        datum_name = crs.datum
    except Exception:
        datum_name = "Undefined"
    return str(datum_name)


def get_coordinate_system(crs: pyproj.CRS) -> str:
    """Returns coordinate system name"""
    try:
        coord_system = crs.coordinate_system.name
    except Exception:
        coord_system = "Undefined"
    return str(coord_system)


def get_geodetic_crs(crs: pyproj.CRS) -> str:
    try:
        crs_name = crs.source_crs.to_json_dict()["name"]
    except Exception:
        crs_name = "Undefined"
    return str(crs_name)


def get_coordinate_operation(crs: pyproj.CRS) -> str:
    """Returns name of projection"""
    try:
        proj_name = crs.coordinate_operation.name
    except Exception:
        proj_name = "Undefined"
    return str(proj_name)


def get_epsg_version_string() -> str:
    """Returns version and revision date of EPSG Database"""
    return (
        f"{pyproj.database.get_database_metadata('EPSG.VERSION')} "
        f"{pyproj.database.get_database_metadata('EPSG.DATE')}"
    )

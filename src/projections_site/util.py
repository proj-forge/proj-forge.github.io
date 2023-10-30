"""Utilities for parsing CRS"""
import pyproj


def get_datum(crs) -> str:
    """Returns name of datum"""
    try:
        datum_name = crs.datum
    except Exception as e:
        datum_name = "Undefined"
    return datum_name


def get_coordinate_system(crs):
    """Returns coordinate system name"""
    try:
        coord_system = crs.coordinate_system.name
    except Exception as e:
        coord_system = "Undefined"
    return coord_system


def get_coordinate_operation(crs):
    """Returns name of projection"""
    try:
        proj_name = crs.coordinate_operation.name
    except Exception as e:
        proj_name = "Undefined"
    return proj_name


def get_epsg_version_string():
    """Returns version and revision date of EPSG Database"""
    return (
        f"{pyproj.database.get_database_metadata('EPSG.VERSION')}"
        f" ({pyproj.database.get_database_metadata('EPSG.DATE')})"
    )

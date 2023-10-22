import importlib.metadata

import projections_site as m


def test_version():
    assert importlib.metadata.version("projections_site") == m.__version__

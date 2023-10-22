# Enables using e.g. built-in `list` in annotations in Python 3.8:
from __future__ import annotations

from dataclasses import dataclass

from pyproj import database


@dataclass
class AuthorityCode:
    authority: str
    code: str


def get_all_crs() -> list[AuthorityCode]:
    authorities = database.get_authorities()

    codes: list[AuthorityCode] = []
    for a in authorities:
        auth_codes = database.get_codes(a, "CRS", allow_deprecated=True)
        codes.extend(AuthorityCode(authority=a, code=c) for c in auth_codes)

    return codes

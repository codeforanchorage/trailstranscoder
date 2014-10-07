"""Wrangle together all of the appropriate configs in this file
"""

temp_path = "../temp-data/temp.sqlite"

from .muni import muni_all
from .suppressions import suppression

configList = (
    muni_all,
    suppression,
    )


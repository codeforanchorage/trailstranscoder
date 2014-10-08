"""Wrangle together all of the appropriate configs in this file
"""

temp_path = "../temp-data/temp.sqlite"
output_path = "../output"

from .muni import muni_all
from .chugach import chugach_all
from .hatcher import hatcher_all
from .suppressions import suppression

configList = (
    muni_all, # This config needs to come first
    chugach_all,
    hatcher_all,
    suppression,
    )


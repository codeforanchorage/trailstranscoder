"""Wrangle together all of the appropriate configs in this file
"""

temp_path = "../temp-data/temp.sqlite"
migrations_path = "sql/migrations"
cleanup_path = "sql/cleanup"
output_path = "../output"

from .muni import muni_all
from .chugach import chugach_all
from .hatcher import hatcher_all
from .matsu import matsu_all
from .kincaid_singletrack import kincaid_all
from .kincaid_trailheads import kincaid_trailheads

configList = (
    muni_all, # This config needs to come first
    chugach_all,
    hatcher_all,
    matsu_all,
    kincaid_all,
    kincaid_trailheads,
    )


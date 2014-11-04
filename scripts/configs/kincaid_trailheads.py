"""Define your configuration below
"""

import collections

# basic muni config

kincaid_trailheads = collections.OrderedDict()
kincaid_trailheads["append"] = None
kincaid_trailheads["tsrs"] = "crs:84"
kincaid_trailheads["source"] = "../source-data/POIs/kincaid.vrt"
kincaid_trailheads["sql"] = '''
    SELECT 'AdHoc' AS source,
        'Kincaid Park' AS system,
        *
    FROM kincaid
    '''
kincaid_trailheads["newlayername"] = "kincaid_trailheads"
kincaid_trailheads["type"] = "POINT"


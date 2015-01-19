"""Define your configuration below
"""

import collections

# basic muni config

hillside_trailheads = collections.OrderedDict()
hillside_trailheads["append"] = None
hillside_trailheads["tsrs"] = "crs:84"
hillside_trailheads["source"] = "../source-data/POIs/hillside.vrt"
hillside_trailheads["sql"] = '''
    SELECT 'AdHoc' AS source,
        'Hillside' AS system,
        *
    FROM hillside
    '''
hillside_trailheads["newlayername"] = "hillside_trailheads"
hillside_trailheads["type"] = "POINT"


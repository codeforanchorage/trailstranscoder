"""Define your configuration below
"""

import collections

# basic muni config

muni_all = collections.OrderedDict()
muni_all["crs"] = "crs:84"
muni_all["source"] = "../source-data/trails_shp"
muni_all["sql"] = '''
    SELECT 'Muni' AS source,
        SYSTEM_NAM AS system,
        TRAIL_NAME AS name,
        'Muni/' + SYSTEM_NAM + '/' + TRAIL_NAME AS identifier,
        SURFACE AS surface,
        TRAIL_CLAS AS class,
        LIGHTING AS lighting,
        GRADE AS difficulty,
        SKI_TYPE AS skiType
    FROM trails
    '''
muni_all["newlayername"] = "muni_trails"


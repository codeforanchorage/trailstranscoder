"""Define your configuration below
"""

import collections

# basic matsu pass config

matsu_all = collections.OrderedDict()
matsu_all["append"] = None
matsu_all["tsrs"] = "crs:84"
matsu_all["source"] = "../source-data/MSB_Trails"
matsu_all["sql"] = '''
    SELECT 'Matsu' AS source,
        name AS system,
        name_2 AS name,
        'Matsu/' + name + '/' + name_2 AS identifier,
        NULL AS surface,
        NULL AS class,
        NULL AS lighting,
        NULL AS difficulty,
        NULL AS skiType,
        NULL AS comments,
        NULL AS image_url
    FROM MSB_Trails_Legal_Aug2014
    '''
matsu_all["newlayername"] = "matsu_trails"
matsu_all["type"] = "MULTILINESTRING"


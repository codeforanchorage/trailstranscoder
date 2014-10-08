"""Define your configuration below
"""

import collections

# basic dnr config

chugach_all = collections.OrderedDict()
chugach_all["append"] = None
chugach_all["tsrs"] = "crs:84"
chugach_all["source"] = "../source-data/chugachstatepark.kmz"
chugach_all["sql"] = '''
    SELECT 'DNR' AS source,
        'Chugach State Park' AS system,
        name,
        'DNR/Chugach State Park/' + name AS identifier,
        NULL AS surface,
        NULL AS class,
        NULL AS lighting,
        NULL AS difficulty,
        NULL AS skiType
    FROM trails
    '''
chugach_all["newlayername"] = "chugach_trails"


"""Define your configuration below
"""

import collections

# basic hatcher pass config

hatcher_all = collections.OrderedDict()
hatcher_all["append"] = None
hatcher_all["tsrs"] = "crs:84"
hatcher_all["source"] = "../source-data/hatcherpassma.kmz"
hatcher_all["sql"] = '''
    SELECT 'DNR' AS source,
        'Hatcher Pass' AS system,
        name,
        'DNR/Hatcher Pass/' + name AS identifier,
        NULL AS surface,
        NULL AS class,
        NULL AS lighting,
        NULL AS difficulty,
        NULL AS skiType
    FROM trails
    '''
hatcher_all["newlayername"] = "hatcher_pass_trails"
hatcher_all["type"] = "MULTILINESTRING"


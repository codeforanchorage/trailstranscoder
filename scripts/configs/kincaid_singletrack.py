"""Define your configuration below
"""

import collections

# basic kincaid singletrack config

kincaid_all = collections.OrderedDict()
kincaid_all["append"] = None
kincaid_all["ssrs"] = "epsg:3857"
kincaid_all["tsrs"] = "crs:84"
kincaid_all["source"] = "../source-data/Kincaid_Singletrack"
kincaid_all["sql"] = '''
    SELECT 'ACE' AS source,
        'Kincaid Single Track' AS system,
        name,
        'ACE/Kincaid Single Track/' + name AS identifier,
        NULL AS surface,
        NULL AS class,
        NULL AS lighting,
        NULL AS difficulty,
        NULL AS skiType,
        NULL AS comments,
        NULL AS image_url
    FROM Kincaid_Single_Track_North_Section_2013
    '''
kincaid_all["newlayername"] = "kincaid_singletrack_trails"
kincaid_all["type"] = "MULTILINESTRING"


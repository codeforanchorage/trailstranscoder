"""Define your configuration below
"""

import collections

# ad hoc adjustments made to trails by source/system/name triad

trail_adjustments = collections.OrderedDict()
trail_adjustments["append"] = None
trail_adjustments["tsrs"] = "crs:84"
trail_adjustments["source"] = "../source-data/adhoc/trail_adjustments.csv"
trail_adjustments["sql"] = '''
    SELECT *
    FROM trail_adjustments
    '''
trail_adjustments["newlayername"] = "trail_adjustments"
trail_adjustments["type"] = "POINT"


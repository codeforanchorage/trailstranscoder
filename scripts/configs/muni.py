"""Define your configuration below
"""

# basic muni config

muni_all = {
    "crs": "crs:84",
    "source": "../source-data/trails_shp",
    "sql": '''
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
        ''',
    "newlayername": "muni_trails",
}


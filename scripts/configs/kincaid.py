"""Define your configuration below
"""

config = {
    "crs": "crs:84",
    "source": "../source-data/trails_shp",
    "destination": "../temp-data/kincaid-bounding-box.geojson",
    "sql": '''
        SELECT 'Muni' AS Source,
            SYSTEM_NAM AS System,
            TRAIL_NAME AS Name,
            'Muni/' + SYSTEM_NAM + '/' + TRAIL_NAME AS Identifier,
            SURFACE AS Surface,
            TRAIL_CLAS AS Class,
            LIGHTING AS Lighting,
            GRADE AS Difficulty,
            SKI_TYPE AS SkiType
        FROM trails
        ''',
    "clip": {
        "southwest": ["-150.1153", "61.12301"],
        "northeast": ["-149.98707", "61.18463"]
    }
}


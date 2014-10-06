"""Define your configuration below
"""

# basic muni config

muni_all = {
    "crs": "crs:84",
    "source": "../source-data/trails_shp",
    "destination": "../temp-data/muni-all-trails.geojson",
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
        '''
}

kincaid_all = muni_all.copy()
kincaid_all["destination"] = "../temp-data/kincaid-all.geojson"
kincaid_all["clip"] = {"southwest": ["-150.1153", "61.12301"], "northeast": ["-149.98707", "61.18463"]} #these are the boundaries of Kincaid, accoring to us

# Then, we can start to extract sub-configs as needed
# Kincaid ski trails
kincaid_ski = kincaid_all.copy()
kincaid_ski["destination"] = "../temp-data/kincaid-xc.geojson"
kincaid_ski["sql"] += " WHERE SYSTEM_NAM = 'Kincaid Ski Trails' or SYSTEM_NAM = 'Coastal Trail'"

# single track
kincaid_bike = kincaid_all.copy()
kincaid_bike["destination"] = "../temp-data/kincaid-bike.geojson"
kincaid_bike["sql"] += " WHERE SYSTEM_NAM = 'Kincaid Single Track'"

coastal_trail = muni_all.copy()
coastal_trail["destination"] = "../temp-data/coastal-trail.geojson"
coastal_trail["sql"] += " WHERE SYSTEM_NAM = 'Coastal Trail'"

chester_creek = muni_all.copy()
chester_creek["destination"] = "../temp-data/chester-creek-trail.geojson"
chester_creek["sql"] += " WHERE SYSTEM_NAM LIKE '%Chester Creek%'"

tour_of_anc = muni_all.copy()
tour_of_anc["destination"] = "../temp-data/tour-of-anchorage.geojson"
tour_of_anc["sql"] += " WHERE SYSTEM_NAM LIKE '%Tour of Anchorage%'"

girdwood = muni_all.copy()
girdwood["destination"] = "../temp-data/girdwood.geojson"
girdwood["sql"] += " WHERE SYSTEM_NAM LIKE '%Girdwood Trails%'"

hillside_all = muni_all.copy()
hillside_all["destination"] = "../temp-data/hillside-all.geojson"
hillside_all["clip"] = {"southwest": ["-149.80545", "61.136441"], "northeast": ["-149.683571", "61.179584"]} #these are the boundaries of Kincaid, accoring to us

hillside_ski = hillside_all.copy()
hillside_ski["destination"] = "../temp-data/hillside-ski.geojson"
hillside_ski["sql"] += " WHERE SYSTEM_NAM LIKE '%Hillside Ski Trails%'"

hillside_bike = hillside_all.copy()
hillside_bike["destination"] = "../temp-data/hillside-bike.geojson"
hillside_bike["sql"] += " WHERE SYSTEM_NAM LIKE '%Mt Bike Single Track%'"

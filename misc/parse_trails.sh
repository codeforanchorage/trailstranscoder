
# this runs though a bunch of ogr2ogr scenarios
# and dumps geojson files to temp-files

mkdir ../temp-data

#bounding box for kincaid
#hopefully this will clip and include all trails within the box
rm ../temp-data/kincaid-bounding-box.geojson
ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/kincaid-bounding-box.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -clipdst -150.1153 61.12301 -149.98707 61.18463

ogr2ogr -f GPX -t_srs crs:84 ../temp-data/kincaid-bounding-box.gpx -dsco GPX_USE_EXTENSIONS=YES trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -clipdst -150.1153 61.12301 -149.98707 61.18463

rm ../temp-data/hillside-bounding-box.geojson
ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/hillside-bounding-box.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -clipdst -149.80545 61.136441 -149.683571 61.179584


rm ../temp-data/kincaid-ski-trails.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/kincaid-ski-trails.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Kincaid Ski%'"

rm ../temp-data/kincaid-singletrack.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/kincaid-singletrack.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING -where "SYSTEM_NAM like '%Kincaid Singletrack%'"

rm ../temp-data/kincaid-other.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/kincaid-other.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING -where "SYSTEM_NAM like '%Kincaid Other%'"

rm ../temp-data/coastal-trail.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/coastal-trail.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Coastal Trail%'"

rm ../temp-data/chester-creek-trail.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/chester-creek-trail.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Chester Creek Trail%'"

rm ../temp-data/hillside-ski-trails.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/hillside-ski-trails.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Hillside Ski Trails%'"

rm ../temp-data/hillside-singletrack.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/hillside-singletrack.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING -where "SYSTEM_NAM like '%Mt Bike Single Track%'"

rm ../temp-data/tour-of-anchorage.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/tour-of-anchorage.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Tour of Anchorage%'"

rm ../temp-data/girdwood-trails.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/girdwood-trails.geojson ../source-data/trails_shp -select SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE -where "SYSTEM_NAM like '%Girdwood Trails%'"
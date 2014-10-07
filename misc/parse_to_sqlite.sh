
mkdir ../temp-data

#this sqlite file is used as an intermediate step in generating the geojson
rm ../temp-data/cache.sqlite
ogr2ogr -f SQLite -t_srs crs:84 ../temp-data/cache.sqlite ../source-data/trails_shp -sql "SELECT 'Muni' AS source, SYSTEM_NAM AS system, TRAIL_NAME AS name, SURFACE AS surface,TRAIL_CLAS AS class,LIGHTING AS lighting,GRADE AS difficulty,SKI_TYPE AS skitype FROM trails" -nln "muni_trails"

#load the suppressions table from a CSV
ogr2ogr -f SQLite -append ../temp-data/cache.sqlite suppressions.csv 

rm ../temp-data/all.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/all.geojson ../temp-data/cache.sqlite -sql "select t.* from muni_trails t left outer join suppressions s on t.source = s.source and t.system = s.system and (t.name = s.name or s.name = '*') and s.suppressed = 'true' where s.suppressed is null"
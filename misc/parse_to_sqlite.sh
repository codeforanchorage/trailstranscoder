
mkdir ../temp-data

#this sqlite file is used as an intermediate step in generating the geojson
rm ../temp-data/cache.sqlite

#muni file
ogr2ogr -f SQLite -t_srs crs:84 ../temp-data/cache.sqlite ../source-data/trails_shp -sql "SELECT 'Muni' AS source, SYSTEM_NAM AS system, TRAIL_NAME AS name, SURFACE AS surface,TRAIL_CLAS AS class,LIGHTING AS lighting,GRADE AS difficulty,SKI_TYPE AS skitype FROM trails" -nln "muni_trails"

#DNR files

ogr2ogr -f SQLite -append -t_srs crs:84 ../temp-data/cache.sqlite ../source-data/chugachstatepark.kml -sql "SELECT 'DNR' AS source, 'Chugach State Park' AS system, Name AS name FROM trails" -nln "chugach_trails"

ogr2ogr -f SQLite -append -t_srs crs:84 ../temp-data/cache.sqlite ../source-data/hatcherpassma.kml -sql "SELECT 'DNR' AS source, 'Hatcher Pass' AS system, Name AS name FROM trails" -nln "hatcher_pass_trails"

#matsu file

ogr2ogr -f SQLite -append -t_srs crs:84 ../temp-data/cache.sqlite ../source-data/MSB_Trails -sql "SELECT 'Matsu' AS source, NAME AS system, NAME_2 AS name FROM MSB_Trails_Legal_Aug2014" -nln "matsu_trails"


#load the suppressions table from a CSV
ogr2ogr -f SQLite -append ../temp-data/cache.sqlite suppressions.csv 

rm ../temp-data/all.geojson

ogr2ogr -f GeoJSON -t_srs crs:84 ../temp-data/all.geojson ../temp-data/cache.sqlite -sql "select t.* from muni_trails t left outer join suppressions s on t.source = s.source and t.system = s.system and (t.name = s.name or s.name = '*') and s.suppressed = 'true' where s.suppressed is null"


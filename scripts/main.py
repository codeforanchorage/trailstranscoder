"""
From:
    http://gis.stackexchange.com/questions/39080/how-do-i-use-ogr2ogr-to-convert-a-gml-to-shapefile-in-python
"""

import ogr2ogr

#note: main is expecting sys.argv, where the first argument is the script name
#so, the argument indices in the array need to be offset by 1
ogr2ogr.main(
    [
        "",
        "-f",
        "GeoJSON",
        "-t_srs",
        "crs:84",
        "../temp-data/kincaid-bounding-box.geojson",
        "../source-data/trails_shp",
        "-select",
        "SYSTEM_NAM,SURFACE,TRAIL_CLAS,TRAIL_NAME,LIGHTING,GRADE,SKI_TYPE",
        "-clipdst",
        "-150.1153",
        "61.12301",
        "-149.98707",
        "61.18463"
   ])


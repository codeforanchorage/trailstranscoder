-- Create table for stashing cleaned trails

CREATE TABLE cleaned_trails (
    OGC_FID INTEGER PRIMARY KEY ASC,
    GEOMETRY BLOB,
    source VARCHAR,
    system VARCHAR,
    name VARCHAR,
    surface VARCHAR,
    lighting VARCHAR,
    winter_usage INTEGER,
    summer_usage INTEGER,
    ski_difficulty VARCHAR,
    ski_mode VARCHAR,
    direction VARCHAR,
    handicap_accessible VARCHAR,
    comments VARCHAR,
    image_url VARCHAR,
    path VARCHAR,
    extent VARCHAR);

-- In order to take advantage of ogr2ogr, we need to make sure that the DB is aware of this layer.
INSERT INTO geometry_columns (
    f_table_name,
    f_geometry_column,
    geometry_type,
    coord_dimension,
    srid,
    geometry_format)
VALUES (
    'cleaned_trails',
    'GEOMETRY',
    5,
    2,
    4326,
    'WKB');


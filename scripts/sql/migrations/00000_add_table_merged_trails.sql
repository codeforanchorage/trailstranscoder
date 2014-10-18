-- Create table for merging trails into

CREATE TABLE merged_trails (
    OGC_FID INTEGER PRIMARY KEY ASC,
    GEOMETRY BLOB,
    source VARCHAR,
    system VARCHAR,
    name VARCHAR,
    identifier VARCHAR,
    surface VARCHAR,
    class VARCHAR,
    lighting VARCHAR,
    difficulty VARCHAR,
    skitype VARCHAR,
    comments VARCHAR,
    image_url VARCHAR);


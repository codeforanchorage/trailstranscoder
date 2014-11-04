-- Create table for merging points into

CREATE TABLE merged_points (
    OGC_FID INTEGER PRIMARY KEY ASC,
    GEOMETRY BLOB,
    source VARCHAR,
    system VARCHAR,
    name VARCHAR,
    type VARCHAR,
    comments VARCHAR,
    image_url VARCHAR,
    amenities int,
    radius float);


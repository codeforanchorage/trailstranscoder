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
    path VARCHAR);


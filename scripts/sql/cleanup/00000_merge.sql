-- Merge trail data from individual tables

INSERT INTO merged_trails (
    GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url)
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url
FROM muni_trails
UNION
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url
FROM chugach_trails
UNION
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url
FROM matsu_trails
UNION
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url
FROM hatcher_pass_trails
UNION
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype,
    comments,
    image_url
FROM kincaid_singletrack_trails


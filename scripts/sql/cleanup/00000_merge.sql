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
    skitype)
SELECT GEOMETRY,
    source,
    system,
    name,
    identifier,
    surface,
    class,
    lighting,
    difficulty,
    skitype
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
    skitype
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
    skitype
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
    skitype
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
    skitype
FROM kincaid_singletrack_trails


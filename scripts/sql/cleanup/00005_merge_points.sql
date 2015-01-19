-- Merge trail data from individual tables

INSERT INTO merged_points (
    GEOMETRY,
    source,
    system,
    name,
    type,
    comments,
    image_url,
    amenities)
SELECT GEOMETRY,
    source,
    system,
    name,
    type,
    comment,
    null,
    (case when parking = 'yes' then 1 else 0 end) + 
    (case when bathrooms = 'yes' then 2 else 0 end)
FROM kincaid_trailheads
union 
SELECT GEOMETRY,
    source,
    system,
    name,
    type,
    comment,
    null,
    (case when parking = 'yes' then 1 else 0 end) + 
    (case when bathrooms = 'yes' then 2 else 0 end)
FROM hillside_trailheads


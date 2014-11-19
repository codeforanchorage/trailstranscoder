-- Clean things up

INSERT INTO cleaned_trails
    SELECT
        OGC_FID,
        GEOMETRY,
        source,
        system,
        name,
        COALESCE(surface, 'Unknown'),
        COALESCE(lighting, 'No'),
        CASE
            WHEN system LIKE '%skijor%' THEN 16
            WHEN system LIKE '%ski%' AND NOT system LIKE '%skijor%' THEN 4
            WHEN system LIKE '%bike%' OR system LIKE '%single track%' THEN 2
            ELSE 1 | 2 | 64
        END AS winter_usage,
        CASE
            WHEN system LIKE '%bike%' OR system LIKE '%single track%' THEN 2
            ELSE 1 | 2 | 64
        END AS summer_usage,
        COALESCE(difficulty, 'Unknown'),
        COALESCE(skitype, 'Both'),
        '2way' AS direction,
        '2way' as summer_direction,
        '2way' as winter_direction,
        CASE
            WHEN surface='Asphalt' THEN 'Yes' ELSE 'No'
        END AS handicap_accessible,
        NULL AS comments,
        NULL AS image_url,
        NULL AS path,
        NULL AS extent,
        NULL AS length
    FROM merged_trails;

-- Some tweaks
UPDATE cleaned_trails SET winter_usage = winter_usage | 4
WHERE system LIKE '%ski%' AND NOT system LIKE '%skijor%';

UPDATE cleaned_trails SET winter_usage = winter_usage | 4
WHERE system LIKE '%campbell creek trail%';

UPDATE cleaned_trails SET winter_usage = winter_usage | 4
WHERE system LIKE '%coastal trail%';

UPDATE cleaned_trails SET winter_usage = winter_usage | 4
WHERE system LIKE '%chester creek trail%';

UPDATE cleaned_trails SET ski_difficulty = NULL, ski_mode = null
WHERE winter_usage & 4 = 0;

UPDATE cleaned_trails SET path = lower(source) || '/' || replace(lower(system), ' ', '_') || '/' || replace(lower(name), ' ', '_') || '.geojson'
WHERE source IS NOT NULL
AND system IS NOT NULL
AND name IS NOT NULL;

--merge in the ad hoc adjustments--
--sqlite doesn't allow joins in update statements, thus this mess---

replace into cleaned_trails
    (rowid, OGC_FID, GEOMETRY, source, system, name, surface, lighting, winter_usage, summer_usage, ski_difficulty, ski_mode, direction, winter_direction, summer_direction, handicap_accessible, comments, image_url, path, extent, length)
select dest.rowid, 
    dest.OGC_FID, 
    dest.GEOMETRY, 
    dest.source, 
    dest.system, 
    dest.name, 
    coalesce(nullif(source.surface,''), dest.surface),
    coalesce(nullif(source.lighting,''), dest.lighting),
    coalesce(nullif(source.winter_usage,''), dest.winter_usage),
    coalesce(nullif(source.summer_usage,''), dest.summer_usage),
    coalesce(nullif(source.ski_difficulty,''), dest.ski_difficulty),
    coalesce(nullif(source.ski_mode,''), dest.ski_mode),
    coalesce(nullif(source.direction,''), dest.direction),
    coalesce(nullif(source.winter_direction,''), dest.winter_direction),
    coalesce(nullif(source.summer_direction,''), dest.summer_direction),
    coalesce(nullif(source.handicap_accessible,''), dest.handicap_accessible),
    coalesce(nullif(source.comments,''), dest.comments),
    coalesce(nullif(source.image_url,''), dest.image_url),
    dest.path,
    dest.extent,
    dest.length
from cleaned_trails dest
    left outer join trail_adjustments source
        on dest.source = source.source
        and dest.system = source.system
        and dest.name = source.name



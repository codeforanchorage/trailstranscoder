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
        CASE
            WHEN surface='Asphalt' THEN 'Yes' ELSE 'No'
        END AS handicap_accessible
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

-- Create view for showing full cleaned trail info

CREATE VIEW v_cleaned_trails AS
    SELECT group_concat(f_summer.name) summer_usage_list, iq.*
    FROM (
        SELECT group_concat(f_winter.name) winter_usage_list, t.*
        FROM cleaned_trails t
        LEFT OUTER JOIN usage_flags f_winter
            ON t.winter_usage & f_winter.flag > 0
        GROUP BY OGC_FID
    ) iq
    LEFT OUTER JOIN usage_flags f_summer
        ON iq.summer_usage & f_summer.flag > 0
    GROUP BY OGC_FID;


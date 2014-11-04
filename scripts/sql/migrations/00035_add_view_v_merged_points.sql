-- Create view for showing full cleaned trail info

CREATE VIEW v_merged_points AS
    SELECT  p.*,
            group_concat(flags.name) amenities_list
        FROM merged_points p
        LEFT OUTER JOIN point_amenities_flags flags
            ON p.amenities & flags.flag > 0
        GROUP BY p.OGC_FID


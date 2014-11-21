--merge in the ad hoc adjustments--
--sqlite doesn't allow joins in update statements, thus this mess---

--this is a match on source/system/name
replace into cleaned_trails
    (rowid, OGC_FID, GEOMETRY, source, system, name, surface, lighting, winter_usage, summer_usage, ski_difficulty, ski_mode, direction, winter_direction, summer_direction, handicap_accessible, comments, image_url, path, extent, length, geometry_hash)
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
    dest.length,
    dest.geometry_hash
from cleaned_trails dest
    left outer join trail_adjustments source
        on dest.source = source.source
        and dest.system = source.system
        and dest.name = source.name
        and nullif(source.geometry_hash,'') is null;

--and this is a match on the geometry_hash
replace into cleaned_trails
    (rowid, OGC_FID, GEOMETRY, source, system, name, surface, lighting, winter_usage, summer_usage, ski_difficulty, ski_mode, direction, winter_direction, summer_direction, handicap_accessible, comments, image_url, path, extent, length, geometry_hash)
select 
    dest.rowid, 
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
    dest.length,
    dest.geometry_hash
from cleaned_trails dest
    join trail_adjustments source
        on dest.geometry_hash = source.geometry_hash;



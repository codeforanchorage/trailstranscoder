CREATE TABLE usage_flags
	(
		Flag INTEGER PRIMARY KEY,
		Name VARCHAR
	);



insert into usage_flags (Flag, Name)
	select 1, 'Foot'
	union
	select 2, 'Bike'
	union
	select 4, 'Ski'
	union
	select 8, 'Snowshoe'
	union
	select 16, 'Skijor'
	union
	select 32, 'Mush'
	union
	select 64, 'Dog Walk'
	union
	select 128, 'Off-Leash Dog';


CREATE TABLE cleaned_trails (OGC_FID INTEGER PRIMARY KEY ASC,
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
            handicap_accessible VARCHAR
            );

insert into cleaned_trails
	select 
		OGC_FID,
		GEOMETRY,
		source,
		system,
		name,
		coalesce(surface, 'Unknown'),
		coalesce(lighting, 'No'),
		case 
			when system like '%skijor%' then 16 
			when system like '%ski%' then 4 
			when system like '%bike%' or system like '%single track%' then 2
			else 1 | 2 | 64 end --default: foot/bike/dog
			winter_usage,
		1 | 2 | 64 summer_usage, --default: foot/bike/dog
		coalesce(difficulty, 'Unknown'),
		coalesce(skitype, 'Both'),
		'2way' direction,
		case when surface = 'Asphalt' then 'Yes' else 'No' end handicap_accessible
	from merged_trails;

-- here go the update statements

--update cleaned_trails set winter_usage = winter_usage | 4 where system like '%ski%'
--update cleaned_trails set winter_usage = winter_usage | 4 where system like '%ski%'

--run ogr2ogr against this when finished
--ogr2ogr -f GeoJSON  ./out.geojson ./temp.sqlite -sql "select * from cleaned_trails"
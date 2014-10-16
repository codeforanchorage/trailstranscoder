trailstranscoder
================

A toolchain for transcoding and cleaning Alaska trail data.

![technicolor_trails](https://cloud.githubusercontent.com/assets/274668/4655646/06c11ec2-54c7-11e4-96ec-f7b6fe6478b7.png)

Motivation
----------

Tools like [GDAL](http://gdal.org) provide excellent out-of-the box support for
processing various geo-related data. The aim of
[trailstranscoder](https://github.com/codeforanchorage/trailstranscoder) is to
provide a set of simple scripts to handle the processing of multiple disparate
data sources, and consolidate them down into a uniform format. This is not an
attempt to provide a service platform like
[trailsyserver](https://github.com/codeforamerica/trailsyserver) --- the idea
is to prepare a standardized dataset for the specific purpose of unifying trail
data. There is no automatic attribute discovery, the burden of understanding
the upstream data falls upon the user.

Requirements
------------

- GDAL >= 1.11.0
- Python >= 2.7.0

Getting Started
---------------

    pip install -r requirements.txt
    cd scripts
    python main.py

Sample Output
-------------
```
output
├── all.geojson
├── dnr
│   ├── all.geojson
│   ├── chugach_state_park
│   │   ├── abes.geojson
│   │   ├── albert_loop.geojson
│   │   ├── alder.geojson
│   │   ├── alder_2.geojson
│   │   ├── all.geojson
│   │   ├── anchorage_overlook.geojson
...
│   └── hatcher_pass
│       ├── all.geojson
│       ├── april_bowl.geojson
│       ├── arch_prospect.geojson
│       ├── assay_spur.geojson
│       ├── gold_cord_lake.geojson
│       ├── gold_mint.geojson
│       ├── hard_rock.geojson
...
├── matsu
│   ├── all.geojson
│   ├── archangel
│   │   ├── all.geojson
│   │   └── none.geojson
│   ├── baxter_mine
│   │   ├── all.geojson
│   │   └── none.geojson
│   ├── big_swamp
│   │   ├── all.geojson
│   │   └── none.geojson
...
└── muni
    ├── abbott_loop_trail
    │   ├── abbott_loop_trail.geojson
    │   └── all.geojson
    ├── abbott_trail
    │   ├── abbott_trail.geojson
    │   ├── all.geojson
    │   └── unnamed.geojson
    ├── all.geojson
    ├── bartlett_ski_trails
    │   ├── all.geojson
    │   └── bartlett.geojson
    ├── beech_lake_dog_trails
    │   ├── all.geojson
    │   └── none.geojson
    ├── beech_lake_ski_trails
    │   ├── all.geojson
    │   ├── appendix.geojson
    │   ├── bridge_loop.geojson
    │   ├── christy_loop.geojson
    │   ├── coach's_cutoff.geojson
    │   ├── corral_loop.geojson
    │   ├── executioner.geojson
    │   ├── hill_loop.geojson
    │   ├── junkyard.geojson
    │   ├── low_road.geojson
    │   ├── mama's_loop.geojson
    │   ├── none.geojson
    │   ├── north_pasture.geojson
    │   └── unnamed.geojson
...
```


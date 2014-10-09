trailstranscoder
================

A toolchain for transcoding and cleaning Alaska trail data.

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


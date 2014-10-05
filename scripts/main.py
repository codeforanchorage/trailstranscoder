"""A toolchain for transcoding and cleaning Alaska trail data.

Drop your data in source-data (unpacked), define a new config in scripts/configs,
add the config to scripts/configs/__init__.py, then run this file.
"""

# Global imports
import os

# Local imports
import ogr2ogr
import configs

for config in configs.configList:
    try:
        os.remove(config["destination"])
    except OSError:
        pass
    # note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1
    opts = [
        "",
        "-f",
        "GeoJSON",
        "-t_srs",
        config["crs"],
        config["destination"],
        config["source"],
        "-sql",
        config["sql"],
        "-clipdst",
        config["clip"]["southwest"][0],
        config["clip"]["southwest"][1],
        config["clip"]["northeast"][0],
        config["clip"]["northeast"][1]
    ]
    ogr2ogr.main(opts)

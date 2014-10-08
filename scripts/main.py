"""A toolchain for transcoding and cleaning Alaska trail data.

Drop your data in source-data (unpacked), define a new config in scripts/configs,
add the config to scripts/configs/__init__.py, then run this file.
"""

# Global imports
from os import remove
from subprocess import call

# Local imports
import configs

def buildOpts(config, outFormat, outPath):
    # Note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1
    opts = ["ogr2ogr", "-f", outFormat, outPath]

    flagMap = {
        "sql": "-sql",
        "crs": "-t_srs",
        "clip": "-clipdst",
        "newlayername": "-nln",
        "append": "-append",
        "update": "-update",
    }

    for c in config:
        if c in flagMap:
            if c != "clip":
                if c not in ["append", "update"]:
                    opts.extend([flagMap[c], config[c]])
                else:
                    opts.extend([flagMap[c]])
            else:
                opts.extend([flagMap[c],
                    config[c]["southwest"][0], config[c]["southwest"][1],
                    config[c]["northeast"][0], config[c]["northeast"][1]])
        else:
            opts.append(config[c])

    return opts

def cleanup(path):
    try:
        remove(path)
    except OSError:
        pass

def sourceImport(config):
    opts = buildOpts(config, "SQLite", configs.temp_path)
    call(opts)

def mergeTrails(path):
    pass

def generateJSON(path):
    # Todo: revisit once merging is done (geojson doesn't support exporting
    # multiple layers
    # outpath = configs.output_path + "/all.geojson"
    # cleanup(outpath)
    # config = {
    #     "crs": "crs:84",
    #     "source": configs.temp_path,
    # }
    # opts = buildOpts(config, "GeoJSON", outpath)
    # call(opts)
    pass

def main():
    cleanup(configs.temp_path)
    for config in configs.configList:
        sourceImport(config)
    mergeTrails(configs.temp_path)
    generateJSON(configs.temp_path)

if __name__ == "__main__":
    main()


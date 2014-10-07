"""A toolchain for transcoding and cleaning Alaska trail data.

Drop your data in source-data (unpacked), define a new config in scripts/configs,
add the config to scripts/configs/__init__.py, then run this file.
"""

# Global imports
from os import remove

# Local imports
import ogr2ogr
import configs

def buildOpts(config):
    # Note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1
    opts = ["", "-f", "SQLite"]

    flagMap = {
        "sql": "-sql",
        "crs": "-t_srs",
        "clip": "-clipdst",
        "newlayername": "-nln",
    }

    for c in config:
        if c in flagMap:
            if c != "clip":
                opts.extend([flagMap[c], config[c]])
            else:
                opts.extend([flagMap[c],
                    config[c]["southwest"][0], config[c]["southwest"][1],
                    config[c]["northeast"][0], config[c]["northeast"][1]])
        else:
            opts.append(config[c])

    return opts

def cleanup(config):
    try:
        remove(config["destination"])
    except OSError:
        pass

def main():
    for config in configs.configList:
        cleanup(config)
        opts = buildOpts(config)
        ogr2ogr.main(opts)

if __name__ == "__main__":
    main()


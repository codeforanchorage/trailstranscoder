"""A toolchain for transcoding and cleaning Alaska trail data.

Drop your data in source-data (unpacked), define a new config in scripts/configs,
add the config to scripts/configs/__init__.py, then run this file.
"""

# Global imports
from os import remove, makedirs
from shutil import rmtree
from subprocess import call
import sqlite3
import collections

# Local imports
import configs

def buildOpts(config, outFormat, outPath):
    # Note: main is expecting sys.argv, where the first argument is the script name
    # so, the argument indices in the array need to be offset by 1
    opts = ["ogr2ogr", "-f", outFormat, outPath]

    flagMap = {
        "sql": "-sql",
        "tsrs": "-t_srs",
        "ssrs": "-s_srs",
        "clip": "-clipdst",
        "newlayername": "-nln",
        "append": "-append",
        "update": "-update",
        "type": "-nlt",
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

def cleanup_file(path):
    try:
        remove(path)
    except OSError:
        pass

def cleanup_path(path):
    try:
        rmtree(path)
    except OSError:
        pass

def sourceImport(config):
    opts = buildOpts(config, "SQLite", configs.temp_path)
    call(opts)

def mergeTrails(path, tablenames):
    conn = sqlite3.connect(configs.temp_path)
    c = conn.cursor()
    # Create table to merge into
    c.execute("""
        CREATE TABLE merged_trails(OGC_FID INTEGER PRIMARY KEY ASC,
            GEOMETRY BLOB, source VARCHAR, system VARCHAR, name VARCHAR,
            identifier VARCHAR, surface VARCHAR, class VARCHAR, lighting VARCHAR,
            difficulty VARCHAR, skitype VARCHAR);
        """)
    for tn in tablenames:
        c.execute("""
            INSERT INTO merged_trails (
                GEOMETRY, source, system, name, identifier, surface, class,
                lighting, difficulty, skitype
                )
            SELECT t.GEOMETRY, t.source, t.system, t.name, t.identifier, t.surface,
                t.class, t.lighting, t.difficulty, t.skitype
            FROM {0} t
            LEFT OUTER JOIN suppressions s
                ON t.source = s.source
                AND t.system = s.system
                AND (t.name = s.name OR s.name = '*')
                AND suppressed = 'true'
            WHERE s.suppressed IS NULL;
        """.format(tn,))
    conn.commit()
    conn.close()

def generateJSON(path):
    outpath = configs.output_path + "/all.geojson"
    cleanup_file(outpath)
    # All
    config = collections.OrderedDict()
    config["tsrs"] = "crs:84"
    config["ssrs"] = "crs:84"
    config["source"] = configs.temp_path
    config["sql"] = "SELECT * FROM merged_trails;"
    opts = buildOpts(config, "GeoJSON", outpath)
    call(opts)
    # Sources
    conn = sqlite3.connect(configs.temp_path)
    c1 = conn.cursor()
    for source in c1.execute("SELECT DISTINCT source FROM merged_trails;"):
        config["sql"] = "SELECT * FROM merged_trails WHERE source='{0}'".format(source[0])
        outpath = "".join([configs.output_path, "/", source[0].lower()])
        cleanup_path(outpath)
        makedirs(outpath)
        opts = buildOpts(config, "GeoJSON", outpath + "/all.geojson")
        call(opts)
        # Sources + Systems
        c2 = conn.cursor()
        q2 = """SELECT DISTINCT system
                FROM merged_trails
                WHERE source='{0}';""".format(source[0])
        for system in c2.execute(q2):
            config["sql"] = """SELECT *
                               FROM merged_trails
                               WHERE source='{0}'
                               AND system='{1}';""".format(source[0], system[0])
            if not system[0]:
                s = 'none'
            else:
                s = system[0].replace(' ', '_').lower()
            outpath = "".join([configs.output_path, "/", source[0].lower(), "/", s])
            makedirs(outpath)
            opts = buildOpts(config, "GeoJSON", outpath + "/all.geojson")
            call(opts)
            # Sources + Systems + Names
            c3 = conn.cursor()
            q3 = """SELECT DISTINCT name
                    FROM merged_trails
                    WHERE source='{0}'
                    AND system='{1}';""".format(source[0], system[0])
            for name in c3.execute(q3):
                config["sql"] = """SELECT *
                                   FROM merged_trails
                                   WHERE source='{0}'
                                   AND system='{1}'
                                   AND name='{2}';""".format(source[0], system[0], escape_ogr(name[0]))
                if not name[0]:
                    name = 'none'
                else:
                    name = name[0].replace(' ', '_').lower()
                outpath = "".join([configs.output_path, "/", source[0].lower(),
                    "/", s, "/", name, ".geojson"])
                opts = buildOpts(config, "GeoJSON", outpath)
                call(opts)
    conn.close()

def escape_ogr(s):
    # We need to escape single quotes for OGR SQLite calls
    escape = set ("'")
    if s:
        ret = "".join(char * 2 if char in escape else char for char in s)
    else:
        ret = ""
    return ret

def main():
    cleanup_file(configs.temp_path)
    tables = []
    for config in configs.configList:
        tables.append(config["newlayername"])
        sourceImport(config)
    tables = tables[:-1] # We don't want to include the suppressions
    mergeTrails(configs.temp_path, tables)
    generateJSON(configs.temp_path)

if __name__ == "__main__":
    main()


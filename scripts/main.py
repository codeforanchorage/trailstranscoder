"""A toolchain for transcoding and cleaning Alaska trail data.

Drop your data in source-data (unpacked), define a new config in scripts/configs,
add the config to scripts/configs/__init__.py, update sql/cleanup/00000_merge.sql,
then run this file.

Authors: Code for Anchorage Brigade
"""

# Global imports
from os import remove, makedirs, listdir
from shutil import rmtree
from subprocess import call
import sqlite3
import collections

# Local imports
import configs

def buildOpts(config, outFormat, outPath):
    """Generates a call to ogr2ogr"""
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

def remove_file(path):
    """Removes a file from the filesystem"""
    try:
        remove(path)
    except OSError:
        pass

def remove_path(path):
    """Removes a directory from the filesystem"""
    try:
        rmtree(path)
    except OSError:
        pass

def sourceImport(config):
    """Initial pass for getting data out of upstream format and into something
        that is a bit easier to work with"""
    opts = buildOpts(config, "SQLite", configs.temp_path)
    call(opts)

def runScripts(path):
    """Helper for running SQL scripts on disk"""
    conn = sqlite3.connect(configs.temp_path)
    c = conn.cursor()
    scripts = listdir(path)
    for script in scripts:
        f = open("/".join([path, script]), "r")
        sql = f.read()
        c.executescript(sql)
        conn.commit()
    conn.close()

def migrate():
    """Migrate the SQLite DB"""
    runScripts(configs.migrations_path)

def clean():
    """Run the cleanup protocols"""
    runScripts(configs.cleanup_path)

def generateJSON(path):
    """This could be smarter, but right now the idea is to loop over all of the
        v_cleaned_trails, and dump a structured set of GeoJSON files to disk"""
    outpath = configs.output_path + "/all.geojson"
    remove_file(outpath)
    # All
    config = collections.OrderedDict()
    config["tsrs"] = "crs:84"
    config["ssrs"] = "crs:84"
    config["source"] = configs.temp_path
    config["sql"] = "SELECT * FROM v_cleaned_trails;"
    opts = buildOpts(config, "GeoJSON", outpath)
    call(opts)
    # Sources
    conn = sqlite3.connect(configs.temp_path)
    c1 = conn.cursor()
    for source in c1.execute("SELECT DISTINCT source FROM v_cleaned_trails;"):
        config["sql"] = "SELECT * FROM v_cleaned_trails WHERE source='{0}'".format(source[0])
        outpath = "/".join([configs.output_path, source[0].lower()])
        remove_path(outpath)
        makedirs(outpath)
        opts = buildOpts(config, "GeoJSON", outpath + "/all.geojson")
        call(opts)
        # Sources + Systems
        c2 = conn.cursor()
        q2 = """SELECT DISTINCT system
                FROM v_cleaned_trails
                WHERE source='{0}';""".format(source[0])
        for system in c2.execute(q2):
            config["sql"] = """SELECT *
                               FROM v_cleaned_trails
                               WHERE source='{0}'
                               AND system='{1}';""".format(source[0], system[0])
            if not system[0]:
                s = 'none'
            else:
                s = system[0].replace(' ', '_').lower()
            outpath = "/".join([configs.output_path, source[0].lower(), s])
            makedirs(outpath)
            opts = buildOpts(config, "GeoJSON", outpath + "/all.geojson")
            call(opts)
            # Sources + Systems + Names
            c3 = conn.cursor()
            q3 = """SELECT DISTINCT name
                    FROM v_cleaned_trails
                    WHERE source='{0}'
                    AND system='{1}';""".format(source[0], system[0])
            for name in c3.execute(q3):
                config["sql"] = """SELECT *
                                   FROM v_cleaned_trails
                                   WHERE source='{0}'
                                   AND system='{1}'
                                   AND name='{2}';""".format(source[0], system[0], escape_ogr(name[0]))
                if not name[0]:
                    name = 'none'
                else:
                    name = name[0].replace(' ', '_').lower()
                outpath = "/".join([configs.output_path, source[0].lower(), s, name+".geojson"])
                opts = buildOpts(config, "GeoJSON", outpath)
                call(opts)
    conn.close()

def escape_ogr(s):
    """We need to escape single quotes for OGR SQLite calls"""
    escape = set ("'")
    if s:
        ret = "".join(char * 2 if char in escape else char for char in s)
    else:
        ret = ""
    return ret

def main():
    """Main workflow"""
    remove_file(configs.temp_path)
    # First import all source data into their own tables
    for config in configs.configList:
        sourceImport(config)
    # Then, apply our migrations
    migrate()
    # Then, apply our cleanup rules
    clean()
    # Lastly, generate output
    generateJSON(configs.temp_path)

if __name__ == "__main__":
    main()


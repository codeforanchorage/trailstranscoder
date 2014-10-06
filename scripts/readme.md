This directory contains the Python scripts that participate in the main workflow.

To run it:

```
python main.py
```

Basically, it works this way:

1. main.py looks in the /configs directory for which transcodings to run. It simply loops over them and builds a complex command for each one to be sent to ogr2ogr.
2. ogr2ogr.py does the heavy lifting of transcoding.
3. The files in the /configs directory basically contain a bunch of dictionaries with settings for each transoding (such as source, destination, filters, field mappings, etc.)

Note:

To run this, you need to view index.html via HTTP, not FILE.

A simple way to do this is using the built-in Python HTTP server.

```
cd feature-browser
python -m SimpleHTTPServer 8000
```

You now have a web server running on port 8000. 

Open a browser and go to http://127.0.0.1:8000 to view index.html.

Note that index.html looks for the geojson files in a directory called "output" which is symlinked to the output directory in the root of the repo. That directory will be empty until you run main.py.

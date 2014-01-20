tanr
====

This script creates a new Python Flask web application given an application name. This script utilizes the directions given on the Flask website: http://flask.pocoo.org/docs/patterns/packages/

##Usage
python tanr.py app_name path/to/destination

If no path provided, tanr assumes that the current directory is the desired directory.

Optional flags are:
-s, --search: This flag generates a '/search' endpoint, stub search code, and a search template to render your results.

# Simple web scraper to make finding a used car easier

Written in Python using Flask.

## To run the app

First set up a virtual environment:

`$ sudo pip install virtualenv`

Set up a virtual environment in the project root directory:

`$ virtualenv venv`

To activate the environment run:

`$ . venv/bin/activate`

To run the Flask server from the terminal, set the FLASK_APP environment variable:

`$ export FLASK_APP=server.py`

And to run the server:

`$ flask run`

This runs local host on port 5000.

To run with [Gunicorn](http://gunicorn.org/#quickstart), for the web server, run:

`gunicorn -b 127.0.0.1:4000 server:app`

To add worker processes, add `-w 4` flag for 4 processors.

For further information, see the [Flask docs](http://flask.pocoo.org/docs/0.12/quickstart/#quickstart) and the Python docs for [Virtual environments](https://pypi.python.org/pypi/virtualenv).

#!/usr/bin/python3
"""  a script that starts a flask web application on 0.0.0.0:5000
    routes:
        /: displays Hello HBNB!
        /hbnb: displays HBNB
        /c/<text>: displays 'C ' + any test given
"""

from flask import Flask
""" Importing the Flask module """

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ represents the main page """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ represents /hbnb page """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """ represents /c/<anytext> """
    return "C " + " ".join(text.split('_'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

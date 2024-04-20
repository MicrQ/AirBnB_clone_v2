#!/usr/bin/python3
"""  a script that starts a flask web application on 0.0.0.0:5000
    routes:
        /: displays Hello HBNB!
        /hbnb: displays HBNB
        /c/<text>: displays 'C ' + any test given
        /python/<text>: displays 'Python is cool' by default is no text
                        is given. else the 'Python text'
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
    """ represents /c/<anytext> page """
    return "C " + " ".join(text.split('_'))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pythoniscool(text="is cool"):
    """ represents /python/<anytext> page """
    return "Python " + " ".join(text.split('_'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

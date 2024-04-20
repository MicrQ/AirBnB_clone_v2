#!/usr/bin/python3
""" a script that starts a flask web application on 0.0.0.0:5000 """

from flask import Flask
""" Importing the Flask module """

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ represents the main page """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')

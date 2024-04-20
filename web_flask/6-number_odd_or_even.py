#!/usr/bin/python3
"""  a script that starts a flask web application on 0.0.0.0:5000
    routes:
        /: displays Hello HBNB!
        /hbnb: displays HBNB
        /c/<text>: displays 'C ' + any test given
        /python/<text>: displays 'Python is cool' by default is no text
                        is given. else the 'Python text'
        /number/<n>: displays 'n is a number' only if n is integer.
        /number_template/<n>: renders content of templates/5-number.html file.
        /number_odd_or_even/<n>: display a HTML page only if n is an integer:
                            H1 tag: “Number: n is even|odd” inside the tag BODY
"""

from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ represents number/<int:n> page """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ represents /number_template/<int:n> page """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ represents /number_odd_or_even/<n> page """
    # dataType = 'even' if n % 2 == 0 else 'odd'
    """ return render_template('6-number_odd_or_even.html',
                             n=n, dataType=dataType)
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')

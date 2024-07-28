#!/usr/bin/python3
"""Module for running flask app"""


from flask import Flask
from flask import abort
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Route handler for the index page request"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route handler for /hbnb request"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def cfun(text):
    """Route handler for /c/<text> request"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_cool(text):
    """Route handler for /python/<text> request"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def is_number(n):
    """Route handler for /number/<n> request"""
    if n.isnumeric():
        return f"{n} is a number"
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """Route handler for /number_template/<n> request"""
    if n.isnumeric():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """Route handler for /number_odd_or_even/<n> request"""
    if n.isnumeric():
        return render_template('6-number_odd_or_even.html', n=int(n))
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

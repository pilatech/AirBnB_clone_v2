#!/usr/bin/python3
"""Module for running flask app"""


from flask import Flask
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

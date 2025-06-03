#!/usr/bin/python3
"""
4-number_route.py
All routes use strict_slashes=False.
The app listens on 0.0.0.0, port 5000.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route '/' that returns 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route '/hbnb' that returns 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route '/c/<text>' that returns 'C ' followed by the text variable.
    Underscores in text are replaced with spaces.
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """
    followed by the text variable.
    The default value of text is 'is cool'.
    Underscores in text are replaced with spaces.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    n is a number' only if n is an integer.
    Flask automatically handles type checking for <int:n>.
    """
    return "{} is a number".format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#!/usr/bin/python3
"""Flask app: Route for dynamic Python text with default value"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """replacing underscores with spaces"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """Displays Python followed by value of text (default: is cool)"""
    text = text.replace('_', ' ')
    response = "Python {}".format(text)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

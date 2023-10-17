#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def rout():
    """Route '/'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route '/hbnb'"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_variable(text):
    """Adding an argument to the definition"""
    return "C {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

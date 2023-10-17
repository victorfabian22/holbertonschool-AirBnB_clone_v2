#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(exception):
    """remove session from SQLAlchemy"""
    storage.close()


@app.route('/states_list', strict_slashes=False):
def states_list():
    """Path to display html page"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', my_dict=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

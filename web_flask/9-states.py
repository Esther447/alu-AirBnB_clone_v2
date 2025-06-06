#!/usr/bin/python3
"""Starts a Flask web application with states and cities"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove current SQLAlchemy session after each request"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Display a page with all states or one state with its cities"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)

    if id:
        for state in states:
            if state.id == id:
                return render_template(
                    '9-states.html', state=state, all_states=False
                )
        return render_template('9-states.html', state=None, all_states=False)

    return render_template('9-states.html', states=states, all_states=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

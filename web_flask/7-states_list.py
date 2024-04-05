#!/usr/bin/python3
"""
start flask
"""

from flask import Flask, render_template
from models import storage
from models import *
applica = Flask(__name__)


@applica.route('/states_list', strict_slashes=False)
def listState():
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@applica.teardown_appcontext
def db_db(exception):
    storage.close()

if __name__ == '__main__':
    applica.run(host='0.0.0.0', port='5000')

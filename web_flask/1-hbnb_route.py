#!/usr/bin/python3
"""
start flask
"""

from flask import Flask
applica = Flask(__name__)


@applica.route('/', strict_slashes=False)
def idx():
    return 'Hello HBNB!'

@applica.route('/hbnb', strict_slashes=False)
def hbnbR():
    return 'HBNB'
if __name__ == '__main__':
    applica.run(host='0.0.0.0', port='5000')

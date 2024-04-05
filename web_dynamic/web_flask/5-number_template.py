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

@applica.route('/c/<text>', strict_slashes=False)
def Cisfun(text):
    return 'C ' + text.replace('_', ' ')

@applica.route('/python', strict_slashes=False)
@applica.route('/python/<text>', strict_slashes=False)
def pythoniscool(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

@applica.route('/number/<int:n>', strict_slashes=False)
def NumBer(n):
    return "{:d} is a number".format(n)

@applica.route('/number_template/<int:n>', strict_slashes=False)
def numbertotemp(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    applica.run(host='0.0.0.0', port='5000')

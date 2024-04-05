#!/usr/bin/python3
"""start Flask web application """

from flask import Flask
applica = Flask(__name__)


@applica.route('/', strict_slashes=False)
def helloBNB():
    return 'Hello HBNB!'

if __name__ == '__main__':
    applica.run(host='0.0.0.0', port=5000)

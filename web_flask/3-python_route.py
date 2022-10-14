#!/usr/bin/python3
"""
starys flask app
"""
from flask import Flask
app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_variable_name(text):
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_variable_name(text='is cool'):
    return 'Python ' + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

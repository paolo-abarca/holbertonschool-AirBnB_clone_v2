#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """
    function that returns a Hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """
    function that returns a HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    function that returns a c and text
    """
    result = text.replace("_", " ")
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """
    function that returns a python and text
    """
    result = text.replace("_", " ")
    return "Python {}".format(result)


@app.route("/number/<int:n>", strict_slashes=False)
def number_text(n):
    """
    function that returns a n and text
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

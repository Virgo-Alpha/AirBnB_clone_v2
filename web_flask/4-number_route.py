#!/usr/bin/python3
"""
A script that starts a Flask Web Application
/: Diplays "Hello HBNB!"
/hbnb: Displays "HBNB"
/c/<text>: display “C ” followed by \
    the value of the text variable
/python/(<text>): display “Python ”,
    followed by the value of the text variable
/number/<n>: display “n is a number”
    *only if n is an integer
    (replace underscore _ symbols with a space)
"""


from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
def python_magic():
    return "Python is cool"


@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'python' followed by the value of <text>"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Displays 'n is a number' if n is an integer"""
    return "{:d} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')

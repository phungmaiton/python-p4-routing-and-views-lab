#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"


@app.route("/print/<string:string>")
def print_string(string):
    print(f"{string}")
    return string


@app.route("/count/<int:num>")
def count(num):
    result = ""
    for i in range(num):
        result += str(i) + "\n"
    return result


@app.route("/math/<int:num1>/<operator>/<int:num2>")
def perform_math(num1, operator, num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "div":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    else:
        return "Invalid operator"

    return str(result)


if __name__ == "__main__":
    app.run(port=5555, debug=True)

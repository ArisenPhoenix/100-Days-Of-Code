from flask import Flask
from decorators import embolden, italicize, to_header, time_to_run
from random import random

app = Flask(__name__)

rand = int(random() * 10)

print(rand)


@app.route("/")
@time_to_run
@to_header
@italicize
@embolden
def guess():
    return "Guess a number between 0 and 9"


@app.route("/<number>")
def get_number(number):
    if int(number) == rand:
        return "<h1>Correct</h1>"
    elif int(number) > rand:
        return "<h1>That  Number is too High</h1>"
    elif int(number) < rand:
        return "<h1>That Number is too Low</h1>"


if __name__ == "__main__":
    app.run(debug=True)
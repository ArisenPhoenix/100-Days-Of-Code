from flask import Flask
from decorators import embolden, italicize, to_header, time_to_run

app = Flask(__name__)


@app.route("/")
@time_to_run
@to_header
@italicize
@embolden
def bye():
    text = "Bye!"
    return text


if __name__ == "__main__":
    app.run(debug=True)

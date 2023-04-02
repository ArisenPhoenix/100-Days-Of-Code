from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests


app = Flask(__name__)


@app.route("/")
def home():
    rand = randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=rand, year=current_year)


@app.route("/guess")
def guess():
    return "<h1>What's Your Name? Put it in.</h1>"


@app.route("/guess/<name>")
def guessed(name):
    gender_uri = f"https://api.genderize.io?name={name}"
    age_uri = f"https://api.agify.io?name={name}"
    gender = requests.get(gender_uri).json()["gender"]
    age = requests.get(age_uri).json()["age"]
    
    print(gender)
    print(age)
    return render_template("name_response.html", name=name.title(), gender=gender, age=age )


@app.route("/blogs/<num>")
def get_blog(num):
    uri = "https://api.npoint.io/c489f8cfe08da2d35bee"
    response = requests.get(uri)
    posts = response.json()
    return render_template("blog.html", posts=posts)

    
if __name__ == "__main__":
    app.run(debug=True)

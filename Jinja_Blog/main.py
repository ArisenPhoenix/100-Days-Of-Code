from flask import Flask, render_template
from datetime import datetime
import requests
from pprint import pprint
app = Flask(__name__)


currentYear = datetime.now().year

uri = "https://api.npoint.io/ca9da7b936dbd5db25a2"
posts = requests.get(uri).json()
# pprint(posts)


@app.route("/")
def home():
    return render_template("index.html", year=currentYear, posts=posts)


@app.route("/<post_id>")
def full_post(post_id):
    show_post = [posted for posted in posts if str(posted["id"]) == str(post_id)]
    return render_template("full_post.html", post=show_post[0])


@app.route("/about")
def about():
    return render_template("about.html", year=currentYear)


@app.route("/post")
def post():
    return render_template("post.html", year=currentYear)


@app.route("/contact")
def contact():
    return render_template("contact.html", year=currentYear)


if __name__ == "__main__":
    app.run(debug=True)

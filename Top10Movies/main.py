from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Top_10_Movies-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer,  nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250),  nullable=False)
    
    def __repr__(self):
        return f'<Book  {self.title}'


db.create_all()


all_movies = db.session.query(Movie).all()


class UpdateForm(FlaskForm):
    update = StringField(label="Rating")
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html", movies=all_movies)


def update():
    form = UpdateForm()
    if form.validate_on_submit():
        f = form.update.data
        f.save(os.path.join(app.instance_path, "updates",))


if __name__ == '__main__':
    app.run(debug=True)



# new_movie = Movie(title="Phone Booth",
#                   year=2002,
#                   description=""" Publicist Stuart Shepard finds
#                   himself trapped in a phone booth, pinned down by
#                   an extortionist's sniper rifle. Unable to leave.""",
#                   rating=7.3,
#                   ranking=10,
#                   review="My favorite character was the caller",
#                   img_url="""https://image.tmdb.org/t/p/w500/tjrX2
#                   oWRCM3Tvarz38zlZM7Uc10.jpg""")
#
#
# db.session.add(new_movie)
# db.session.commit()
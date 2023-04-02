from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = StringField("Password", validators=[DataRequired()])


app = Flask(__name__)
app.secret_key = "MerK"

WTF_CSRF_SECRET_KEY = 'a random string'


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login")
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template("login.html", form=login_form)


@app.route("/secrets")
def secrets():
    return render_template("success.html")


if __name__ == '__main__':
    app.run(debug=True)
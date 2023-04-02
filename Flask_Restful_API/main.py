from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record
@app.route("/all")
def get_all():
    all_cafes = Cafe.query.all()
    print(all_cafes)
    return render_template("all.html", cafes=all_cafes)

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record


@app.route("/update_price<cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    cafe_to_update = Cafe.query.filter_by(id=cafe_id).first()
    if cafe_to_update:
        cafe_to_update.coffee_price = new_price
        db.session.commit()
        print(cafe_id)
        print(cafe_to_update)
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(response={"error": "Sorry, a cafe with that id was not found."})
6

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

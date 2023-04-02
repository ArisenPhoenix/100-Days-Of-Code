from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from jinja2.utils import markupsafe


Markup = markupsafe.Markup
Markup("")
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Book  {self.title}'


db.create_all()


all_books = db.session.query(Book).all()


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


# searching will be this syntax:
# book = Book.query.filter_by(title="Harry Potter").first()

# Updating One Record:
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "NEW TITLE"
# db/session.commit()

# Delete by primary key
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        
        a_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }

        new_book = Book(title=a_book["title"], author=a_book["author"], rating=a_book["rating"])
        db.session.add(new_book)
        db.session.commit()
        
        all_books.append(a_book)
        return redirect(url_for("home"))
    
    return render_template("add.html")


@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_edit = Book.query.get(book_id)
        book_to_edit.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for("home"))
    book_id = request.args.get('id')
    book_selected = Book.query.get(book_id)
    
    return render_template("edit_rating.html", book=book_selected)


@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)

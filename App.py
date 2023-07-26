from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

db=SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///Notes.db"

db.init_app(app)

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String)
    date_created=db.Column(db.DateTime,default=datetime.utcnow())


    def __repr__(self) -> str:
        return f"{self.id} - {self.email}"

with app.app_context():
    db.create_all()

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def about():
    new_data=Note(email="dk@outlook.com")
    db.session.add(new_data)
    db.session.commit()
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/market")
def market():
    all_data=Note.query.all()
    details = [
        {"name": "deepak", "role": "developer", "phn": 70426},
        {"name": "dk1", "role": "front-end", "phn": 70092},
    ]
    return render_template("market.html", d=details, data=all_data)


@app.route("/about/<user>")
def dyn(user):
    return f"<h1>hello {user}</h1>"


app.run(debug=True)

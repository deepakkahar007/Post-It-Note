from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

db=SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///Notes.db"
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///User.db"

db.init_app(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    email=db.Column(db.String(length=30),nullable=False,unique=True)
    password=db.Column(db.String(length=30),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow())

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

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="POST":
        new_user=User(name=request.form['name'],email=request.form['email'],password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()
        print(new_user)

    return render_template("register.html")

@app.route("/market")
def market():
    all_data=Note.query.all()
    all_user=User.query.all()
    details = [
        {"name": "deepak", "role": "developer", "phn": 70426},
        {"name": "dk1", "role": "front-end", "phn": 70092},
    ]
    return render_template("market.html", d=details, data=all_data, user=all_user)


@app.route("/delete/<int:id>")
def delete(id):
    del_user=User.query.filter_by(id=id).first()
    db.session.delete(del_user)
    db.session.commit()
    return f"user deleted by id= {id} and name is {del_user.name}"


app.run(debug=True)

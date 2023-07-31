from src import app,db 
from flask import render_template,request
from src.Models import Note, User

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/about")
def about():
    # new_data=Note(email="dk@outlook.com")
    # db.session.add(new_data)
    # db.session.commit()
    return render_template("about.html")

@app.route("/login",methods=['GET','POST'])
def login():
    email=request.form['email']
    password=request.form['password']

    if request.method=="POST":
        u=User.query.all()
        print(email,password,u)
    return render_template("signin.html")

@app.route("/register",methods=['GET','POST'])
def register():
    if request.method=="POST":
        new_user=User(name=request.form['name'],email=request.form['email'],password=request.form['password'])
        db.session.add(new_user)
        db.session.commit()

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


@app.route("/notes")
def notes():
    return render_template("show.html")
from src import app,db, bcrypt
from flask import render_template,request,redirect,url_for
from src.Models import Note, User
from src.forms import CreateNotes,RegisterUser,LoginUser
from flask_login import login_user,logout_user,login_required,current_user
from datetime import datetime


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    form=LoginUser()

    if request.method=="POST":
        u=User.query.filter_by(email=request.form.get("email")).first()
        if(u):
            compare_password=bcrypt.check_password_hash(u.password,request.form.get("password"))
            if(not compare_password): return "pls check your password"
            login_user(u)
            return redirect(url_for("main"))
        else:
            return "pls check email and pssword then try again !!!"   

    return render_template("signin.html",form=form)

@app.route("/logout",methods=["GET"])
def logout():
    logout_user()
    return redirect(url_for("main"))

@app.route("/register",methods=['GET','POST'])
def register():
    form=RegisterUser()
    if request.method=="POST":
        new_user=User(name=request.form.get("name"),email=request.form.get("email"),password= bcrypt.generate_password_hash(request.form.get("password"),10).decode("utf-8"))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html",form=form)

@app.route("/all-notes")
def all_notes():
    all_data=Note.query.all()
    return render_template("all-notes.html", data=all_data)

@app.route("/delete/<int:id>")
def delete(id):
    del_note=Note.query.filter_by(id=id).first()
    db.session.delete(del_note)
    db.session.commit()
    return redirect(url_for("all_notes"))

@app.route("/notes",methods=['GET','POST'])
@login_required
def notes():
    form=CreateNotes()
    if form.validate_on_submit():
        notes_to_create=Note(title=form.title.data,description=form.description.data,label=form.label.data,Created_By=current_user.id)
        db.session.add(notes_to_create)
        db.session.commit()
        return redirect(url_for('all_notes'))
    return render_template("Notes.html",form=form)


@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id):
    up_id=Note.query.filter_by(id=id).first()
    form=CreateNotes(request.form,obj=up_id)
    if request.method=="POST" and form.validate_on_submit:
        form.populate_obj(up_id)
        up_id.Updated_At=datetime.utcnow()
        db.session.commit()
        return redirect(url_for('all_notes'))
    
    return render_template("Notes.html",form=form)

@app.route("/pinned/<int:id>")
def pinned(id):
    pin_id=Note.query.filter_by(id=id).first()
    if pin_id.isPinned==False:
        pin_id.isPinned=True
        db.session.commit()
    else:
        pin_id.isPinned=False
        db.session.commit()
        
    return redirect(url_for("all_notes"))


from src import app,db
from datetime import datetime
from src import bcrypt
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(length=30),nullable=False)
    email=db.Column(db.String(length=30),nullable=False,unique=True)
    password=db.Column(db.String(length=70),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow())
    Created_Notes=db.relationship('Note',backref="owned_user",lazy=True)

class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(length=100),nullable=False)
    description=db.Column(db.String(length=500),nullable=True)
    category=db.Column(db.String(length=30),default="other")
    Created_At=db.Column(db.DateTime,default=datetime.utcnow())
    Updated_At=db.Column(db.DateTime,default=datetime.utcnow())
    Created_By=db.Column(db.Integer(),db.ForeignKey('user.id'))


def __repr__(self):
    return f"{self.id}"

with app.app_context():
    db.create_all()
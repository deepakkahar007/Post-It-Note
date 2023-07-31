from src import app,db
from datetime import datetime


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
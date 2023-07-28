from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()



class Note(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String)
    date_created=db.Column(db.DateTime,default=datetime.utcnow())


    def __repr__(self) -> str:
        return f"{self.id} - {self.email}"



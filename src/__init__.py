from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_bcrypt import Bcrypt

app = Flask(__name__)

db=SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///Note.db"
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///User.db"
app.config["SECRET_KEY"]="123456789"

db.init_app(app)

bcrypt=Bcrypt(app)

from src import Models
from src import Routes
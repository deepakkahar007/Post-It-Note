from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

db=SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///Notes.db"
app.config["SQLALCHEMY_DATABASE_URI"]= "sqlite:///User.db"

db.init_app(app)

from src import Routes
from src import Models
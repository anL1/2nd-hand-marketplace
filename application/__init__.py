# importing Flask
from flask import Flask
app = Flask(__name__)

#import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
#print sql-querys to console
app.config["SQLALCHEMY_ECHO"] = True

#creating database
db = SQLAlchemy(app)

#import views-file
from application import views
from application.products import models
from application.products import views

from application.auth import models
from application.auth import views

db.create_all()

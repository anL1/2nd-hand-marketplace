# importing Flask
from flask import Flask
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)

from flask_sqlalchemy import SQLAlchemy
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
    app.config["SQLALCHEMY_ECHO"] = True

#creating database
db = SQLAlchemy(app)

#import views-file
from application import views
from application.products import models
from application.products import views

from application.auth import models
from application.auth import views

from application.comments import models
from application.comments import views

from application.categories import models
from application.categories import views

from application.productCategory import models

from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#initialize database
try:
    db.create_all()
except:
    pass

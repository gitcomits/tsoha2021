from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
uri = getenv("DATABASE_URL")
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config["SQLALCHEMY_DATABASE_URI"] = uri    #.env tiedostosta haetaan tietokannan osoite
# app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")    #.env tiedostosta haetaan tietokannan osoite
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)                                              # db olio joka suorittaa sql komentoja
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes

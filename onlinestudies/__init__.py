from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")    #.env tiedostosta haetaan tietokannan osoite
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)                                              # db olio joka suorittaa sql komentoja
bcrypt = Bcrypt(app)                                              # cyptographer for passwords
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from onlinestudies import routes

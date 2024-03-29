from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_bootstrap import Bootstrap5
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

# Construct the path to the database file inside the 'market' package
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

app.secret_key = "tO$&!|0wkamvVia0?n$NqIRVWOG"

# Bootstrap-Flask requires this line
bootstrap = Bootstrap5(app)
# Flask-WTF requires this line
csrf = CSRFProtect(app)

# bycrpt for hashing the passwords
bcrypt = Bcrypt(app)

# login manager
login_manager = LoginManager(app)

# must import routes after we define the application
from app import routes

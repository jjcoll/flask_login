from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Construct the path to the database file inside the 'market' package
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

# must import routes after we define the application
from app import routes

from app import app
from flask import render_template


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/register")
def register_page():
    return render_template("register.html")


@app.route("/login")
def login_page():
    return render_template("login.html")

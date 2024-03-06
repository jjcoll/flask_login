from app import app, db
from flask import render_template, redirect, url_for
from app.forms import RegisterForm
from app.models import User


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/user")
def user_page():
    return render_template("user.html")


@app.route("/register", methods=["POST", "GET"])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        # must add the user to the database
        user_to_add = User(
            username=form.username.data,
            email=form.email.data,
            # execute password setter
            password=form.password1.data,
        )

        db.session.add(user_to_add)
        db.session.commit()

        return redirect(url_for("user_page"))

    return render_template("register.html", form=form)


@app.route("/login")
def login_page():
    return render_template("login.html")

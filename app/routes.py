from app import app, db
from flask import render_template, redirect, url_for, flash, request, abort
from app.forms import RegisterForm, LoginForm
from app.models import User
from flask_login import login_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("index.html")


@app.route("/about")
def about_page():
    return render_template("about.html")


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

        login_user(user_to_add)

        return redirect(url_for("user_page"))

    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        # validate login details
        # check user exists
        user_to_check = User.query.filter_by(username=form.username.data).first()
        if user_to_check:
            # user exists check password match
            if user_to_check.check_password(form.password.data):
                # user and password match => login user
                print("Login successful")
                flash(f"User {user_to_check.username} logged in successfuly", "success")

                # login user
                login_user(user_to_check)

                next = request.args.get("next")
                # url_has_allowed_host_and_scheme should check if the url is safe
                # for redirects, meaning it matches the request host.
                # See Django's url_has_allowed_host_and_scheme for an example.
                # if not url_has_allowed_host_and_scheme(next, request.host):
                #     return abort(400)

                return redirect(next or url_for("user_page"))

            else:
                # password is not correct
                flash("Password is not correct", "danger")
        else:
            # user does not exist
            flash("User does not exist", "danger")

    return render_template("login.html", form=form)

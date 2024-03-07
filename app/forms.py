from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError, EqualTo
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField(
        label="Username: ", validators=[DataRequired(), Length(4, 10)]
    )
    email = StringField(
        label="Enter your Email: ", validators=[DataRequired(), Email()]
    )
    password1 = PasswordField(
        label="Enter your Password: ", validators=[DataRequired(), Length(min=8)]
    )
    password2 = PasswordField(
        label="Repeat your Password:", validators=[DataRequired(), EqualTo("password1")]
    )
    submit = SubmitField(label="Create Account")

    def validate_username(form, field):
        username_to_add = User.query.filter_by(username=field.data).first()
        if username_to_add:
            raise ValidationError("This username already exists!")

    def validate_email(form, field):
        email_to_add = User.query.filter_by(email=field.data).first()
        if email_to_add:
            raise ValidationError("This email is already being used!")


class LoginForm(FlaskForm):
    username = StringField(label="Enter Username:", validators=[DataRequired()])
    password = PasswordField(label="Enter you password", validators=[DataRequired()])
    submit = SubmitField(label="Login in", validators=[DataRequired()])

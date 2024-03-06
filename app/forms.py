from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from app.models import User


class RegisterForm(FlaskForm):
    username = StringField(
        label="Username: ", validators=[DataRequired(), Length(4, 10)]
    )
    email = StringField(label="Email: ", validators=[DataRequired(), Email()])
    password = PasswordField(
        label="Password: ", validators=[DataRequired(), Length(min=8)]
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

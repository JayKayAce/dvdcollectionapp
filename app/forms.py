from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import BooleanField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import ValidationError
from wtforms.validators import EqualTo
from wtforms.validators import Length

from app.models import User

class LoginForm(FlaskForm):
    """
    Class for handling login for the page
    """
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField ("Password", validators=[DataRequired()])
    remember_me = BooleanField("Remember Me?")
    submit = SubmitField("Sign In")

class RegistrationForm(FlaskForm):
    """
    Handles User registration
    Creates a new user in the database
    """
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired(),Email()])
    password = PasswordField ("Password", validators=[DataRequired()])
    password_repeat = PasswordField(
        "Repeat Password", 
        validators = [DataRequired(),EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError("Invalid Username, already taken")
        
    def validate_email(self, email):
        user = User.query.filter_by(email= email.data).first()
        if user is not None:
            raise ValidationError("Email already registered, please reset your password")


class EditProfileForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    about_me = TextAreaField("About Me", validators=[Length(min=0, max=140)])
    submit = SubmitField("Submit")
# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import Required, Email, EqualTo


# Define the login form (WTForms)

class RegisterForm(FlaskForm):
    email = TextField('Email Address', [Email(), Required(message='Must provide an email address')])
    password = PasswordField('Password', [Required(message='Must provide a password.')])

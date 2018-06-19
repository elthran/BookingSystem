# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Define the create new user form (WTForms)

class UserForm(FlaskForm):
    name = StringField('Name',
                       [DataRequired(message='You must enter your name.')])
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.'),
                         DataRequired(message='You must enter an email address.')])
    password = PasswordField('Password',
                             [DataRequired(message='You must enter a password.'),
                              Length(min=4),
                              EqualTo('confirmation', message='Passwords must match.')])
    confirmation = PasswordField('Repeat password')

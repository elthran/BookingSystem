# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email, EqualTo, Length


# Define the login form (WTForms)
class MainForm(FlaskForm):
    business = StringField('Business',
                         [DataRequired(message='You must enter a business name.')])
    name = StringField('Name',
                     [DataRequired(message='You must enter your name.')])
    email = StringField('Email Address',
                      [Email(message='Not a valid email address.'),
                       DataRequired(message='You must enter an email address.')])


class PasswordForm(FlaskForm):
    password = PasswordField('Password',
                             [DataRequired(message='You must enter a password.'),
                              Length(min=4),
                              EqualTo('confirmation', message='Passwords must match.')])
    confirmation = PasswordField('Repeat password')


class EmployeeForm(FlaskForm):
    name = StringField('Name',
                     [DataRequired(message='You must enter your name.')])
    email = StringField('Email Address',
                      [Email(message='Not a valid email address.'),
                       DataRequired(message='You must enter an email address.')])

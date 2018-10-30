# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField, SelectField  # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Define the create new business form (WTForms)

class BusinessForm(FlaskForm):
    name = StringField('Name',
                       [DataRequired(message='You must enter your name.')])
    location = StringField('Location')

    country = SelectField('country', coerce=int)
    currency = SelectField('currency', coerce=int)
    province = SelectField('province', coerce=int)
    city = SelectField('city', coerce=int)
    address = StringField('Address')

    username = StringField('Name',
                           [DataRequired(message='You must enter your name.')])
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.'),
                         DataRequired(message='You must enter an email address.')])
    password = PasswordField('Password',
                             [DataRequired(message='You must enter a password.'),
                              Length(min=4),
                              EqualTo('confirmation', message='Passwords must match.')])
    confirmation = PasswordField('Repeat password')

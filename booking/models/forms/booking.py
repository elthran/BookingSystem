# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import TextField # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the login form (WTForms)
class BookingInit(FlaskForm):
    email = TextField('Email Address',
                      [Email(message='Not a valid email address.'),
                       DataRequired(message='You must enter an email address.')])
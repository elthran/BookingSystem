# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField  # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the create new appointment form (WTForms)

class BookingInit(FlaskForm):
    email = StringField('Email Address',
                      [Email(message='Not a valid email address.'),
                       DataRequired(message='You must enter an email address.')])
    name = StringField('Name',
                      [DataRequired(message='You must enter an email address.')])
    phone = StringField('Phone')

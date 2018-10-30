# Import Form and RecaptchaField (optional)
import flask_wtf.form
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, SelectField, BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the create new appointment form (WTForms)

class CustomerBooking(FlaskForm):
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.'),
                         DataRequired(message='You must enter an email address.')])
    name = StringField('Name',
                       [DataRequired(message='You must enter an email address.')])
    phone = StringField('Phone')
    service = SelectField('Services', coerce=int)


class ManualBooking(FlaskForm):
    anonymous = BooleanField('Anonymous')
    name = StringField('Name')
    phone = StringField('Phone')
    email = StringField('Email Address')
    service = SelectField('Service', coerce=int)

    # If anonymous is checked, the other fields should become locked and auto-filled in with "Anonymous"

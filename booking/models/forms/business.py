# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the create new business form (WTForms)

class BusinessForm(FlaskForm):
    name = StringField('Name',
                       [DataRequired(message='You must enter your name.')])
    location = StringField('Location')
    address = StringField('Address')
    town = StringField('Town')

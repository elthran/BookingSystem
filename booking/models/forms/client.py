# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the create new user form (WTForms)

class ClientForm(FlaskForm):
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.'),
                         DataRequired(message='You must enter an email address.')])
    name = StringField('Name',
                       [DataRequired(message='You must enter an email address.')])
    phone = StringField('Phone')

class EditClientForm(FlaskForm):
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.')])
    name = StringField('Name')
    phone = StringField('Phone')

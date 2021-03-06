# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField  # BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email


# Define the login form (WTForms)

class ContactForm(FlaskForm):
    first_name = StringField('First_name')
    last_name = StringField('Last_name')
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.')])
    phone = StringField('Phone')
    message = StringField('Message',
                          [DataRequired(message='You must enter a name.')])

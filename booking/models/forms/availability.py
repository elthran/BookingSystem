# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import SelectField

# Import Form validators
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Define the create new user form (WTForms)

class AvailabilityForm(FlaskForm):
    monday_start = SelectField('Monday_start', coerce=int)
    monday_end = SelectField('Monday_end', coerce=int)
    tuesday_start = SelectField('Tuesday_start', coerce=int)
    tuesday_end = SelectField('Tuesday_end', coerce=int)

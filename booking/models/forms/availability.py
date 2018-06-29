# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import SelectField, BooleanField

# Import Form validators
from wtforms.validators import DataRequired, Email, Length, EqualTo


# Define the create new user form (WTForms)

class AvailabilityForm(FlaskForm):
    day = SelectField('day', coerce=int)
    start = SelectField('start', coerce=int)
    end = SelectField('end', coerce=int)

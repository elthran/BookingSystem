# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, BooleanField, DecimalField, IntegerField

# Import Form validators
from wtforms.validators import DataRequired


# Define the create new user form (WTForms)

class ServiceForm(FlaskForm):
    name = StringField('Name',
                       [DataRequired(message='You must enter a name.')])
    availability = StringField('Availability',
                       [DataRequired(message='You must enter an availability')])
    cost = DecimalField('Cost',
                       [DataRequired(message='You must enter a cost as a decimal.')])
    length = IntegerField('Length',
                       [DataRequired(message='You must enter a length as an integer.')])
    deposit = BooleanField('Deposit')
    locations = BooleanField('Locations')


class EditServiceForm(FlaskForm):
    pass

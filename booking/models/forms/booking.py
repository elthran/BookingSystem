# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, SelectField

# Import Form validators
from wtforms.validators import DataRequired, Email

# Import models
from booking.models.businesses import Business


# Define the create new appointment form (WTForms)

class CustomerBooking(FlaskForm):
    email = StringField('Email Address',
                      [Email(message='Not a valid email address.'),
                       DataRequired(message='You must enter an email address.')])
    name = StringField('Name',
                      [DataRequired(message='You must enter an email address.')])
    phone = StringField('Phone')

class ManualBooking(FlaskForm):
    name = StringField('Name',
                      [DataRequired(message='You must enter an email address.')])
    phone = StringField('Phone')
    email = StringField('Email Address',
                        [Email(message='Not a valid email address.'),
                         DataRequired(message='You must enter an email address.')])
    service = SelectField('Service')

    def display_services(request, id):
        business = Business.query.filter_by(id=id)
        form = ManualBooking(request.POST, obj=business)
        form.service.choices = [(thing.id, thing.name) for thing in business.services]
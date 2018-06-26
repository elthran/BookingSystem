# Import Form and RecaptchaField (optional)
import flask_wtf.form
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

    def __init__(self, business_id, formdata=flask_wtf.form._Auto, **kwargs):
        super().__init__(formdata=formdata, **kwargs)
        business = Business.query.get(business_id)
        self.service.choices = [(thing.id, thing.name) for thing in business.services]

    def display_services(request, id):
        business = Business.query.get(id)
        form = ManualBooking(request.POST, obj=business)
        form.service.choices = [(thing.id, thing.name) for thing in business.services]

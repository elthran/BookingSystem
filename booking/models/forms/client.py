# Import Form and RecaptchaField (optional)
from flask_wtf import FlaskForm  # , RecaptchaField

# Import Form elements such as TextField and BooleanField (optional)
from wtforms import StringField, PasswordField  # BooleanField

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


class ClientSearchForm(FlaskForm):
    keywords = StringField("Search Terms")

    def get_as_data_dict(self):
        kw = self.keywords.data.split()
        # print("keywords:", kw)
        data = {"name": [], "email": [], "phone": []}
        # Should do some kind of sensible sorting at some point.
        for k in kw:
            data['name'].append(k)
            data['email'].append(k)
            data['phone'].append(k)
        # print("keyword matrix:", data)
        return data

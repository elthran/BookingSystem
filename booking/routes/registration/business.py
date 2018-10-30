# Import the app itself
from flask_mail import Message

from booking import app, mail
# Import flask dependencies
from flask import redirect, url_for, render_template, request
# Import models
from booking.models import Location
from booking.models.forms.business import BusinessForm
from booking.models.businesses import Business
from booking.models.mappings import Mapping
from booking.models.users import User
# Import database
from booking.models.bases import db

# These should be pulled from the metadata file in /static
countries = ["Canada"]
currencies = ["CAD", "USD"]
provinces = ["BC", "AB"]
cities = ["Vancouver", "Edmonton"]


@app.route('/register/business/', methods=['GET', 'POST'])
def register_business():
    form = BusinessForm(request.form)
    form.country.choices = [(i, j) for i, j in enumerate(countries)]
    form.currency.choices = [(i, j) for i, j in enumerate(currencies)]
    form.province.choices = [(i, j) for i, j in enumerate(provinces)]
    form.city.choices = [(i, j) for i, j in enumerate(cities)]
    if form.validate_on_submit() and User.query.filter_by(email=form.email.data).first() is None:
        business = Business(form.name.data,
                            countries[form.country.data],
                            form.currency.data,
                            form.province.data,
                            form.city.data,
                            form.address.data)
        db.session.add(business)
        db.session.commit()

        user = User(form.username.data, form.email.data, form.password.data, business.id, is_owner=True)
        db.session.add(user)
        db.session.commit()

        location = Location(business_id=business.id, name=business.city)
        db.session.add(location)
        db.session.commit()

        mapping = Mapping(business_id=business.id, location_id=location.id, user_id=user.id)
        db.session.add(mapping)
        db.session.commit()

        print("All employees:",
              Mapping.query.filter_by(business_id=business.id).filter_by(location_id=location.id).all())
        print("All locations:", Mapping.query.filter_by(business_id=business.id).filter_by(user_id=user.id).all())

        subject = "Welcome to JaChang!"
        msg = Message(recipients=[form.email.data], subject=subject)
        msg.html = "<p>To activate your account, please click this link: %r</p>" % (
            user.get_verification_link())
        mail.send(msg)

        return render_template("registration/verification.html", form=form)

    return render_template("registration/business.html", form=form)

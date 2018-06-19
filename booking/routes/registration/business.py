# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request
# Import session handling
from flask_login import login_user, current_user
# Import models
from booking.models.forms.business import BusinessForm
from booking.models.businesses import Business
# Import database
from booking.models.bases import db


@app.route('/register/business/', methods=['GET', 'POST'])
def register_business():
    form = BusinessForm(request.form)
    if form.validate_on_submit():
        business = Business(form.name.data)
        db.session.add(business)
        db.session.commit()
        current_user.business_id = business.id
        db.session.commit()
        return redirect(url_for('business_profile'))
    return render_template("authentication/business.html", form=form)

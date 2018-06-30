# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import login_user
# Import models
from booking.models.forms.user import UserForm
from booking.models.businesses import Business
from booking.models.users import User
# Import database
from booking.models.bases import db

@app.route('/register/user/', methods=['GET', 'POST'])
@app.route('/register/user/<int:business_id>/<string:business_referral>/', methods=['GET', 'POST'])
def register_user(business_id=1, business_referral=""):
    if business_id == 1:
        owner = True
    else:
        owner = False
    form = UserForm(request.form)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first() is None:
            user = User(form.name.data, form.email.data, form.password.data, business_id, owner)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            if owner:
                return redirect(url_for('register_business'))
            else:
                return redirect(url_for('business_calendar'))
        else:
            flash("User already exists with that email.", "error")
    return render_template("registration/user.html", form=form, owner=owner)

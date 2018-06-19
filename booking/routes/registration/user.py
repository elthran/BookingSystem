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
            print(user.id, user.business.id)
            if owner:
                return redirect(url_for('register_business'))
            else:
                return redirect(url_for('business_profile'))
        else:
            flash("User already exists with that email.", "error")
    return render_template("authentication/user.html", form=form, owner=owner)



    if Hours.query.first() is None:
        default_hours = Hours()
        db.session.add(default_hours)
        db.session.commit()
    user_shell = UserShell.query.filter_by(id=user_shell_id).first()
    business_shell = BusinessShell.query.filter_by(id=business_shell_id).first()
    business = Business(business_shell.name)
    db.session.add(business)
    db.session.commit()
    business = Business.query.filter_by(id=business.id).first()
    # Need to create a location object for the business. It uses the default hours.
    first_location = Location(1, business.id)
    db.session.add(first_location)
    db.session.commit()
    duplicate_user = User.query.filter_by(email=user_shell.email).first()
    if duplicate_user is None:
        user = User(user_shell.name, user_shell.email, user_shell.password, business.id, user_shell.is_owner)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(id=user.id).first()
        login_user(user)
    else:
        print("A user with that email already exists in the database!!!!", duplicate_user)
    return redirect(url_for('business_profile', year=2018, month=6, day=0))

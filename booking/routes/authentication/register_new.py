# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for
# Import session handling
from flask_login import login_user
# Import models
from booking.models.users_shell import UserShell
from booking.models.businesses_shell import BusinessShell
from booking.models.users import User
from booking.models.businesses import Business
from booking.models.locations import Location
from booking.models.hours import Hours

# Import database
from booking.models.bases import db


@app.route('/register/<int:user_shell_id>/<int:business_shell_id>', methods=['GET', 'POST'])
def register_new(user_shell_id, business_shell_id):
    # I need a default hour set so that new locations have an hour object to pass in. And it seems useful anyway
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

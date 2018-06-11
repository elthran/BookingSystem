# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import session handling
from flask_login import login_user
# Import models
from booking.models.users_shell import UserShell
from booking.models.businesses_shell import BusinessShell
from booking.models.users import User
from booking.models.businesses import Business
# Import database
from booking.models.bases import db

@app.route('/register/<int:user_id>/<int:business_id>', methods=['GET', 'POST'])
def register_new(user_id, business_id):
    user = UserShell.query.filter_by(id=user_id).first()
    business = BusinessShell.query.filter_by(id=business_id).first()
    business = Business(business.name)
    db.session.add(business)
    db.session.commit()
    business = Business.query.filter_by(name=business.name).first()
    duplicate_user = User.query.filter_by(email=user.email).first()
    if duplicate_user == None:
        user = User(user.name, user.email, user.password, business.id)
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(email=user.email).first()
        login_user(user)
    else:
        print("A user with that email already exists in the database!!!!", duplicate_user)
    return redirect(url_for('business_profile', chosen_year=2018, chosen_month=6, chosen_day=0))
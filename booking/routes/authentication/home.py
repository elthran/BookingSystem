# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for, flash
from flask_login import current_user
# Import models
from booking.models.users import User
from booking.models.businesses import Business
from booking.models.hours import Hours
# Import database
from booking.models.bases import db

"""
app.route('setup_account)
def setup_account():
    account = Account(form.data.business_name, form.data.email, form.data.name)
    business = Business(account, form.data.business_name)
    session.add(account)
    session.commit()
    return url_for("page you see after you log in")
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    if Business.query.all() == []:
        business1 = Business("Temporary")
        db.session.add(business1)
        db.session.commit()
        user = User("Mr. Brunner", "admin@admin.com", "admin", business1.id, True)
        db.session.add(user)
        db.session.commit()
    if Hours.query.all() == []:
        hours1 = Hours()
        db.session.add(hours1)
        db.session.commit()
    if current_user.is_authenticated:
        return redirect(url_for('business_calendar'))
    users = User.query.all()
    businesses = Business.query.all()
    print("Printing all users:")
    for user in users:
        print("Printing user::", user)
    print("Printing all businesses:")
    for business in businesses:
        print("Printing business::", business)
    return render_template("authentication/home.html")


# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
#
from flask_login import login_required
# Import models
from booking.models import Business
# Import calendar
from calendar import month

@login_required
@app.route('/home')
def home():
    businesses = Business.query.all()
    this_month = month(2018, 6)
    return render_template("home.html", businesses=businesses, calendar=this_month)
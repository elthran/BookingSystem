# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
from booking.models.businesses import Business
from booking.models.locations import Location


@app.route('/business/payment/')
@login_required
def business_payment():
    return render_template("business/payment.html")

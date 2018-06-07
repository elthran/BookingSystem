# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models import Business

@app.route('/book_appointment/<int:business_id>/')
def book_appointment(business_id):
    business = Business.query.filter_by(id=business_id).first()
    return render_template("bookings/book_appointment.html", business=business)
# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models.appointments import Appointment


@login_required
@app.route('/profile/appointment/<int:business_id>/<int:appointment_id>/')
def appointment_profile(business_id, appointment_id):
    appointment = Appointment.query.filter_by(business_id=business_id).get(appointment_id)
    return render_template("profiles/appointment.html", appointment=appointment)

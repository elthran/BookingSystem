# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.availability import AvailabilityForm
from booking.models.availabilities import Availability
# Import database
from booking.models.bases import db


@app.route('/business/delete_employee_availability/<int:availability_id>', methods=['GET', 'POST'])
def delete_employee_availability(availability_id):
    if availability_id == 0:
        availabilities = Availability.query.filter_by(user_id=current_user.id).all()
        for availability in availabilities:
            db.session.delete(availability)
            db.session.commit()
    else:
        availability = Availability.query.get(availability_id)
        db.session.delete(availability)
        db.session.commit()
    flash("Availability deleted", "notice")
    return redirect(url_for('edit_employee_availability'))

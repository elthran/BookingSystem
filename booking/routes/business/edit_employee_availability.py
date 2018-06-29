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

@app.route('/business/edit_employee_availability/', methods=['GET', 'POST'])
def edit_employee_availability():
    form = AvailabilityForm(request.form)
    days = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    form.day.choices = [(i, days[i]) for i in range(1, 8)]
    form.start.choices = [(i, str(i)+":00") for i in range(1,13)]
    form.end.choices = [(i, str(i)+":00") for i in range(1,13)]
    if form.validate_on_submit():
        length = form.end.data - form.start.data
        if length <= 0:
            flash("Can't add a negative time", "error")
            return redirect(url_for('edit_employee_availability'))
        availability = Availability(current_user.location.id, current_user.id, form.day.data, form.start.data, length)
        db.session.add(availability)
        db.session.commit()
        flash("Availability updated", "notice")
        return redirect(url_for('edit_employee_availability'))
    return render_template("business/edit_employee_availability.html", form=form)

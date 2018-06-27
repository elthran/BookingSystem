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

@app.route('/business/edit_availability/', methods=['GET', 'POST'])
def edit_availability():
    if current_user.availabilities:
        monday_start = current_user.get_availability_by_day(1)[0].start
        monday_end = current_user.get_availability_by_day(1)[0].end
        tuesday_start = current_user.get_availability_by_day(2)[0].start
        tuesday_end = current_user.get_availability_by_day(2)[0].end
    else:
        monday_start = 1
        monday_end = 12
        tuesday_start = 1
        tuesday_end = 12
    form = AvailabilityForm(request.form,
                            monday_start=monday_start, monday_end=monday_end,
                            tuesday_start=tuesday_start, tuesday_end=tuesday_end)
    form.monday_start.choices = [(i, str(i)+":00") for i in range(1,13)]
    form.monday_end.choices = [(i, str(i)+":00") for i in range(1,13)]
    form.tuesday_start.choices = [(i, str(i) + ":00") for i in range(1, 13)]
    form.tuesday_end.choices = [(i, str(i) + ":00") for i in range(1, 13)]
    if form.validate_on_submit():
        monday_length = form.monday_end.data - form.monday_start.data
        tuesday_length = form.tuesday_end.data - form.tuesday_start.data
        if monday_length <= 0 or tuesday_length <= 0:
            flash("Can't add a negative time", "error")
            return redirect(url_for('edit_availability'))
        availabilities = Availability.query.filter_by(employee_id=current_user.id).all()
        for availability in availabilities:
            db.session.delete(availability)
        availability = Availability(current_user.id, 1, form.monday_start.data, monday_length)
        db.session.add(availability)
        db.session.commit()
        availability = Availability(current_user.id, 2, form.tuesday_start.data, tuesday_length)
        db.session.add(availability)
        db.session.commit()
        flash("Availability added", "notice")
        return redirect(url_for('edit_availability'))
    return render_template("business/edit_availability.html", form=form)

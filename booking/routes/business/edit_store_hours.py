# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.availability import AvailabilityForm
from booking.models.hours import Hour
from booking.models.locations import Location
# Import database
from booking.models.bases import db

@app.route('/business/edit_store_hours/', methods=['GET', 'POST'])
def edit_store_hours():
    location = Location.query.get(current_user.location_id)
    if location.hours:
        """
        This returns the first in the list for each day because there could be multiple times in one day. This obviously needs to be improved.
        """
        for hour in location.hours:
            if hour.day == 1:
                monday_closed = hour.closed
                monday_start = hour.start
                monday_end = hour.end
            elif hour.day == 2:
                tuesday_closed = hour.closed
                tuesday_start = hour.start
                tuesday_end = hour.end
    else:
        monday_start = 1
        monday_end = 12
        monday_closed = False
        tuesday_start = 1
        tuesday_end = 12
        tuesday_closed = False
    form = AvailabilityForm(request.form,
                            monday_closed=monday_closed, monday_start=monday_start, monday_end=monday_end,
                            tuesday_closed=tuesday_closed, tuesday_start=tuesday_start, tuesday_end=tuesday_end)
    form.monday_start.choices = [(i, str(i)+":00") for i in range(1,13)]
    form.monday_end.choices = [(i, str(i)+":00") for i in range(1,13)]
    form.tuesday_start.choices = [(i, str(i) + ":00") for i in range(1, 13)]
    form.tuesday_end.choices = [(i, str(i) + ":00") for i in range(1, 13)]
    if form.validate_on_submit():
        monday_closed = form.monday_closed.data
        monday_length = form.monday_end.data - form.monday_start.data
        tuesday_closed = form.tuesday_closed.data
        tuesday_length = form.tuesday_end.data - form.tuesday_start.data
        if monday_length <= 0 or tuesday_length <= 0:
            flash("Can't add a negative time", "error")
            return redirect(url_for('edit_store_hours'))
        hours = Hour.query.filter_by(location_id=location.id).all()
        for hour in hours:
            db.session.delete(hour)
        print(location.hours)
        hour = Hour(location.id, 1, form.monday_start.data, monday_length, monday_closed)
        db.session.add(hour)
        db.session.commit()
        hour = Hour(location.id, 2, form.tuesday_start.data, tuesday_length, tuesday_closed)
        db.session.add(hour)
        db.session.commit()
        flash("Hours updated", "notice")
        return redirect(url_for('edit_store_hours'))
    return render_template("business/edit_store_hours.html", form=form,
                           monday_closed=monday_closed, tuesday_closed=tuesday_closed)

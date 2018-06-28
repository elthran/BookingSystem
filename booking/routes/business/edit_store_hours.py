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
    print(location.hours)
    if location.hours:
        monday_start = location.get_hours_by_day(1)[0].start
        monday_end = location.get_hours_by_day(1)[0].end
        tuesday_start = location.get_hours_by_day(2)[0].start
        tuesday_end = location.get_hours_by_day(2)[0].end
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
            return redirect(url_for('edit_store_hours'))
        hours = Hour.query.filter_by(location_id=location.id).all()
        for hour in hours:
            db.session.delete(hour)
        print(location.hours)
        hour = Hour(location.id, 1, form.monday_start.data, monday_length)
        db.session.add(hour)
        db.session.commit()
        hour = Hour(location.id, 2, form.tuesday_start.data, tuesday_length)
        db.session.add(hour)
        db.session.commit()
        flash("Hours updated", "notice")
        return redirect(url_for('edit_store_hours'))
    return render_template("business/edit_store_hours.html", form=form)

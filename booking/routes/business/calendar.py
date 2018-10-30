# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required, current_user
# Import calendar
from calendar import monthcalendar
from datetime import datetime
from booking.models.calendars import CustomCalendar


# from booking.models.locations import Location


@app.route('/business/calendar/', methods=['GET', 'POST'])
@app.route('/business/calendar/<int:location_id>/<int:year>/<int:month>/<int:day>', methods=['GET', 'POST'])
@login_required
def business_calendar(location_id=1, year=datetime.now().year, month=datetime.now().month, day=0):
    # location = Location.query.filter_by(business_id=current_user.business.id).filter_by(id=location_id).first()
    custom_calendar = CustomCalendar(year, month, day)
    calendar_month = monthcalendar(year, month)
    return render_template("business/calendar.html", location_id=location_id,
                           custom_calendar=custom_calendar, calendar_month=calendar_month,
                           day=day, month=month, year=year)

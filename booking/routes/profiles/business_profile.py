# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import calendar
from calendar import monthcalendar
from datetime import datetime
from booking.models.calendars import CustomCalendar

@app.route('/business_profile/')
@app.route('/business_profile/<int:year>/<int:month>/<int:day>')
@login_required
def business_profile(year=datetime.now().year, month=datetime.now().month, day=0):
    custom_calendar = CustomCalendar(year, month, day)
    calendar_month = monthcalendar(year, month)
    return render_template("profiles/business_profile.html", custom_calendar=custom_calendar, calendar_month=calendar_month, day=day, month=month, year=year)
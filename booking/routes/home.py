# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import calendar
from calendar import monthcalendar
from booking.models.calendars import CustomCalendar

@login_required
@app.route('/home/<int:chosen_year>/<int:chosen_month>/<int:chosen_day>')
def home(chosen_year, chosen_month, chosen_day):
    custom_calendar = CustomCalendar(chosen_year, chosen_month, chosen_day)
    calendar_month = monthcalendar(chosen_year, chosen_month)
    return render_template("home.html", custom_calendar=custom_calendar, calendar_month=calendar_month, day=chosen_day, month=chosen_month, year=chosen_year)
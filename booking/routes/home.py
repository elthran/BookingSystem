# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import calendar
from calendar import monthcalendar

@login_required
@app.route('/home/<int:chosen_year>/<int:chosen_month>/<int:chosen_day>')
def home(chosen_year, chosen_month, chosen_day):
    testing = monthcalendar(chosen_year, chosen_month)
    print(testing)
    return render_template("home.html", testing=testing, day=chosen_day, month=chosen_month, year=chosen_year)
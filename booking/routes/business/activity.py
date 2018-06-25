# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
from booking.models.businesses import Business


@app.route('/business/activity/', methods=['GET', 'POST'])
@app.route('/business/activity/<int:business_id>/', methods=['GET', 'POST'])
@login_required
def business_activity(business_id):
    # location = Location.query.filter_by(business_id=current_user.business.id).filter_by(id=location_id).first()
    business = Business.query.filter_by(id=business_id).first()
    return render_template("business/calendar.html", location_id=location_id,
                           custom_calendar=custom_calendar, calendar_month=calendar_month,
                           day=day, month=month, year=year)

# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models import Business, Location


@login_required
@app.route('/business/employees/<int:business_id>/<int:location_id>/')
def employees(business_id, location_id):
    employee_list = Business.query.filter_by(id=business_id).first().get_employees()
    location_name = "All locations"
    if location_id != 0:
        employee_list = [employee for employee in employee_list if location_id in employee.get_location_ids()]
        try:
            location_name = Location.query.filter_by(business_id=business_id).filter_by(id=location_id).first().name
        except:
            location_name = "wtf"
    return render_template("business/employees.html", employees=employee_list, location_name=location_name)

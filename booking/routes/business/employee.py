# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models.users import User


@login_required
@app.route('/business/employee/<int:business_id>/<int:employee_id>/')
def employee_profile(business_id, employee_id):
    employee = User.query.filter_by(business_id=business_id).filter_by(id=employee_id).first()
    return render_template("business/employee.html", employee=employee)

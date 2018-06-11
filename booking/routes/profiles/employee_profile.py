# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models.clients import Client

@login_required
@app.route('/profile/employee/<int:business_id>/<int:employee_id>/')
def employee_profile(business_id, employee_id):
    employee = User.query.filter_by(business_id=business_id).filter_by(id=employee_id).first()
    print(employee)
    return render_template("profiles/client_profile.html", employee=employee)
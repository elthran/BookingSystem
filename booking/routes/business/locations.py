# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template
# Import session management
from flask_login import login_required
# Import models
from booking.models import Business


@login_required
@app.route('/business/locations/<int:business_id>/')
def locations(business_id):
    locations = Business.query.filter_by(id=business_id).first().locations
    return render_template("business/locations.html", locations=locations)

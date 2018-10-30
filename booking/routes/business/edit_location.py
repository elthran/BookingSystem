# Import the app itself
from booking import app
# Import flask dependencies
from flask import redirect, url_for, render_template, request, flash
# Import session handling
from flask_login import current_user
# Import models
from booking.models.forms.service import ServiceForm
from booking.models.services import Service
from booking.models.locations import Location
# Import database
from booking.models.bases import db


@app.route('/business/edit_location/<int:location_id>', methods=['GET', 'POST'])
def edit_location(location_id):
    return render_template("business/edit_location.html", location_id=location_id)

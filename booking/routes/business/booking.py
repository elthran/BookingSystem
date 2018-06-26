# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for, flash
# Import session management
from flask_login import login_required, current_user
# Import models
from booking.models.forms.booking import ManualBooking
from booking.models.clients import Client
from booking.models.appointments import Appointment
# Import database
from booking.models.bases import db
# Import datetime
from datetime import datetime


@app.route('/business/booking/<int:location_id>/', methods=['GET', 'POST'])
@login_required
def business_booking(location_id):
    form = ManualBooking(request.form)
    if form.validate_on_submit():
        date = datetime.now()
        # The following if tree is ugly. Please fix
        # @klndikemarlen
        if form.email.data:
            client = Client.query.filter_by(business_id=current_user.business.id).filter_by(email=form.email.data).first()
            if client:
                flash("Client found matching that email address", "notice")
        if form.phone.data and client == None:
            client = Client.query.filter_by(business_id=current_user.business.id).filter_by(phone=form.phone.data).first()
            if client:
                flash("Client found matching that phone number", "notice")
        if form.name.data and client == None:
            client = Client.query.filter_by(business_id=current_user.business.id).filter_by(name=form.name.data).first()
            if client:
                flash("Client found matching that name", "notice")
        if client == None:
            flash("No client found. Creating new client", "notice")
            client = Client(form.email.data, current_user.business.id, form.name.data, form.phone.data)
            db.session.add(client)
            db.session.commit()
        appointment = Appointment(current_user.business.id, client.id, 30, date)
        db.session.add(appointment)
        db.session.commit()
        if client:
            flash("Appointment has been booked!", "notice")
        return redirect(url_for('business_booking', location_id=location_id))
    # Not sure why my flash messages double appear here
    return render_template("business/booking.html", form=form)

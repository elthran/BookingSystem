# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, flash
# Import models
from booking.models import Business, Client, Appointment
# Import forms
from booking.models.forms.booking import CustomerBooking
# Import database
from booking.models.bases import db
from datetime import datetime


@app.route('/booking/appointment/<int:id>/', methods=['GET', 'POST'])
def book_appointment(id):
    business = Business.query.get(id)
    # If sign in form is submitted
    form = CustomerBooking(request.form)
    form.service.choices = [(service.id, service.name) for service in business.services]
    # Verify the sign in form
    if form.validate_on_submit():
        date = datetime.now()
        client = Client.query.filter_by(business_id=id).filter_by(email=form.email.data).first()
        if client:
            flash('Client with that email address already exists', 'notice')
        else:
            client = Client(form.email.data, id, form.name.data, form.phone.data)
            db.session.add(client)
            db.session.commit()
            flash('New client being created', 'notice')
        appointment = Appointment(id, client.id, form.service.data, date)
        db.session.add(appointment)
        db.session.commit()
    return render_template("bookings/book_appointment.html", business=business, form=form)

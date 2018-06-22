# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, flash
# Import models
from booking.models import Business, Client, Appointment
# Import forms
from booking.models.forms.booking import BookingInit
# Import database
from booking.models.bases import db
from datetime import datetime


@app.route('/booking/appointment/<int:business_id>/', methods=['GET', 'POST'])
def book_appointment(business_id):
    business = Business.query.filter_by(id=business_id).first()
    # If sign in form is submitted
    form = BookingInit(request.form)
    # Verify the sign in form
    if form.validate_on_submit():
        date = datetime(2018, 6, 8)
        client = Client.query.filter_by(business_id=business_id).filter_by(email=form.email.data).first()
        print(client)
        if client:
            print("Client with that email address already exists", client)
            flash('Client with that email address already exists', 'notice')
        else:
            client = Client(form.email.data, business_id, form.name.data, form.phone.data)
            db.session.add(client)
            db.session.commit()
            print("New client being created", client)
            flash('New client being created', 'notice')
        appointment = Appointment(business_id, client.id, 30, date)
        db.session.add(appointment)
        db.session.commit()
        print(appointment)
    return render_template("bookings/book_appointment.html", business=business, form=form)

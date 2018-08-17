# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, flash, request
from booking.models import Email
from booking.models.forms.contact import ContactForm
from booking.models.bases import db

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    emails = Email.query.all()
    print(emails)
    form = ContactForm(request.form)
    if form.validate_on_submit():
        flash('Thank you for your feedback', 'notice')
        email = Email(form.email.data, form.message.data)
        db.session.add(email)
        db.session.commit()
    return render_template("index/contact.html", form=form)


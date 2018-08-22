# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, flash, request
from booking.models.forms.contact import ContactForm
from booking import mail
from flask_mail import Message

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm(request.form)
    if form.validate_on_submit():
        subject = "Customer Feedback from JaChang"
        msg = Message(recipients=["jacobbrunner@gmail.com"], subject=subject)
        msg.html = "<p>From: %r %r</p><p>Email: %r</p><p>Content: %r</p>" % (form.first_name.data, form.last_name.data, form.email.data, form.message.data)
        mail.send(msg)
        flash("Message sent! Thanks for your support.", "notice")
    return render_template("index/contact.html", form=form)
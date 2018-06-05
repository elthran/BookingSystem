# Import the app itself
from booking import app
# Import flask dependencies
from flask import render_template, request, redirect, url_for
# Import models
from booking.models import User
# Import forms
from booking.models.forms.register import MainForm
# Import database
from booking.models.bases import db

@app.route('/', methods=['GET', 'POST'])
def main():
    form = MainForm(request.form)

    if form.validate_on_submit():
        name = form.name.data
        business = form.business.data
        email = form.email.data
        return redirect(url_for('create_password', name=name, business=business, email=email))
    return render_template("authentication/main.html", form=form)
